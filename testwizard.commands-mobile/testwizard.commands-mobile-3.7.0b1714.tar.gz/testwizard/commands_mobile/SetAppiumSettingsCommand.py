import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.SimpleResult import SimpleResult


class SetAppiumSettingsCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Mobile.SetAppiumSettings")

    def execute(self, settings):
        requestObj = [json.dumps(settings)]

        result = self.executeCommand(requestObj, "Could not execute command")

        return SimpleResult(result, "SetAppiumSettings was successful", "SetAppiumSettings failed")
