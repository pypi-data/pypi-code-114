# Repositories uses in this example:
#   https://github.com/neopkr/RotMGRPC - by neokeee & etherlesss
#   https://github.com/qwertyquerty/pypresence - by qwertyquerty and +


# TEST LAYOUT

# Connecting rpc from pypresence
# https://github.com/qwertyquerty/pypresence


from pypresence import Presence
from RPCLayout import RPCLayout
import time

clientID = "955142324378296371" # replace with your client_id
rpc = Presence(clientID)
rpc.connect() # connecting rpc

# I will make a simple Realm of the Mad God Exalt RPC with an API - https://github.com/neopkr/RotMGRPC (LICENSE: MIT)
# URL API-KEY
url = "https://nightfirec.at/realmeye-api/?player=Neopkr&filter=player+characters+class+fame+rank"
layout = RPCLayout() # init class

''' Check if the game is open, i will comment this because you need the game and bla bla bla.
game_win32 = layout._detectGame('RotMG Exalt.exe') # Do exact for another OS
game_macOS = layout._detectGame('RotMGExalt') # _detectGame returns a boolean, true if game is open, false is game is closed
if game_win32 is True or game_macOS is True:
    print("RPC Connected!")
    pass
else:
    print("Game is not open!") # Here you have a choice to wait at user open the game. Using _waitingForOpen function.
    # for 2 OS, use platform
    if platform.system() == "Windows":
        _waitingForGame(game_win32)
    else:
        _waitingForGame(game_macOS)
'''
while True:
    data = layout.request_api(url) # init request, with this you have all ready to start.
    # Extracting data.json from api, thanks etherless.
    player_name = data['player']
    starQty = data['rank']
    charactersList = data['characters']
    playingAs = charactersList[0]
    
    # update made by etherless in https://github.com/neopkr/RotMGRPC
    rpc.update(
        state = f"Playing as: {playingAs['class']}",
        details = f"IGN: {player_name}",
        start = str(layout.timestamp()), # Use timestamp for start in 00:00 seconds
        large_image = "image_large", # Image imported in discord developer app
        large_text = 'Large Image Text!', # When you put the cursor over the large_image appears this text.
        small_image = 'star', # small_image, icon.
        small_text = str(starQty) # and the same at large_text. 
    ) # init update event from pypresence.Presence.update()
    
    # And that is, you're ready for use it.
    
    time.sleep(60) # while loop in 60 seconds. (ideal 5 seconds)