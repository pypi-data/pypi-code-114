import json
import os
import pathlib
import pkg_resources
from string import Template
from typing import Optional, Tuple

import click
from click import ClickException
from requests import Session

from glean.credentials import CliCredentials

GLEAN_BASE_URI = os.environ.get("GLEAN_CLI_BASE_URI", default="https://glean.io")
VALID_FILE_EXTENSIONS = set([".json", ".yml"])
GLEAN_CLI_VERSION = pkg_resources.get_distribution("glean-cli").version


def login(session: Session, credentials: CliCredentials):
    """Authenticates the session with the provided credentials.

    :return The user's project ID, if successfully logged in.
    :raises ClickException if the login is not successful.
    """
    r = session.post(
        GLEAN_BASE_URI + "/auth/login-cli",
        data={
            "accessKeyId": credentials.access_key_id,
            "accessKeyToken": credentials.access_key_token,
        },
        headers={"Glean-CLI-Version": GLEAN_CLI_VERSION},
    )
    # TODO(dse): Show custom error message from server, if present.
    if r.status_code >= 500:
        raise ClickException("Unexpected error initiating your Glean session.")
    elif r.status_code >= 400:
        raise ClickException("Your access key is invalid.")
    if not r.ok:
        raise ClickException("Unexpected error initiating your Glean session.")

    return credentials.project_id


def create_build_from_git_revision(
    session: Session,
    project_id: str,
    git_revision: Optional[str],
    git_path: Optional[str],
    deploy: bool,
):
    """Creates a build based on a git revision and returns the result."""
    build_spec = {"configFilesFromGit": {"revision": git_revision, "path": git_path}}
    return _create_build(session, project_id, build_spec, deploy)


def create_build_from_local_files(
    session: Session, project_id: str, path: str, deploy: bool, targets: set
):
    """Creates a build using local files and returns the result."""
    build_spec = _build_spec_from_local(path, project_id, targets)
    return _create_build(session, project_id, build_spec, deploy)


def get_model_and_build_summary(
    session: Session,
    datasource_id: str,
    project_id: str,
    **kwargs,
) -> Tuple[dict, dict]:
    build_summary = _model_build_from_db(
        session,
        project_id,
        datasource_id,
        add_all_columns_as_attributes=True,
        **kwargs,
    )

    if "errors" in build_summary:
        click.secho("Error encountered when creating your build: ", fg="red")
        raise RuntimeError(build_summary["errors"][0]["extensions"]["userMessage"])

    model = build_summary["data"]["modelPreviewBuildFromGleanDb"]["resources"]["added"][
        "models"
    ][0]
    model = _format_model(model)
    return model, build_summary


def _format_model(model: dict) -> dict:
    """Get model columns into format needed to generate a config"""
    columns = {}
    for col in model["cols"]:
        columns[col.get("id")] = {k: v for k, v in col.items() if k != "id"}
    model["cols"] = columns
    return model


def get_datasources(s: Session, project_id: str) -> dict:
    """Queries and formats datasources"""
    query = _get_data_connections(s, project_id)
    data_sources = {d["name"]: d["id"] for d in query["data"]["dataConnections"]}
    return data_sources


def _parse_table_names(table_data: dict) -> list:
    """Formats table names for output"""
    tables = table_data["data"]["getAvailableGleanDbTables"]
    table_names = [
        table["schema"] + "." + table["name"] if table["schema"] else table["name"]
        for table in tables
    ]
    return table_names


def _create_build(session, project_id, build_spec, deploy):
    return _graphql_query(
        session,
        """
        mutation CreateBuild($projectId: String!, $buildSpec: BuildSpecInput!, $deploy: Boolean!) {
            createBuild( projectId: $projectId, buildSpec: $buildSpec, deploy: $deploy ) {
                id,
                resources {
                    added { models { name }, savedViews { name }, dashboards { name } }
                    updated { models { name }, savedViews { name }, dashboards { name } }
                    deleted { models { name }, savedViews { name }, dashboards { name } }
                },
                warnings,
                errors
            }
        }
        """,
        {
            "projectId": project_id,
            "buildSpec": build_spec,
            "deploy": deploy,
        },
    )


def _get_data_connections(session: Session, project_id: str) -> dict:
    query = _graphql_query(
        session,
        """
        query dataConnections($projectId: String!){
            dataConnections(projectId: $projectId){
                id,
                name
            }
        }
        """,
        {"projectId": project_id},
    )
    return query


def _get_table_names(session: Session, datasource_id: str) -> dict:
    query = _graphql_query(
        session,
        """ 
        query getAvailableGleanDbTables($datasourceId: String!){
            getAvailableGleanDbTables (datasourceId: $datasourceId){
                name,
                schema
            }
        }
        """,
        {"datasourceId": datasource_id},
    )
    return query


