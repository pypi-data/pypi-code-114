# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import logging
from typing import List

from availsim4core.src.context.phase.phase import Phase
from availsim4core.src.context.phase.phase_manager import PhaseManager
from availsim4core.src.context.system.architecture_entry import ArchitectureEntry
from availsim4core.src.context.system.failure_factory import FailureFactory
from availsim4core.src.context.system.failure_mode import FailureMode
from availsim4core.src.context.system.failure_mode_assignments import FailureModeAssignments
from availsim4core.src.context.system.inspection import Inspection
from availsim4core.src.context.system.minimal_replaceable_unit import MinimalReplaceableUnitFactory
from availsim4core.src.context.system.phase_jump_trigger import PhaseJumpTriggerFactory
from availsim4core.src.context.system.probability_law.probability_law_factory import ProbabilityLawFactory
from availsim4core.src.context.system.rca_trigger import RootCauseAnalysisTriggerFactory
from availsim4core.src.context.system.system_template import SystemTemplate
from availsim4core.src.reader.xlsx.xlsx_reader import XLSXReader


class SystemTemplateSheet:
    ARCHITECTURE = "ARCHITECTURE"
    FAILURE_MODES = "FAILURE_MODES"
    FAILURE_MODE_ASSIGNMENTS = "FAILURE_MODE_ASSIGNMENTS"
    MINIMAL_REPLACEABLE_UNIT = "MRU"
    INSPECTIONS = "INSPECTIONS"
    PHASES = "PHASES"
    ROOT_CAUSE_ANALYSIS = "ROOT_CAUSE_ANALYSIS"
    PHASE_JUMP = "PHASE_JUMP"


class SystemTemplateArchitectureColumn:
    COMPONENT_NAME = "COMPONENT_NAME"
    COMPONENT_TYPE = "COMPONENT_TYPE"
    COMPONENT_NUMBER = "COMPONENT_NUMBER"
    CHILDREN_NAME = "CHILDREN_NAME"
    CHILDREN_LOGIC = "CHILDREN_LOGIC"
    IN_MRU = "IN_MRU"
    TRIGGER_MRU = "TRIGGER_MRU"


class SystemTemplateFailureModeAssignmentsColumn:
    COMPONENT_NAME = "COMPONENT_NAME"
    FAILURE_MODE_NAME = "FAILURE_MODE_NAME"


class SystemTemplateFailureModeColumn:
    FAILURE_MODE_NAME = "FAILURE_MODE_NAME"
    FAILURE_LAW = "FAILURE_LAW"
    FAILURE_PARAMETERS = "FAILURE_PARAMETERS"
    REPAIR_LAW = "REPAIR_LAW"
    REPAIR_PARAMETERS = "REPAIR_PARAMETERS"
    TYPE_OF_FAILURE = "TYPE_OF_FAILURE"
    HELD_BEFORE_REPAIR = "HELD_BEFORE_REPAIR"
    INSPECTION_NAME = "INSPECTION_NAME"
    PHASE_NAME = "PHASE_NAME"
    PHASE_NEXT_IF_FAILURE_NAME = "NEXT_PHASE_IF_FAILURE"
    PHASE_CHANGE_TRIGGER = "PHASE_CHANGE_TRIGGER"
    HELD_AFTER_REPAIR = "HELD_AFTER_REPAIR"


class SystemTemplateMinimalReplaceableUnitColumn:
    MINIMAL_REPLACEABLE_UNIT_NAME = "MRU_NAME"
    REPAIR_LAW = "MRU_LAW"
    REPAIR_PARAMETERS = "MRU_PARAMETERS"
    REPAIR_SCHEDULE = "MRU_SCHEDULE"
    LOWEST_COMMON_ANCESTOR = "LOWEST_COMMON_ANCESTOR_SCOPE"
    TRIGGERING_STATUS = "TRIGGERING_STATUS"


class SystemTemplateInspectionsColumn:
    INSPECTION_NAME = "INSPECTION_NAME"
    INSPECTION_PERIOD = "INSPECTION_PERIOD"
    INSPECTION_DURATION = "INSPECTION_DURATION"


