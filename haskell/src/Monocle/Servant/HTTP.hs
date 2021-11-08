{-# LANGUAGE DataKinds #-}

-- Generated by monocle-codegen. DO NOT EDIT!

-- |
-- Copyright: (c) 2021 Monocle authors
-- SPDX-License-Identifier: AGPL-3.0-only
module Monocle.Servant.HTTP (MonocleAPI, server) where

import Monocle.Api.Server (configGetAbout, configGetProjects, configGetWorkspaces, crawlerAddDoc, crawlerCommit, crawlerCommitInfo, searchCheck, searchFields, searchQuery, searchSuggestions, userGroupGet, userGroupList)
import Monocle.Config (GetAboutRequest, GetAboutResponse, GetProjectsRequest, GetProjectsResponse, GetWorkspacesRequest, GetWorkspacesResponse)
import Monocle.Crawler (AddDocRequest, AddDocResponse, CommitInfoRequest, CommitInfoResponse, CommitRequest, CommitResponse)
import Monocle.Env
import Monocle.Search (CheckRequest, CheckResponse, FieldsRequest, FieldsResponse, QueryRequest, QueryResponse, SuggestionsRequest, SuggestionsResponse)
import Monocle.Servant.PBJSON (PBJSON)
import Monocle.UserGroup (GetRequest, GetResponse, ListRequest, ListResponse)
import Servant

type MonocleAPI =
  "get_workspaces" :> ReqBody '[JSON] GetWorkspacesRequest :> Post '[PBJSON, JSON] GetWorkspacesResponse
    :<|> "get_projects" :> ReqBody '[JSON] GetProjectsRequest :> Post '[PBJSON, JSON] GetProjectsResponse
    :<|> "about" :> ReqBody '[JSON] GetAboutRequest :> Post '[PBJSON, JSON] GetAboutResponse
    :<|> "suggestions" :> ReqBody '[JSON] SuggestionsRequest :> Post '[PBJSON, JSON] SuggestionsResponse
    :<|> "search" :> "fields" :> ReqBody '[JSON] FieldsRequest :> Post '[PBJSON, JSON] FieldsResponse
    :<|> "search" :> "check" :> ReqBody '[JSON] CheckRequest :> Post '[PBJSON, JSON] CheckResponse
    :<|> "search" :> "query" :> ReqBody '[JSON] QueryRequest :> Post '[PBJSON, JSON] QueryResponse
    :<|> "user_group" :> "list" :> ReqBody '[JSON] ListRequest :> Post '[PBJSON, JSON] ListResponse
    :<|> "user_group" :> "get" :> ReqBody '[JSON] GetRequest :> Post '[PBJSON, JSON] GetResponse
    :<|> "crawler" :> "add" :> ReqBody '[JSON] AddDocRequest :> Post '[PBJSON, JSON] AddDocResponse
    :<|> "crawler" :> "commit" :> ReqBody '[JSON] CommitRequest :> Post '[PBJSON, JSON] CommitResponse
    :<|> "crawler" :> "get_commit_info" :> ReqBody '[JSON] CommitInfoRequest :> Post '[PBJSON, JSON] CommitInfoResponse

server :: ServerT MonocleAPI AppM
server =
  configGetWorkspaces
    :<|> configGetProjects
    :<|> configGetAbout
    :<|> searchSuggestions
    :<|> searchFields
    :<|> searchCheck
    :<|> searchQuery
    :<|> userGroupList
    :<|> userGroupGet
    :<|> crawlerAddDoc
    :<|> crawlerCommit
    :<|> crawlerCommitInfo
