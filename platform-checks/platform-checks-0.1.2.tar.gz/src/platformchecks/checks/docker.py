#   -------------------------------------------------------------
#   Platform checks
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Check if a container is up
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import json
import subprocess


def inspect_container(container):
    p = subprocess.run(
        ["docker", "container", "inspect", container], capture_output=True
    )

    if p.returncode > 0:
        raise ValueError(p.stderr.decode().strip())

    return json.loads(p.stdout)[0]


def describe_state(state):
    return f"{state['Status']} ({state['ExitCode']}) {state['FinishedAt']}"


class DockerContainerCheck:
    def __init__(self):
        self.containers = []

        self.error = ""

    def initialize(self):
        p = subprocess.run(
            "docker container ls | awk '(NR>1) {print $NF}'",
            shell=True,
            capture_output=True,
        )

        if p.stderr:
            self.error = p.stderr.decode().strip()
            return False

        self.containers = p.stdout.decode().strip().split("\n")
        return True

    def perform(self, container):
        return self.has(container), self.build_message(container)

    def has(self, container):
        return container in self.containers

    def build_message(self, container):
        if self.has(container):
            return f"{container} UP"

        message = f"{container} DOWN"

        try:
            # Returns container state lik
            state = inspect_container(container)["State"]
            message += " " + describe_state(state)
        except ValueError as ex:
            # Detect cases when the container doesn't exist
            message += " " + str(ex)
        except subprocess.CalledProcessError:
            pass

        return message
