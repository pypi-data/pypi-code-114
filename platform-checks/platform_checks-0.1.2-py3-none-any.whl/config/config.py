#   -------------------------------------------------------------
#   Platform checks
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import os
import yaml


#   -------------------------------------------------------------
#   Parse configuration
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def get_configuration_path():
    candidates = [
        "/usr/local/etc/monitoring/checks.yml",
        "/etc/monitoring/checks.yml",
        ".checks.yml",
    ]

    for candidate in candidates:
        if os.path.exists(candidate):
            return candidate

    raise FileNotFoundError("Can't find monitoring configuration file")


def parse_config():
    with open(get_configuration_path()) as fd:
        return yaml.safe_load(fd)


#   -------------------------------------------------------------
#   Extract relevant data for checks
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def get_all_checks(prefix=""):
    return {
        key: (check_type, value)
        for check_type, checks in parse_config()["checks"].items()
        if check_type.startswith(prefix)
        for key, value in checks.items()
    }


def get_check_value(prefix="", key=None):
    for check_type, checks in parse_config()["checks"].items():
        if not check_type.startswith(prefix):
            continue

        for current_key, value in checks.items():
            if current_key == key:
                return check_type, value

    raise ValueError("Service not defined in configuration")
