// Copyright (C) 2021 Monocle authors
// SPDX-License-Identifier: AGPL-3.0-or-later
//
// The change component
//

open Prelude

module TaskData = {
  type t = TaskDataTypes.new_task_data

  module TaskType = {
    @react.component
    let make = (~ttype: string) => <Patternfly.Label> {ttype->str} </Patternfly.Label>
  }

  module TaskPS = {
    let getLabelColor = (level: string) =>
      switch level {
      | "urgent" => #Purple
      | "high" => #Red
      | "medium" => #Orange
      | "low" => #Green
      | _ => #Green
      }
    @react.component
    let make = (~ps, ~name) => {
      let label = name ++ ": " ++ ps
      <Patternfly.Label color={ps->getLabelColor}> {label} </Patternfly.Label>
    }
  }

  module TaskScore = {
    @react.component
    let make = (~score) => {
      let label = "Score: " ++ string_of_int(Int32.to_int(score))
      <Patternfly.Label> {label} </Patternfly.Label>
    }
  }

  module TaskLink = {
    @react.component
    let make = (~td: TaskDataTypes.new_task_data) =>
      switch td.url {
      | url if Js.String.indexOf("show_bug.cgi", url) >= 0 =>
        <a href=url> <Patternfly.Icons.ExternalLinkAlt /> {(" rhbz#" ++ td.tid)->str} </a>
      | url => <a href=url> {url->str} </a>
      }
  }

  @react.component
  let make = (~td: t) => {
    <>
      {"Task: "->str}
      <TaskLink td />
      <TaskPS ps=td.priority name="Priority" />
      <TaskPS ps=td.severity name="Severity" />
      <TaskScore score=td.score />
      <Patternfly.LabelGroup categoryName="Type">
        {td.ttype->Belt.List.map(x => <TaskType ttype={x} />)->Belt.List.toArray->React.array}
      </Patternfly.LabelGroup>
    </>
  }
}

module Search = {
  module Info = {
    @react.component
    let make = (~name, ~value) =>
      <DescriptionListGroup>
        <DescriptionListTerm> {name->str} </DescriptionListTerm>
        <DescriptionListDescription> {value->str} </DescriptionListDescription>
      </DescriptionListGroup>
  }
  @react.component
  let make = (~change: SearchTypes.change) =>
    <DataListItemRow key={change.url}>
      <DataListCell>
        <Card>
          <CardHeader> <Label> {change.state->str} </Label> {change.title->str} </CardHeader>
          <CardBody>
            <DescriptionList isHorizontal={true}>
              <Info name="Repository" value={change.repository_fullname} />
              <Info name="Branch" value={change.branch} />
              <Info name="URL" value={change.url} />
            </DescriptionList>
          </CardBody>
          <CardFooter>
            {change.task_data->Belt.List.map(td => <TaskData td />)->Belt.List.toArray->React.array}
          </CardFooter>
        </Card>
      </DataListCell>
    </DataListItemRow>
}
