import multiprocessing
import os
from argparse import ArgumentParser

import regex

import pssteval
from pssteval import logger


def get_args():
    parser = ArgumentParser()
    parser.add_argument("tsv_files", nargs="+")
    parser.add_argument("--out-dir", help="Where to write the analysis. If unspecfied, writes in same dir as tsv_files")
    parser.add_argument("--n-jobs", type=int, default=multiprocessing.cpu_count() - 1)
    parser.add_argument("--log-level", default="INFO", choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"))
    return parser.parse_args()


def do_asr_evaluation(tsv_files, out_dir, n_jobs=None, log_level="INFO"):
    if out_dir:
        out_dir = os.path.expanduser(out_dir)
    n_jobs = n_jobs or multiprocessing.cpu_count() - 1
    logger.setLevel(log_level)
    for tsv_file in tsv_files:
        analysis = pssteval.evaluate_asr(tsv_file, n_jobs=n_jobs, log_level=log_level)
        out_filename = os.path.join(
            out_dir or os.path.dirname(tsv_file),
            regex.sub("\.\w+", "-analysis.json", os.path.basename(tsv_file))
        )
        assert os.path.abspath(out_filename) != os.path.abspath(tsv_file), f"Unexpected filename: {tsv_file}, add .json extension?"
        analysis.save(out_filename)
        logger.info(f"Wrote analysis to {out_filename}")


def main():
    args = get_args()
    do_asr_evaluation(**vars(args))


if __name__ == '__main__':
    main()