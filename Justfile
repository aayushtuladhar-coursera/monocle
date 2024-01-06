# Copyright (C) 2023 Monocle authors
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# doc: https://just.systems/man/en/chapter_1.html

PINCLUDE := "-I /usr/include ${PROTOC_FLAGS} -I ./schemas/"
# just doesn't support array so we create a space separated string for bash
# see: https://github.com/casey/just/issues/1570
PBS := `ls schemas/monocle/protob/*.proto | grep -v http.proto | sed 's/schemas.//' | tr '\n' ' '`

# Update code after changing protobuf schema (./schemas/monocle/protob), ci.dhall or architecture.plantuml
codegen: codegen-ci codegen-doc codegen-stubs codegen-javascript codegen-openapi codegen-haskell

# Generate CI config from .github/workflows/ci.dhall
[private]
codegen-ci:
    set -euxo pipefail
    echo "(./.github/workflows/ci.dhall).Nix" | dhall-to-yaml > .github/workflows/nix.yaml
    echo "(./.github/workflows/ci.dhall).NixBuild" | dhall-to-yaml > .github/workflows/nix-build.yaml
    echo "(./.github/workflows/ci.dhall).Web" | dhall-to-yaml > .github/workflows/web.yaml
    echo "(./.github/workflows/ci.dhall).Docker" | dhall-to-yaml > .github/workflows/docker.yaml
    echo "(./.github/workflows/ci.dhall).Publish-Master-Image" | dhall-to-yaml > .github/workflows/publish-master.yaml
    echo "(./.github/workflows/ci.dhall).Publish-Tag-Image" | dhall-to-yaml > .github/workflows/publish-tag.yaml

# Generate doc/architecture.png from doc/architecture.plantuml
# just doesn't support timestamp based rule, so we keep make for plantuml
# see: https://github.com/casey/just/issues/867
[private]
codegen-doc:
    set -euxo pipefail
    make doc/architecture.png

# Generate HTTP clients and server
[private]
codegen-stubs:
    set -euxo pipefail
    mkdir -p srcgen/
    cabal -fcodegen run monocle-codegen ./schemas/monocle/protob/http.proto ./src/Monocle/Client/Api.hs ./src/Monocle/Servant/HTTP.hs ./srcgen/WebApi.res
    fourmolu -i ./src/Monocle/Client/Api.hs ./src/Monocle/Servant/HTTP.hs
    ./web/node_modules/.bin/bsc -format ./srcgen/WebApi.res > ./web/src/components/WebApi.res
    rm -Rf srcgen/

# Generate haskell data type from protobuf
[private]
codegen-haskell:
    set -euxo pipefail
    for pb in {{PBS}}; do \
      compile-proto-file --includeDir /usr/include --includeDir schemas/ --includeDir ${PROTOBUF_SRC} --proto ${pb} --out codegen/; \
    done
    find codegen/Monocle -type f -name "*.hs" -exec sed -i {} -e '1i{-# LANGUAGE NoGeneralisedNewtypeDeriving #-}' \;
    fourmolu -i codegen/Monocle

# Generate javascript data type from protobuf
[private]
codegen-javascript:
    set -euxo pipefail
    rm -f web/src/messages/*
    for pb in {{PBS}}; do \
      ocaml-protoc {{PINCLUDE}} -bs -ml_out web/src/messages/ schemas/${pb}; \
    done
    python3 ./codegen/rename_bs_module.py ./web/src/messages/

# Generate openapi from protobuf
[private]
codegen-openapi:
    set -euxo pipefail
    protoc {{PINCLUDE}} --openapi_out=./doc/ monocle/protob/http.proto
    echo Created doc/openapi.yaml
