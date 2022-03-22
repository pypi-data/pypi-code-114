from __future__ import unicode_literals

import logging
import os
import sys

from . import laucher  # noqa
from . import api, config_section, mapper  # noqa
from .odoo_config_maker import OdooConfig, OdooEnvConverter  # noqa

_logger = logging.getLogger(__name__)
# _logger.setLevel(logging.DEBUG)


def main():
    env_vars = dict(os.environ)
    _logger.info("create config")
    odoo_path = os.getenv("ODOO_PATH")
    server_path = os.getenv("NDP_SERVER_PATH")
    odoo_rc = os.getenv("ODOO_RC")
    launcher = laucher.Launcher(sys.argv[1:], odoo_path=odoo_path, odoo_rc=odoo_rc, server_path=server_path)
    launcher.init_addons(env_vars)
    return_code = launcher.launch_config_file(env_vars).wait()
    if return_code:
        sys.exit(return_code)
    if os.getenv("UPDATE") or os.getenv("INSTALL"):
        _logger.info("Update or init detected")
        maintenance_server_proc = launcher.launch_maintenance_server()
        return_code = launcher.launch_update(env_vars).wait()
        maintenance_server_proc.kill()
        if return_code:
            sys.exit(return_code)
    _logger.info("#############################################")
    _logger.info("Run Odoo")
    sys.exit(launcher.launch({}).wait())


if __name__ == "__main__":
    main()
