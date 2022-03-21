# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from __future__ import annotations

import argparse
import logging
import logging.config
import os
import pathlib

from availsim4core._version import __version__

LOGGING_CONFIG_FILE = '/logging/logging.conf'


def logger_config(debug: bool, output_folder: str) -> str:
    """
    Loads the configuration from the `LOGGING_CONFIG_FILE`.
    :param debug: If set the root logger level is set to debug
    :param output_folder: the output folder where the log will be written.
    :return: The path of the first `FileHandler` where the logs are written.
    """
    # using logging namespace
    logging.output_folder = output_folder
    
    path = pathlib.Path(__file__).parent.absolute()
    logging.config.fileConfig(f"{path}{LOGGING_CONFIG_FILE}")
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
    return next((handler.baseFilename
                 for handler in logging.getLogger().handlers
                 if isinstance(handler, logging.FileHandler)), None)


def parser_config():
    # read arguments
    parser = argparse.ArgumentParser(description=f"running AvailSim4 -")

    parser.add_argument('--version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))

    parser.add_argument('--simulation', type=str, required=True,
                        help='parameters of the algorithm')

    parser.add_argument('--system', type=str, required=True,
                        help='system file to simulate')

    parser.add_argument('--sensitivity_analysis', type=str, required=False,
                        help='sensitivity analysis file to explore',
                        default=None)

    parser.add_argument('--children_logic', type=str, required=False,
                        help='python file defining a custom children logic',
                        default=None)

    parser.add_argument('--HTCondor', default=False, action='store_true',
                        help='if the flag is present, then HTCondor is used to '
                             'run the different jobs of the sensitivity analysis')

    parser.add_argument('--HTCondor_extra_argument', type=str, required=False, default="",
                        help='possible extra argument used when submitting jobs '
                             'most likely a group/quota definition such as: +AccountingGroup="group_u_XX.XXX"')

    parser.add_argument('--nb_processes', type=int, required=False,
                        help='number of processes used in the parallel part of the code '
                             '(over the sensitivity analysis when HTCondor is not used)',
                        default=1)

    parser.add_argument('--output_folder', type=str, required=True,
                        help='folder in which the results are exported')

    parser.add_argument('--debug', default=False, action='store_true',
                        help='if the flag is present, then debug mode is used in the logging file')

    return parser.parse_args()


def init():
    """
    Parse the command arguments and loads the logging configuration.
    :return tuple coming from given argument
    simulation_path, system_path, sensitivity_analysis_path, output_folder, HTCondor, nb_process
    """
    args = parser_config()

    os.makedirs(args.output_folder, exist_ok=True)

    log_file_path = logger_config(args.debug, args.output_folder)

    logging.info(f"- Availsim4 - version: {__version__}")
    logging.info(f"- Init configuration -")

    if args.debug:
        if log_file_path is None:
            logging.error("DEBUG mode activated but logging file not defined or misconfigured.")
        logging.info(f"DEBUG mode activated -> Check: {log_file_path}")

    logging.debug(f"Arguments: "
                  f"simulation:{args.simulation} - "
                  f"system:{args.system} - "
                  f"sensitivity analysis:{args.sensitivity_analysis} - "
                  f"output_folder:{args.output_folder} - "
                  f"HTCondor:{args.HTCondor} - "
                  f"HTCondor_extra_argument:{args.HTCondor_extra_argument} - "
                  f"nb_processes:{args.nb_processes} - "
                  f"children_logic:{args.children_logic}")

    return (args.simulation,
            args.system,
            args.sensitivity_analysis,
            args.output_folder,
            args.HTCondor,
            args.HTCondor_extra_argument,
            args.nb_processes,
            args.children_logic)
