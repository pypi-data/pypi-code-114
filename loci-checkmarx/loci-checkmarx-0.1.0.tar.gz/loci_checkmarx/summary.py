import click
import loci_checkmarx.utils as lcu


def get_text(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


@click.command()
@click.option("-i", "--input-file",
              prompt="Checkmarx XML file",
              help="The Checkmarx XML file with the output of a scan",
              required=True,
              type=str)
def summary(input_file):
    """Summarize a Checkmarx XML file"""
    results_list = lcu.open_results_file_and_get_results(input_file)

    lcu.print_info(f"Summary for Results of [bold]{input_file}[/bold]:")
    total_results = len(results_list)
    lcu.print_info(f"  Total issues: {total_results}")
    lcu.print_info("-----------------------------------------------")

    results_by_sev_dict = {}
    results_by_sev_dict["High"] = []
    results_by_sev_dict["Medium"] = []
    results_by_sev_dict["Low"] = []
    results_by_sev_dict["Information"] = []

    for result in results_list:
        results_by_sev_dict[result.severity].append(result)

    for current_sev in ["High", "Medium", "Low", "Information"]:
        lcu.print_info(f"  {current_sev}-severity issues: {len(results_by_sev_dict[current_sev])}")

        result_count = {}
        for result in results_by_sev_dict[current_sev]:
            try:
                result_count[result.query_name]
            except KeyError:
                result_count[result.query_name] = 0
            result_count[result.query_name] += 1

        for w in sorted(result_count, key=result_count.get, reverse=True):
            lcu.print_info(f"    x[bold]{result_count[w]}[/bold] {w}")

        lcu.print_info("----------------------------------------------")

    lcu.print_success("Results summarized.")
