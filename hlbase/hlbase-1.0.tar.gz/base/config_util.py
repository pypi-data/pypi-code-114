# -*- coding: utf-8 -*-
# python 3.x
# author：huangxiaoyan
# data:"2021/7/20 10:47"

import os
from configparser import NoOptionError, NoSectionError
from base.config_handle import ConfigHandle
from base import rootPath
from base.logger import Log

logger = Log('ConfigUtil')

class ConfigUtil:
    # 用例执行配置文件路径case
    @staticmethod
    def get_config_file(dirname, second_dir=None, filename=None):
        conf_path = os.path.join(dirname, second_dir, filename)
        return conf_path

    # 获取当前运行环境
    @classmethod
    def getGlobalsProjectEnv(cls):
        try:
            env_conf_path = cls.get_config_file(rootPath, "config", "globals.conf")
            project_env = ConfigHandle(env_conf_path).get_eval_data('ENV', 'project_env')
            return project_env
        except Exception as e:
            logger.error("运行环境{}配置获取错误".format("ENV"))
            return None

    # 获取当前环境的数据库配置
    @classmethod
    def getDb(cls):
        cls.getDb(dbName='db')

        # 指定库名，获取当前环境的数据库配置

    @classmethod
    def getDb(cls, dbName='db'):
        project_env = cls.getGlobalsProjectEnv()
        # try:
        env_conf_path = cls.get_config_file(rootPath, "config", project_env + ".conf")
        # logger.info(env_conf_path)
        re_db = ConfigHandle(env_conf_path).get_eval_data('DB', dbName)
        return re_db
        # except :
        #     logger.error("{}环境->数据库{}配置获取错误".format(project_env, dbName))G
        #     return None

    @classmethod
    def getRedis(cls, redisName):
        project_env = cls.getGlobalsProjectEnv()
        env_conf_path = cls.get_config_file(rootPath, "config", project_env + ".conf")
        re_db = ConfigHandle(env_conf_path).get_eval_data('REDIS', redisName)
        return re_db

    # 获取环境变量
    @classmethod
    def getEnvParam(cls, section, option):
        project_env = cls.getGlobalsProjectEnv()
        try:
            env_conf_path = cls.get_config_file(rootPath, "config", project_env + ".conf")
            env_value = ConfigHandle(env_conf_path).get_eval_data(section, option)
            return env_value
        except SyntaxError:
            try:
                env_value = ConfigHandle(env_conf_path).get_value(section, option)
                return env_value
            except NoOptionError or NoSectionError:
                return cls.getGlobalsEnvHost(section, option)

    @classmethod
    def getGlobalsEnvHost(cls, section, option):
        try:
            env_value = ConfigHandle(cls.getGlobals()).get_value(section, option)
            return env_value
        except NoOptionError or NoSectionError:
            logger.error("globals配置文件无该参数:{}".format(option))
            return ''

    # 获取用例执行策略
    @classmethod
    def getExecutionStrategy(cls):
        case = []
        try:
            mode = cls.getGlobalsMode()
            if mode == 1:
                case = ConfigHandle(cls.getGlobals()).get_eval_data("ENV", "appoint_case")
            if mode == 2:
                case = ConfigHandle(cls.getGlobals()).get_eval_data("ENV", "region_case")
        except Exception as e:
            logger.error('获取用例运行模式失败' + str(e))
        return case

    @classmethod
    def getGlobalsMode(cls):
        mode = ConfigHandle(cls.getGlobals()).get_value("ENV", "mode")
        return int(mode)

    @classmethod
    def getGlobalsRunnerModule(cls):
        runner_module = ConfigHandle(cls.getGlobals()).get_value("ENV", "runner_module")
        return runner_module

    @classmethod
    def getGlobalsHttpEnv(cls):
        http_env = ConfigHandle(cls.getGlobals()).get_value("ENV", "datafactory_http")
        return http_env

    @classmethod
    def getGlobals(cls):
        globals_conf_path = cls.get_config_file(rootPath, "config", "globals.conf")
        return globals_conf_path

    @classmethod
    def getTestCaseBD(cls):
        test_case_db = ConfigHandle(cls.getGlobals()).get_value("CASE_DB", "test_case")
        return test_case_db