class SystemTemplatePhasesColumn:
    PHASE_NAME = "PHASE_NAME"
    PHASE_LAW = "PHASE_LAW"
    PHASE_PARAMETERS = "PHASE_PARAMETERS"
    PHASE_NEXT = "NEXT_DEFAULT_PHASE"
    PHASE_FIRST = "FIRST_PHASE"
    PHASE_NEXT_IF_FAILURE = "NEXT_DEFAULT_PHASE_IF_FAILURE"


class SystemTemplateRootCauseAnalysisColumn:
    COMPONENT_NAME = "TRIGGERING_COMPONENT_NAME"
    COMPONENT_STATUS = "TRIGGERED_BY_COMPONENT_STATUS"
    PHASE = "TRIGGERED_IN_PHASE"


class SystemTemplatePhaseJumpColumn:
    COMPONENT_NAME = "TRIGGERING_COMPONENT_NAME"
    COMPONENT_STATUS = "TRIGGERED_BY_COMPONENT_STATUS"
    FROM_PHASE = "FROM_PHASE"
    TO_PHASE = "TO_PHASE"


class SystemTemplateField:
    NONE = "NONE"


class DuplicatedEntry(Exception):
    pass


class SystemTemplateReader(XLSXReader):

    @classmethod
    def generate_system_template(cls,
                                 system_file_path: str,
                                 custom_children_logic_path: str):
        """
        Given a file `system_file_path` which describe the system template.
        This methods generates the corresponding {SystemTemplate} object.
        :return SystemTemplate based on the given file path.
        """
        logging.debug(f"Reading System File = {system_file_path}")

        system_dictionary = cls.read(system_file_path)

        architecture_entry_list = cls.generate_architecture_entry_list(
            system_dictionary[SystemTemplateSheet.ARCHITECTURE])

        mru_list = cls.generate_mrus(system_dictionary[SystemTemplateSheet.MINIMAL_REPLACEABLE_UNIT])

        inspections_list = cls.generate_inspections(system_dictionary[SystemTemplateSheet.INSPECTIONS])

        phases_list = cls.generate_phases(system_dictionary[SystemTemplateSheet.PHASES])

        failure_modes_list = cls.generate_failure_modes(system_dictionary[SystemTemplateSheet.FAILURE_MODES],
                                                        inspections_list,
                                                        phases_list)

        failure_mode_assignments_list = cls.generate_failure_mode_assignments(
            system_dictionary[SystemTemplateSheet.FAILURE_MODE_ASSIGNMENTS],
            failure_modes_list)

        root_cause_analysis_triggers_list = cls.generate_root_cause_analysis_triggers(system_dictionary[SystemTemplateSheet.ROOT_CAUSE_ANALYSIS])

        phase_jump_triggers_list = cls.generate_phase_jump_triggers(system_dictionary[SystemTemplateSheet.PHASE_JUMP],
                                                                    phases_list)

        return SystemTemplate(architecture_entry_list,
                              failure_mode_assignments_list,
                              failure_modes_list,
                              mru_list,
                              inspections_list,
                              phases_list,
                              set(root_cause_analysis_triggers_list),
                              set(phase_jump_triggers_list),
                              custom_children_logic_path)

    @classmethod
    def generate_architecture_entry_list(cls, system_dictionary_architecture):
        """
        Extract from the given system_dictionary_architecture the list of the {ArchitectureEntry} of the global system.
        :param system_dictionary_architecture: the system_dictionary failure mode under the panda dictionary format.
        :return: List of {ArchitectureEntry} of the global system.
        """

        architecture_entry_list = []

        for row in system_dictionary_architecture.values():
            try:

                exception_message_hint = f"architecture row:{row}"

                component_name_str = cls.clean_cell_str_else_raise(row[SystemTemplateArchitectureColumn.COMPONENT_NAME],
                                                                   exception_message_hint=exception_message_hint)

                if component_name_str in [architecture_entry.component_name for architecture_entry in architecture_entry_list]:
                    message = f"The component name {component_name_str} is not unique in the list of architecture entries"
                    logging.exception(message)
                    raise DuplicatedEntry(message)
                
                component_type_str = cls.clean_cell_str_else_raise(row[SystemTemplateArchitectureColumn.COMPONENT_TYPE],
                                               exception_message_hint=exception_message_hint)

                component_number = row[SystemTemplateArchitectureColumn.COMPONENT_NUMBER]

                children_name_str = row[SystemTemplateArchitectureColumn.CHILDREN_NAME].upper()
                children_name_list = [] if children_name_str == SystemTemplateField.NONE \
                    else cls.extract_from_str_list(children_name_str, exception_message_hint=exception_message_hint)

                children_logic_str = cls.clean_cell_str_else_raise(row[SystemTemplateArchitectureColumn.CHILDREN_LOGIC],
                                                   exception_message_hint=exception_message_hint)
                children_logic_str = '' if children_logic_str == SystemTemplateField.NONE else children_logic_str

                in_mru_line = row[SystemTemplateArchitectureColumn.IN_MRU].upper()
                in_mru_str_list = [] if in_mru_line == SystemTemplateField.NONE \
                    else cls.extract_from_str_list(in_mru_line,exception_message_hint=exception_message_hint)

                trigger_mru_line = row[SystemTemplateArchitectureColumn.TRIGGER_MRU].upper()
                trigger_mru_str_list = [] if trigger_mru_line == SystemTemplateField.NONE \
                    else cls.extract_from_str_list(trigger_mru_line,exception_message_hint=exception_message_hint)

                architecture_entry_list.append(
                    ArchitectureEntry(
                        component_name_str,
                        component_type_str,
                        component_number,
                        children_name_list,
                        children_logic_str,
                        in_mru_str_list,
                        trigger_mru_str_list
                    )
                )
            except AttributeError:
                logging.info(f"Non-empty line with missing content present in the architecture sheet."
                             f"\nCheck row:{row}")

        logging.debug(f"Extracted from system file architecture_entry_list = {architecture_entry_list}")

        return architecture_entry_list

    @classmethod
    def generate_mrus(cls, system_dictionary_mru):
        """
        Extract from the given system_dictionary_mru the list of the MRUs of the global system.
        :param system_dictionary_mru: the system_dictionary mru under the panda dictionary format.
        see> SystemTemplate
        :return: List of Minimal Replaceable Unit of the global system.
        """

        mru_list = []

        for row in system_dictionary_mru.values():
            try:

                exception_message_hint = f"mru row:{row}"

                mru_name_str = cls.clean_cell_str_else_raise(
                    row[SystemTemplateMinimalReplaceableUnitColumn.MINIMAL_REPLACEABLE_UNIT_NAME],
                    exception_message_hint=exception_message_hint)

                if mru_name_str in [mru.name for mru in mru_list]:
                    message = f"The mru name {mru_name_str} is not unique in the list of mru entries"
                    logging.exception(message)
                    raise DuplicatedEntry(message)

                mru_repair_law_name = cls.clean_cell_str_else_raise(
                    row[SystemTemplateMinimalReplaceableUnitColumn.REPAIR_LAW],
                    exception_message_hint=exception_message_hint)

                mru_repair_parameters = row[SystemTemplateMinimalReplaceableUnitColumn.REPAIR_PARAMETERS]
                mru_repair_parameters = [mru_repair_parameters] if isinstance(mru_repair_parameters, (int, float)) \
                    else cls.extract_from_str_list(mru_repair_parameters,exception_message_hint=exception_message_hint)

                minimal_replaceable_repair_schedule = cls.clean_cell_str_else_raise(
                    row[SystemTemplateMinimalReplaceableUnitColumn.REPAIR_SCHEDULE],
                    exception_message_hint=exception_message_hint)

                lowest_common_parent_name_list = cls.extract_from_str_list(
                    row[SystemTemplateMinimalReplaceableUnitColumn.LOWEST_COMMON_ANCESTOR],
                    exception_message_hint=exception_message_hint)

                triggering_status_list_of_str = cls.extract_from_str_list(
                    row[SystemTemplateMinimalReplaceableUnitColumn.TRIGGERING_STATUS],
                    exception_message_hint=exception_message_hint)

                mru = MinimalReplaceableUnitFactory.build(mru_name_str,
                                                          mru_repair_law_name,
                                                          mru_repair_parameters,
                                                          minimal_replaceable_repair_schedule,
                                                          triggering_status_list_of_str,
                                                          lowest_common_parent_name_list)

                mru_list.extend(mru)
            except AttributeError:
                logging.info("Non-empty line with missing content present in the MRU sheet."
                             f"\nCheck row:{row}")

        logging.debug(f"Extracted from system file mru_list = {mru_list}")

        return mru_list

    @classmethod
    def generate_inspections(cls, system_dictionary_inspections):
        """
        Extract from the given system_dictionary_inspections the list of the inspection of the global system.
        :param system_dictionary_inspections: the system_dictionary inspections under the panda dictionary format.
        see> SystemTemplate
        :return: List of inspections of the global system.
        """

        inspections_list = []

        for row in system_dictionary_inspections.values():
            try:

                exception_message_hint = f"inspection row: {row}"

                inspection_name_str = cls.clean_cell_str_else_raise(row[SystemTemplateInspectionsColumn.INSPECTION_NAME],
                                                exception_message_hint=exception_message_hint)

                if inspection_name_str in [inspection.name for inspection in inspections_list]:
                    message = f"The inspection {inspection_name_str} is not unique in the list of inspections"
                    logging.exception(message)
                    raise DuplicatedEntry(message)

                inspection_period = row[SystemTemplateInspectionsColumn.INSPECTION_PERIOD]

                inspection_duration = row[SystemTemplateInspectionsColumn.INSPECTION_DURATION]

                inspections_list.append(Inspection(inspection_name_str,
                                                   inspection_period,
                                                   inspection_duration))
            except AttributeError:
                logging.info("Non-empty line with missing content present in the Inspections sheet."
                             f"\nCheck row:{row}")

        logging.debug(f"Extracted from system file inspections_list = {inspections_list}")

        return inspections_list

    @classmethod
    def generate_phases(cls, system_dictionary_phases):
        """
        Extract from the given `system_dictionary_phase` the list of the {Phase} of the global system.
        :param system_dictionary_phases: the system_dictionary_phases under the panda dictionary format.
        :return: List of {Phase} of the global system.
        """

        phases_list = []
        dict_phase_next = {}
        dict_next_phase_if_failure = {}

        for row in system_dictionary_phases.values():
            try:

                exception_message_hint = f"phases row: {row}"

                phase_name_str = cls.clean_cell_str_else_raise(row[SystemTemplatePhasesColumn.PHASE_NAME],exception_message_hint=exception_message_hint)

                if phase_name_str in [phase.name for phase in phases_list]:
                    message = f"The phase {phase_name_str} is not unique in the list of phases"
                    logging.exception(message)
                    raise DuplicatedEntry(message)

                phase_law_str = cls.clean_cell_str_else_raise(row[SystemTemplatePhasesColumn.PHASE_LAW],exception_message_hint=exception_message_hint)

                phase_parameters = row[SystemTemplatePhasesColumn.PHASE_PARAMETERS]
                phase_parameters = [phase_parameters] if isinstance(phase_parameters, (int, float)) \
                    else cls.extract_from_str_list(phase_parameters,exception_message_hint=exception_message_hint)

                phase_next_name_str = cls.clean_cell_str_else_raise(row[SystemTemplatePhasesColumn.PHASE_NEXT],exception_message_hint=exception_message_hint)

                phase_first = bool(row[SystemTemplatePhasesColumn.PHASE_FIRST])

                next_phase_if_failure_name_str = cls.clean_cell_str_else_raise(row[SystemTemplatePhasesColumn.PHASE_NEXT_IF_FAILURE],
                                                               exception_message_hint=exception_message_hint)

                phase_law = ProbabilityLawFactory.build(phase_law_str,
                                                        phase_parameters)

                not_linked_phase = Phase(phase_name_str,
                                         phase_law,
                                         phase_first)

                dict_phase_next[not_linked_phase] = phase_next_name_str

                dict_next_phase_if_failure[not_linked_phase] = next_phase_if_failure_name_str

                phases_list.append(not_linked_phase)
            except AttributeError:
                logging.info("Non-empty line with missing content present in the Phases sheet."
                             f"\nCheck row:{row}")

        for not_linked_phase in phases_list:
            for phase in phases_list:
                if phase.name == dict_phase_next[not_linked_phase]:
                    not_linked_phase.set_next_phase(phase)
                if phase.name == dict_next_phase_if_failure[not_linked_phase]:
                    not_linked_phase.set_next_phase_if_failure(phase)

        if not phases_list:
            phases_list = [PhaseManager.NO_PHASE]  # Default is NO_PHASE

        logging.debug(f"Extracted from system file phases_list = {phases_list}")

        return phases_list

    @classmethod
    def generate_failure_modes(cls,
                               system_dictionary_failure_mode,
                               inspections_list,
                               phase_list):
        """
        Extract from the given system_dictionary_failure_mode the list of the FailureModes of the global system.
        :param system_dictionary_failure_mode: the system_dictionary failure mode under the panda dictionary format.
        see> SystemTemplate
        :param inspections_list: the list of inspections objects
        :param phase_list: List of phases {Phase}
        :return: List of FailureMode of the global system.
        """

        failure_modes_list = []

        for row in system_dictionary_failure_mode.values():
            try:

                exception_message_hint = f"failure mode row: {row}"

                failure_mode_name_str = cls.clean_cell_str_else_raise(row[SystemTemplateFailureModeColumn.FAILURE_MODE_NAME],
                                                      exception_message_hint=exception_message_hint)

                if failure_mode_name_str in [failure_mode.name for failure_mode in failure_modes_list]:
                    message = f"The failure mode {failure_mode_name_str} is not unique in the list of failure modes"
                    logging.exception(message)
                    raise DuplicatedEntry(message)

                failure_mode_failure_law = cls.clean_cell_str_else_raise(row[SystemTemplateFailureModeColumn.FAILURE_LAW],
                                                         exception_message_hint=exception_message_hint)

                failure_mode_failure_parameters = row[SystemTemplateFailureModeColumn.FAILURE_PARAMETERS]
                failure_mode_failure_parameters = [failure_mode_failure_parameters] \
                    if isinstance(failure_mode_failure_parameters, (int, float)) \
                    else cls.extract_from_str_list(failure_mode_failure_parameters, exception_message_hint=exception_message_hint)

                failure_mode_repair_law = cls.clean_cell_str_else_raise(row[SystemTemplateFailureModeColumn.REPAIR_LAW],
                                                        exception_message_hint=exception_message_hint)

                failure_mode_repair_parameters = row[SystemTemplateFailureModeColumn.REPAIR_PARAMETERS]
                failure_mode_repair_parameters = [failure_mode_repair_parameters] \
                    if isinstance(failure_mode_repair_parameters, (int, float)) \
                    else cls.extract_from_str_list(failure_mode_repair_parameters, exception_message_hint=exception_message_hint)

                failure_mode_type_of_failure = cls.clean_cell_str_else_raise(row[SystemTemplateFailureModeColumn.TYPE_OF_FAILURE],
                                                             exception_message_hint=exception_message_hint)

                failure_mode_failure = FailureFactory.build(failure_mode_type_of_failure)

                failure_mode_phase_str = row[SystemTemplateFailureModeColumn.PHASE_NAME]
                failure_mode_phase_str = cls.extract_from_str_list(failure_mode_phase_str, exception_message_hint=exception_message_hint)

                failure_mode_next_phase_if_failure_name_str = cls.clean_cell_str_else_raise(
                    row[SystemTemplateFailureModeColumn.PHASE_NEXT_IF_FAILURE_NAME],
                    exception_message_hint=exception_message_hint)

                failure_mode_held_before_repair_str = cls.extract_from_str_list(
                    row[SystemTemplateFailureModeColumn.HELD_BEFORE_REPAIR],
                    exception_message_hint=exception_message_hint)

                failure_mode_phase_change_trigger = cls.clean_cell_str_else_raise(
                    row[SystemTemplateFailureModeColumn.PHASE_CHANGE_TRIGGER],
                    exception_message_hint=exception_message_hint)

                failure_mode_held_after_repair_str = cls.extract_from_str_list(
                    row[SystemTemplateFailureModeColumn.HELD_AFTER_REPAIR],
                    exception_message_hint=exception_message_hint)

                failure_law = ProbabilityLawFactory.build(failure_mode_failure_law,
                                                          failure_mode_failure_parameters)

                repair_law = ProbabilityLawFactory.build(failure_mode_repair_law,
                                                         failure_mode_repair_parameters)

                failure_mode_inspection_name_line = row[SystemTemplateFailureModeColumn.INSPECTION_NAME].upper()
                failure_mode_inspection = next(
                    (inspection
                    for inspection in inspections_list
                    if inspection.name == failure_mode_inspection_name_line),
                    None)

                failure_mode_phase_set = {phase
                                        for phase in phase_list
                                        if phase.name in failure_mode_phase_str}

                failure_mode_next_phase_if_failure = None
                if failure_mode_next_phase_if_failure_name_str != SystemTemplateField.NONE:
                    for phase in phase_list:
                        if phase.name == failure_mode_next_phase_if_failure_name_str:
                            failure_mode_next_phase_if_failure = phase

                if failure_mode_held_after_repair_str[0] == "HELD_FOREVER":
                    failure_mode_held_after_repair_phase_set= {PhaseManager.HELD_FOREVER}  # Special phase used to never release some held components
                elif failure_mode_held_after_repair_str[0] == "NEVER_HELD":
                    failure_mode_held_after_repair_phase_set = set(phase_list)
                else:
                    failure_mode_held_after_repair_phase_set = {phase
                                                for phase in phase_list
                                                if phase.name in failure_mode_held_after_repair_str}

                if failure_mode_held_before_repair_str[0] == "HELD_FOREVER":
                    failure_mode_held_before_repair_phase_set= {PhaseManager.HELD_FOREVER}  # Special phase used to never release some held components
                elif failure_mode_held_before_repair_str[0] == "NEVER_HELD":
                    failure_mode_held_before_repair_phase_set = set(phase_list)
                else:
                    failure_mode_held_before_repair_phase_set = {phase
                                                for phase in phase_list
                                                if phase.name in failure_mode_held_before_repair_str}

                failure_modes_list.append(FailureMode(failure_mode_name_str,
                                                      failure_law,
                                                      repair_law,
                                                      failure_mode_failure,
                                                      failure_mode_held_before_repair_phase_set,
                                                      failure_mode_inspection,
                                                      failure_mode_phase_set,
                                                      failure_mode_next_phase_if_failure,
                                                      failure_mode_phase_change_trigger,
                                                      failure_mode_held_after_repair_phase_set))
            except AttributeError:
                logging.info("Non-empty line with missing content present in the failure_modes sheet."
                             f"\nCheck row:{row}")

        logging.debug(f"Extracted from system file failure_modes_list = {failure_modes_list}")
        return failure_modes_list

    @classmethod
    def generate_failure_mode_assignments(cls,
                                          system_dictionary_assignments,
                                          failure_mode_list):
        """
        Generates failure mode assignments containing failure mode components by matching failure modes from the given
        `system_dictionary_assignments` with failure modes in the `failure modes list`.
        :param system_dictionary_assignments: The dictionary of failure assignments under the panda dataframe format.
        see> SystemTemplate.
        :param failure_mode_list: The List of Failure Mode to be associated to each of the FailureModeAssignment.
        :return: The complete list of the FailureModeAssignment for the system.
        """
        failure_mode_assignments_list = []
        for row in system_dictionary_assignments.values():
            try:

                exception_message_hint = f"failure mode assignements row: {row}"

                failure_mode_assignments_component_name_str = cls.clean_cell_str_else_raise(
                    row[SystemTemplateFailureModeAssignmentsColumn.COMPONENT_NAME],
                    exception_message_hint=exception_message_hint)
                if failure_mode_assignments_component_name_str in [failure_mode_assignment.component_name
                                                                   for failure_mode_assignment
                                                                   in failure_mode_assignments_list]:
                    message = f"The component name {failure_mode_assignments_component_name_str} is not unique in the list of failure mode assignement names"
                    logging.exception(message)
                    raise DuplicatedEntry(message)

                failure_mode_assignments_failure_mode_name_str = cls.clean_cell_str_else_raise(
                    row[SystemTemplateFailureModeAssignmentsColumn.FAILURE_MODE_NAME],
                    exception_message_hint=exception_message_hint)

                failure_mode = [failure_mode for failure_mode in failure_mode_list
                                if failure_mode.name == failure_mode_assignments_failure_mode_name_str][0]
                failure_mode_assignments_list.append(FailureModeAssignments(failure_mode_assignments_component_name_str,
                                                                            failure_mode))
            except AttributeError:
                logging.info("Non-empty line with missing content present in the failure_mode_assignments sheet."
                             f"\nCheck row:{row}")

        logging.debug(f"Extracted from system file failure_mode_assignments_list = {failure_mode_assignments_list}")
        return failure_mode_assignments_list

    @classmethod
    def generate_root_cause_analysis_triggers(cls, system_dictionary_root_cause_analysis):
        """
        Generates a list of components and their statuses which trigger Root Cause Analysis dumps.
        :param system_dictionary_root_cause_analysis:
        :return: The complete list of RCA triggers for the system.
        """

        root_cause_analysis_triggers_list = []

        for row in system_dictionary_root_cause_analysis.values():
            try:

                exception_message_hint = f"root cause analysis row: {row}"

                root_cause_analysis_trigger_component_name = cls.clean_cell_str_else_raise(
                    row[SystemTemplateRootCauseAnalysisColumn.COMPONENT_NAME],
                    exception_message_hint=exception_message_hint)
                root_cause_analysis_trigger_component_status_list = cls.extract_from_str_list(
                    row[SystemTemplateRootCauseAnalysisColumn.COMPONENT_STATUS],
                    exception_message_hint=exception_message_hint)
                root_cause_analysis_trigger_phase_list = cls.extract_from_str_list(
                    row[SystemTemplateRootCauseAnalysisColumn.PHASE],
                    exception_message_hint=exception_message_hint)

                rca = RootCauseAnalysisTriggerFactory.build(
                    root_cause_analysis_trigger_component_name,
                    root_cause_analysis_trigger_component_status_list,
                    root_cause_analysis_trigger_phase_list
                )

                root_cause_analysis_triggers_list.extend(rca)
            except AttributeError:
                logging.info("Non-empty line with missing content present in the root_cause_analysis sheet."
                             f"\nCheck row:{row}")

        logging.debug(f"Extracted from system file root_cause_analysis_list = {root_cause_analysis_triggers_list}")
        return root_cause_analysis_triggers_list

    @classmethod
    def generate_phase_jump_triggers(cls,
                                     system_dictionary_phase_jump,
                                     phase_list: List[Phase]):
        """
        Generates a list of (component, status, in_phase, jump_to_phase) which trigger phase jumps.
        :param system_dictionary_phase_jump:
        :return: The complete list of phase jump triggers.
        """

        phase_jump_triggers_list = []

        for row in system_dictionary_phase_jump.values():
            try:

                exception_message_hint = f"phase jump row: {row}"

                phase_jump_trigger_component_name = cls.clean_cell_str_else_raise(
                    row[SystemTemplatePhaseJumpColumn.COMPONENT_NAME],
                    exception_message_hint=exception_message_hint)
                phase_jump_trigger_component_status_list = cls.extract_from_str_list(
                    row[SystemTemplatePhaseJumpColumn.COMPONENT_STATUS],
                    exception_message_hint=exception_message_hint)
                phase_jump_trigger_from_phase_list = cls.extract_from_str_list(
                    row[SystemTemplatePhaseJumpColumn.FROM_PHASE],
                    exception_message_hint=exception_message_hint)
                phase_jump_trigger_to_phase = cls.clean_cell_str_else_raise(
                    row[SystemTemplatePhaseJumpColumn.TO_PHASE],
                    exception_message_hint=exception_message_hint)

                phase_jump = PhaseJumpTriggerFactory.build(
                    phase_jump_trigger_component_name,
                    phase_jump_trigger_component_status_list,
                    phase_jump_trigger_from_phase_list,
                    phase_jump_trigger_to_phase,
                    phase_list
                )

                phase_jump_triggers_list.extend(phase_jump)
            except AttributeError:
                logging.info("Non-empty line with missing content present in the phase_jump sheet."
                             f"\nCheck row:{row}")

        logging.debug(f"Extracted from system file phase_jump_triggers_list = {phase_jump_triggers_list}")
        return phase_jump_triggers_list