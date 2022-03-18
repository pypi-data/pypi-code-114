import pathlib
from time import perf_counter, time
from src.isthmuslib.logging import auto_extract_from_file
from src.isthmuslib.utils import human_time

# path_to_test_file = pathlib.Path.cwd() / '..' / 'data' / 'local_only' / '1cshort.txt'
path_to_test_file = pathlib.Path.cwd() / '..' / 'data' / 'local_only' / 'reference_logs_1.txt'
#
# print(f"Starting in serial at {human_time(time())}...")
# tic_1: float = perf_counter()
# times_ns = auto_extract_from_file(path_to_test_file, parallelize_read=False, parallelize_processing=True)
# toc_1: float = perf_counter()
# print(f"... took {toc_1 - tic_1} seconds")


print('-----------------------------------')

for n in [64, 32, 16, 1]:
    print(f"Starting in parallel at {human_time(time())} on {n} CPUs...")
    tic_2: float = perf_counter()
    v = auto_extract_from_file(path_to_test_file, parallelize_read=False, parallelize_processing=n)
    toc_2: float = perf_counter()
    print(f"... took {toc_2 - tic_2} seconds")
