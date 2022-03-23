#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   __init__.py
   @Create  :   2021/09/06 19:45:16
   @Author  :   Your Name
   @Update  :   2021/09/06
   @License :   (C)Copyright 2014-2021 SmartAHC All Rights Reserved 
   @Desc    :   Coding Below
"""

from .app_product import product
from .app_logger import logger, BASIC_FORMAT

import logging
import json


class App():

    """
    项目主入口
    """

    def __init__(self):
        """
        根据需要初始化
        """
        if product.IS_DEBUG:
            logging.basicConfig(level=logging.DEBUG, format=BASIC_FORMAT)
        else:
            logging.basicConfig(level=logging.ERROR, format=BASIC_FORMAT)
        # 打印配置信息
        CONFIG = json.dumps(product.__dict__, indent=4)
        logger.info("----------------------------------------------------")
        if product.IS_DEBUG:
            logger.debug(CONFIG)
        else:
            logger.info(f"DEBUG: {product.IS_DEBUG}")
        logger.info("----------------------------------------------------")
        logger.debug("APP RUNNING")

    def run(self):
        """
        主函数入口
        """
        pass
