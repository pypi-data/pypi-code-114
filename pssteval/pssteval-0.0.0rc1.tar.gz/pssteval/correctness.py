import logging
import multiprocessing
import os
import time
from argparse import ArgumentParser

import pssteval
from pssteval import logger


def get_args():
    parser = ArgumentParser()
    parser.add_argument("tsv_files", nargs="+")
    parser.add_argument("--out-dir", help="Where to write the analysis. If unspecfied, writes in same dir as tsv_files")
    parser.add_argument("--log-level", default="INFO", choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"))
    return parser.parse_args()


def do_correctness_evaluation(tsv_files, out_dir=None, log_level="INFO"):
    logger.setLevel(log_level)
    for tsv_file in tsv_files:
        analysis = pssteval.evaluate_correctness(tsv_file, log_level=log_level)
        # out_filename = os.path.join(analysis_dir, f"analysis-{split}.json")
        # time.sleep(0.1)
        # analysis.save(out_filename)


def main():
    args = get_args()
    do_correctness_evaluation(**vars(args))


if __name__ == '__main__':
    main()