def _model_build_from_db(
    session: Session,
    project_id: str,
    datasource_id: str,
    **kwargs,
) -> dict:
    """
    Queries modelPreviewBuildFromGleanDb controller.
    Returns relevant fields from model needed to generate a data ops config, as well the names of other resources for formatting purposes
    """

    add_all_columns_as_attributes = True
    table_name = kwargs.get("tableName")
    sql_statement = kwargs.get("sqlStatement")
    columns_to_exclude = kwargs.get("columnsToExclude")
    columns_to_include = kwargs.get("columnsToInclude")
    columns_regex = kwargs.get("columnsRegex")

    query = _graphql_query(
        session,
        """
        mutation modelPreviewBuildFromGleanDb(
            $datasourceId: String!, 
            $projectId: String!,
            $tableName: String, 
            $sqlStatement: String,
            $columnsToExclude: [String]
            $columnsToInclude: [String]
            $columnsRegex: String
            $addAllColumnsAsAttributes: Boolean,
            ) {
            modelPreviewBuildFromGleanDb(
                datasourceId: $datasourceId, 
                projectId: $projectId
                tableName: $tableName, 
                sqlStatement: $sqlStatement,
                columnsToExclude: $columnsToExclude,
                columnsToInclude: $columnsToInclude,
                columnsRegex: $columnsRegex,
                addAllColumnsAsAttributes: $addAllColumnsAsAttributes,
                ) {
                id,
                resources {
                    added { 
                        models { 
                            id, 
                            name, 
                            schema,
                            datasource,
                            datasourceId,
                            datasourceName,
                            sqlStatement,
                            physicalName, 
                            primaryDate, 
                            cols { 
                                id, 
                                parentColumnId, 
                                name, 
                                index, 
                                datatype, 
                                type, 
                                physicalName, 
                                aggregate, 
                                metadata{key,value}
                            }
                            },
                        savedViews { name }, dashboards { name } 
                        } 
                    updated { models { name }, savedViews { name }, dashboards { name } } 
                    deleted { models { name }, savedViews { name }, dashboards { name } } 
                },
                warnings,
                errors
            }
        }
        """,
        {
            "datasourceId": datasource_id,
            "projectId": project_id,
            "tableName": table_name,
            "sqlStatement": sql_statement,
            "columnsToExclude": columns_to_exclude,
            "columnsToInclude": columns_to_include,
            "columnsRegex": columns_regex,
            "addAllColumnsAsAttributes": add_all_columns_as_attributes,
        },
    )
    return query


def get_tables(s: Session, datasource_id: str) -> list:
    """Queries and formats table from datasource"""
    query = _get_table_names(s, datasource_id)
    tables = _parse_table_names(query)
    return tables


preview_uri = lambda build_results, query_name="createBuild": click.style(
    f"{GLEAN_BASE_URI}/app/?build={build_results['data'][query_name]['id']}",
    underline=True,
)

build_details_uri = lambda build_results, query_name="createBuild": click.style(
    f"{GLEAN_BASE_URI}/app/p/builds/{build_results['data'][query_name]['id']}",
    underline=True,
)

preview_model_uri = (
    lambda model_id, build_results, query_name="modelPreviewBuildFromGleanDb": f"{GLEAN_BASE_URI}/app/m/{model_id}?build={build_results['data'][query_name]['id']}"
)


def _graphql_query(session: Session, query: str, variables: dict):
    r = session.post(
        GLEAN_BASE_URI + "/graphql/",
        json={"query": query, "variables": variables},
        headers={"Glean-CLI-Version": GLEAN_CLI_VERSION},
    )
    if r.status_code != 200:
        raise ClickException("Unexpected error received from the Glean server.")
    return r.json()


def export_query(
    session: Session, endpoint: str, data: str, additional_headers: dict = {}
):
    """POST request to export controllers"""
    r = session.post(
        GLEAN_BASE_URI + f"/export/{endpoint}",
        data=json.dumps(data),
        headers={"Glean-CLI-Version": GLEAN_CLI_VERSION, **additional_headers},
    )
    if r.status_code != 200:
        raise ClickException("Unexpected error received from the Glean server.")
    return r.text


def _build_spec_from_local(path: str, project_id: str, targets: set = {}) -> dict:
    # Maps parent_directory -> filename -> file contents
    inline_files = []
    for root, subdirs, filenames in os.walk(path):
        for filename in filenames:
            if pathlib.Path(filename).suffix not in VALID_FILE_EXTENSIONS:
                continue
            if targets:
                if filename not in targets:
                    continue
            with open(os.path.join(root, filename), "r") as f:
                # Right now, changing the filepath of a config file changes its generated ID.
                # So, we set parentDirectory here to mimic the format that the server uses
                # when pulling from a git repo.
                parent_directory = root.replace(path, f"/tmp/repos/{project_id}")
                try:
                    file_contents = Template(f.read()).substitute(**os.environ)
                except KeyError as e:
                    raise ClickException(
                        f"No value found for environment variable substitution in {filename}: {str(e)}"
                    )

                inline_files.append(
                    {
                        "parentDirectory": parent_directory,
                        "filename": filename,
                        "fileContents": file_contents,
                    }
                )
    return {"inlineConfigFiles": inline_files}
