import enum
from collections import OrderedDict
from typing import Dict, Union

from addons_installer import addons_installer

from .api import OdooConfigABC, OdooConfigSection


class WorkersOdooConfigSection(OdooConfigSection):
    class UseCase(enum.Enum):
        CLASSIC = "CLASSIC"
        ONLY_HTTP = "ONLY_HTTP"
        ONLY_JOB_RUNNER = "ONLY_JOB_RUNNER"
        ONLY_JOB_WORKER = "ONLY_JOB_WORKER"
        ONLY_CRON = "ONLY_CRON"

    def __init__(self, odoo_config_maker, env_vars):
        # type: (OdooConfigABC, Dict[str, Union[str, bool, int, None]]) -> None
        super(WorkersOdooConfigSection, self).__init__(odoo_config_maker, env_vars)
        self.http = self.to_int(env_vars.get("WORKER_HTTP", 1))
        self.cron = self.to_int(env_vars.get("WORKER_CRON", 2))
        self.job = self.to_int(env_vars.get("WORKER_JOB", 0))
        self.split_use_case = self.is_true(env_vars.get("SPLIT_ODOO_USE_CASE", str(False)))

        use_case_env = env_vars.get("ODOO_USE_CASE")
        if not use_case_env or use_case_env not in (list(WorkersOdooConfigSection.UseCase)):
            self.odoo_use_case = WorkersOdooConfigSection.UseCase.CLASSIC
        else:
            self.odoo_use_case = WorkersOdooConfigSection.UseCase[use_case_env]

        if not odoo_config_maker.main_instance and self.odoo_use_case != WorkersOdooConfigSection.UseCase.ONLY_CRON:
            self.cron = 0

    @property
    def total(self):
        return self.http + self.cron + self.job

    @property
    def worker(self):
        if self.odoo_use_case == WorkersOdooConfigSection.UseCase.ONLY_JOB_WORKER:
            return self.job
        if self.odoo_use_case == WorkersOdooConfigSection.UseCase.ONLY_JOB_RUNNER:
            return 0
        if self.odoo_use_case == WorkersOdooConfigSection.UseCase.ONLY_HTTP:
            return self.http
        if self.odoo_use_case == WorkersOdooConfigSection.UseCase.ONLY_CRON:
            return 0
        return self.http + self.job

    def to_dict(self):
        if not self.enable:
            return {}
        return {
            "--workers": self.worker,
            "--max-cron-threads": self.cron,
        }


class LimitOdooConfigSection(OdooConfigSection):
    def __init__(self, odoo_config_maker, env_vars):
        super(LimitOdooConfigSection, self).__init__(odoo_config_maker, env_vars)
        self.limit_request = int(env_vars.get("LIMIT_REQUEST", 0)) or None
        self.limit_time_cpu = int(env_vars.get("LIMIT_TIME_CPU", 0)) or None
        self.limit_time_real = int(env_vars.get("LIMIT_TIME_REAL", 0)) or None
        self.osv_memory_count_limit = int(env_vars.get("OSV_MEMORY_COUNT_LIMIT", 0)) or None
        self.osv_memory_age_limit = int(env_vars.get("OSV_MEMORY_AGE_LIMIT", 0)) or None
        self.limit_memory_hard = int(env_vars.get("LIMIT_MEMORY_HARD", 0)) or None
        self.limit_memory_soft = int(env_vars.get("LIMIT_MEMORY_SOFT", 0)) or None

        if not self.limit_memory_hard or not self.limit_memory_soft:
            global_limit_memory_hard = int(env_vars.get("GLOBAL_LIMIT_MEMORY_HARD", 0))
            global_limit_memory_soft = int(env_vars.get("GLOBAL_LIMIT_MEMORY_SOFT", 0))
            total = WorkersOdooConfigSection(odoo_config_maker, env_vars).total or 1
            if not self.limit_memory_soft and global_limit_memory_soft:
                self.limit_memory_soft = global_limit_memory_soft // total
            if not self.limit_memory_hard and global_limit_memory_hard:
                self.limit_memory_hard = global_limit_memory_hard // total

    def to_dict(self):
        return {
            "--limit-request": self.limit_request,
            "--limit-time-cpu": self.limit_time_cpu,
            "--limit-time-real": self.limit_time_real,
            "--limit-memory-hard": self.limit_memory_hard,
            "--limit-memory-soft": self.limit_memory_soft,
            "--osv-memory-count-limit": self.osv_memory_count_limit,
            "--osv-memory-age-limit": self.osv_memory_age_limit,
        }


