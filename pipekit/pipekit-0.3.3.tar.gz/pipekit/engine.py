#!/usr/bin/env python3

import asyncio
import logging

from pipekit.component import ComponentInterrupted

_l = logging.getLogger(__name__)


class ETLEngine:
    """Executor for Workflow instances."""

    def __init__(self, workflow):
        self.workflow = workflow
        self.workflows = workflow.app.workflows

    def run(self):
        loop = asyncio.get_event_loop()
        _l.info(f'Workflow started ({self.workflow.source})')
        loop.run_until_complete(asyncio.gather(*list(
            n.instance.start() for w in self.workflows.values() for n in w.values())))
        _l.info(f'Workflow ended ({self.workflow.source})')
        for task in asyncio.Task.all_tasks():
            try:
                task.get_coro().throw(ComponentInterrupted)
            except (RuntimeError, ComponentInterrupted):
                pass
        # for task in asyncio.Task.all_tasks():
        #     _l.debug(f'*** interrupting task {task}')
        #     try:
        #         if not task.done():
        #             task.get_coro().throw(ComponentInterrupted)
        #     except (RuntimeError, ComponentInterrupted):
        #         pass
        #     _l.debug(f'*** interrupted task {task}')
        # self._report = self.report()
        # _l.debug('*** awaiting tasks')
        # loop.run_until_complete(self._report)
        _l.debug('*** closing loop')
        loop.close()
        _l.debug('*** loop closed')

    async def report(self):
        # await asyncio.wait(list(t for t in asyncio.Task.all_tasks()))
        # return
        for task in asyncio.Task.all_tasks():
            _l.debug(f'*** awaiting task {task}')
            try:
                if (task.exception() or not task.done()) and task.get_coro() is not self._report:
                    await task
            except asyncio.QueueEmpty:
                pass

            except Exception:
                _l.exception(f'*** exception in task {task}')
            _l.debug(f'*** awaited task {task}')
