##################################################################################
#
# ddrlib - Collection of functions used in DDR-Python scripts for NX-OS
#
# ddrlib functions interact with device management interfaces including cli
# Scripts using ddrlib functions can perform multiple operations including:
#
#    * Triggering execution when specific Syslog messages are generated
#    * Triggering execution by executing show commands, extracting parameters and triggering on values
#    * Generate a Syslog message with content passed to the function
#    * Execute a CLI command on the device in exec mode and optionally return the results
#    * Delay execution for a specified number of seconds
#    * Decode a btrace log file, save the decoded file, find specified parameters in the log and return values
#
#  Revision History
#    * 1.0 - 5.18.21 - petervh - Initial version
#
#################################################################################
import pexpect
import re
import time
import datetime
from datetime import datetime
from genie_parsers import *
import pprint as pp
import os
import operator
from ddrlib import *
# if running in device Guestshell import python CLI package
try:
    import cli
except: pass

def info_msg(message):
  print("#### DDR Info: " + str(message))
  
def debug_msg(debug_flag, message):
  if debug_flag:
    print("**** DDR Debug: " + str(message))
    
def warning_msg(message):
  print("!!!! DDR Warning: " + str(message))

def error_msg(message):
  print("%%%% DDR Error: " + str(message))

def ddr_write_to_file(data: str, target_dir: str, filename: str, mode: str = "w"):
    with open(target_dir+filename, mode) as f:
        f.write(data)

def ddr_delete_file(target_dir: str, filename: str):
    os.remove(target_dir+filename)

def ddr_append_to_file(data: str, target_dir: str, filename: str):
    ddr_write_to_file(data, target_dir, filename, "a")

def ddr_log_data(data: str, target_dir: str,):
    ddr_append_to_file(data, target_dir, "output.json")

def ddr_save_output(data: str, target_dir: str) -> None:
    ddr_write_to_file(data, target_dir, "output.json", "w")

def ddr_get_truth(data, relate, value, debug_flag): 
    '''
        This function compares input "data" to a test "value" using the relationship operator
        defined in "relate".  The function returns True or False depending on the evaluation
        
        :param data: Input data value for comparison
        :param relate: Using the "operator" python object operator.xx where xx is: eq, ne, le, ge, lt, gt
        :param value: Value to compare with the input "data"
    '''
    result = relate(int(data), int(value))
    debug_msg(debug_flag, f"ddr_get_truth: data_read: {str(data)} operator: {str(relate)} value: {str(value)} result: {str(result)}")
    return result

