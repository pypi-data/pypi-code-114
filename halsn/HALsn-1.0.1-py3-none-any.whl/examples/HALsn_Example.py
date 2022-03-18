#! /usr/bin/env python3

'''

HEY EVERYONE! THIS IS A QUICK DEMO TO SHOWCASE THE CAPABILITIES WE HAVE 
WITH BDP AND HAL ABSTRACTION. THIS CODE WILL BE SHARED WITH THE GROUP
AFTER THIS MEETING. IF YOU WANT TO PLAY AROUND WITH THE TOOLS I'LL HAVE
A CFP SET UP AT MY DESK AND YOU CAN COME GET FAMILIAR WITH CONTROLLING IT
USING THIS API.

'''

from HALsn.SKU import CFP                       # import the CFP SKU into the code
from HALsn.scheduler import Routine             # import the Routine utility to schedule tasks 
from HALsn.dataSupervisor import dataSupervisor # import Data Supervisor Class for collecting/managing data

cfp = CFP()                     # declare the SKU
cfp.open_port()                 # open the serial port, default is closed

rout = Routine()                # declare a routine

sup = dataSupervisor(map=cfp.queries, headers=False, s3_enable=False) # declare the data supervisor

def bfnc(*args):
    '''
    This is the BREAK function for the routine.
    a routine must have a BREAK function but it
    does not require STANDARD functions. As long
    as your BREAK function returns True it can do
    whatever other tasks are required as well.
    '''

    time = rout.ext_timer()     # print the Routines current time
    data = cfp.master_query()   # collect all master_query() enabled queries

    print(data)                 # print the data
    
    sup.parser.lst.append(data)

    if data[0] == '$LT0\r':     # if the first index (current brew) is equivalent
                                # to '$LT0\r', the command for idle, then break
        return True             # the loop by returning True

rout.add_break_functions(bfnc, None) # Add break function to the routine

cfp.command('6_oz_classic_K')        # Start the brew with an external command
cfp.command('debug_on')              # Enable debug mode to collect all avilable data

try:                        
    rout.run()                       # Start the routine. Runs unitl break condition is met
except KeyboardInterrupt:               
    cfp.command('debug_off')         # If ctrl+c is pressed, the loop will break and the
    cfp.command('cancel_brew')       # machine will turn off

sup.interpreted_parse()              # Parse the dataframe for exporting
sup.add_filename('/home/pi/Documents/Test_Folder/', 'test.csv')
sup.export_csv()                     # export the dataframe as a csv