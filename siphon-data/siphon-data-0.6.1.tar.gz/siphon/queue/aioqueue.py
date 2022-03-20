import asyncio
import csv
import functools
import json
from asyncio import Queue
from typing import (IO, Any, AsyncGenerator, Callable, Coroutine, Dict,
                    Generator, List, Optional, Tuple, Type, Union)

from siphon.queue import violations
from siphon.queue.types import DataT


class AioQueue(Queue):
    async def wait_for_consumer(self):
        """
        Queue.join is a terrible name for what it does which is wait until all tasks on the queue
        have been processed. This is just a method with a more obvious name that mimics join.
        """
        await self.join()

    def add_consumer(self, callback: Union[Callable, Coroutine]) -> asyncio.Task:
        task = asyncio.create_task(self._consumer(callback))
        return task

    async def _consumer(self, callback: Union[Callable, Coroutine]):
        while True:
            val = await self.get()
            if asyncio.iscoroutinefunction(callback):
                await callback(val)
            else:
                callback(val)
            self.task_done()

    def collect(self, transform: Optional[Callable] = None):
        return [
            transform(self.get_nowait()) if transform else self.get_nowait()
            for _ in range(self.qsize())
        ]

    async def __aiter__(self) -> AsyncGenerator:
        for _ in range(self.qsize()):
            row = await self.get()
            yield row

    def to_json(
        self,
        path: Union[str, bytes, IO],
        pre_transform: Optional[Callable] = None,
        mode: str = 'w',
        **kwargs,
    ) -> str:
        with open(path, mode, **kwargs) as file:
            json.dump(self.collect(pre_transform), file)
            return path

    def to_csv(
        self,
        path: Union[str, bytes, IO],
        cols: List[str],
        pre_transform: Optional[Callable] = None,
        mode: str = 'w',
        **kwargs,
    ) -> str:
        with open(path, mode, **kwargs) as file:
            writer = csv.DictWriter(file, fieldnames=cols)
            writer.writeheader()
            for row in self:
                if pre_transform:
                    writer.writerow(pre_transform(row))
                else:
                    writer.writerow(row)
            return path

    def __iter__(self) -> Generator:
        for _ in range(self.qsize()):
            yield self.get_nowait()


class TypedAioQueue(AioQueue):
    def __init__(
        self,
        model: DataT = None,
        violations_strategy: Type[violations.ViolationStrategy] = violations.RaiseOnViolation,
        maxsize: int = 0,
    ):
        self._model = model
        self._check_for_violation = violations_strategy()
        super().__init__(maxsize=maxsize)

    def _put(self, item: Dict):
        if self._model:
            new = self._check_for_violation(item, self._model)
            if new:
                return super()._put(new)


class CollectedError:
    def __init__(self, func: Callable, error: Exception, args: Tuple[Any], kwargs: Dict):
        self.func = func
        self.initial_error = error
        self.args = args
        self.kwargs = kwargs
        self.retries = 0

    @property
    def reraise(self):
        raise self.initial_error

    @property
    def error_name(self) -> str:
        return self.initial_error.__class__.__name__

    @property
    def func_name(self) -> str:
        return self.func.__name__

    def __repr__(self) -> str:
        return f'CollectedError({self.func_name}:{self.initial_error.__str__()})'


def queuecollect(errors: Queue, success: Queue = None):
    """
    Collect outputs from a function/coroutine and optionally write to a Queue for both errors and
    successes. Why is this useful? Mostly it is used as part of a pipeline from aiostream library.
    The idea is that in a pipeline, rather than stopping execution of a pipeline due to an error,
    you would instead want to defer dealing with error until later, and continue to process any
    items that are successful. This helps you achieve that by catching any errors and instead of
    raising them, we write them to a queue. Successes can also be optionally written to a queue
    instead of being returned. Although you should note that if a value is written to the queue,
    the subsequent steps in the pipeline won't receive these values.
    Examples:
        from aiostream import stream, pipe
        import asyncio
        failed = asyncio.Queue()

        @queuecollect(errors=failed)
        def fail_on_five(i: int):
            if i == 5:
                raise Exception("I am a five")
            else:
                return i

        pipeline = stream.range(10) | pipe.map(fail_on_five)

        # len(output) == 9; len(failed.collect()) == 1;
        output = await pipeline

    Args:
        errors: An asyncio.Queue to write any exceptions to. Errors are wrapped in a CollectQueue
        object for context
        success: An asyncio.Queue to write successful outputs to. Optional:
        Defaults to None. If None, we return the output value as normal
    Returns: Wrapped func
    """

    def wrapper(func):
        @functools.wraps(func)
        async def inner(*args, **kwargs):
            try:
                if asyncio.iscoroutinefunction(func):
                    result = await func(*args, **kwargs)
                else:
                    result = func(*args, **kwargs)
                if success:
                    success.put_nowait(result)
                else:
                    return result
            except Exception as err:
                await errors.put(CollectedError(func=func, error=err, args=args, kwargs=kwargs))

        return inner

    return wrapper
