"""Implementation of mcli get runs"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
import textwrap
from enum import Enum
from typing import Any, Dict, List, NamedTuple, Optional, Tuple, cast

from mcli.cli.m_get.display import OutputDisplay, create_display_table
from mcli.config import PAGER_LIMIT, MCLIConfig
from mcli.utils.utils_kube import KubeContext, list_jobs_across_contexts
from mcli.utils.utils_kube_labels import label
from mcli.utils.utils_rich import console


class RunStatus(Enum):
    """Status of an individual run
    """
    FAILED = 'failed'
    QUEUED = 'queued'
    RUNNING = 'running'
    SUCCEEDED = 'succeeded'
    UNKNOWN = 'unknown'


class RunDisplay(NamedTuple):
    """Tuple that extracts run data for display purposes.
    """
    name: str
    instance: str
    sweep: str
    created_time: str
    updated_time: str
    status: RunStatus

    @classmethod
    def from_spec(cls, spec: Dict[str, Any]) -> RunDisplay:
        extracted = {'name': spec['metadata']['name']}
        labels = spec['metadata'].get('labels', {})
        extracted['instance'] = labels.get(label.mosaic.LABEL_INSTANCE, '-')
        extracted['sweep'] = labels.get(label.mosaic.LABEL_SWEEP, '-')

        status = spec.get('status', {})
        created_time_str = '-'
        if status.get('startTime'):
            created_time = dt.datetime.fromisoformat(status['startTime'])
            created_time_str = created_time.strftime('%c')
        extracted['created_time'] = created_time_str
        updated_time_str = '-'
        if status.get('conditions'):
            updated_time = status['conditions'][-1].get('lastProbeTime')
            if updated_time:
                updated_time = dt.datetime.fromisoformat((updated_time))
                updated_time_str = updated_time.strftime('%c')
        extracted['updated_time'] = updated_time_str

        run_status = RunStatus.UNKNOWN
        if status.get('succeeded') == 1:
            run_status = RunStatus.SUCCEEDED
        elif status.get('failed') == 1:
            run_status = RunStatus.FAILED
        extracted['status'] = run_status

        return cls(**extracted)


def _get_runs(run_list: Optional[List[str]] = None,
              instance: Optional[str] = None,
              platform: Optional[str] = None,
              status: Optional[RunStatus] = None,
              sweep: Optional[str] = None,
              output: OutputDisplay = OutputDisplay.TABLE,
              sort_by: str = 'updated_time',
              **kwargs) -> int:
    """Get a table of ongoing and completed runs
    """
    del status
    del kwargs
    if run_list is not None:
        raise NotImplementedError
    with console.status('Retreiving requested runs...'):
        conf = MCLIConfig.load_config()

        # Filter platforms
        if platform is not None:
            chosen_platforms = [p for p in conf.platforms if p.name == platform]
            if not chosen_platforms:
                platform_names = [p.name for p in conf.platforms]
                print(textwrap.dedent(f"""
                                    No runs found. Platform name should be one of {platform_names}, not '{platform}'.

                                    If you think this is an error, try adding the platform using `mcli create platform`.
                                    """),
                      file=sys.stderr)
                sys.exit(1)
        else:
            chosen_platforms = conf.platforms
        contexts = [KubeContext(cluster=p.kubernetes_context, namespace=p.namespace, user='') for p in chosen_platforms]

        labels = {}
        # Filter instances
        if instance is not None:
            labels[label.mosaic.LABEL_INSTANCE] = instance

        # Filter sweep
        if sweep is not None:
            labels[label.mosaic.LABEL_SWEEP] = sweep

        # Query for requested jobs
        all_jobs = list_jobs_across_contexts(contexts=contexts, labels=labels)

    # Exit if no runs were found
    if len(all_jobs) == 0:
        print('No runs found.', file=sys.stderr)
        sys.exit(0)

    # Process data for display
    ## Extract data from specs
    display_runs = [RunDisplay.from_spec(spec) for spec in all_jobs]

    ## Sort runs
    if sort_by == 'updated_time':
        display_runs = sorted(display_runs, key=lambda x: dt.datetime.strptime(x.updated_time, '%c'), reverse=True)

    ## Setup for output
    if output == OutputDisplay.TABLE:
        column_names: List[str] = [c.upper() for c in RunDisplay._fields]
        unzipped = list(zip(*display_runs))
        names: List[str] = cast(List[str], list(unzipped[0]))  # First element is "name", so always str type
        data: List[Tuple[str, str]] = cast(List[Tuple[str, str]], list(zip(*unzipped[1:3])))
        output_table = create_display_table(names=names, columns=data, column_names=column_names)
        if len(display_runs) >= PAGER_LIMIT:
            with console.pager():
                console.print(output_table)
        else:
            console.print(output_table)
    elif output == OutputDisplay.NAME:
        display_names: str = '\n'.join(run.name for run in display_runs)
        if len(display_runs) >= PAGER_LIMIT:
            with console.pager():
                console.print(display_names)
        else:
            console.print(display_names)
    elif output == OutputDisplay.JSON:
        raise NotImplementedError
    return 0


def get_runs_argparser(subparsers):
    """Configures the ``mcli get runs`` argparser
    """
    # mcli get runs
    run_examples: str = """Examples:
    $ mcli get runs

    NAME                         INSTANCE      SWEEP
    run-foo                      inst-g0-type  sweep-foo
    run-bar                      inst-g0-type  sweep-bar
    """
    runs_parser = subparsers.add_parser('runs',
                                        aliases=['run'],
                                        help='Get information on all of your existing runs across all platforms.',
                                        epilog=run_examples,
                                        formatter_class=argparse.RawDescriptionHelpFormatter)
    runs_parser.add_argument('--platform')
    runs_parser.add_argument('--instance')
    runs_parser.add_argument('--sweep')
    runs_parser.add_argument('--output',
                             type=OutputDisplay,
                             choices=list(OutputDisplay),
                             default=OutputDisplay.TABLE,
                             metavar='FORMAT',
                             help=f'Output display format. Should be one of {list(OutputDisplay)}')
    runs_parser.set_defaults(func=_get_runs)
