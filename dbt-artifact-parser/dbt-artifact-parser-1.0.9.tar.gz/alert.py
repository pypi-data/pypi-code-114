import os

from bigquery.bigquery import save_test_results
from message.builder import build_slack_message
from parsers.manifest_parser import ManifestParser
from parsers.parse_run_results import DbtResultsLogFactory
from slack.client import Slack

SLACK_HOST = os.environ.get("SLACK_HOST")
SLACK_CHANNEL = os.environ.get("SLACK_CHANNEL")
DAG = os.environ.get("DAG")
STAGE = os.environ.get("STAGE")
UNIQUE_RUN_ID = os.environ.get("UNIQUE_RUN_ID")
ARTEFACT_STORAGE_LOCATION = os.environ.get("ARTEFACT_STORAGE_LOCATION")
PATH_RUN_RESULTS = "./target/run_results.json"
PATH_MANIFEST = "./target/manifest.json"
PATH_FRESHNESS = "./target/sources.json"

log_factory = DbtResultsLogFactory()
manifest_parser = ManifestParser()

if SLACK_HOST is not None and SLACK_CHANNEL is not None:
    slack = Slack(SLACK_HOST, SLACK_CHANNEL)


def trigger():
    manifest = {}
    print(f"Does manifest file exist? {os.path.exists(PATH_MANIFEST)}")
    with open(PATH_MANIFEST) as manifest_file:
        print("Reading manifest.json file...")
        manifest = manifest_parser.parse(manifest_file.read())
        print("Completed")

    with open(PATH_RUN_RESULTS) as results_file:
        print("Reading run_results.json...")
        results = log_factory.build_results(results_file.read(), manifest)
        print("Completed")

        message = None
        if DAG is not None and UNIQUE_RUN_ID is not None:
            print("Building Slack message...")
            message = build_slack_message(
                DAG, results, UNIQUE_RUN_ID, ARTEFACT_STORAGE_LOCATION
            )  # noqa
            print("Completed")

        if message is not None:
            print(message)
            slack.alert(message)

    if os.path.exists(PATH_FRESHNESS):
        print("Freshness check exists, processing...")
        with open(PATH_FRESHNESS) as freshness_file:
            freshness_results = log_factory.build_results(
                freshness_file.read(), manifest
            )
            results.extend(freshness_results)

            message = None
            if DAG is not None and UNIQUE_RUN_ID is not None:
                message = build_slack_message(
                    DAG, freshness_results, UNIQUE_RUN_ID, ARTEFACT_STORAGE_LOCATION
                )  # noqa

            if message is not None:
                print(message)
                slack.alert(message)

    if UNIQUE_RUN_ID is not None:
        save_test_results(UNIQUE_RUN_ID, results)


if __name__ == "__main__":
    trigger()
