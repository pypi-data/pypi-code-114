# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import logging
import os
from datetime import datetime
from typing import List

import pandas

from availsim4core.src.analysis import Analysis
from availsim4core.src.exporter.xlsx_analysis_exporter import XLSXAnalysisExporter


class HTCondorRunner:
    """
    class used to run simulations on a cluster interfaced by HTCondor
    """

    # Note : This does not work due to permissions issues.
    #  Did not find a quick working solution, let's postpone it as the solution below is enough so far...
    #
    # @staticmethod
    # def run(root_output_folder, path_simulation, path_system, system_template):
    #     date_time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    #     output_folder = root_output_folder + "run___" + date_time_str + "___" + str(system_template.id) + "/"
    #     os.makedirs(output_folder, exist_ok=True)
    #
    #     hostname_job = htcondor.Submit({
    #         "executable": "python3 availsim4.py",  # the program to run on the execute node
    #         "--system": path_system,
    #         "--simulation": path_simulation,
    #         "--output_folder": output_folder,
    #         "output": "out.txt",  # anything the job prints to standard output will end up in this file
    #         "error": "err.txt",  # anything the job prints to standard error will end up in this file
    #         "log": "log.txt",  # this file will contain a record of what happened to the job
    #         "request_cpus": "1",  # how many CPU cores we want
    #     })
    #
    #     print(hostname_job)

    @staticmethod
    def create_one_analysis_folder(root_output_folder:str,
                                   pipinstall_folder: str,
                                   date_time_str: str,
                                   analysis: Analysis,
                                   HTCondor_extra_argument: str):
        """
        :param root_output_folder: folder in which the analysis' folder will be created
        :param pipinstall_folder: folder where the requirements are installed
        :param date_time_str: unique identifier used to name the new folders
        :param analysis: the analysis to perform in the folder
        :param HTCondor_extra_argument: any extra argument used when submitting the job
        :return: nothing, the function just create folders and files
        """

        # creating a unique subdirectory containing on of the simulation of the sensitivity analysis
        output_folder = root_output_folder + "run___" + date_time_str + "___" + str(analysis.id) + "/"
        os.makedirs(output_folder,
                    exist_ok=True)
        logging.debug(f"Creating HTCondor output folder {output_folder}")

        # copying simulation file
        simulation_filename = output_folder + "simulation.xlsx"
        system_filename = output_folder + "system.xlsx"

        writer_system = pandas.ExcelWriter(system_filename, engine='xlsxwriter')
        XLSXAnalysisExporter.export_system(writer_system,
                                           analysis.system_template)
        writer_system.save()

        writer_simulation = pandas.ExcelWriter(simulation_filename, engine='xlsxwriter')
        XLSXAnalysisExporter.export_simulation(writer_simulation,
                                               analysis.simulation)
        writer_simulation.save()

        code_directory = os.getcwd()
        bash_filename = output_folder + "run.sh"
        with open(bash_filename, 'w') as file:
            try:
                file.write(
                    f"#!/usr/bin/env bash\n"
                    f"source /afs/cern.ch/eng/tracking-tools/python_installations/activate_default_python\n"
                    f"export PYTHONPATH={pipinstall_folder}\n"
                    f"export PYTHONNOUSERSITE=1\n"
                    f"python3.7 {code_directory}/availsim4.py"
                    f" --system {system_filename}"
                    f" --simulation {simulation_filename}"
                    f" --output_folder {output_folder}\n"
                    f"tar -czvf out.tar.gz out.txt\n"
                    f"rm -rf out.txt"
                )
            except IOError as e:
                print(f"I/O error({e.errno}): {e.strerror}")

        os.system("chmod +x " + bash_filename)

        runtime = int(analysis.simulation.maximum_execution_time * 1.1 + 10)

        # creating submission file for a unique job
        sub_filename = output_folder + "sub.sub"
        with open(sub_filename, 'w') as file:
            try:
                content_of_sub = (f"executable = {bash_filename}\n"
                                  f"output = {output_folder + 'out.txt'}\n"
                                  f"error = {output_folder + 'err.txt'}\n"
                                  f"log = {output_folder + 'log.txt'}\n"
                                  "RequestCpus = 1\n"
                                  f"+MaxRuntime = {runtime}\n"
                                  f"{HTCondor_extra_argument}\n"
                                  f"queue")
                file.write(content_of_sub)
            except IOError as e:
                logging.info(f"I/O error({e.errno}): {e.strerror}")

    @staticmethod
    def run(root_output_folder: str,
            analysis_list: List[Analysis],
            HTCondor_extra_argument: str):
        """
        The runner of HTCondor is taking care of running jobs on HTCondor. This is done in 2 steps:
        1) checking that the requirements are installed in the pipinstall folder
        2) creating the directory / input file / etc of each analysis one wants to perform
        3) submitting all the analyses in one job, requesting as many cores as analyses
        """

        date_time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # creating a pipinstall folder for the analysis
        pipinstall_folder = root_output_folder + "pipinstall"
        if os.path.isdir(pipinstall_folder):
            logging.info("pipinstall folder already exists, no need to create it")
        else:
            logging.info("pipinstall folder does not already exist, installation of requirements")
            code_directory = os.getcwd()
            os.makedirs(pipinstall_folder, exist_ok=True)
            command = f"pip install --target={pipinstall_folder} -r {code_directory}/requirements.txt"
            os.system(command)

        # creating one folder per analysis
        for analysis in analysis_list:
            HTCondorRunner.create_one_analysis_folder(
                root_output_folder,
                pipinstall_folder,
                date_time_str,
                analysis,
                HTCondor_extra_argument)

        # creating the master bash file
        master_bash_filename = root_output_folder + "run.sh"
        with open(master_bash_filename, 'w') as file:
            try:
                file.write("#!/usr/bin/env bash" + "\n")
                file.write("cd " + root_output_folder + "*__$1" + "\n")
                file.write("source ./run.sh" + "\n")
            except IOError as e:
                print(f"I/O error({e.errno}): {e.strerror}")
        os.system("chmod +x " + master_bash_filename)

        # creating the master sub file

        master_sub_filename = root_output_folder + "sub.sub"
        runtime = int(analysis_list[0].simulation.maximum_execution_time * 1.1 + 10)

        output_folder = root_output_folder + "/run___" + date_time_str + "___" + "$(ProcId)/"

        with open(master_sub_filename, 'w') as file:
            try:
                content_of_sub = (f"executable = {master_bash_filename}\n"
                                  f"arguments = $(ProcId)\n"
                                  f"output = {output_folder+'out.txt'}\n"
                                  f"error = {output_folder+'err.txt'}\n"
                                  f"log = {output_folder+'log.txt'}\n"
                                  "RequestCpus = 1\n"
                                  f"+MaxRuntime = {runtime}\n"
                                  f"{HTCondor_extra_argument}\n"
                                  f"queue {len(analysis_list)}")
                file.write(content_of_sub)

            except IOError as e:
                logging.info(f"I/O error({e.errno}): {e.strerror}")

        # submitting a unique request to HTCondor
        command = "cd " + root_output_folder + "; condor_submit " + master_sub_filename
        logging.debug(f"Executing HTCondor command {command}")
        os.system(command)
