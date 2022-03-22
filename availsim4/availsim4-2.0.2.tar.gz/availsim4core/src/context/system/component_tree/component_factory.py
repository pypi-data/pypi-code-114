# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import logging
from typing import List

from availsim4core.src.context.system.architecture_entry import ArchitectureEntry
from availsim4core.src.context.system.children_logic.children_logic_factory import ChildrenLogicFactory
from availsim4core.src.context.system.component_tree.basic import Basic
from availsim4core.src.context.system.component_tree.component import Component, ComponentType
from availsim4core.src.context.system.component_tree.compound import Compound
from availsim4core.src.context.system import sanity_check
from availsim4core.src.context.system.system_template import SystemTemplate
from availsim4core.src.context.system.system_utils import SystemUtils


class ComponentTypeError(Exception):
    pass


class EmptySystemException(Exception):
    pass


class ComponentFactory:
    """
    class used to handle components describing a system
    """

    def __init__(self,
                 system_template: SystemTemplate):
        self.system_template = system_template
        self.shared_children_list: List[Component] = []
        self.uniq_id = 0

    def build(self):
        """
        Function generating a system from a dictionary describing a system
        :return: the single root node of tree representing the system.
        """
        # checking if tree is empty
        if not self.system_template.architecture_entry_list:
            message_exception = "The system architecture tree is empty."
            logging.exception("The system architecture tree is empty.")
            raise EmptySystemException(message_exception)

        # find root component, root component is the first line of the architecture tab.
        root_architecture_entry = \
            self.system_template.architecture_entry_list[0]

        component_list = self._add_component(root_architecture_entry,
                                             [],
                                             self.system_template.custom_children_logic_path)

        root_node = component_list[0]

        if not sanity_check.run(self.system_template, root_node):
            logging.warning('The input file and simulated tree do not match perfectly, please check the warnings.')

        return root_node

    def _add_component(self,
                       architecture_entry: ArchitectureEntry,
                       parents: List[Component],
                       custom_children_logic_path: str):
        """
        Recursive method to build the system graph.
        :param architecture_entry: The architecture_entry of the component to add in the system.
        :param parents: list of component parents of the component to add.
        :param custom_children_logic_path: string defining the path toward an optional python file containing custom
         children logic
        :return: List of the sibling components.
        """

        if architecture_entry.component_type_str == ComponentType.BASIC:
            return self._add_basics(architecture_entry,
                                    parents)

        elif architecture_entry.component_type_str == ComponentType.COMPOUND:
            return self._add_compound(architecture_entry,
                                      parents,
                                      custom_children_logic_path)
        else:
            message_exception = f"{architecture_entry.component_name} wrong type of component for component."
            logging.exception(message_exception)
            raise ComponentTypeError(message_exception)

    def _add_basics(self,
                    architecture_entry: ArchitectureEntry,
                    parents: List[Component]):
        """
        Part of the recursive logic from the _add_component.
        This methods creates a list of sibling Basic Components and return it.
        :param architecture_entry
        :param parents: the parents component for each of the basic components.
        :return: a list of Basics.
        """

        list_of_mrus__group = self.get_list_of_mru_from_list_of_strings(self.system_template.mru_list,
                                                                        architecture_entry.in_mru_str_list)

        list_of_mrus__trigger = self.get_list_of_mru_from_list_of_strings(self.system_template.mru_list,
                                                                          architecture_entry.trigger_mru_str_list)

        list_of_basic = []
        for component_number in range(0, int(architecture_entry.component_number)):
            self.uniq_id = self.uniq_id + 1
            for failure_mode_assignments in self.system_template.failure_mode_assignments_list:
                if failure_mode_assignments.component_name == architecture_entry.component_name:
                    list_of_basic.append(Basic(self.uniq_id,
                                               architecture_entry.component_name,
                                               component_number,
                                               parents.copy(),
                                               failure_mode_assignments.failure_mode,
                                               list_of_mrus__trigger,
                                               list_of_mrus__group)
                                         )
        return list_of_basic

    @staticmethod
    def get_list_of_mru_from_list_of_strings(mru_list,
                                             mru_list_of_names):
        list_of_mrus = [mru for mru in mru_list for mru_name in mru_list_of_names if mru.name == mru_name]
        return list_of_mrus

    def _add_compound(self,
                      architecture_entry: ArchitectureEntry,
                      parents: List[Component],
                      custom_children_logic_path: str):
        """
        Part of the recursive logic from the _add_component.
        This methods instantiates a new list of Compounds and their associated children.
        If the children are shared with multiple parents, they are created and stored in the shared_children_list.
        If the shared children has been created, then the compound is added to the list of parents.
        If the children is not shared (normal), then the children are created by calling the _add_component method.
        :param architecture_entry: the line describing the component within the input file
        :param parents: the list of parents.
        :param custom_children_logic_path: string defining the path toward an optional python file containing custom
        :return: list of the sibling compounds.
        """

        list_of_mru__trigger = self.get_list_of_mru_from_list_of_strings(self.system_template.mru_list,
                                                                         architecture_entry.trigger_mru_str_list)

        list_compounds = []
        for component_number in range(0, int(architecture_entry.component_number)):
            self.uniq_id = self.uniq_id + 1

            children_logic = ChildrenLogicFactory.build(architecture_entry.children_logic_str,
                                                        custom_children_logic_path)

            compound = Compound(self.uniq_id,
                                architecture_entry.component_name,
                                component_number,
                                parents,
                                children_logic,
                                list_of_mru__trigger)
            list_compounds.append(compound)

            for child_name in architecture_entry.children_name_list:
                if SystemUtils.is_string_containing_parenthesis(child_name):
                    shared_child_list = self.find_shared_children(compound,
                                                                  child_name,
                                                                  self.shared_children_list)
                    if shared_child_list:
                        for shared_child in shared_child_list:
                            shared_child.add_parent(compound)
                        component_list = shared_child_list
                    else:
                        architecture_entry_child = self.system_template.find_architecture_entry(
                            SystemUtils.extract_name_of_function_from_string(child_name))
                        if architecture_entry_child is None:
                            logging.warning(
                                f"child name {child_name} of the component {architecture_entry.component_name} not found")
                        component_list = self._add_component(architecture_entry_child,
                                                             [compound],
                                                             custom_children_logic_path)
                        self.shared_children_list.extend(component_list)
                else:
                    architecture_entry_child = self.system_template.find_architecture_entry(child_name)
                    if architecture_entry_child is None:
                        logging.warning(
                            f"child name {child_name} of the component {architecture_entry.component_name} not found")
                    component_list = self._add_component(architecture_entry_child, [compound], custom_children_logic_path)
                compound.add_children_list(component_list)
        return list_compounds

    @classmethod
    def find_shared_children(cls,
                             compound,
                             shared_child_name_str,
                             shared_children_list):
        """
        Find the shared child from the shared_children_list based on its name and its compound parent.
        :param compound: The parent compound of the child.
        :param shared_child_name_str: the name of the shared child (contains parenthesis)
        :param shared_children_list: the list of shared children already instantiated.
        :return: The shared child if is the list. None otherwise.
        """
        lowest_common_parent_name = SystemUtils.extract_arguments_within_parenthesis(shared_child_name_str)

        compound_lowest_common_parent = SystemUtils.find_first_lowest_level_ancestor_with_name(compound,
                                                                                               lowest_common_parent_name)

        shared_children = filter(
            lambda component: component.name == SystemUtils.extract_name_of_function_from_string(shared_child_name_str),
            shared_children_list)

        shared_children_found = []
        for shared_child in shared_children:
            shared_child_common_parent = SystemUtils.find_first_lowest_level_ancestor_with_name(shared_child,
                                                                                                lowest_common_parent_name)
            if compound_lowest_common_parent == shared_child_common_parent:
                shared_children_found.append(shared_child)
        return shared_children_found