def ddr_show_trigger(device, access_type, genie_parser_name, show_template, pcount, par1, par2, par3, parameter, relate, test_value, interval, retries, debug_flag=False):
        """
            This function executes a show command to read specified parameter and enables triggering of the use case
            by testing the parameter value periodically
                * Execute show command using python "cli" package or SSH
                * Substitute parameters in the show command if required
                * Use the dictionary returned by the parser to compare the value of "leaf" to the "test_value"
                * Perform comparison using the "operator.xx" value in "relate"
                * Periodically perform the test "retries" times waiting "interval" seconds between tries

            :param device: Device information and credentials for running show command
            :param access_type: EXAMPLE to use the Python cli package in the guestshell or 'ssh' for ssh device access
            :param genie_parser_name: genie parser to use to process show command
            :param show_template: show command to execute with optional parameters identified by {0}, {1}, {2}
            :param pcount: Number of parameters to substitute in the show_command 0 to 3
            :param parx: Values for parmeters 1, 2 and 3
            :param parameter: The parameter (dictionary key name) to use as the test value
            :param relate: logical comparision relation "operator.xx" where xx: ne, eq, gt, lt, ge, le
            :param test_value: Value to compare
            :param interval: Time in seconds between testing the value
            :param retries: Number of times to try before exiting, -1 to continue until the condition is found or script terminated
            :param debug_flag: True to enable debug output for this call, False no debug output (default)
        
        Usage::

              ddr_show_trigger(device, 'cli', 'ShowInterfaceState', show_command, 1, 'Loopback1', 'none', 'none', 'admin_state', operator.eq, 'down', 10, 5, debug_flag=True)

            :raises none:

        """
        #######################################################################
        #
        # Generate the show command with parameters
        #
        #######################################################################
        try:
          cmdline = str(show_template)
        #
        # substitute parameters in command string if included in call
        #
          if int(pcount) == 0:
            command = str(cmdline)
          else:
            if int(pcount) == 1:
              command = str(show_template).format(str(par1))
            elif int(pcount) == 2:
              command = str(show_template).format(str(par1), str(par2))
            elif int(pcount) == 3:
              command = str(show_template).format(str(par1), str(par2), str(par3))
        #
        # Loop for a maximum of retries times to test value
        #
          debug_msg(debug_flag, f"ddr_show_trigger: command: " + str(command))

          condition_met = False
          test_count = 1
          while (test_count <= retries) and (condition_met == False):
            test_count = test_count + 1
            if retries == -1:
              test_count = 1 # Loop until condition found or script terminated
        #
        # If access-type is cli use the Python CLI package to run command
        #
            if str(access_type) == 'cli':
              response = cli.cli(command)
              debug_msg(debug_flag, f" ddr_show_trigger: cli python response: {str(response)}")

            else:
        #
        # Use SSH to run the show command
        #
              try:
                options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'
                ssh_cmd = 'ssh %s@%s %s "%s"' % (device[2], device[0], options, command)
                debug_msg(debug_flag, f"ddr_show_trigger: ssh_cmd: {str(ssh_cmd)}")

                child = pexpect.spawn(ssh_cmd, timeout= 20, encoding='utf-8')
                child.delaybeforesend = None
                child.expect(['\r\nPassword: ', '\r\npassword: ', 'Password: ', 'password: '])
                child.sendline(device[3])
                child.expect(pexpect.EOF) #result contains the ping result
                response = child.before
                debug_msg(debug_flag, f"ddr_show_trigger: ssh response: {str(response)}")

              except Exception as e:
                error_msg(f"ddr_show_trigger Exception: {str(e)}")
                child.close()
                raise
    #
    # parse the response to get the test leaf value
    #
            parser = genie_str_to_class(genie_parser_name)
            dictionary = parser.parse(output=response)
            debug_msg(debug_flag, f"ddr_show_trigger: parser dictionary: {str(dictionary)}")
            parameter_value = dictionary[str(parameter)]
    #
    # Test to see if condition to trigger is satisfied
    #
            if ddr_get_truth(parameter_value, relate, test_value, debug_flag):
              condition_met = True
            if condition_met == True:
              info_msg("ddr_show_trigger trigger conditions satisfied")
              return dictionary
            else:
              debug_msg(debug_flag, f"ddr_show_trigger: wait seconds and test again: {str(interval)}")
            time.sleep(interval)
    #
    # If event does not occur during number of interations return None
    #
          return "show trigger did not occur in expected time"

        except Exception as e:
          error_msg(f"ddr_show_trigger Exception: {str(e)}")
          raise

def ddr_wait(seconds, debug_flag=False):
    """
      Wait for the number of seconds in the argument before returning
      
      :param seconds: Number of seconds to delay
      :param debug_flag: True to enable debug output for this call, False no debug output (default)
    """
    
    time.sleep(seconds)

