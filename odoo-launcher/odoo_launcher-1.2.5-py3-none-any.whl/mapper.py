from typing import Dict, Union

from .api import EnvMapper


class OdooCompatibilityMapper(EnvMapper):
    """
    <WORKER_HTTP> is put in <WORKERS> if <WORKERS> not exist
    and
    <WORKERS> is put in <WORKER_HTTP> if <WORKER_HTTP> not exist
    """

    def map_vars(self, env_vars):
        # type: (Dict[str, str]) -> Dict[str, str]
        return {
            "WORKER_HTTP": env_vars.get("WORKER_HTTP", env_vars.get("WORKERS")),
            "WORKER_CRON": env_vars.get("WORKER_CRON", env_vars.get("WORKERS")),
            "WORKER_JOB": env_vars.get("WORKER_JOB", env_vars.get("WORKERS")),
            "HTTP_INTERFACE": env_vars.get("HTTP_INTERFACE", env_vars.get("XMLRPC_INTERFACE")),
            "HTTP_PORT": env_vars.get("HTTP_PORT", env_vars.get("XMLRPC_PORT")),
            "HTTP_ENABLE": env_vars.get("HTTP_ENABLE", env_vars.get("XMLRPC_ENABLE")),
            "LONGPOLLING_PORT": env_vars.get("LONGPOLLING_PORT"),
            "SERVER_WIDE_MODULES": env_vars.get("SERVER_WIDE_MODULES", env_vars.get("LOAD")),
        }


class OdooQueueJobMapper(EnvMapper):
    """
    <WORKER_HTTP> is put in <WORKERS> if <WORKERS> not exist
    and
    <WORKERS> is put in <WORKER_HTTP> if <WORKER_HTTP> not exist
    """

    def map_vars(self, env_vars):
        # type: (Dict[str, str]) -> Dict[str, str]
        enable = self.is_true(env_vars.get("ODOO_QUEUE_JOB_ENABLE"))
        return {
            "ODOO_QUEUE_JOB_ENABLE": str(enable),
            "ODOO_QUEUE_JOB_CHANNELS": enable
            and env_vars.get("ODOO_QUEUE_JOB_CHANNELS", env_vars.get("ODOO_CONNECTOR_CHANNELS"))
            or None,
            "ODOO_QUEUE_JOB_SCHEME": enable
            and env_vars.get("ODOO_QUEUE_JOB_SCHEME", env_vars.get("ODOO_CONNECTOR_SCHEME"))
            or None,
            "ODOO_QUEUE_JOB_HOST": enable
            and env_vars.get("ODOO_QUEUE_JOB_HOST", env_vars.get("ODOO_CONNECTOR_HOST"))
            or None,
            "ODOO_QUEUE_JOB_PORT": enable
            and env_vars.get("ODOO_QUEUE_JOB_PORT", env_vars.get("ODOO_CONNECTOR_PORT"))
            or None,
            "ODOO_QUEUE_JOB_HTTP_AUTH_USER": enable
            and env_vars.get("ODOO_QUEUE_JOB_HTTP_AUTH_USER", env_vars.get("ODOO_CONNECTOR_HTTP_AUTH_USER"))
            or None,
            "ODOO_QUEUE_JOB_HTTP_AUTH_PASSWORD": enable
            and env_vars.get("ODOO_QUEUE_JOB_HTTP_AUTH_PASSWORD", env_vars.get("ODOO_CONNECTOR_HTTP_AUTH_PASSWORD"))
            or None,
            "ODOO_QUEUE_JOB_JOBRUNNER_DB_HOST": enable
            and env_vars.get("ODOO_QUEUE_JOB_JOBRUNNER_DB_HOST", env_vars.get("ODOO_CONNECTOR_JOBRUNNER_DB_HOST"))
            or None,
            "ODOO_QUEUE_JOB_JOBRUNNER_DB_PORT": enable
            and env_vars.get("ODOO_QUEUE_JOB_JOBRUNNER_DB_PORT", env_vars.get("ODOO_CONNECTOR_JOBRUNNER_DB_PORT"))
            or None,
        }


