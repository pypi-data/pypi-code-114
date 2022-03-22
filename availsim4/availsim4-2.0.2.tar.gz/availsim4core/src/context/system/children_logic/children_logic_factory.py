# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import importlib
import logging
import os

from availsim4core.src.context.system.children_logic.and_ import And
from availsim4core.src.context.system.children_logic.children_logic import ChildrenLogic
from availsim4core.src.context.system.children_logic.oo import Oo
from availsim4core.src.context.system.children_logic.required_component import RequiredComponent
from availsim4core.src.context.system.children_logic.tolerated_fault import ToleratedFault


class ChildrenLogicFactoryError(Exception):
    pass


class ChildrenLogicFactory:

    @staticmethod
    def moduleNameFromPath(custom_children_logic_path: str) -> str:
        """
        function getting the name of the module out of the path of the custom children logic file
        :param custom_children_logic_path: path of the custom children logic file
        :return: name of the module
        """
        return '.'+os.path.split(custom_children_logic_path)[-1].split(".")[0]

    @staticmethod
    def packageNameFromPath(custom_children_logic_path: str) -> str:
        """
        function getting the name of the package out of the path of the custom children logic file
        :param custom_children_logic_path: path of the custom children logic file
        :return: path of the package
        """
        name = ChildrenLogicFactory.moduleNameFromPath(custom_children_logic_path)
        return ''.join(custom_children_logic_path.replace('.', '').replace('/', '.').rsplit(name, 1)[0])

    @staticmethod
    def build(children_logic_str: str, custom_children_logic_path: str) -> ChildrenLogic:
        """
        Given a string children logic word, this method instantiates the corresponding children_logic class.
        :param children_logic_str: word to analyse from (not case sensitive.)
        :param custom_children_logic_path: string defining the path toward an optional python file containing custom
        :return: the children_logic instance corresponding to the given string.
        """

        if children_logic_str == "AND":
            return And()
        elif "OO" in children_logic_str:
            minimum_number_of_required_component = int(children_logic_str.split('OO')[0])
            total_number_of_component = int(children_logic_str.split('OO')[1])
            return Oo(minimum_number_of_required_component, total_number_of_component)
        elif "TF" in children_logic_str:
            fault_tolerance = int(children_logic_str.split('TF')[0])
            return ToleratedFault(fault_tolerance)
        elif "RC" in children_logic_str:
            required_component = int(children_logic_str.split('RC')[0])
            return RequiredComponent(required_component)
        elif custom_children_logic_path:
            name = ChildrenLogicFactory.moduleNameFromPath(custom_children_logic_path)
            package = ChildrenLogicFactory.packageNameFromPath(custom_children_logic_path)
            mod = importlib.import_module(name, package)
            custom_children_logic = getattr(mod, children_logic_str)
            return custom_children_logic()
        else:
            exception_message = f"{children_logic_str} not supported type of children logic."
            logging.exception(exception_message)
            raise ChildrenLogicFactoryError(exception_message)
