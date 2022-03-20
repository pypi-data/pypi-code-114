from pathlib import Path

from typer import Typer, Option

from ldflex import LDFlex
from octadocs.cli.formatters.csv import csv_print
from octadocs.cli.formatters.json import print_json
from octadocs.cli.formatters.pretty import pretty_print
from octadocs.conversions import src_path_to_iri
from octadocs.storage import load_graph
from octadocs.types import QueryResultsFormat

app = Typer(name='show')


def find_docs_dir() -> Path:
    """Find the docs dir of the MkDocs site."""
    cwd = Path.cwd()

    while True:
        docs = cwd / 'docs'
        if docs.is_dir():
            return docs

        cwd = cwd.parent


@app.command(name='file')
def show_file(
    path: Path,
    fmt: QueryResultsFormat = Option(
        default=QueryResultsFormat.PRETTY,
        metavar='format',
    ),
):
    """Show graph from a file."""
    docs_dir = find_docs_dir()
    path = path.absolute().relative_to(docs_dir)

    iri = src_path_to_iri(str(path))

    graph = load_graph(Path.cwd() / '.cache/octadocs')
    ldflex = LDFlex(graph)

    query_result = ldflex.query(
        '''
        SELECT ?s ?p ?o WHERE {
            GRAPH ?g {
                ?s ?p ?o
            }
        }
        ''',
        g=iri,
    )

    {
        QueryResultsFormat.CSV: csv_print,
        QueryResultsFormat.PRETTY: pretty_print,
        QueryResultsFormat.JSON: print_json,
    }[fmt](query_result)   # type: ignore