class DatabaseOdooConfigSection(OdooConfigSection):
    class MaxConnMode(enum.Enum):
        AUTO = "AUTO"
        FIXED = "FIXED"

    def __init__(self, odoo_config_maker, env_vars):
        super(DatabaseOdooConfigSection, self).__init__(odoo_config_maker, env_vars)
        self.name = env_vars.get("DB_NAME")
        self.host = env_vars.get("DB_HOST")
        self.port = self.to_int(env_vars.get("DB_PORT")) or None
        self.user = env_vars.get("DB_USER")
        self.password = env_vars.get("DB_PASSWORD")
        self.max_conn = self.to_int(env_vars.get("DB_MAX_CONN"))
        self.filter = env_vars.get("DB_FILTER")
        self.log_enable = env_vars.get("LOG_DB")
        self.log_level = env_vars.get("LOG_DB_LEVEL")
        self.show = self.is_true(env_vars.get("LIST_DB"))
        mode_env = env_vars.get("DB_MAX_CONN_MODE")
        if not mode_env or mode_env not in (
            DatabaseOdooConfigSection.MaxConnMode.FIXED.value,
            DatabaseOdooConfigSection.MaxConnMode.AUTO.value,
        ):
            mode = DatabaseOdooConfigSection.MaxConnMode.AUTO
        else:
            mode = DatabaseOdooConfigSection.MaxConnMode[mode_env]

        nb_workers = WorkersOdooConfigSection(odoo_config_maker, env_vars).total or 1
        min_conn = nb_workers + int(nb_workers // 2)
        if mode == DatabaseOdooConfigSection.MaxConnMode.FIXED and not self.max_conn:
            # Switch to auto if no max_conn in env_vars but in mode FIXED
            mode = DatabaseOdooConfigSection.MaxConnMode.AUTO
        if mode == DatabaseOdooConfigSection.MaxConnMode.AUTO and not self.max_conn:
            self.max_conn = min_conn
            # We add some security because sometime worker open 2 or more connecions (Ex :bus.bus)
            self.max_conn = max(self.max_conn, min_conn, 2)

        if self.filter and not self.show:
            self.show = True
        if self.name and not self.show:
            self.filter = self.name
        if self.name and self.show and not self.filter:
            self.filter = self.name + ".*"

    def to_dict(self):
        if not self.enable:
            return {}
        res = OrderedDict()
        res["--db_host"] = self.host
        res["--db_port"] = self.port
        res["--db_user"] = self.user
        res["--db_password"] = self.password
        res["--database"] = self.name
        res["--no-database-list"] = not self.show
        res["--db_maxconn"] = self.max_conn
        res["--db-filter"] = self.filter
        return res


class HttpOdooConfigSection(OdooConfigSection):
    def __init__(self, odoo_config_maker, env_vars):
        super(HttpOdooConfigSection, self).__init__(odoo_config_maker, env_vars)
        self.enable = self.is_true(env_vars.get("HTTP_ENABLE", "True"))
        self.interface = None
        self.port = None
        self.longpolling_port = None

        if self.enable:
            self.interface = env_vars.get("HTTP_INTERFACE") or "0.0.0.0"
            self.port = self.to_int(env_vars.get("HTTP_PORT")) or 8080
            self.longpolling_port = self.to_int(env_vars.get("LONGPOLLING_PORT")) or 4040

    def to_dict(self):
        key_http = "http" if self.config_maker.odoo_version > 10 else "xmlrpc"
        if not self.enable:
            return {
                "--no-%s" % key_http: not self.enable,
            }
        res = OrderedDict()
        res["--%s-interface" % key_http] = self.interface
        res["--%s-port" % key_http] = self.port
        res["--longpolling-port"] = self.longpolling_port
        return res


class ServerWideModuleConfigSection(OdooConfigSection):
    def __init__(self, odoo_config_maker, env_vars):
        super(ServerWideModuleConfigSection, self).__init__(odoo_config_maker, env_vars)
        str_server_wide_modules = env_vars.get("SERVER_WIDE_MODULES")
        self.server_wide_modules = str_server_wide_modules and str_server_wide_modules.split(",") or ["base", "web"]
        self.queue_job_module_name = None
        if env_vars.get("QUEUE_JOB_ENABLE"):
            self.queue_job_module_name = "queue_job"
            if odoo_config_maker.odoo_version < 10:
                self.queue_job_module_name = "connector"
            self.server_wide_modules.append(self.queue_job_module_name)

        print(
            "enable odoo_filestore_s3 ?",
            self.is_true(env_vars.get("S3_FILESTORE_ENABLE")),
            env_vars.get("S3_FILESTORE_ENABLE"),
        )
        print(
            "enable odoo_session_redis ? ",
            self.is_true(env_vars.get("REDIS_SESSION_ENABLE")),
            env_vars.get("REDIS_SESSION_ENABLE"),
        )
        if self.is_true(env_vars.get("S3_FILESTORE_ENABLE")):
            self.server_wide_modules.append("odoo_filestore_s3")
        if self.is_true(env_vars.get("REDIS_SESSION_ENABLE")):
            self.server_wide_modules.append("odoo_session_redis")

    def remove_queue_job(self):
        if self.queue_job_module_name:
            self.server_wide_modules.remove(self.queue_job_module_name)

    def to_dict(self):
        return {
            "--load": self.server_wide_modules,
        }


class OtherSection(OdooConfigSection):
    def __init__(self, odoo_config_maker, env_vars):
        super(OtherSection, self).__init__(odoo_config_maker, env_vars)
        self.unaccent = self.is_true(env_vars.get("UNACCENT", True))
        self.test_enable = self.is_true(env_vars.get("TEST_ENABLE"))
        self.without_demo = self.is_true(env_vars.get("WITHOUT_DEMO", "all"))

    def to_dict(self):
        if not self.enable:
            return {"--unaccent": self.unaccent}
        res = OrderedDict()
        res["--unaccent"] = self.unaccent
        res["--test-enable"] = self.test_enable
        res["--without-demo"] = self.without_demo
        return res


class LoggerSection(OdooConfigSection):
    def __init__(self, odoo_config_maker, env_vars):
        super(LoggerSection, self).__init__(odoo_config_maker, env_vars)
        self.logfile = env_vars.get("LOGFILE")
        self.log_handler = env_vars.get("LOG_HANDLER")
        self.log_request = self.is_true(env_vars.get("LOG_REQUEST"))
        self.log_response = self.is_true(env_vars.get("LOG_RESPONSE"))
        self.log_web = self.is_true(env_vars.get("LOG_WEB"))
        self.log_sql = self.is_true(env_vars.get("LOG_SQL"))
        self.log_db = self.is_true(env_vars.get("LOG_DB"))
        self.log_db_level = env_vars.get("LOG_DB_LEVEL")
        self.log_level = env_vars.get("LOG_LEVEL")

    def to_dict(self):
        if not self.enable:
            return {}
        res = OrderedDict()
        res["--logfile"] = self.logfile
        res["--log-handler"] = self.log_handler
        res["--log-request"] = self.log_request
        res["--log-response"] = self.log_response
        res["--log-web"] = self.log_web
        res["--log-sql"] = self.log_sql
        res["--log-db"] = self.log_db
        res["--log-db-level"] = self.log_db_level
        res["--log-level"] = self.log_level
        return res


class UpdateInstallSection(OdooConfigSection):
    def __init__(self, odoo_config_maker, env_vars):
        super(UpdateInstallSection, self).__init__(odoo_config_maker, env_vars)
        self.update = [u.strip() for u in env_vars.get("UPDATE", "").split(",")]
        self.install = [i.strip() for i in env_vars.get("INSTALL", "").split(",")]
        self.stop_after_init = self.is_true(env_vars.get("STOP_AFTER_INIT"))
        self.save_config_file = self.is_true(env_vars.get("SAVE_CONFIG_FILE"))
        self.force_stop_after_init = False
        self.force_save_config_file = False

    def to_dict(self):
        default_res = OrderedDict()
        if self.force_save_config_file:
            default_res["--save"] = self.force_save_config_file
        if self.force_stop_after_init:
            default_res["--stop-after-init"] = self.force_stop_after_init
        if not self.enable:
            return default_res
        res = OrderedDict()
        res["--update"] = ",".join(self.update)
        res["--init"] = ",".join(self.install)
        res["--stop-after-init"] = self.stop_after_init
        res["--save"] = self.save_config_file
        res.update(default_res)
        return res


class AddonsPathConfigSection(OdooConfigSection):
    def __init__(self, odoo_config_maker, env_vars):
        super(AddonsPathConfigSection, self).__init__(odoo_config_maker, env_vars)
        registry = addons_installer.AddonsRegistry()
        result = registry.parse_env(env_vars=env_vars)
        self.addons_path = [r.addons_path for r in result]

    def to_dict(self):
        if not self.enable:
            return {}
        return {
            "--addons-path": self.addons_path,
        }
