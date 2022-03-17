# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Implement software testing life-cycle."""
# TODO: refactor to dynamically populate tasks

import logging
import os
from dataclasses import asdict
from pprint import pprint
from typing import TYPE_CHECKING

from invoke import Executor, task

# TODO: switch to executor
from proman_workflows import formatter, package, qa, sca, system
from proman_workflows.collection import Collection
from proman_workflows.config import (  # Plugin,
    Job,
    Phase,
    ProjectConfig,
    WorkflowConfig,
)

if TYPE_CHECKING:
    from invoke import Context

logging.getLogger(__name__).addHandler(logging.NullHandler())


def execute(
    ctx, collection, task_name
):  # type: (Context, Collection, str) -> None
    """Execute tasks within collection."""
    for x in ctx.phases:
        print(x)
    config = [p for p in ctx.phases if p['name'] == task_name][0]
    jobs = [(j['command'], j['args']) for j in config['jobs']]
    try:
        Executor(
            collection,
            config=WorkflowConfig(ctx.config),
        ).execute(*jobs)
    except Exception as err:
        print(err)


@task
def static_analysis(ctx):  # type: (Context) -> None
    """Perform static code analysis."""
    if 'plugins' in ctx:
        pprint(ctx.plugins)
    else:
        pprint(ctx.config.__dict__)
    print('task names', sca.namespace.task_names)
    # Executor(
    #     sca.namespace,
    #     config=WorkflowConfig(ctx.config)
    # ).execute('package.publish')
    execute(ctx, collection=sca.namespace, task_name='static-analysis')


@task(name='style')
def formatting(ctx):  # type: (Context) -> None
    """Perform install."""
    print('tasks', formatter.namespace.task_names)
    execute(ctx, collection=formatter.namespace, task_name='formatter')


@task
def install(ctx):  # type: (Context) -> None
    """Perform install."""
    execute(ctx, collection=package.namespace, task_name='install')


@task
def build(ctx):  # type: (Context) -> None
    """Perform build."""
    execute(ctx, collection=package.namespace, task_name='build')


@task
def unit_test(ctx):  # type: (Context) -> None
    """Perform unit-testing."""
    print(qa.namespace.task_names)
    # pprint(ctx.config.__dict__['_defaults']['plugins'])
    ctx.project_dir = os.path.join(os.getcwd(), 'tests')
    execute(ctx, collection=qa.namespace, task_name='unit-test')


@task
def integration_test(ctx):  # type: (Context) -> None
    """Perform integration testing."""
    print(qa.namespace.task_names)
    ctx.project_dir = os.path.join(os.getcwd(), 'integration')
    execute(ctx, collection=qa.namespace, task_name='integration-test')


@task
def system_test(ctx):  # type: (Context) -> None
    """Perform system testing."""
    print(system.namespace.task_names)
    execute(ctx, collection=system.namespace, task_name='system-test')


@task
def acceptance_test(ctx):  # type: (Context) -> None
    """Perform acceptance testing."""
    execute(ctx, collection=qa.namespace, task_name='acceptance-test')


@task
def publish(ctx):  # type: (Context) -> None
    """Publish package."""
    print(package.namespace.task_names)
    Executor(
        package.namespace,
        config=WorkflowConfig(ctx.config),
    ).execute('package.publish')


project_config = ProjectConfig(
    # plugins=[
    #     Plugin(
    #         name='poetry',
    #         driver_name='package',
    #         driver_namespace='proman_workflows.package.poetry',
    #     ),
    #     Plugin(
    #         name='vcs',
    #         driver_name='git',
    #         driver_namespace='proman.workflows.vcs',
    #     ),
    #     Plugin(
    #         name='sort-headers',
    #         driver_name='isort',
    #         driver_namespace='proman.workflows.formatter',
    #     ),
    #     Plugin(
    #         name='format',
    #         driver_name='black',
    #         driver_namespace='proman.workflows.formatter',
    #     ),
    #     Plugin(
    #         name='unit-tests',
    #         driver_name='pytest',
    #         driver_namespace='proman.workflows.unit_tests',
    #     ),
    # ],
    phases=[
        Phase(
            name='install',
            plugins=['poetry'],
            jobs=[Job(command='poetry.install', args={})],
        ),
        Phase(
            name='formatter',
            jobs=[
                Job(command='sort-headers.run', args={}),
                Job(command='format.run', args={}),
            ],
        ),
        Phase(
            name='static-analysis',
            jobs=[
                Job(command='lint.run', args={}),
                Job(command='type-checking.run', args={}),
            ],
        ),
        Phase(
            name='build',
            plugins=['poetry'],
            jobs=[Job(command='poetry.build', args={})],
        ),
        Phase(
            name='unit-test',
            jobs=[Job(command='unit-test.run', args={})],
        ),
        Phase(
            name='acceptance-test',
            jobs=[Job(command='acceptance-test.run', args={})],
        ),
        Phase(
            name='integration-test',
            jobs=[Job(command='unit-test.run', args={})],
        ),
        Phase(
            name='system-test',
            jobs=[Job(command='system-test.run', args={})],
        ),
        Phase(
            name='publish',
            plugins=['poetry'],
            jobs=[Job(command='poetry.publish', args={})],
        ),
        # Phase(
        #     name='deploy',
        #     plugins=['ansible'],
        #     jobs=[Job(command='system.run', args={})],
        # ),
    ]
)
namespace = Collection(
    formatting,
    install,
    static_analysis,
    build,
    unit_test,
    acceptance_test,
    integration_test,
    system_test,
    publish,
)
# pprint(asdict(project_config))
namespace.configure(asdict(project_config))
# namespace.load_collections()

__all__ = ['namespace']
