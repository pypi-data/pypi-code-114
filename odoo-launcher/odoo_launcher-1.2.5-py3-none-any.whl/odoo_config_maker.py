from __future__ import unicode_literals

import logging
import os
import pprint
from collections import OrderedDict
from typing import Dict, List, Optional

from .api import ConfigConvert, Dictable, EnvMapper, OdooConfigABC
from .config_section import (
    AddonsPathConfigSection,
    DatabaseOdooConfigSection,
    HttpOdooConfigSection,
    LimitOdooConfigSection,
    LoggerSection,
    OtherSection,
    ServerWideModuleConfigSection,
    UpdateInstallSection,
    WorkersOdooConfigSection,
)
from .mapper import (
    CleverCloudCellarCompatibilityMapper,
    CleverCloudPostgresCompatibilityMapper,
    OdooCompatibilityMapper,
    OdooQueueJobMapper,
    OdooRedisSessionMapper,
)

_logger_level = getattr(logging, os.environ.get("NDP_SERVER_LOG_LEVEL", "INFO"), logging.INFO)

_logger = logging.getLogger("install_addons")
handler = logging.StreamHandler()
_logger.addHandler(handler)
_logger.setLevel(_logger_level)

PG_MAX_CONN_MODE_AUTO = "AUTO"
PG_MAX_CONN_MODE_DEFAULT = "DEFAULT"


def is_main_instance(env_vars):
    return env_vars.get("INSTANCE_NUMBER", 0) == 0


class OdooConfig(OdooConfigABC, Dictable):
    def __init__(self, env_vars, odoo_rc=None, main_instance=None):
        super(OdooConfig, self).__init__(main_instance is None and is_main_instance(env_vars))
        self._odoo_version = self.to_int(env_vars.get("ODOO_VERSION"))
        self.odoo_rc = odoo_rc
        env_converter = OdooEnvConverter()
        env_vars = env_converter.map_env_vars(env_vars)
        env_converter.assert_env(env_vars)

        self.addons_config = AddonsPathConfigSection(self, env_vars)
        self.workers_config = WorkersOdooConfigSection(self, env_vars)
        self.limit_config = LimitOdooConfigSection(self, env_vars)
        self.db_config = DatabaseOdooConfigSection(self, env_vars)
        self.http_config = HttpOdooConfigSection(self, env_vars)
        self.wide_module = ServerWideModuleConfigSection(self, env_vars)
        self.other_section = OtherSection(self, env_vars)
        self.logger_section = LoggerSection(self, env_vars)
        self.update_install = UpdateInstallSection(self, env_vars)

    @property
    def odoo_version(self):
        return self._odoo_version

    def to_dict(self):
        result = OrderedDict()
        result["--config"] = self.odoo_rc
        result.update(self.update_install.to_dict())
        result.update(self.addons_config.to_dict())
        result.update(self.workers_config.to_dict())
        result.update(self.limit_config.to_dict())
        result.update(self.http_config.to_dict())
        result.update(self.db_config.to_dict())
        result.update(self.wide_module.to_dict())
        result.update(self.other_section.to_dict())
        result.update(self.logger_section.to_dict())
        return result

    def __repr__(self):
        return pprint.pformat(self.to_dict())

    def to_odoo_args(self):
        # type: () -> List[str]
        result = []
        dict_values = Dictable.clean_none_env_vars(self.to_dict())
        dict_values = Dictable.clean_config_dict(dict_values)
        for key, value in dict_values.items():
            if not value:
                continue

            if value == str(True):
                result.append(key)
            else:
                result.append("%s=%s" % (key, value))
        return result


class OdooEnvConverter(ConfigConvert):
    def __init__(self, mappers=None):
        # type: (Optional[List[EnvMapper]]) -> OdooEnvConverter
        self.mappers = list(mappers or [])
        self.mappers.append(CleverCloudCellarCompatibilityMapper())
        self.mappers.append(CleverCloudPostgresCompatibilityMapper())
        self.mappers.append(OdooCompatibilityMapper())
        self.mappers.append(OdooRedisSessionMapper())
        self.mappers.append(OdooQueueJobMapper())

    def map_env_vars(self, env_vars):
        # type: (Dict[str, str]) -> Dict[str, str]
        result = dict(env_vars)
        for mapper in self.mappers:
            result.update(mapper.map_vars(env_vars))
        for key in dict(result).keys():
            if not result[key]:
                result.pop(key, None)
        return result

    def assert_env(self, env_vars):
        if not self.is_true(env_vars.get("REMOTE_DB", str(True))):
            return
        if (
            not env_vars.get("DB_NAME")
            or not env_vars.get("DB_PORT")
            or not env_vars.get("DB_HOST")
            or not env_vars.get("DB_USER")
            or not env_vars.get("DB_PASSWORD")
        ):
            raise TypeError(
                "Can't start Odoo without a db name "
                "Please add the one of the following environment variable"
                "- DATABASE"
                "- DB_NAME"
                "- POSTGRESQL_ADDON_DB"
            )

    def create_config_dict(self, env_vars):
        env_vars = self.map_env_vars(env_vars)
        config = OdooConfig(env_vars, is_main_instance(env_vars))
        new_options = config.to_dict()
        new_options = Dictable.clean_config_dict(new_options)
        return new_options