def ddr_cli_command(device, access_type, command, return_response, timestamp, debug_flag=False):
    """
        Runs an exec command in the guestshell on the management device using the
        Python "cli" package installed by default in the guestshell or ssh connection to a device  
            
        :param access_type: EXAMPLE to use the Python cli package in the guestshell or 'ssh' for ssh device access
        :param command: CLI exec command to execute
        :param return_response: True if the command response should be returned
        :param timestamp: Timestamp to include in log output
        :param debug_flag: True to enable debug output for this call, False no debug output (default)
        
        Usage::

          ddr_cli_command(device, "ssh", "show interfaces", True, timestamp, debug_flag=False)
        :raises none:

    """
    try:
      cli_command = command
      if "append" in command:
          cli_command = command + "_" + str(timestamp)
            
    #
    # If access-type is cli use the Python CLI package to run command
    #
      if str(access_type) == 'cli':
          if return_response:
              response = cli.cli(cli_command)
              debug_msg(debug_flag, f"ddr_cli_command: {str(cli_command)} response: {str(response)}")
          else:
              response = cli.clip(cli_command)
              debug_msg(debug_flag, f"ddr_cli_command: {str(cli_command)} response: {str(response)}")
      else:
    #
    # Use SSH to run the show command
    #
        try:
          options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'
          ssh_cmd = 'ssh %s@%s %s "%s"' % (device[2], device[0], options, cli_command)
          debug_msg(debug_flag, f"ddr_cli_command: ssh_cmd: {str(ssh_cmd)}")

          child = pexpect.spawn(ssh_cmd, timeout= 20, encoding='utf-8')
          child.delaybeforesend = None
          child.logfile = None
          child.expect(['\r\nPassword: ', '\r\npassword: ', 'Password: ', 'password: '])
          child.sendline(device[3])
          child.expect(pexpect.EOF)
          response = child.before
          debug_msg(debug_flag, f"ddr_cli_command: response: {str(response)}")

        except Exception as e:
          child.close()
          print("%%%% DDR Error ddr_cli_command SSH or timeout Error: " + str(ssh_cmd) + "\n")
          child.close()
      if return_response:
        return response
      else:
        return None
    except Exception as e:
      error_msg(f"ddr_cli_command Exception: {str(e)} : {str(cli_command)}")
      raise

def ddr_cli_configure(device, access_type, command, return_response, timestamp, debug_flag=False):
    """
        Runs configuration commands in the guestshell on the management device using the
        Python "cli" package installed by default in the guestshell or ssh connection to a device  
            
        :param access_type: EXAMPLE to use the Python cli package in the guestshell or 'ssh' for ssh device access
        :param command: string or list of configurations to apply
        :param return_response: True if the command response should be returned
        :param timestamp: Timestamp to include in log output
        :param debug_flag: True to enable debug output for this call, False no debug output (default)
        
        Usage::

          ddr_cli_configure(device, "ssh", "show interfaces", True, timestamp, debug_flag=False)
        :raises none:

    """
    try:
      cli_command = command
      if "append" in command:
          cli_command = command + "_" + str(timestamp)
            
    #
    # If access-type is cli use the Python CLI package to apply configuration
    #
      if str(access_type) == 'cli':
          if return_response:
              response = cli.configure(cli_command)
              debug_msg(debug_flag, f"ddr_cli_configure: {str(cli_command)} response: {str(response)}")
          else:
              response = cli.clip(cli_command)
              debug_msg(debug_flag, f"ddr_cli_configure: {str(cli_command)} response: {str(response)}")
      else:
    #
    # Use SSH to run the configuration command
    #
        try:
          options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'
          ssh_cmd = 'ssh %s@%s %s "%s"' % (device[2], device[0], options, cli_command)
          debug_msg(debug_flag, f"ddr_cli_configure: ssh_cmd: {str(ssh_cmd)}")

          child = pexpect.spawn(ssh_cmd, timeout= 20, encoding='utf-8')
          child.delaybeforesend = None
          child.logfile = None
          child.expect(['\r\nPassword: ', '\r\npassword: ', 'Password: ', 'password: '])
          child.sendline(device[3])
          child.expect(pexpect.EOF)
          response = child.before
          debug_msg(debug_flag, f"ddr_cli_configure: response: {str(response)}")

        except Exception as e:
          child.close()
          print("%%%% DDR Error ddr_cli_configure SSH or timeout Error: " + str(ssh_cmd) + "\n")
          child.close()
      if return_response:
        return response
      else:
        return None
    except Exception as e:
      error_msg(f"ddr_cli_configure Exception: {str(e)}")
      raise

