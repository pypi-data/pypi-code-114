"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         process_results = bgisimtool.process_results:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``process_results`` inside your current environment.

References:
    - nope
"""
import dataclasses
import argparse
import logging
import sys
import shutil
import collections
import os

import numpy as np
from bgisimtool.fileUtils import find_file_with_multiple_extension, get_path_minus_n_branch, check_if_list_like
from bgisimtool import __version__
from bgisimtool.ipmsim import IpmsimResult
from bgisimtool.mathfunc import process_vipm_histogram
from bgisimtool.plot_io import plot_vipmprofile_to_File
import pandas as pd
from tqdm import tqdm

__author__ = "Swann Levasseur"
__copyright__ = "Swann Levasseur"
__license__ = "MIT"

process_results_logger = logging.getLogger('bgisimtool.process_results')

# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from bgisimtool.skeleton import fib`,
# when using this Python module as a library.
@dataclasses.dataclass(frozen=True)
class InputTypes:
    file: int = 0
    file_list: int = 1
    file_repo: int = 2
    sweep: int = 3


def check_if_result_file(file):
    # is it a string
    if isinstance(file, str):
        if os.path.splitext(file)[1] == '.csv' or os.path.splitext(file)[1] == '.gz':
            if os.path.exists(file):
                return True
    return False


def check_inputs(file_name_s, log_level=logging.WARNING):
    process_results_logger.setLevel(log_level)
    process_results_logger.info("Checking input.")
    # check if we have only one filename, a list of filenames
    if isinstance(file_name_s, collections.abc.Iterable) and not isinstance(file_name_s, str):
        process_results_logger.info(f"input is a list of {len(file_name_s)} paths.")
        # check each file
        result_path_list = []
        for file in file_name_s:
            if not check_if_result_file(file):
                process_results_logger.warning("Path " + file + " is not a valid result file or does not exist.\n Removing it from input.")
            else:
                result_path_list.append(file)
        # input type, data files, where to place the results
        return InputTypes.file_list, result_path_list, get_path_minus_n_branch(os.path.dirname(file_name_s[0]), 1)
    # check if path is a dir
    elif os.path.isdir(file_name_s):
        process_results_logger.info(f"input is a directory, checking if valid...")
        # check if there is this is a sweep result
        is_res = os.path.isdir(os.path.join(file_name_s, "files/results"))
        is_conf = os.path.isfile(os.path.join(file_name_s, "files/data.csv"))
        result_path_list = find_file_with_multiple_extension(file_name_s, [".gz", 'csv'])
        if is_res and is_conf:
            process_results_logger.info(f"input is a parameter sweep.")
            result_path_list = find_file_with_multiple_extension(os.path.join(file_name_s, "files/results"), [".gz", 'csv'])
            # input type, data files, where to place the results
            return InputTypes.sweep, result_path_list, os.path.join(file_name_s, "files")
        # check if the path contain results files
        elif len(result_path_list) > 0:
            # input type, data files, where to place the results
            return InputTypes.file_repo, result_path_list, get_path_minus_n_branch(file_name_s, 1)
        else:
            process_results_logger.error("Given input is not a recognised type of inputs")
            raise ValueError

    # check if we just have one file
    elif os.path.isfile(file_name_s):
        process_results_logger.info(f"input is a single file.")
        if not check_if_result_file(file_name_s):
            process_results_logger.error("Path " + file_name_s + " is not a valid result file or does not exist.")
            raise ValueError
        else:
            # input type, data files, where to place the results
            return InputTypes.file, [file_name_s], get_path_minus_n_branch(os.path.dirname(file_name_s), 1)
    # the input type is not supported
    else:
        process_results_logger.error("Given input is not a recognised type of inputs")
        raise ValueError


def calc_relative_error(sigma, beam_size):
    return (sigma - beam_size) / beam_size


def calc_error_on_rel_error(sigma, sigma_err, beam_size):
    minim = ((sigma - sigma_err) - beam_size)/beam_size
    maxim = ((sigma + sigma_err) - beam_size)/beam_size
    return (maxim - minim)/2


def get_data_from_results(file_paths,
                          original_beam_size=None,
                          plot=False,
                          plot_location=None,
                          chi_limit=0.01,
                          log_level=logging.WARNING,
                          scale="m",
                          position_bin_width=55e-6,
                          energy_bin_width=10,
                          drift_bin_width=10e-6):
    process_results_logger.setLevel(log_level)
    # if the original beam size is not given
    if original_beam_size is None:
        beam_size = np.zeros(len(file_paths))
    # if the given beam size is a list
    elif check_if_list_like(original_beam_size):
        # check that the list has the same size as the number of file to process.
        if len(original_beam_size) == len(file_paths):
            beam_size = np.array(original_beam_size)
        else:
            process_results_logger.error(f"The length of the list of original beam size " +
                                         f"provided ({len(original_beam_size)})" +
                                         f" does not match the number of results ({len(file_paths)}) to process.")
            beam_size = np.zeros(len(file_paths))
    # if we just have a single value, make an array with them (use the same original beam size for all)
    else:
        beam_size = np.zeros(len(file_paths))
        beam_size = beam_size + original_beam_size
    results = []
    process_results_logger.info(f"Processing {len(file_paths)} dataset.")
    index = 0
    for path in tqdm(file_paths):
        data = IpmsimResult(path, scale=scale,
                            position_bin_width=position_bin_width,
                            energy_bin_width=energy_bin_width,
                            drift_bin_width=drift_bin_width)
        hist_init, exp_init, fit_init, chi_init, success_init = process_vipm_histogram(data.initial_hist)
        hist_final, exp_final, fit_final, chi_final, success_final = process_vipm_histogram(data.final_hist)
        #
        if plot:
            # get file name
            result_file_name_final = os.path.join(plot_location, os.path.basename(path).split('.')[0] + '_final')
            result_file_name_init = os.path.join(plot_location, os.path.basename(path).split('.')[0] + '_init')
            plot_vipmprofile_to_File(hist_final, result_file_name_final, fit_param=fit_final, chi=chi_final,
                             expected_value=exp_final, display_expected=True, exp_err=True, plot_residuals=True)
            plot_vipmprofile_to_File(hist_init, result_file_name_init, fit_param=fit_init, chi=chi_init,
                             expected_value=exp_init, display_expected=True, exp_err=True, plot_residuals=True)
        #
        transmission_factor = data.final_hist.integral / data.initial_hist.integral
        #
        if fit_init is None:
            init_fit_mean = None
            init_fit_sigma_err = None
            init_fit_sigma = None
            init_fit_sigma_err = None
        else:
            init_fit_mean = fit_init[0][1]
            init_fit_sigma_err = fit_init[1][1]
            init_fit_sigma = fit_init[0][2]
            init_fit_sigma_err = fit_init[1][2]
        #
        if fit_final is None:
            final_fit_mean = None
            final_fit_sigma_err = None
            final_fit_sigma = None
            final_fit_sigma_err = None
        else:
            final_fit_mean = fit_final[0][1]
            final_fit_sigma_err = fit_final[1][1]
            final_fit_sigma = fit_final[0][2]
            final_fit_sigma_err = fit_final[1][2]

        if chi_init[1] >= chi_limit:
            init_fit_ok = True
        else:
            init_fit_ok = False

        if chi_final[1] >= chi_limit:
            final_fit_ok = True
        else:
            final_fit_ok = False
        # if the beam size is not provided we use the initial beam size instead
        if beam_size[index] == 0:
            # init
            init_relative_error = None
            init_err_on_rel_err = None
            init_relative_fit_error = None
            init_err_on_rel_fit_err = None
            # final
            final_relative_error = calc_relative_error(hist_final.stdev, hist_init.stdev)
            final_err_on_rel_err = calc_error_on_rel_error(hist_final.stdev, final_relative_error, hist_init.stdev)
            final_relative_error = calc_relative_error(hist_final.stdev, hist_init.stdev)
            final_err_on_rel_err = calc_error_on_rel_error(hist_final.stdev, final_relative_error, hist_init.stdev)
            if fit_final is None or fit_init is None:
                final_relative_fit_error = None
                final_err_on_rel_fit_err = None
            else:
                final_relative_fit_error = calc_relative_error(final_fit_sigma, init_fit_sigma)
                final_err_on_rel_fit_err = calc_error_on_rel_error(final_fit_sigma_err, final_relative_fit_error, init_fit_sigma)

        else:
            # init
            init_relative_error = calc_relative_error(hist_init.stdev, beam_size)
            init_err_on_rel_err = calc_error_on_rel_error(hist_init.stdev, init_relative_error, beam_size)
            if fit_init is None:
                init_relative_fit_error = None
                init_err_on_rel_fit_err = None
            else:
                init_relative_fit_error = calc_relative_error(init_fit_sigma, beam_size)
                init_err_on_rel_fit_err = calc_error_on_rel_error(init_fit_sigma_err, init_relative_fit_error, beam_size)
            # final
            final_relative_error = calc_relative_error(hist_final.stdev, beam_size)
            final_err_on_rel_err = calc_error_on_rel_error(hist_final.stdev, final_relative_error, beam_size)
            if fit_final is None:
                final_relative_fit_error = None
                final_err_on_rel_fit_err = None
            else:
                final_relative_fit_error = calc_relative_error(final_fit_sigma, beam_size)
                final_err_on_rel_fit_err = calc_error_on_rel_error(final_fit_sigma_err, final_relative_fit_error, beam_size)
        # write results
        results.append([hist_init.mean, hist_init.mean_err, hist_init.stdev, hist_init.stdev_err,
                        init_relative_error, init_err_on_rel_err,
                        init_fit_mean, init_fit_sigma_err, init_fit_sigma, init_fit_sigma_err,
                        init_relative_fit_error, init_err_on_rel_fit_err,
                        init_fit_ok, chi_init[1], chi_init[2],
                        hist_final.mean, hist_final.mean_err, hist_final.stdev, hist_final.stdev_err,
                        final_relative_error, final_err_on_rel_err,
                        final_fit_mean, final_fit_sigma_err, final_fit_sigma, final_fit_sigma_err,
                        final_relative_fit_error, final_err_on_rel_fit_err,
                        final_fit_ok, chi_final[1], chi_final[2],
                        data.energy_tot_hist.mean, data.energy_tot_hist.stdev,
                        transmission_factor])
        index +=1
    return pd.DataFrame(results, columns=["init mean", "init mean error", "init stdev", "init stdev error",
                                          "init stdev relative error", "init error on stdev error",
                                          "init fit mean", "init fit mean error", "init fit sigma", "init fit sigma error",
                                          "init fit relative error", "init error on fit error",
                                          "init fit isOk", "init fit Pvalue", "init fit ndf",
                                          "final mean", "final mean error", "final stdev", "final stdev error",
                                          "final stdev relative error", "final error on stdev error",
                                          "final fit mean", "final fit mean error", "final fit sigma",
                                          "final fit sigma error",
                                          "final fit relative error", "final error on fit error",
                                          "final fit isOk", "final fit Pvalue", "final fit ndf",
                                          "mean electron energy", "stdev electron energy",
                                          "average transmission factor"])


def process_vipm_results(input_path,
                         plot=False,
                         log_level=logging.WARNING,
                         original_beam_size=None,
                         scale="m",
                         position_bin_width=55e-6,
                         energy_bin_width=10,
                         drift_bin_width=10e-6
                         ):
    process_results_logger.setLevel(log_level)
    # manage the scale
    input_type, files, result_path = check_inputs(input_path, log_level=log_level)
    process_results_logger.info(f"Will write results in {result_path}.")
    # get path an folder for the plots if needed
    plot_path = os.path.join(result_path, "profile_plots")
    # if we ask for ploting
    # if the folder does not exist, we create it, other wise we erase it and make a new one
    if plot:
        process_results_logger.info(f"Will save plots in {plot_path}.")
        if os.path.exists(plot_path):
            shutil.rmtree(plot_path)
        os.mkdir(plot_path)
    # save it
    data = get_data_from_results(files,
                                 original_beam_size=original_beam_size,
                                 plot=plot,
                                 plot_location=plot_path,
                                 log_level=log_level,
                                 scale=scale,
                                 position_bin_width=position_bin_width,
                                 energy_bin_width=energy_bin_width,
                                 drift_bin_width=drift_bin_width)
    if input_type == InputTypes.sweep:
        meta_data = pd.read_csv(os.path.join(input_path, "files", "data.csv"))
        res = pd.concat([meta_data, data], axis=1)
        res.to_csv(os.path.join(result_path, "processed_data.csv"))
    else:
        # save it
        data.to_csv(os.path.join(result_path, "processed_data.csv"))

# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="A script to process the results from a virtualipm simulation")
    parser.add_argument('input_path', type=str, help='The input path.')
    parser.add_argument('-p', '--plot', action='store_true')
    parser.add_argument(
        '-b',
        '--beam_size',
        dest="beam_size",
        default=None,
        type=float)
    parser.add_argument(
        '-s',
        '--scale',
        dest="scale",
        default='m',
        type=str)
    parser.add_argument(
        '--nrj_bin_width',
        dest="nrj_bin_width",
        default=10,
        type=float)
    parser.add_argument(
        '--drift_bin_width',
        dest="drift_bin_width",
        default=10e-6,
        type=float)
    parser.add_argument(
        '--pos_bin_width',
        dest="pos_bin_width",
        default=55e-6,
        type=float)
    parser.add_argument(
        "--version",
        action="version",
        version="BGISimtool {ver}".format(ver=__version__),
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        default=logging.WARNING,
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
        default=logging.WARNING,
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`fib`, it prints the result to the
    ``stdout`` in a nicely formatted message.

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    process_results_logger.info("Starting processing virtualIPM results")
    if args.scale == "mm":
        position_bin_width = args.pos_bin_width * 1e3
        drift_bin_width = args.drift_bin_width * 1e3
    elif args.scale == "um":
        position_bin_width = args.pos_bin_width * 1e6
        drift_bin_width = args.drift_bin_width * 1e6
    else:
        position_bin_width = args.pos_bin_width
        drift_bin_width = args.drift_bin_width

    process_vipm_results(args.input_path,
                         original_beam_size=args.beam_size,
                         scale=args.scale,
                         plot=args.plot,
                         energy_bin_width=args.nrj_bin_width,
                         drift_bin_width=drift_bin_width,
                         position_bin_width=position_bin_width,
                         log_level=args.loglevel)
    process_results_logger.info("Script ends here")


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m bgisimtool.skeleton 42
    #
    run()