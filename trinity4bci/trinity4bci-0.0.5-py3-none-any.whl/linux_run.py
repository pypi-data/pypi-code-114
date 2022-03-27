import os
import time
from subprocess import call
from trinity4bci._boardInfo import getBoardFromInput, getPortFromInput
# from _boardInfo import getBoardFromInput, getPortFromInput


# THIS IS THE LINUX version of RUN

# TODO: Add options menu to select boards to stream from, COM ports, serial ports if need be, etc...


class LR:

    def __init__(self, useDefaultOutput=True):

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
                peter griffin
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

        print("Now opening Communications Client, please hold gdhasigh;...\n")

        # TODO - call needs to work, does not if is a package 
        # argparse is likely not the way to go here...
        
        # Uncomment these lines if you want to try using argparse functionality
        # callString_A = "python3 client.py"+" --board-id "+str(board)
        # if port!='':
        #     callString_A+=" --serial-port "+str(port)
        # call(['gnome-terminal', '-e', str(callString_A)])

        clientCallString = 'python -i -c "from trinity4bci import client; c = client.runClient()" '
        call(['gnome-terminal', '-e', clientCallString])
        # call([])
        
        time.sleep(1)
        
        print("Now opening Signal Filtering and Processing Relay , please hold ...\n")

        time.sleep(2)
        
        # Uncomment if you have the source files and want to try using argparse functionality
        # callString_B = "python3 sfpr.py"+" --master-id "+str(board)
        # # TODO: Add logic to incorporate more metrics
        # # right now defaults to focus
        # doFocus=True
        # callString_B+=" --do-focus "+str(doFocus)
        #####################33
        sfprCallString = 'python -i -c "from trinity4bci import sfpr; sfpr.run()" '
        call(['gnome-terminal', '-e', sfprCallString])

        time.sleep(1)

        if useDefaultOutput:
        # TODO: add functionality to choose different out file
          print("Now opening Concentration output , please hold ...\n")

          time.sleep(1)
          
          defaultFocusCallString = 'python -i -c "from trinity4bci import out; out.run()" '

          call(['gnome-terminal', '-e', defaultFocusCallString])

        exit = input("Press <ENTER> again to exit")

    def chooseBoards(self):
        pass

    def chooseMetric(self):
        pass

if __name__ == "__main__":
  LR()