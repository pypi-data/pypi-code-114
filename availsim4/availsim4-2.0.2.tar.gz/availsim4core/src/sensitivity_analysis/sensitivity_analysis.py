# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import copy
import logging

from availsim4core.src.analysis import Analysis
from availsim4core.src.reader.xlsx.monte_carlo_reader import SimulationMonteCarloColumn
from availsim4core.src.reader.xlsx.sensitivity_analysis_reader import SensitivityAnalysisReader
from availsim4core.src.reader.xlsx.system_template_reader import SystemTemplateArchitectureColumn, \
    SystemTemplateFailureModeColumn, SystemTemplateMinimalReplaceableUnitColumn, SystemTemplateInspectionsColumn


class ParameterOfSensitivityAnalysisNotFoundError(Exception):
    pass


class SensitivityAnalysis:
    """
    Manages the sensitivity analysis from the initial simulation and initial system.
    """

    def __init__(self,
                 initial_simulation,
                 initial_system_template):
        self.initial_simulation = initial_simulation
        self.initial_system_template = initial_system_template

    def generate_analysis_list(self,
                               path_sensitivity_analysis):
        """
        From the given path of the sensitivity analysis it reads the file and returns a list of Analysis to perform.
        :param path_sensitivity_analysis path of the configuration file for the sensitivity analysis.
        :return List[Analysis]
        :see Analysis
        """

        system_modifier_combination_list = SensitivityAnalysisReader.generate_system_modifier_combination_list(
            path_sensitivity_analysis)

        analysis_list = []
        for idx, system_modifier_combination in enumerate(system_modifier_combination_list):
            analysis = self._generate_analysis(idx,
                                               system_modifier_combination)
            analysis_list.append(analysis)
        return analysis_list

    def _generate_analysis(self,
                           idx,
                           system_modifier_combination):
        """
        Given a combination {SystemModifierCombination} and based of the initial simulation and system,
        it generates the corresponding analysis.
        :param idx the id of the analysis to generate
        :param system_modifier_combination the SystemModifierCombination to apply on initial simulation and system.
        :returns Corresponding Analysis {Analysis}
        """

        new_simulation = self._apply_combination_modifier_on_simulation(system_modifier_combination)
        new_system_template = self._apply_combination_modifier_on_system(system_modifier_combination)
        return Analysis(idx,
                        new_system_template,
                        new_simulation)

    def _apply_combination_modifier_on_system(self,
                                              system_modifier_combination):
        """
        Given a {SystemModifierCombination} it applies the modification to the copy of the initial system template.
        :param system_modifier_combination the combination with the system modifier to apply on the initial system template.
        """
        modified_initial_system_template = copy.deepcopy(self.initial_system_template)

        for system_modifier in system_modifier_combination.system_modifier_list:

            modification_applied = False

            column_name, name = system_modifier.parameter_name.partition("/")[::2]

            if column_name=="SEED":
                # modification applied in another function
                modification_applied = True

            architecture_entry = modified_initial_system_template.find_architecture_entry(name)
            if architecture_entry is not None:
                if column_name == SystemTemplateArchitectureColumn.COMPONENT_NUMBER:
                    architecture_entry.component_number = int(system_modifier.value)
                    modification_applied = True
                if column_name == SystemTemplateArchitectureColumn.CHILDREN_LOGIC:
                    architecture_entry.children_logic_str = system_modifier.value
                    modification_applied = True

            failure_mode = modified_initial_system_template.find_failure_mode(name)
            if failure_mode is not None:
                if column_name == SystemTemplateFailureModeColumn.FAILURE_PARAMETERS:
                    failure_mode.failure_law.parameters = system_modifier.value
                    modification_applied = True
                if column_name == SystemTemplateFailureModeColumn.REPAIR_PARAMETERS:
                    failure_mode.repair_law.parameters = system_modifier.value
                    modification_applied = True

            mru = modified_initial_system_template.find_mru(name)
            if mru is not None:
                if column_name == SystemTemplateMinimalReplaceableUnitColumn.REPAIR_PARAMETERS:
                    mru.repair_law.parameters = system_modifier.value
                    modification_applied = True
                if column_name == SystemTemplateMinimalReplaceableUnitColumn.REPAIR_SCHEDULE:
                    mru.repair_schedule = system_modifier.value
                    modification_applied = True

            inspection = modified_initial_system_template.find_inspection(name)
            if inspection is not None:
                if column_name == SystemTemplateInspectionsColumn.INSPECTION_DURATION:
                    inspection.duration = float(system_modifier.value)
                    modification_applied = True
                if column_name == SystemTemplateInspectionsColumn.INSPECTION_PERIOD:
                    inspection.periodicity = float(system_modifier.value)
                    modification_applied = True

            if not modification_applied:
                exception_message = (f"System_modifier {system_modifier } could not be applied: wrong parameter name={name}")
                logging.exception(exception_message)
                raise ParameterOfSensitivityAnalysisNotFoundError(exception_message)

        return modified_initial_system_template

    def _apply_combination_modifier_on_simulation(self, system_modifier_combination):
        """
        Given a {SystemModifierCombination} it applies the modification to the copy of the initial simulation.
        :param system_modifier_combination the combination with the system modifier to apply on the initial simulation.
        Note: Because the simulation has only one line entry, only the column name of the system modifier is taken into account.
        """
        modified_initial_simulation = copy.deepcopy(self.initial_simulation)

        for system_modifier in system_modifier_combination.system_modifier_list:
            column_name, *_ = system_modifier.parameter_name.split("/")

            if column_name == SimulationMonteCarloColumn.SEED:
                modified_initial_simulation.seed = int(system_modifier.value)

        return modified_initial_simulation
