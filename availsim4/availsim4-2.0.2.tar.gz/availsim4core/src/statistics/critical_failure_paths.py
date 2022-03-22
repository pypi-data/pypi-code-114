# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import logging

from availsim4core.src.context.context import Context
import itertools
import numpy as np

from typing import List, Set
from availsim4core.src.context.system.children_logic.tolerated_fault import ToleratedFault

from availsim4core.src.context.system.component_tree.basic import Basic
from availsim4core.src.context.system.component_tree.component import Component
from availsim4core.src.context.system.children_logic.and_ import And
from availsim4core.src.context.system.children_logic.oo import Oo
from availsim4core.src.simulation.importance_splitting.simple_weights import SimpleWeights


class ChildrenLogicCriticalFailurePathsError(Exception):
    pass


class SpecificComponentNotFoundCriticalFailurePathsError(Exception):
    pass


class CriticalFailurePaths:
    """
    Class used to gather information about minimal critical failure paths. Creation of an object of this class
    triggers analysis of the component tree to identify combinations of components leading to critical failures
    of the overall system. The overall system is identified by a system root component selected by users in the
    simulation input sheet (in anticipation of systems which root is not identical with the AvailSim4 component
    tree).
    """

    def __init__(self, context: Context, system_root_component_name: str):
        self.context = context
        basic_components = [component for component in context.root_component.to_set() if isinstance(component, Basic)]
        global_to_basic_id_dict = {}
        basic_to_global_id_dict = {}
        for idx, component in enumerate(basic_components):
            global_to_basic_id_dict[component.global_id] = idx
            basic_to_global_id_dict[idx] = component.global_id
        self.n_basic_components = len(basic_components)
        self.global_to_basic_id_dict = global_to_basic_id_dict
        self.basic_to_global_id_dict = basic_to_global_id_dict

        self.cfp_analysis_starting_node = self.find_system_root_component(
            system_root_component_name)
        self.critical_failure_paths = self.generate_critical_failure_paths(
            self.cfp_analysis_starting_node)

        self.longest_cfp_len = max(
            [len(failure_path) for failure_path in self.critical_failure_paths])
        self.cfp_matrix = self.fetch_cfp_matrix(self.critical_failure_paths)
        self.weights = SimpleWeights
        self.component_weights = self.calculate_component_failure_weight_vector(
            context.root_component.to_set())



    def find_system_root_component(self, system_root_component_name: str) -> Component:
        """
        This function returns a component object from the tree which has the same name as
        the system_root_component_name parameter decided by the user in the simulation input file. If the component
        is not found, an exception is logged and a SpecificComponentNotFoundCriticalFailurePathsError is raised.
        Both contain a message which states the missing name recovered during execution.
        """
        for component in self.context.root_component.to_set():
            if component.name == system_root_component_name:
                return component
        message_exception = f"The component name {system_root_component_name} specified for the CRITICAL_FAILURE_PATHS " \
                            f"diagnostic has not be found"
        logging.exception(message_exception)
        raise SpecificComponentNotFoundCriticalFailurePathsError(
            message_exception)

    @staticmethod
    def getXooYfailureCombinations(
            n: int,
            failure_paths_of_children_grouped: List[List[Component]],
            failure_paths: List[List[Component]]):
        # n is the number of components that have to work. n = 1 is essentially OR logic.
        # We get children_n groups of components causing critical failures of each of the children.
        # children_cfp is children_n lists of critical failure paths for each children
        # cfp is the returned result

        # XooY is referring to the way failure logic is defined. X stands for the number of components
        # that are required to work, and Y for the number of all children components
        x = int(n)
        y = len(failure_paths_of_children_grouped)

        # creating all possible combinations of choosing X groups of failure paths out of Y children groups
        failure_groups_combinations = [list(x) for x in list(
            itertools.combinations(failure_paths_of_children_grouped, y-x+1))]

        for failure_group_combination in failure_groups_combinations:
            # identifying the value of a largest  path created in all cobinations
            max_path_len = max([len(failure_path)
                               for failure_path in failure_group_combination])
            indices = list(itertools.product(
                range(0, max_path_len), repeat=len(failure_group_combination)))

            for index_set in indices:
                new_failure_paths = []
                for idx, i in enumerate(index_set):
                    if i < len(failure_group_combination[idx]):
                        new_failure_paths.extend(failure_group_combination[idx][i])
                    else:
                        new_failure_paths = []
                        break
                if new_failure_paths:
                    failure_paths.append(new_failure_paths)

    def generate_critical_failure_paths_recursive_call(self, component: Component) -> List[List[Component]]:
        """
        Recursive function parsing the entire tree
        :param component: component recursively explored
        :return cfp: the list of failure paths for the component inputed
        """

        # recursive part
        children_cfp = []
        for child in component.get_children():
            children_cfp.append(
                self.generate_critical_failure_paths_recursive_call(child))

        # handling the failure paths at the current level, according to the children logic
        cfp = []
        if not component.get_children():
            cfp.append([component])
        else:
            if isinstance(component.children_logic, And):
                for children_group in children_cfp:
                    cfp.extend(children_group)
            elif isinstance(component.children_logic, ToleratedFault):
                self.getXooYfailureCombinations(len(component.get_children()) - component.children_logic.fault_tolerance,
                                                children_cfp, cfp)
            elif isinstance(component.children_logic, Oo):
                # the extend of cfp is done within the function getXooYfailureCombinations
                self.getXooYfailureCombinations(
                    component.children_logic.minimum_number_of_required_component, children_cfp, cfp)
            else:
                message_exception = f"The children logic {component.children_logic} of component {component} is not " \
                                    f"implemented in the function generate_critical_failure_paths_recursive_call"
                logging.exception(message_exception)
                raise ChildrenLogicCriticalFailurePathsError(message_exception)

        return cfp

    def search_for_minimal_paths(self, input_list_of_lists_of_components: List[List[Component]]) -> List[List[Component]]:
        """
        Function parsing a list of list of elements and spotting if any list is included in an other list. The goal is
        to find "minimal failure critical path" so if a path A is included in B it means that B is not a minimal paths.
        :param cfp: list of list of components representing critical paths
        :return cfp: cleaned list of list of components
        """

        # transforming the list of lists into a list of sets to avoid duplicates within one list
        # and better check the inclusion
        list_of_sets_of_components = []
        for path in input_list_of_lists_of_components:
            list_of_sets_of_components.append(set(path))

        # nested loops used to compare two elements in the list
        output_list_of_lists_of_components = []
        for ida, A_path in enumerate(list_of_sets_of_components):
            A_path_is_minimal = True
            for idb, B_path in enumerate(list_of_sets_of_components):
                if ida != idb:  # if ida == idb then A == B then A include in B and B included in A
                    if B_path.issubset(A_path):
                        # A_path is not a minimal path because B_path is included in A_path
                        A_path_is_minimal = False
                        break

            if A_path_is_minimal:
                output_list_of_lists_of_components.append(list(A_path))

        return output_list_of_lists_of_components

    def generate_critical_failure_paths(self, component: Component) -> List[List[Component]]:
        """
        This function aggregates calls to two other functions: one which is responsible for identifying all
        critical failure paths in the system (recursively) and one which ensures that the identified
        combinations are not repeated (also within other combinations). The taken argument points
        to the start of the tree and the function returns a list of minimal critical failure paths.
        """
        critical_failure_paths = self.generate_critical_failure_paths_recursive_call(component)
        critical_failure_paths = self.search_for_minimal_paths(critical_failure_paths)

        return critical_failure_paths

    def fetch_cfp_matrix(self, results) -> np.ndarray:
        """
        This function creates a matrix describing critical failure paths as consecutive vectors of
        true/false values. Such a representation is going to be useful for fast criticallity lookup.
        """
        cfp_matrix = np.zeros([len(results), self.n_basic_components])
        for idx, result in enumerate(results):
            for component in result:
                cfp_matrix[idx,
                           self.global_to_basic_id_dict[component.global_id]] = 1
        return cfp_matrix

    def calculate_component_failure_weight_vector(self, components_set: Set[Component]) -> np.ndarray:
        """
        This function prepares an integer vector representation of weights for components in the system.
        Each individual basic component is assigned a value according to the formula in this function and
        then stored in a vector on a position assigned to the component. Such a representation is applied
        to improve the speed of responses for fast criticallity lookups.
        """
        weight_vector = np.zeros(self.n_basic_components)
        for component in components_set:
            if isinstance(component, Basic):
                weight = self.weights.calculate_component_failure_weight(
                    component)
                weight_vector[self.global_to_basic_id_dict[component.global_id]] = weight
        return weight_vector

    def calculate_failures_atm_vector(self, components_set: Set[Component]) -> np.ndarray:
        """
        The basic components provided in a set as the only argument of this function are then checked for blind
        failures. Their statuses in this aspect decide on the value in a true/false vector describing the current
        state of the system. Positions of each component in that vector are fixed.
        """
        failure_states_atm_vector = np.zeros(self.n_basic_components)
        for component in components_set:
            if self.weights.is_cfp_component(component):
                failure_states_atm_vector[self.global_to_basic_id_dict[component.global_id]] = 1
        return failure_states_atm_vector

    def calculate_criticallity_atm(self, failure_state_atm: np.ndarray) -> np.ndarray:
        """
        This function is a shorthand for a dot operation between argument failure_state_atm which is a matrix
        expected to contain failure states at the moment and component weights vector.
        """
        return np.dot(failure_state_atm, self.component_weights)

    def calculate_distance_to_critical_failure(self, failure_states_atm: np.ndarray) -> float:
        """
        This function is expected to be extended in the future. For now, its role is limited to counting a number
        of blind failures in the system (by summing true/false vector). The only extension in the current state is
        the condition on the number of failures: whenever there is more failures in the system than there is in the
        longest minimal critical failure path, the result is 0.  This makes sure that whenever cfp_threshold is set
        to a non-zero natural number (which triggers the ISp and thus CFP approaches), the branching will not occur.
        """
        result = self.weights.calculate_distance_to_critical_failure(failure_states_atm)
        if result >= self.longest_cfp_len:
            return 0
        return result
