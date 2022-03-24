import os
import shutil
import subprocess
import traceback
from abc import abstractmethod

from optimeed.core import InterfaceDevice, Option_class
from optimeed.core import printIfShown, SHOW_WARNING, SHOW_INFO
from optimeed.core.tools import getPath_workspace
from optimeed.optimize import InterfaceCharacterization


class CustomException(Exception):
    def __init__(self, theStr):
        super().__init__(theStr)
        self.output = theStr


class FEM_Characterization(InterfaceCharacterization, Option_class):
    """ Template for a FEM simulation using gmsh/getdp"""

    RES_FOLDER_NAME = 100
    TEMPLATES_FOLDER = 101
    TIMEOUT_GMSH = 102
    TIMEOUT_GETDP = 103
    DELETE_FOLDER = 104
    MESH_NAME = 105
    SIMULATION_NAME = 106
    RESOLUTION_NAME = 107
    PROBLEM_DIMENSION = 108
    ONELAB_VERBOSE = 109
    GEOMETRY_NAME = 110

    def __init__(self):
        """
        Initialisation of the interface, defining the default variables useful for a FEM simulation
        """
        super().__init__()
        self.workspace_folder = getPath_workspace()

        # Default values
        self.add_option(self.TEMPLATES_FOLDER, "Folder with the useful onelab files", "Templates_FEM")
        self.add_option(self.TIMEOUT_GMSH, "Meshing timeout", 10000)
        self.add_option(self.TIMEOUT_GETDP, "Solving timeout", 10000)
        self.add_option(self.DELETE_FOLDER, "Delete temporary files", True)
        self.add_option(self.MESH_NAME, "Filename of mesh file  (relative to template folder)", "myMesh.msh")
        self.add_option(self.GEOMETRY_NAME, "Filename of geo file to mesh (relative to template folder)", "myGeo.geo")
        self.add_option(self.SIMULATION_NAME, "Filename of simulation file (relative to template folder)", "mySimu.pro")
        self.add_option(self.RES_FOLDER_NAME, " Resolution folder (relative to simulation file)", "res/")
        self.add_option(self.RESOLUTION_NAME, "Name of getdp resolution", "myResolution")
        self.add_option(self.PROBLEM_DIMENSION, "Geometrical dimension of the problem", 2)
        self.add_option(self.ONELAB_VERBOSE, "Onelab verbose level", 1)

    def compute(self, theDevice: InterfaceDevice):
        """
        Function to call for launching the simulation, the three main steps are
         1) preparation of the simulation, writing the files;
         2) executing the mesh and solver;
         3) reading the results
        :param theDevice:
        :return:
        """
        # noinspection PyBroadException
        try:
            # noinspection PyBroadException
            try:
                self.prepare_simulation(theDevice)
                self.launch_simulation(theDevice)
                print("COMPUTE")
                print(os.path.join(self.workspace_folder, os.path.dirname(self.get_optionValue(self.SIMULATION_NAME)), self.get_optionValue(self.RES_FOLDER_NAME)))
                self.get_results(os.path.join(self.workspace_folder, os.path.dirname(self.get_optionValue(self.SIMULATION_NAME)), self.get_optionValue(self.RES_FOLDER_NAME)), theDevice)
            except KeyboardInterrupt:
                raise
            except CustomException as e:
                printIfShown("Following error occurred in characterization :" + e.output, SHOW_WARNING)
            except Exception:
                printIfShown("Following error occurred in characterization :" + traceback.format_exc(), SHOW_WARNING)

            self.end_simulation()

        except KeyboardInterrupt:
            raise
        except Exception:
            printIfShown("Following error occurred in characterization :" + traceback.format_exc(), SHOW_WARNING)

    def prepare_simulation(self, theDevice: InterfaceDevice):
        """
        It copies the templates, formulations and writes the parameters files.
        :param theDevice:
        :return:
        """
        workspace_folder = self.workspace_folder
        success = False
        while not success:
            try:
                number_simulation = 1
                workspace_folder = getPath_workspace() + '/FEM_' + str(number_simulation) + str(os.getpid())
                while os.path.isdir(workspace_folder):
                    number_simulation += 1
                    workspace_folder = getPath_workspace() + '/FEM_' + str(number_simulation) + str(os.getpid())
                shutil.copytree(self.get_optionValue(self.TEMPLATES_FOLDER), workspace_folder)
                success = True
            except FileExistsError:
                printIfShown("Folder already exists, trying again ...", SHOW_INFO)

        self.workspace_folder = workspace_folder
        self.write_init_simulation_files(workspace_folder, theDevice)

    def launch_simulation(self, theDevice):
        """
        Creation of the mesh and then execution of the FEM simulation
        :return:
        """

        gmsh_path, getdp_path = self.get_onelab_program_path()

        # Check if geometry feasible
        try:
            subprocess.check_output('{} -0 {} -v {}'.format(gmsh_path,
                                                            os.path.join(self.workspace_folder, self.get_optionValue(self.GEOMETRY_NAME)),
                                                            self.get_optionValue(self.ONELAB_VERBOSE)), shell=True)
            # , stderr=subprocess.STDOUT
        except subprocess.CalledProcessError as e:
            print("subprocess.CalledProcessError:",e)
            raise CustomException(str(e.output))

        # Launch gmsh
        meshCmd = "{} {} -{} -v {} -o {} {}".format(gmsh_path,
                                                    os.path.join(self.workspace_folder, self.get_optionValue(self.GEOMETRY_NAME)),
                                                    self.get_optionValue(self.PROBLEM_DIMENSION),
                                                    self.get_optionValue(self.ONELAB_VERBOSE),
                                                    os.path.join(self.workspace_folder, self.get_optionValue(self.MESH_NAME)),
                                                    self.gmsh_append_to_cmdLine(theDevice))
        # try:
        subprocess.run(meshCmd, timeout=self.get_optionValue(self.TIMEOUT_GMSH), check=True, shell=True)
        # except subprocess.CalledProcessError as e:
        #    raise CustomException(str(e.output))
        # except subprocess.TimeoutExpired:
        #    raise CustomException("Timeout gmsh")

        # Launch getdp
        getdpCmd = "{} {} -solve {} -v {} -msh {} {}".format(getdp_path,
                                                             os.path.join(self.workspace_folder, self.get_optionValue(self.SIMULATION_NAME)),
                                                             self.get_optionValue(self.RESOLUTION_NAME),
                                                             self.get_optionValue(self.ONELAB_VERBOSE),
                                                             os.path.join(self.workspace_folder, self.get_optionValue(self.MESH_NAME)),
                                                             self.getdp_append_to_cmdLine(theDevice))

        try:
            subprocess.run(getdpCmd, timeout=self.get_optionValue(self.TIMEOUT_GETDP), check=True, shell=True)  # Wait for simulation to be over
        except subprocess.CalledProcessError as e:
            raise CustomException(str(e.output))
        except subprocess.TimeoutExpired:
            raise CustomException("Timeout getdp")

    def end_simulation(self):
        """
        Management of the simulation end
        :return:
        """
        if self.get_optionValue(self.DELETE_FOLDER):
            try:
                shutil.rmtree(self.workspace_folder, ignore_errors=False)
            except OSError:
                shutil.rmtree(self.workspace_folder, ignore_errors=True)

    @staticmethod
    def get_onelab_program_path():
        """
        Method to define the paths/command shortcuts of gmsh and getdp on your computer
        :return: gmsh path, getdp path
        """
        return 'gmsh', 'getdp'

    @abstractmethod
    def get_results(self, folderName: str, theDevice: InterfaceDevice):
        """
        This method is called to gather the results after the simulation is done
        :param folderName:
        :param theDevice:
        :return:
        """
        pass

    @abstractmethod
    def write_init_simulation_files(self, workspace: str, theDevice: InterfaceDevice):
        """
        This method is called at the beginning of a simulation to write all the necessary files
        :param workspace:
        :param theDevice:
        :return:
        """
        pass

    # noinspection PyUnusedLocal
    @staticmethod
    def getdp_append_to_cmdLine(theDevice):
        """
        Additional command to append to getdp (ex -SetNumber)
        :param theDevice: Device that is analyzed
        :return:
        """
        return ''

    # noinspection PyUnusedLocal
    @staticmethod
    def gmsh_append_to_cmdLine(theDevice):
        """
        Additional command to append to gmsh (ex -SetNumber)
        :param theDevice: Device that is analyzed
        :return:
        """
        return ''
