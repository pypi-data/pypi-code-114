import sys
import json

from testwizard.commands_core import CommandBase
from .GetAppiumSettingsResult import GetAppiumSettingsResult


class GetAppiumSettingsCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Mobile.GetAppiumSettings")

    def execute(self):
        requestObj = []

        result = self.executeCommand(requestObj, "Could not execute command")

        return GetAppiumSettingsResult(result, "GetAppiumSettings was successful", "GetAppiumSettings failed")
