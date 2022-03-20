#!/usr/bin/python

import numpy as np
import gfort2py as gf

import tracemalloc
import os
import linecache


def display_top(snapshot, key_type="lineno", limit=3):
    snapshot = snapshot.filter_traces(
        (
            tracemalloc.Filter(False, ""),
            tracemalloc.Filter(False, ""),
        )
    )
    top_stats = snapshot.statistics(key_type)
    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print(
            "#%s: %s:%s: %.1f KiB" % (index, filename, frame.lineno, stat.size / 1024)
        )
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print("    %s" % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


SHARED_LIB_NAME = "./memory_leak.so"
MOD_FILE_NAME = "memory_leak.mod"

x = gf.fFort(SHARED_LIB_NAME, MOD_FILE_NAME)

numloops = 10
dim = 3000
arr_test = np.random.rand(dim, dim)
print(arr_test[0, 0])

tracemalloc.start()
for ii in np.arange(numloops):

    print("python %d" % ii)
    y1 = x.set_param_defaults(
        arr_test, {"simtype": 2, "l0": 0, "field_int_on_currently": True}
    )

    snapshot = tracemalloc.take_snapshot()
    display_top(snapshot)

    # print('returned allocatable array')
    # print(y1.args['alloc_test'])

    arr_test = y1.args["alloc_test"]
    print("python kb: %f" % (arr_test.nbytes / 1024))
    print(arr_test[0, 0])
    print("\n")
