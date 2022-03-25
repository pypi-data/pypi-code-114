import os
import time
from subprocess import call
from _boardInfo import getBoardFromInput, getPortFromInput

# THIS IS THE LINUX version of RUN

# TODO: Add options menu to select boards to stream from, COM ports, serial ports if need be, etc...


class LR:

    def __init__(self):

        ascii_logo = '''                                             
                                °°                             
                              °@@@@@@°                          
                            *@@@@@@@@@@°                        
                          @@@@@@@@@@@@@@                       
                        °@@@@@@@oo@@@@@@@°                     
                        °@@@@@@@    @@@@@@@°                    
                        @@@@@@#      #@@@@@@                    
                      #@@@@@@        @@@@@@#                   
                      @@@@@@O@@@@@@@@@@@@@@@                   
                      .@@@@@@O@@@@@@@@@@@@@@@o                  
                  *@@O@@@@@@O@@@@@@@@@@@@@@@@@@*               
                o@@@@@O@@@@@@       .@@@@@@@@@@@@o             
              .@@@@@@@*@@@@@@@      @@@@@@@@@@@@@@@.           
              *@@@@@@@°  @@@@@@@.  .@@@@@@@  °@@@@@@@*          
            *@@@@@@#    .@@@@@@@*#@@@@@@@     #@@@@@@*         
            @@@@@@o       O@@@@@@@@@@@@O       o@@@@@@         
            #@@@@@@O**°°°*o#@@@@@@@@@@@@Oo*°°°**O@@@@@@O        
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
            °#@@@@@@@@@@@@@@@@@@#*.o@@@@@@@@@@@@@@@@@@#°        
                °*OO#####O*°          °*O#####OO*°             
                
                [Mind] --> [Computer] --> [Machine]
    '''

        print("Welcome to Trinity v0.12 [for linux]!")
        print(ascii_logo)
        start = input("Press <ENTER> to start!\n")

        board = ''
        metric = ''

        # get current working directory

        current_directory = os.getcwd()
        os.system(f"cd {current_directory}")
        print(f"Current directory: {current_directory}\n")

        # Get board information

        board = getBoardFromInput()
        
        time.sleep(1)
        
        port = getPortFromInput(board)
              
        time.sleep(1)

        print("Now opening Communications Client, please hold ...\n")

        callString_A = "python3 client.py"+" --board-id "+str(board)
        if port!='':
            callString_A+=" --serial-port "+str(port)
        call(['gnome-terminal', '-e', str(callString_A)])

        time.sleep(1)
        
        print("Now opening Signal Filtering and Processing Relay , please hold ...\n")

        time.sleep(2)
        callString_B = "python3 sfpr.py"+" --master-id "+str(board)
        # TODO: Add logic to incorporate more metrics
        # right now defaults to focus
        doFocus=True
        callString_B+=" --do-focus "+str(doFocus)
        call(['gnome-terminal', '-e', callString_B])

        time.sleep(1)

        print("Now opening Concentration output , please hold ...\n")

        time.sleep(1)

        call(['gnome-terminal', '-e', "python3 out.py"])

        exit = input("Press <ENTER> again to exit")

    def chooseBoards(self):
        pass

    def chooseMetric(self):
        pass

if __name__ == "__main__":
  LR()
  