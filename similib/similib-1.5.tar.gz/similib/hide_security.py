import os
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from similib.conf import SIMILIB_BASE_DIR

with open(os.path.join(SIMILIB_BASE_DIR, "file", "stealth.min.js"), "r") as f:
    stealth_js = f.read()


def hide_security(bro):
    bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": stealth_js
    })


software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)


def get_user_agents():
    return user_agent_rotator.get_user_agents()


def get_random_user_agent():
    return user_agent_rotator.get_random_user_agent()


