import datetime
import textwrap

import yaml

from steam_sdk.data.DataCircuit import DataCircuit, Component
from steam_sdk.parsers.ParserExcel import compare_two_parameters


class ParserPSPICE:
    """
        Class with methods to read/write PSPICE information from/to other programs
    """

    def __init__(self, circuit_data: DataCircuit):
        """
            Initialization using a DataCircuit object containing circuit netlist structure
        """

        self.circuit_data: DataCircuit = circuit_data


    def read_netlist(self, full_path_file_name: str, verbose: bool = False):
        '''
        ** Reads a PSPICE netlist file **

        :param full_path_file_name:
        :param verbose:
        :return: ModelCircuit dataclass with filled keys
        '''

        # Initialize
        self.circuit_data = DataCircuit()
        # Set flags indicating that the last read line corresponds to an item that might span to the next line
        self._set_all_flags_to_false()

        with open(full_path_file_name) as file:
            for row, line in enumerate(file):
                if verbose: print(line.rstrip())

                # Reset all flags to False if the line does not contain '+ '
                if not '+ ' in line:
                    self._set_all_flags_to_false()

                # If the line is a comment, skip to the next
                if '*' in line and line[0] == '*':
                    continue
                # If the line is empty, skip to the next
                if line == [] or line == [''] or line == '\n':
                    continue
                # If the line is the ending command, skip to the next
                if '.END' in line:
                    continue

                # Read stimuli
                if '.STMLIB' in line:
                    line_split = line.rstrip('\n').split(' ')  # Note: .rstrip('\n') removes the endline. .spolit(' ') makes a list of space-divided strings
                    value = line_split[1].strip('"')  # Note: .strip('"') removes all " sybmbols from the string
                    self.circuit_data.Stimuli.stimulus_files.append(str(value))
                    continue

                # Read libraries
                if '.LIB' in line:
                    line_split = line.rstrip('\n').split(' ')
                    value = line_split[1].strip('"')
                    self.circuit_data.Libraries.component_libraries.append(str(value))
                    continue

                # Read global parameters
                if '.PARAM' in line:  # it also covers the case where ".PARAMS" is written
                    self.flag_read_global_parameters = True
                    continue
                if self.flag_read_global_parameters and '+ ' in line:
                    line_split = line.rstrip('\n').split(' ')
                    line_split = line_split[1].split('=')
                    name  = line_split[0].strip('"')
                    value = line_split[1].strip('{').strip('}')
                    self.circuit_data.GlobalParameters.global_parameters.append([str(name), str(value)])
                    continue

                # Read options
                if '.OPTION' in line:  # it also covers the case where ".OPTIONS" is written
                    self.flag_read_options = True
                    continue
                if self.flag_read_options and '+ ' in line:
                    line_split = line.rstrip('\n').split(' ')
                    line_split = line_split[1].split('=')
                    name  = line_split[0].strip('"')
                    value = line_split[1].strip('{').strip('}')
                    self.circuit_data.Options.options_simulation.append([str(name), str(value)])
                    continue

                # Read options
                if '.AUTOCONVERGE' in line:
                    self.flag_read_autoconverge = True
                    continue
                if self.flag_read_autoconverge and '+ ' in line:
                    line_split = line.rstrip('\n').split(' ')
                    line_split = line_split[1].split('=')
                    name  = line_split[0].strip('"')
                    value = line_split[1].strip('{').strip('}')
                    self.circuit_data.Options.options_autoconverge.append([str(name), str(value)])
                    continue

                # Read analysis
                if '.TRAN' in line:
                    self.circuit_data.Analysis.analysis_type = 'transient'
                    line_split = line.rstrip('\n').split(' ')
                    self.circuit_data.Analysis.simulation_time.time_start = str(line_split[1])
                    self.circuit_data.Analysis.simulation_time.time_end = str(line_split[2])
                    if len(line_split) > 3:
                        self.circuit_data.Analysis.simulation_time.min_time_step = str(line_split[3])
                    continue
                elif '.AC' in line:
                    self.circuit_data.Analysis.analysis_type = 'frequency'
                    continue
                elif '.STEP' in line:
                    # TODO. Parametric analysis
                    continue

                # Read time schedule
                if '+ {SCHEDULE(' in line:
                    self.flag_read_time_schedule = True
                    continue
                # If the line is the end of the time schedule section, skip to the next
                if '+ )}' in line or '+)}' in line:
                    continue
                if self.flag_read_time_schedule and '+ ' in line:
                    line_split = line.rstrip('\n').split('+ ')
                    line_split = line_split[1].split(',')
                    name  = line_split[0].strip(' ').strip('\t').strip(' ')
                    value = line_split[1].strip(' ').strip('\t').strip(' ')
                    self.circuit_data.Analysis.simulation_time.time_schedule.append([str(name), str(value)])
                    continue

                # Read probe
                if '.PROBE' in line:
                    if '/CSDF' in line:
                        self.circuit_data.PostProcess.probe.probe_type = 'CSDF'
                    else:
                        self.circuit_data.PostProcess.probe.probe_type = 'standard'
                    self.flag_read_probe = True
                    # TODO: Known issue: If probe variables are defined in this same line, they are ignored
                    continue
                if self.flag_read_probe and '+ ' in line:
                    line_split = line.rstrip('\n').split(' ')
                    value = line_split[1]
                    self.circuit_data.PostProcess.probe.variables.append(str(value))
                    continue

                # Read additional files
                if '.INC' in line:
                    line_split = line.rstrip('\n').split(' ')
                    value = line_split[1].strip('"')
                    self.circuit_data.AuxiliaryFiles.files_to_include.append(str(value))
                    continue

                # Read netlist - If this part of the code is reached without hitting "continue", it means that this line does not define a special command, and hence it defines a component of the netlist
                self.flag_read_parametrized_component = True
                if '+ PARAM' in line:  # This line defines parameters of the component
                    # Reminder: This type of line looks like this: + PARAMS: name1={value1} name2={value2} name3={value3}
                    line_split = line.rstrip('\n').partition(':')[2]  # Take the part of the string after the first "+" char
                    # line_split = line.rstrip('\n').split(':')  # Split line in two, before and after the "+ PARAMS:" command
                    # line_split = line_split[1].strip(' ')      # Take the second element and remove whitespaces at its extremities
                    line_split = line_split.split('}')         # Split into different parameters
                    for par in line_split:                     # Loop through the parameters
                        par_split = par.split('=')             # Split into name and value of the parameter
                        if len(par_split) == 2:                # Only take into account entries with two elements (for example, avoid None)
                            name_par = str(par_split[0].strip(' '))
                            value_par = str(par_split[1].strip(' { '))  # Strip spaces and bracket at the extremities
                            self.circuit_data.Netlist[-1].parameters.append([str(name_par), str(value_par)])
                    continue
                elif '+' in line and line[0] == '+':  # This line defines additional parameters of the component
                    # Reminder: This type of line looks like this: + PARAMS: name1={value1} name2={value2} name3={value3}
                    line_split = line.rstrip('\n').partition('+')[2]        # Take the part of the string after the first "+" char
                    line_split = line_split.split('}')                      # Split into different parameters
                    for par in line_split:                                  # Loop through the parameters
                        par_split = par.split('=')                          # Split into name and value of the parameter
                        if len(par_split) == 2:                             # Only take into account entries with two elements (for example, avoid None)
                            name_par  = str(par_split[0].strip(' '))
                            value_par = str(par_split[1].strip(' { '))  # Strip spaces and bracket at the extremities
                            self.circuit_data.Netlist[-1].parameters.append([str(name_par), str(value_par)])
                    continue
                # If this part of the code is reached, the line defines a new component

                line_split = line.rstrip('\n').split('(')  # TODO: Improve the logic, which now fails if the value includes the character "("
                name = line_split[0].strip(' ')
                line_split = line_split[1].rstrip('\n').split(')')
                nodes = line_split[0].split(' ')
                value = line_split[1].strip(' { } ')  # Strip spaces and bracket at the extremities
                if not self.circuit_data.Netlist[0].name == None:  # do not append a new element if it is the first component
                    self.circuit_data.Netlist.append(Component())
                self.circuit_data.Netlist[-1].type = 'component'
                self.circuit_data.Netlist[-1].name  = str(name)
                self.circuit_data.Netlist[-1].nodes = nodes
                self.circuit_data.Netlist[-1].value = str(value)
                # self.circuit_data.Netlist[-1].type  =  # TODO: Add logic

        return self.circuit_data

    def _set_all_flags_to_false(self):
        '''
            # Set flags indicating that the last read line corresponds to an item that might span to the next line
        '''
        self.flag_read_global_parameters = False
        self.flag_read_parametrized_component = False
        self.flag_read_options = False
        self.flag_read_autoconverge = False
        self.flag_read_time_schedule = False
        self.flag_read_probe = False


    def write2pspice(self, full_path_file_name: str, verbose: bool = False):
        '''
        ** Writes a PSPICE netlist file **

        :param full_path_file_name:
        :param verbose:
        :return:
        '''

        # Prepare header
        time_start = datetime.datetime.now()
        rows_header = [
            add_comment('PSPICE Netlist Simulation File'),
            add_comment('Generated at {} at CERN using STEAM_SDK'.format(time_start)),
            add_comment('Authors: STEAM Team'),
        ]

        # Prepare stimuli
        rows_stimuli = []
        for s in self.circuit_data.Stimuli.stimulus_files:
            rows_stimuli.append(add_stimulus(s))

        # Prepare libraries
        rows_libraries = []
        for s in self.circuit_data.Libraries.component_libraries:
            rows_libraries.append(add_library(s))

        # Prepare global parameters
        rows_global_parameters = []
        for s, global_parameter in enumerate(self.circuit_data.GlobalParameters.global_parameters):
            # Check input size
            if len(global_parameter) != 2:
                raise Exception ('All global parameters entries must have 2 elements (name, value), but parameter {}, in position #{} has {} elements.'.format(global_parameter, s+1, len(global_parameter)))
            # Add comment and .PARAM command before the first entry
            if s == 0:
                rows_global_parameters.append(add_comment('**** Global parameters ****'))  # Add header of this section
                rows_global_parameters.append('.PARAM')  # Add header of this section
            # Add global parameter entry
            name, value = global_parameter[0], global_parameter[1]
            rows_global_parameters.append(add_global_parameter(name, value))

        # Prepare netlist
        rows_netlist = []
        # Check inputs
        if not self.circuit_data.Netlist[0].type:
            raise Exception('At least one netlist entry of known type must be added. Supported component types:\n' +
                            '- comment\n' +
                            '- component\n'
                            'Netlist cannot be generated.')
        rows_global_parameters.append(add_comment('**** Netlist ****'))  # Add header of this section
        for s, component in enumerate(self.circuit_data.Netlist):
            # Read keys
            name, nodes, value, model, parameters, type = \
                component.name, component.nodes, component.value, component.model, component.parameters, component.type

            # Add the relevant row depending on the component type
            if type == 'comment':
                if verbose: print('Netlist entry {} in position #{} is treated as a comment.'.format(name, s + 1))
                rows_netlist.append(add_comment(value))
            elif type == 'component':
                if name == None or nodes == None or value == None:
                    raise Exception('Netlist component in position #{} is of type {} and requires name, nodes, and value.'.format(s+1, type))
                if parameters == None:
                    if verbose: print('Netlist entry {} in position #{} is treated as a non-parametrized component.'.format(name, s + 1))
                    rows_netlist.append(add_standard_component(name, nodes, value))
                else:
                    if verbose: print('Netlist entry {} in position #{} is treated as a parametrized component.'.format(name, s+1))
                    rows_netlist.append(add_parametrized_component(name, nodes, value, parameters))
            else:
                raise Exception ('Netlist entry {} in position #{} has an unknown type: {}.'.format(component.name, s+1, type))

        # Prepare options - Simulation options
        rows_options = []

        options = self.circuit_data.Options.options_simulation
        if options == ['default']:
            print('Default simulation options are applied.')
            options = [
                ['RELTOL', '0.0001'],
                ['VNTOL', '0.00001'],
                ['ABSTOL', '0.0001'],
                ['CHGTOL', '0.000000000000001'],
                ['GMIN', '0.000000000001'],
                ['ITL1', '150'],
                ['ITL2', '20'],
                ['ITL4', '10'],
                ['TNOM', '27'],
                ['NUMDGT', '8'],
            ]
        for s, option in enumerate(options):
            # Check input size
            if len(option) != 2:
                raise Exception(
                    'All global parameters entries must have 2 elements (name, value), but parameter {}, in position #{} has {} elements.'.format(
                        option, s + 1, len(option)))
            # Add comment and .OPTIONS command before the first entry
            if s == 0:
                rows_options.append(
                    add_comment('**** Simulation options ****'))  # Add header of this section
                rows_options.append('.OPTIONS')  # Add header of this section
            # Add global parameter entry
            name, value = option[0], option[1]
            rows_options.append(add_option(name, value))

        # Prepare options - Autoconverge simulation options
        options_autoconverge = self.circuit_data.Options.options_autoconverge
        if options_autoconverge == ['default']:
            print('Default autoconverge simulation options_autoconverge are applied.')
            options_autoconverge = [
                ['RELTOL', '0.05'],
                ['VNTOL', '0.0001'],
                ['ABSTOL', '0.0001'],
                ['ITL1', '1000'],
                ['ITL2', '1000'],
                ['ITL4', '1000'],
                ['PIVTOL', '0.0000000001'],
                ]
        for s, option in enumerate(options_autoconverge):
            # Check input size
            if len(option) != 2:
                raise Exception(
                    'All global parameters entries must have 2 elements (name, value), but parameter {}, in position #{} has {} elements.'.format(option, s + 1, len(option)))
            # Add comment and .AUTOCONVERGE command before the first entry
            if s == 0:
                rows_options.append(add_comment('**** Simulation autoconverge options ****'))  # Add header of this section
                rows_options.append('.AUTOCONVERGE')  # Add header of this section
            # Add global parameter entry
            name, value = option[0], option[1]
            rows_options.append(add_option(name, value))

        # Prepare analysis settings
        rows_analysis = []
        analysis_type = self.circuit_data.Analysis.analysis_type
        if analysis_type == 'transient':
            # Unpack inputs
            time_start = self.circuit_data.Analysis.simulation_time.time_start
            time_end = self.circuit_data.Analysis.simulation_time.time_end
            min_time_step = self.circuit_data.Analysis.simulation_time.min_time_step
            time_schedule = self.circuit_data.Analysis.simulation_time.time_schedule
            # Check inputs
            if not time_start:
                time_start = '0'
                print('Parameter time_start set to {} by default.'.format(time_start))
            if not time_end:
                raise Exception('When "transient" analysis is selected, parameter Analysis.simulation_time.time_end must be defined.')
            if not min_time_step:
                print('Parameter min_time_step was missing and it will not be written.')
            # Add analysis entry
            rows_analysis.append(add_transient_analysis(time_start, time_end, min_time_step))
            # If defined, add time schedule (varying minimum time stepping) entry
            if time_schedule and len(time_schedule) > 0 and len(time_schedule[0]):
                rows_analysis.append(add_transient_time_schedule(time_schedule))
        elif analysis_type == 'frequency':
            # TODO: frequency analysis. EXAMPLE: .AC DEC 50 1Hz 200kHz
            # TODO: DC analysis
            # TODO: parametric analysis. EXAMPLE: .STEP PARAM C_PARALLEL LIST 100n 250n 500n 750n 1u
            pass
        elif analysis_type == None:
            pass  # netlists can exist that do not have analysis set (for example, it could be defined in an auxiliary file)
        else:
            raise Exception('Analysis entry has an unknown type: {}.'.format(analysis_type))

        # Prepare post-processing settings
        rows_post_processing = []
        probe_type = self.circuit_data.PostProcess.probe.probe_type
        probe_variables = self.circuit_data.PostProcess.probe.variables
        if probe_type:
            rows_post_processing.append(add_probe(probe_type, probe_variables))

        # Prepare additional files to include
        rows_files_to_include = []
        for s in self.circuit_data.AuxiliaryFiles.files_to_include:
            rows_files_to_include.append(add_auxiliary_file(s))

        # Prepare file end
        rows_file_end = [add_end_file()]

        # Assemble all rows to write
        rows_to_write = \
            rows_header + \
            rows_stimuli + \
            rows_libraries + \
            rows_global_parameters + \
            rows_netlist + \
            rows_options + \
            rows_analysis + \
            rows_post_processing + \
            rows_files_to_include + \
            rows_file_end

        # Write netlist file
        with open(full_path_file_name, 'w') as f:
            for row in rows_to_write:
                if verbose: print(row)
                f.write(row)
                f.write('\n')

        # Display time stamp
        time_written = datetime.datetime.now()
        if verbose:
            print(' ')
            print('Time stamp: ' + str(time_written))
            print('New file ' + full_path_file_name + ' generated.')


    def readFromYaml(self, full_path_file_name: str, verbose: bool = False):
        # Load yaml keys into DataCircuit dataclass
        with open(full_path_file_name, "r") as stream:
            dictionary_yaml = yaml.safe_load(stream)
            self.circuit_data = DataCircuit(**dictionary_yaml)
        if verbose:
            print('File ' + full_path_file_name + ' read.')


    def write2yaml(self, full_path_file_name: str, verbose: bool = False):
        '''
        ** Write netlist to yaml file **
        :param full_path_file_name:
        :param verbose:
        :return:
        '''

        all_data_dict = {**self.circuit_data.dict()}
        with open(full_path_file_name, 'w') as outfile:
            yaml.dump(all_data_dict, outfile, default_flow_style=False, sort_keys=False)
        if verbose:
            print('New file ' + full_path_file_name + ' generated.')


