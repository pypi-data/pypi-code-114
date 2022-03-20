from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Generator, Mapping


class Runner:
    def __init__(self, func, tasks: Mapping[str, Mapping[str, Any]], **kwargs):
        self.func = func
        self.tasks = tasks
        self.kwargs = kwargs

    def run(self) -> Generator[Any, None, None]:
        for key, arguments in self.tasks.items():
            arguments.update(self.kwargs)
            try:
                yield {"task_name": key, "result": self.func(**arguments)}
            except Exception as exc:
                print(exc)
                yield {"task_name": key, "result": None}


class MultiThreadRunner(Runner):
    def __init__(self, func, tasks: Mapping[str, Mapping[str, Any]], threads=None, **kwargs):
        super().__init__(func, tasks, **kwargs)
        self.threads = threads

    def run(self) -> Generator[Any, None, None]:
        with ThreadPoolExecutor(self.threads) as executor:
            futures = {}
            for key, arguments in self.tasks.items():
                arguments.update(self.kwargs)
                futures[executor.submit(self.func, **arguments)] = key

            for ft in as_completed(futures):
                key = futures[ft]
                try:
                    yield {"task_name": key, "result": ft.result()}
                except Exception as exc:
                    print(exc)
                    yield {"task_name": key, "result": None}
