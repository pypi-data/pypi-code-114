import os
import time
from multiprocessing import Pool
from typing import List, Callable, Optional

from tqdm import tqdm

from ._to_pickle import save, load

__all__ = ["run_multithread"]


def run_multithread(items: List, function: Callable, threads: int = 4,
                    out_file: Optional[str] = None, dump_time_step: int = 60,
                    force_restart: bool = False) -> List:
    """Run pool of threads applying `function` over the `items`.

    Args:
        items: list of elements to pass to the function.
        function: function to apply to the items.
        threads: number of threads to use (if 0: multiprocessing is disabled, useful to debug).
        out_file: file path where to save the processed data.
        dump_time_step: number of seconds at which is saved a checkpoint of the processed data.
        force_restart: force to process from the beginning and not continue from last checkpoint.
    """
    debug = threads == 0
    threads = 1
    # Load if exists
    if not force_restart and out_file is not None and os.path.exists(out_file):
        computed = load(out_file)
    else:
        computed = []

    # Progress bar
    total_items = len(items)
    progress_bar = tqdm(total=total_items)
    progress_bar.update(len(computed))

    # Begin
    t1 = time.time()
    p_list = []
    for i, param in enumerate(items[len(computed):], len(computed)):
        p_list.append(param)
        if len(p_list) == threads or i == total_items - 1:
            if not debug:
                with Pool(threads) as pool:
                    # Launch pool of threads computing the function
                    all_results = pool.map(function, p_list)
                    computed.extend(all_results)
            else:
                computed.append(function(p_list[0]))
            progress_bar.update(len(p_list))
            p_list = []
        t2 = time.time()

        # Dump each dump_time_step seconds
        if out_file is not None and (t2 - t1) > dump_time_step:
            save(computed, out_file)
            t1 = time.time()
    if out_file is not None:
        save(computed, out_file)
    return computed