#######################  Helper functions - START  #######################
def add_comment(text: str):
    ''' Format comment row '''
    if text[0] == '*':
        return text  # If the input string starts with a "*", leave it unchanged (it is already a comment)
    formatted_text = '* ' + text
    return formatted_text

def add_stimulus(text: str):
    ''' Format stimulus row '''
    formatted_text = '.STMLIB ' + text
    return formatted_text

def add_library(text: str):
    ''' Format library row '''
    formatted_text = '.LIB \"' + text + '\"'
    return formatted_text

def add_global_parameter(name: str, value: str):
    ''' Format global parameters row '''
    formatted_text = '+ ' + name + '={' + value + '}'
    return formatted_text

def add_standard_component(name: str, nodes: list, value: str):
    ''' Format standard component netlist row '''
    str_nodes = " ".join(nodes)  # string with space-separated nodes
    formatted_text = name + ' (' + str_nodes + ') ' + '{' + value + '}'
    return formatted_text

# def add_stimulus_controlled_component(name: str, nodes: list, value: str):
#     ''' Format stimulus-controlled component netlist row '''
#     str_nodes = " ".join(nodes)  # string with space-separated nodes
#     str_stimulus = 'STIMULUS = ' + value
#     formatted_text = name + ' (' + str_nodes + ') ' + str_stimulus
#     return formatted_text

