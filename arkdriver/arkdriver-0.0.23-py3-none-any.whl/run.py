from time import sleep
import requests
from arkdriver import ArkDriver


def run(key=None):
    url = "https://ark-administration.herokuapp.com/"
    driver = ArkDriver(url, key)
    while True:
        try:
            commands = requests.get(f"{url}/new_commands").json()
            if len(commands):
                for command in commands:
                    print('\033[34m' + f"{command} " + '\033[0m')
                driver.write_console(*commands)
            sleep(30)
        except Exception as e:
            print('\033[31m' + f"[FAILED]: {e}" + '\033[0m')