def ddr_decode_btrace_log(device, access_type, show_template, pcount, par1, par2, par3, match_string, log_path, debug_flag=False):

    """
         Decode a btrace log file on the device, find lines containing a match_string, return the matched lines and save the decoded log
         
        :param device: Device identity and credentials
        :param access_type: "cli" or "ssh" for type of exec CLI access
        :param show_template: string with 0 to 3 parameters that is used to read the btrace file
        :param pcount: Number of parameters to substitute in the xpath 0 to 3
        :param parx: Values for parmeters 1, 2 and 3
        :param match_string: String contained in btrace log file lines used to select the lines to include in the results
        :param log_path: path to where the decoded btrace log should be saved
        :param debug_flag: True to enable debug output for this call, False no debug output (default)
                
        Usage::

          ddr_decode_btrace_log(device, "cli", "show platform software trace message {0} {1}", 2, "dmiauthd", "switch active R0", "none", "%DMI-5-AUTH_PASSED:", "/bootflash/guest-share/Btrace_dmiauthd_log", debug_flag=False)

       :raises none:

    """
    timestamp =  datetime.now().strftime("%m-%d-%Y_%H:%M:%S.%f")
          
    #######################################################################
    #
    # Generate the show command with parameters
    #
    #######################################################################
    cmdline = str(show_template)
    #
    # substitute parameters in command string if included in call from rule
    #
    if int(pcount) == 0:
      command = str(cmdline)
    else:
      if int(pcount) == 1:
        command = str(show_template).format(str(par1))
      elif int(pcount) == 2:
        command = str(show_template).format(str(par1), str(par2))
      elif int(pcount) == 3:
        command = str(show_template).format(str(par1), str(par2), str(par3))
      
    try:
    #
    # If access-type is cli use the Python CLI package to run command
    #
      if str(access_type) == 'cli':
        try:
          response = cli.cli(command)
        except:
          error_msg("run_decode_btrace_log cli access method not available")
          raise
                
      else:
      #      
      # Use SSH to run the show command
      #
        
        try:
          options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'
          ssh_cmd = 'ssh %s@%s %s "%s"' % (device[2], device[0], options, command)
          child = pexpect.spawn(ssh_cmd, timeout= 60, encoding='utf-8')
          child.delaybeforesend = None
          child.expect(['\r\nPassword: ', '\r\npassword: ', 'Password: ', 'password: '])
          child.sendline(device[3])
          child.expect(pexpect.EOF)
          response = child.before

        except Exception as e:
          child.close()
          error_msg("run_decode_btrace_log SSH or timeout: {str(ssh_cmd)}")
          raise
        child.close()

    except Exception as e:
      error_msg("run_decode_btrace_log: Exception sending show command: {str(e)}")
      raise
    #
    # Search for content in log file
    #
    matched_lines = []
    try:
      match_pattern = ".*" + str(match_string) + ".*"
      p1 = re.compile(match_pattern)
      for line in response.splitlines():
        line = line.strip()
        m = p1.match(line)
        if m:
          matched_lines.append(line)
    except Exception as e:
      error_msg("run_decode_btrace_log regex: {str(match_string)} {str(e)}")
      raise

    #
    # Save decoded btrace log if required
    #
    if log_path != "none":
      try:
        out_path = str(log_path) + "_" + str(timestamp)
        with open(out_path, 'w') as wfd:
          wfd.write(response)
          wfd.close()
      except Exception as e:
        error_msg("run_decode_btrace_log: Exception saving btrace log: {str(e)}")
        raise
    return matched_lines
    
def ddr_control_file(control_file, delay):
    """
        ddr_control_file("filename", delay)
        
        This function is used to enable an external application to control starting the execution of
        a DDR Python usecase.
        This function looks in the /bootflash/guest-share/ddr with the name 'control_file'
        If the file is found, the function returns and the DDR Python script continues.
        If the file is not found, the function waits for 'delay' seconds and checks again to see
        if the control_file is present.
        When the control_file is found, the DDR Python script deletes the control_file from bootflash/guest-share/ddr
        If the external application wants to start the usecase again, a new control_file is written to the device guestshare
                               
        :param control_file: string with name of file in the guest-share/ddr directory
        :param delay: delay in seconds to wait before trying to find the action-facts file again
        
    Usage::

      ddr_control_file("ddr-control",10)

        :raises none:

    """

    while True: # Look for control file until the file is found or usecase terminates
        if control_file:
                     
            try:
                with open(control_file) as file:
                    os.remove(control_file)
                return

            except Exception as e:
                if delay == 0:
                    return
                else:
                    time.sleep(delay)
        else:
            return
