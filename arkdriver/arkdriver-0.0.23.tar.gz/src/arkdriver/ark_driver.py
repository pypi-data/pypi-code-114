"""
This program controls the admin commands in the game.
Also any menu navigations.


Note: SpecimenImplant has a player's ID called "Sample #: 34225234"
Can have user input their sample #


"""

from arkdriver import ApplicationDriver
from time import sleep


class ArkDriver:
    def __init__(self, url=None, key=None):
        self.app = ApplicationDriver(url or "http://localhost:3000", key)
        self.app.start()
        self.pane = self.app.pane

    def copy_coords(self):
        """ Copies your current coordinates and rotation to clipboard in the form x,y,z Yaw pitch """
        assert self.app.resolved, "You must authenticate the driver"
        self.write_console('ccc')

    def write_console(self, *commands):
        assert self.app.resolved, "You must authenticate the driver"
        self.app.set_focus()
        sleep(1)
        self.app.save_to_clipboard_text('|'.join(['{}'.format(command) for command in commands]) + '|')
        self.app.send_key_tab()
        self.app.send_key_paste()
        self.app.send_key_enter()

    def write_console_args(self, args: list, *command_formats):
        """ player_ids is a list of player ids
            command_formats are commands in format form: "cheat GiveItemTO {} Pickaxe 1 1"
                where there is a '{}' in the string
         """
        assert self.app.resolved, "You must authenticate the driver"
        commands = []
        for str_format in command_formats:
            commands.append(str_format.format(*args))
        self.write_console(*commands)