def add_parametrized_component(name: str, nodes: list, value: str, parameters: list):
    ''' Format parametrized component netlist row '''
    str_nodes = " ".join(nodes)  # string with space-separated nodes
    formatted_component = name + ' (' + str_nodes + ') ' + '{' + value + '}' + '\n'  # First row, which defines the component
    formatted_parameters = '+ PARAMS:'  # First part of the string in the second row, which defines the component parameters
    for parameter in parameters:
        if len(parameter) != 2:
            raise Exception ('All parameters entries in a parametrized element must have 2 elements (name, value), but parameter {} has {} elements.'.format(name, len(parameter)))
        name_parameters, value_parameters = parameter[0], parameter[1]
        formatted_parameters = formatted_parameters + ' ' + name_parameters + '={' + value_parameters + '}'

    # Make sure the maximum number of characters in each row does not exceed 132, which is the maximum that PSPICE supports
    N_MAX_CHARS_PER_ROW = 130
    formatted_parameters = textwrap.fill(formatted_parameters, N_MAX_CHARS_PER_ROW)
    formatted_parameters = formatted_parameters.replace('\n', '\n+ ')  # Add "+ " at the beginning of each new line

    formatted_text = formatted_component + formatted_parameters  # Concatenate the two rows
    return formatted_text

