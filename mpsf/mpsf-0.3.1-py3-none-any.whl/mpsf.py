from __future__ import annotations
import time
import datetime
from multiprocessing import Process, Queue
from queue import Empty
from typing import Callable, Iterable


class StopNow:
    """
    Class used to detect when a queue is empty.
    """

    def __repr__(self):
        return 'You have printed the stopper class representation. Well done.'


def worker(queue: Queue, computation_function: Callable, identifier: int, request_delay=5):
    """
    Function responsible for retrieving a data point and passing it on to the computation function.

    :param queue: Queue with data in it.
    :param computation_function: Function that does computation with the data point as input.
    :param identifier: Identifier for the runner, each runner should have a different identifier.
    :param request_delay: If all runners can compute faster than the queue can be populated, this delay will be imposed
    each time the queue is detected to be empty.
    """
    x = queue.get()
    while not isinstance(x, StopNow):
        try:
            computation_function(x)
            x = queue.get()
        except Empty:
            time.sleep(request_delay)
    print(f'Runner {identifier} is done')


def _add_n_data_to_queue(queue: Queue, data_container: iter, missing_count: int, n_workers: int) -> bool:
    """
    Adds new data points to the queue. When the *data_container* is empty each worker is notified to stop when with a
    StopNow class being put into the queue.

    :param queue: Queue to put data into.
    :param data_container: The iterable that contains the data.
    :param missing_count: The number of data points to be put into the queue.
    :param n_workers: The number of workers used. When *data_container* is empty an amount equal to *n_workers* StopNow
    class instances will be put in the queue.
    :return: Boolean denoting if *data_container* is empty.
    """
    for _ in range(missing_count):
        try:
            queue.put(next(data_container))
        except StopIteration:
            for stop_counter in range(n_workers):
                queue.put(StopNow())
            return False
    return True


def _print_reader_progress(t_start: float, data_container: DataParser, max_queue_size: int):
    """
    If the DataParser class is used as a wrapper for the data this function will print the progress.

    :param t_start: The time when the reader started.
    :param data_container: DataParser object with data.
    :param max_queue_size: The maximum queue size - used to calculate time left.
    """
    assert isinstance(data_container, DataParser)
    t_end = time.time()
    dt = t_end - t_start
    dp_read = data_container.counter - max_queue_size
    dp_per_sec = dp_read / dt
    t_left = datetime.timedelta(seconds=(data_container.data_length - dp_read) / dp_per_sec)
    progress_str = data_container.__repr__()
    progress_str += f'. {dp_per_sec:.1f} data points read per second. Approx time left {t_left}'
    print(progress_str)


def populate_queue(queue: Queue, data_container: Iterable, n_workers: int, fill_pause=10, max_queue_size=100):
    """Populates the queue holding the data.

    :param queue: Queue to place data into.
    :param data_container: Iterable that contains data.
    :param n_workers: The number of workers initialized.
    :param fill_pause: The pause between each check of queue size. Made ot not overuse cpu power on a loop with only a
    qsize check. This might not be relevant - I have not tested it.
    :param max_queue_size: The maximum size of the queue - this limits memory used throughout the process."""
    continue_iteration = _add_n_data_to_queue(queue, data_container, max_queue_size, n_workers)
    is_data_parser_class = isinstance(data_container, DataParser)
    if is_data_parser_class:
        t_start = time.time()
        time.sleep(fill_pause)
    while continue_iteration:
        q_size = queue.qsize()
        missing_count = max_queue_size - q_size
        assert missing_count >= 0
        continue_iteration = _add_n_data_to_queue(queue, data_container, missing_count, n_workers)
        if is_data_parser_class:
            _print_reader_progress(t_start, data_container, max_queue_size)
        time.sleep(fill_pause)

    while queue.qsize() > 0:
        print(f'populator is done, current queue size is {queue.qsize()}')
        time.sleep(fill_pause)
    print('Populator is done - data queue is empty')


class DataParser:
    """Class to create an object which count the number of rows that has been retrieved. Note that to use this, the
    total number of data points *data_length* must be known."""

    def __init__(self, data: Iterable, data_length: int):
        self.data_length = data_length
        self.data = data

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.data_length:
            data_row = next(self.data)
            self.counter += 1
            return data_row
        else:
            raise StopIteration

    def __repr__(self):
        repr = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        repr += f' Rows Retrieved = {self.counter} / {self.data_length} ({self.counter / self.data_length:.1%})'
        return repr


def smart_multi_proc(
    work_function: Callable, data: Iterable, n_processes=4, request_delay=5, fill_pause=10, max_queue_size=100
):
    """
    Runs a function where each row in *data* corresponds to one run of the function - meaning the length of data is
    equal to the total number of runs. Data is fed to the function through a pipe, which can hold *max_queue_size**
    objets at a time. The delay before a new input for the function is requested is set with *request_delta* and
    the time between the queue is being refilled is set with *fill_pause*.

    :param work_function: Function to run.
    :param data: Iterator that with __next__() gives the next row of data.
    :param n_processes: The number of concurrent processes.
    :param request_delay: The delay between a function finished with one job and starts a new one.
    :param fill_pause: The delay between each request to refill the pipe with data rows.
    :param max_queue_size: The maximum queue size.
    """
    print(f'Starting multiprocessor using pipe with {n_processes} processes')
    if isinstance(data, DataParser):
        data = iter(data)
    assert isinstance(data, Iterable)

    queue = Queue()
    processes = [None] * (n_processes + 1)  # +1 for queue populator

    p = Process(
        target=populate_queue, args=(queue, data, n_processes, fill_pause, max_queue_size), name='queue populator'
    )
    p.start()
    processes[0] = p

    for p_counter in range(n_processes):
        name = f'func{p_counter}'
        p = Process(
            target=worker,
            args=(
                queue,
                work_function,
                p_counter,
                request_delay,
            ),
            name=name,
        )
        processes[p_counter + 1] = p
        p.start()

    for p in processes:
        p.join()


if __name__ == '__main__':
    import random

    def my_func(x):
        print(f'func val = {x}')
        time.sleep(1)

    n_data_points = 5
    my_data = (i for i in range(n_data_points))
    # print(my_data)
    my_data = iter(DataParser(my_data, n_data_points))
    smart_multi_proc(my_func, my_data, 1, request_delay=1, fill_pause=1)
