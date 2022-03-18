import argparse
import os
from os.path import isfile, join

from nerblackbox.modules.utils.env_variable import env_variable

# TODO: the following is a workaround
BASE_DIR = os.getcwd()
os.environ["BASE_DIR"] = BASE_DIR
os.environ["DATA_DIR"] = join(BASE_DIR, "data")


def main(_args):
    """
    :return: -
    """
    if len(_args.benchmark_path) == 0:
        benchmark_path = join(
            env_variable("DIR_EXPERIMENT_CONFIGS"),
            "benchmark_experiments",
            "benchmark_experiments.ini",
        )
    else:
        benchmark_path = _args.benchmark_path
    assert isfile(
        benchmark_path
    ), f"ERROR! benchmark_path = {benchmark_path} not found."

    _parse_benchmark_experiment_file(benchmark_path)


def _parse_benchmark_experiment_file(_benchmark_path: str):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--benchmark_path", type=str, default="")
    _args = parser.parse_args()

    main(_args)