def add_option(name: str, value: str):
    ''' Format option row '''
    formatted_text = '+ ' + name + '=' + value
    return formatted_text

def add_transient_analysis(time_start, time_end, min_time_step):
    ''' Format transient analysis row '''
    formatted_text = '.TRAN ' + str(time_start) + ' ' + str(time_end)
    if min_time_step:
        formatted_text = formatted_text + ' ' + str(min_time_step)
    return formatted_text

def add_transient_time_schedule(time_schedule):
    ''' Format transient time schedule rows '''
    # If time_schedule is not defined, output will be None
    if time_schedule == None or len(time_schedule) == 0 or len(time_schedule[0]) == 0:
        return None

    formatted_text = '+ {SCHEDULE(\n'
    for t, time_entry in enumerate(time_schedule):
        time_window_start, time_step_in_window = str(time_entry[0]), str(time_entry[1])
        if t+1 == len(time_schedule):
            formatted_text = formatted_text + '+ ' + time_window_start + ', ' + time_step_in_window + '\n'  # the last entry must not have the comma
        else:
            formatted_text = formatted_text + '+ ' + time_window_start + ', ' + time_step_in_window + ',' + '\n'
    formatted_text = formatted_text + '+)}'
    return formatted_text

def add_probe(probe_type: str, probe_variables: list):
    ''' Format probe row '''
    if probe_type == 'standard':
        formatted_text = '.PROBE'
    elif probe_type == 'CSDF':
        formatted_text = '.PROBE /CSDF'
    elif not probe_type:
        return None
    else:
        raise Exception('Probe entry has an unknown type: {}.'.format(probe_type))

    for var in probe_variables:
        formatted_text = formatted_text + '\n' + '+ ' + var

    # Make sure the maximum number of characters in each row does not exceed 132, which is the maximum that PSPICE supports
    N_MAX_CHARS_PER_ROW = 130
    formatted_text = textwrap.fill(formatted_text, N_MAX_CHARS_PER_ROW)
    formatted_text = formatted_text.replace('\n', '\n+ ')  # Add "+ " at the beginning of each new line
    return formatted_text

def add_auxiliary_file(file_to_add: str):
    ''' Format auxiliary file rows '''
    formatted_text = '.INC ' + file_to_add
    return formatted_text

def add_end_file():
    formatted_text = '.END'
    return formatted_text


def ComparePSPICEParameters(fileA, fileB):
    '''
        Compare all the variables imported from two PSPICE netlists
    '''

    pp_a = ParserPSPICE(None)
    pp_a.read_netlist(fileA, verbose=False)
    pp_b = ParserPSPICE(None)
    pp_b.read_netlist(fileB, verbose=False)
    print("Comparing File A: ({}) and File B: ({})".format(fileA, fileB))

    flag_equal = pp_a.circuit_data == pp_b.circuit_data
    return flag_equal

#######################  Helper functions - END  #######################