class OdooRedisSessionMapper(EnvMapper):
    """
    <WORKER_HTTP> is put in <WORKERS> if <WORKERS> not exist
    and
    <WORKERS> is put in <WORKER_HTTP> if <WORKER_HTTP> not exist
    """

    def map_vars(self, env_vars):
        # type: (Dict[str, str]) -> Dict[str, str]
        enable = self.is_true(env_vars.get("REDIS_SESSION_ENABLE", bool(env_vars.get("REDIS_HOST"))))
        return {
            "REDIS_SESSION_ENABLE": str(enable),
            "REDIS_SESSION_URL": enable and env_vars.get("REDIS_SESSION_URL", env_vars.get("REDIS_URL")) or None,
            "REDIS_SESSION_HOST": enable and env_vars.get("REDIS_SESSION_HOST", env_vars.get("REDIS_HOST")) or None,
            "REDIS_SESSION_PORT": enable and env_vars.get("REDIS_SESSION_PORT", env_vars.get("REDIS_PORT")) or None,
            "REDIS_SESSION_DB_INDEX": enable
            and env_vars.get("REDIS_SESSION_DB_INDEX", env_vars.get("REDIS_DB_INDEX"))
            or None,
            "REDIS_SESSION_PASSWORD": enable
            and env_vars.get("REDIS_SESSION_PASSWORD", env_vars.get("REDIS_PASSWORD"))
            or None,
        }


class CleverCloudCellarCompatibilityMapper(EnvMapper):
    """
    Compatibility mapper to convert Environment varaible provided by Cellar from CleverCloud
    https://www.clever-cloud.com/doc/deploy/addon/cellar/

    IS_TRUE(CELLAR_ADDON_HOST) => S3_FILESTORE_ENABLE
    CELLAR_ADDON_HOST => S3_FILESTORE_HOST
    CELLAR_ADDON_KEY_SECRET => S3_FILESTORE_SECRET_KEY
    CELLAR_ADDON_KEY_ID => S3_FILESTORE_ACCESS_KEY
    CELLAR_ADDON_REGION or "fr-par" => S3_FILESTORE_REGION
    """

    def map_vars(self, env_vars):
        # type: (Dict[str, Union[str, bool, int, None]]) -> Dict[str, Union[str, bool, int, None]]
        enable = self.is_true(env_vars.get("S3_FILESTORE_ENABLE", bool(env_vars.get("CELLAR_ADDON_HOST"))))
        return {
            "S3_FILESTORE_ENABLE": str(enable),
            "S3_FILESTORE_HOST": enable
            and env_vars.get("S3_FILESTORE_HOST", env_vars.get("CELLAR_ADDON_HOST"))
            or None,
            "S3_FILESTORE_SECRET_KEY": enable
            and env_vars.get("S3_FILESTORE_SECRET_KEY", env_vars.get("CELLAR_ADDON_KEY_SECRET"))
            or None,
            "S3_FILESTORE_ACCESS_KEY": enable
            and env_vars.get("S3_FILESTORE_ACCESS_KEY", env_vars.get("CELLAR_ADDON_KEY_ID"))
            or None,
            # Pas de region fournit par S3 CleverCloud
            "S3_FILESTORE_REGION": enable
            and (env_vars.get("S3_FILESTORE_REGION", env_vars.get("CELLAR_ADDON_REGION")) or "fr-par")
            or None,
        }


class CleverCloudPostgresCompatibilityMapper(EnvMapper):
    def map_vars(self, env_vars):
        return {
            "DB_NAME": env_vars.get("DB_NAME", env_vars.get("DATABASE", env_vars.get("POSTGRESQL_ADDON_DB"))),
            "DB_HOST": env_vars.get(
                "DB_HOST", env_vars.get("POSTGRESQL_ADDON_DIRECT_HOST", env_vars.get("POSTGRESQL_ADDON_HOST"))
            ),
            "DB_PORT": (
                env_vars.get(
                    "DB_PORT", env_vars.get("POSTGRESQL_ADDON_DIRECT_PORT", env_vars.get("POSTGRESQL_ADDON_PORT"))
                )
            ),
            "DB_USER": env_vars.get("DB_USER", env_vars.get("POSTGRESQL_ADDON_USER")),
            "DB_PASSWORD": env_vars.get("DB_PASSWORD", env_vars.get("POSTGRESQL_ADDON_PASSWORD")),
        }
