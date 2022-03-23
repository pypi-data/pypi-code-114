import json
from typing import Dict, List, Optional, Tuple

from dbt_utils.dbt_runner import get_downstream_models
from parsers.manifest import Manifest
from parsers.run_result import RunResult, RunResultType

SlackMessageBody = Tuple[List[Dict], int]


def _build_slack_message_header(len_results: int, fail_cnt: int) -> Dict:
    pass_cnt = len_results - fail_cnt
    return {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":dbt: Failures :dbt:",
                    "emoji": True,
                },
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "plain_text",
                        "text": f":green-circle: Pass: {pass_cnt}",
                        "emoji": True,
                    },
                    {
                        "type": "plain_text",
                        "text": f":red_circle: Failures: {fail_cnt}",
                        "emoji": True,
                    },
                ],
            },
            {"type": "divider"},
        ]
    }


def _build_run_message(
    result: RunResult, innvocation_id: str, storage_location: str, footer: str
) -> List[Dict]:
    downstream_models = get_downstream_models(result.table_name)
    compiled_sql_link = f"{storage_location}/{innvocation_id}-run/run/{result.manifest.package_name}/{result.manifest.original_file_path}"
    return [
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f":redsiren: *Critcal Model Failure: {result.table_name}* :redsiren:",
            },
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Compiled SQL", "emoji": True},
                "value": f"{result.table_name}",
                "url": f"{compiled_sql_link}",
                "action_id": "button-action",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f":warning: *Impacts {len(downstream_models)} models, which will not be updated until the error is resolved*",
            },
        },
        {"type": "divider"},
        {"type": "section", "text": {"type": "mrkdwn", "text": f"{result.message}"}},
        {"type": "divider"},
        {"type": "context", "elements": [{"type": "mrkdwn", "text": f"{footer}"}]},
        {"type": "divider"},
    ]


def _build_test_message(
    result: RunResult, innvocation_id: str, storage_location: str, footer: str
) -> List[Dict]:
    test_name = result.table_name if result.test_name is not None else result.test_name
    compiled_sql_link = f"{storage_location}/{innvocation_id}-test/run/{result.manifest.package_name}/{result.manifest.original_file_path}{'/' + result.manifest.path if result.manifest.resource_type == 'generic test' else ''}"
    test_result_message = (
        f"Check: {result.test_name}\n{result.message}"
        if result.test_name is not None
        else f"{result.message}"
    )
    return [
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f":test_tube: *Test Failure: {test_name}* :test_tube:",
            },
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Compiled SQL", "emoji": True},
                "value": f"{test_name}",
                "url": f"{compiled_sql_link}",
                "action_id": "button-action",
            },
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"{test_result_message}"},
        },
        {"type": "divider"},
        {"type": "context", "elements": [{"type": "mrkdwn", "text": f"{footer}"}]},
        {"type": "divider"},
    ]


def _build_freshness_message(
    result: RunResult, innvocation_id: str, storage_location: str, footer: str
) -> List[Dict]:
    return [
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f":clock1: *Model Freshness: {result.table_name}* :clock1:",
            },
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"Stale Data: {result.message}"},
        },
        {"type": "divider"},
        {"type": "context", "elements": [{"type": "mrkdwn", "text": f"{footer}"}]},
        {"type": "divider"},
    ]


def _build_slack_message_body(
    results: List[RunResult], dag_name: str, innvocation_id: str, storage_location: str
) -> SlackMessageBody:

    message_parts = []
    failure_count = 0

    for result in results:
        if not result.is_success:
            failure_count += 1

            team_ownership_text = (
                f"{result.manifest.owner} "
                f"( <!subteam^{result.manifest.slack_support_group_id}> )"
                if result.manifest.owner is not None
                else "WARNING: No assigned team"
            )

            footer = (
                f"Execution time: {round(result.execution_time, 4)}s\n"
                f"Owner | {team_ownership_text}\n"
                f"DAG name | {dag_name}"
            )

            if result.run_type == RunResultType.Model:
                message_parts += _build_run_message(
                    result, innvocation_id, storage_location, footer
                )

            if result.run_type == RunResultType.Test:
                message_parts += _build_test_message(
                    result, innvocation_id, storage_location, footer
                )

            if result.run_type == RunResultType.Freshness:
                message_parts += _build_freshness_message(
                    result, innvocation_id, storage_location, footer
                )

    return message_parts, failure_count


def build_slack_message(
    dag_name: str, results: List[RunResult], invocation_id: str, storage_location: str
) -> Optional[str]:
    """
    Build a slack message blob from the raw dbt results
    """
    body, failure_count = _build_slack_message_body(
        results, dag_name, invocation_id, storage_location
    )
    # print(body)
    header = _build_slack_message_header(len(results), failure_count)
    header["blocks"] += body

    return json.dumps({**header}) if failure_count else None


def lookup_team_info(
    manifest: Dict[str, Manifest], unique_id: str
) -> Tuple[Optional[str], Optional[str]]:
    dbt_item = manifest[unique_id]
    return dbt_item.owner, dbt_item.slack_support_group_id
