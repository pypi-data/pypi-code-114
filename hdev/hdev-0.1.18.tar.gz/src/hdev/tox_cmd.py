"""Wrappers for access to tox functionality."""

import os
import subprocess


def run_tox(tox_env, cmd, check=True, env_vars=None):
    """Run a `cmd` inside tox environment `env`.

    :param tox_env: Tox environment to run the command in
    :param cmd: Command to run
    :param check: Fail if the exit code is an error
    :param env_vars: Dict of items to add to the environment when running the
        task
    :return: Info of the subprocess. Same as subprocess.run
    :rtype: subprocess.CompletedProcess
    """
    env = os.environ.copy()

    if env_vars:
        env.update(env_vars)

    command = ["tox", "-e", tox_env, "--run-command", cmd]
    return subprocess.run(command, check=check, env=env)
