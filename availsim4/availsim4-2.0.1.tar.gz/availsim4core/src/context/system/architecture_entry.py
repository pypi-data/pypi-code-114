# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

class ArchitectureEntry:

    def __init__(self,
                 component_name,
                 component_type_str,
                 component_number,
                 children_name_list,
                 children_logic_str,
                 in_mru_str_list,
                 trigger_mru_str_list):
        self.component_name = component_name
        self.component_type_str = component_type_str
        self.component_number = component_number
        self.children_name_list = children_name_list
        self.children_logic_str = children_logic_str
        self.in_mru_str_list = in_mru_str_list
        self.trigger_mru_str_list = trigger_mru_str_list

    def __str__(self):
        return (f"name: {self.component_name}; "
                f"type: {self.component_type_str}; "
                f"number: {self.component_number}; "
                f"children: {self.children_name_list}; "
                f"logic: {self.children_logic_str}; "
                f"in mru: {self.in_mru_str_list}; "
                f"trigger mru: {self.trigger_mru_str_list}")

    def __eq__(self, other):
        return self.component_name == other.component_name \
               and self.component_type_str == other.component_type_str \
               and self.component_number == other.component_number \
               and self.children_name_list == other.children_name_list \
               and self.children_logic_str == other.children_logic_str \
               and self.in_mru_str_list == other.in_mru_str_list \
               and self.trigger_mru_str_list == other.trigger_mru_str_list

    def __repr__(self):
        return str(self)
