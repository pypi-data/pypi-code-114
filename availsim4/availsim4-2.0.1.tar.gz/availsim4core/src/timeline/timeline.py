# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from typing import List

from availsim4core.src.timeline.record import Record
from availsim4core.src.timeline.record_component import RecordComponent


class Timeline:
    """
    Timeline of records which have been proceed in the simulation.
    The timeline is ordered.
    """

    def __init__(self):
        self.record_list: List[Record] = []

    def __eq__(self,other):
        return self.record_list == other.record_list

    def __str__(self):
        return str(self.record_list)

    def __repr__(self):
        return self.__str__()

    def extract_record_from_types(self, types):
        """
        Given a tuple a class types this method returns corresponding list of record matching this types.
        :param types: Class types to be filtered out from the list.
        :return: the list of records corresponding to the given types.
        """
        return [record
                for record in self.record_list
                if isinstance(record, types)]

    def _get_previous_record_of_type(self, specified_type):
        """
        Function getting the previous record of a given type.
        :param specified_type: type of the desired record
        :return: None if no record have been found, otherwise the record founded
        """
        counter = 0
        for record in reversed(self.record_list):
            if isinstance(record, specified_type):
                counter += 1
                if counter == 2:
                    return record
        return None

    def _get_previous_record_of_basic_in_status(self, basic, status):
        """
        Function getting the previous record linked to a specific basic component in a specific status.
        :param basic: component to find back in the list of event
        :param status: status to find back in the list of event
        :return: None if no record have been found, otherwise the record founded
        """
        counter = 0
        for record in reversed(self.record_list):
            if isinstance(record,RecordComponent):
                if record.component == basic:
                    # the list of events in the inputs all have a 'basic' attribute because they have failures event
                    # attached to them that one wants to postpone
                    counter += 1
                    if (counter >= 2) and (record.status == status):
                        return record
        return None