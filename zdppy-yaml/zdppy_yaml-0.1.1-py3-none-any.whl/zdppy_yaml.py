#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 23:07
# @Author  : 张大鹏
# @Site    : 
# @File    : zdppy_yaml.py
# @Software: PyCharm
import os
from typing import Union, Tuple, List, Dict
from .libs import yaml


class Yaml:
    def __init__(self,
                 config: str = "config/config.yaml",
                 config_secret: str = "config/secret/.config.yaml"
                 ):
        """
        yaml文件操作对象
        :param config: 普通配置文件
        :param config_secret: 私密的配置文件
        """
        self.__config_file = config
        self.__config_secret_file = config_secret
        self.config = {}  # 配置对象
        self.__init_config()  # 初始化配置对象

    def __init_config(self):
        """
        初始化配置
        :return:
        """
        # 读取公共配置
        if os.path.exists(self.__config_file):
            with open(self.__config_file, "r") as f:
                config = yaml.safe_load(f)
                self.config.update(config)

        # 读取私密配置
        if os.path.exists(self.__config_secret_file):
            with open(self.__config_secret_file, "r") as f:
                config = yaml.safe_load(f)
                self.config.update(config)

    def __read_config(self, config: str):
        """
        读取单个配置文件
        :param config: 配置文件
        :return:
        """
        if os.path.exists(config):
            with open(config, "r") as f:
                c = yaml.safe_load(f)
                self.config.update(c)

    def read_config(self, config: Union[str, List, Tuple]):
        """
        读取配置
        :param config:配置源
        :return:
        """
        if isinstance(config, str):
            self.__read_config(config)
        elif isinstance(config, list) or isinstance(config, tuple):
            for c in config:
                self.__read_config(c)

    def save_config(self, config="config/zdppy_yaml_config.yaml"):
        """
        保存配置
        :param config:配置文件地址
        :return:
        """
        with open(config, "w") as f:
            yaml.dump(self.config, f)

    def update_config(self, config: Union[Dict, str, List, Tuple]):
        """
        更新配置
        :param config:配置对象
        :return:
        """
        if isinstance(config, dict):
            self.config.update(config)
        else:
            self.read_config(config)

    def __str__(self):
        return str(self.config)
