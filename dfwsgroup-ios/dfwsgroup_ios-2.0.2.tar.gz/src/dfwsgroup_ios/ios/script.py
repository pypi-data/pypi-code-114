#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/25 16:50
# @Author  : Lifeng
# @Site    : 
# @File    : script.py
# @Software: PyCharm


import os
import json
import logging
import subprocess
from pathlib import Path
from jinja2 import Template


def check_fastbot(command: str):
    """
    根据输入的命令
    检查是否安装了FastbotRunner-Runner软件
    如果已安装就返回FastbotRunner-Runner的BUNDLEID
    :param command:
    :return:
    """
    p = subprocess.run(command, stdout=subprocess.PIPE).stdout
    if p:
        for i in tuple(
                i.rstrip(r"\\r") for i in str(p).split(r"\n")
        ):
            if "FastbotRunner-Runner" in i:
                results = i.split(" ")[0]
                return results
    else:
        raise Exception


def read_command(contents: list):
    """
    读取json文件中的命令。并进行替换处理
    :param contents:
    :return:
    """
    command = ""
    _path = Path(
        __file__
    ).parent.parent.joinpath("data", "command.json")
    with open(_path, "r+", encoding="utf-8") as r:
        data = Template(
            r.read()
        ).render(contents=contents)
        for i in json.loads(data).values():
            command += i + " "
    return command


def gain_fastbot_runner(subparsers):
    """
    设置命令行指定运行命令
    :param subparsers:
    :return:
    """
    sub_subparsers_command = subparsers.add_parser(
        "run", help="运行"
    )
    sub_subparsers_command.add_argument(
        "bundle_id", type=str, nargs="?", help="被测包的bundle_id"
    )
    sub_subparsers_command.add_argument(
        "-d", "--duration", type=int, help="运行时长"
    )
    sub_subparsers_command.add_argument(
        "-t", "--throttle", type=int, help="遍历点击事件"
    )

    return sub_subparsers_command


def command_main(args):
    """
    运行命令
    :return:
    """

    if args.bundle_id:
        fastbotrunner_xctrunner = check_fastbot("tidevice applist")
        package_bundle_id = args.bundle_id
        duration, throttle = args.duration, args.throttle

        if duration or throttle:
            logging.info(f"指定时长-> {duration}")
            logging.info(f"指定事件频率-> {throttle}")
        else:
            duration, throttle = 5, 500
            logging.info(f"默认时长-> {duration}")
            logging.info(f"默认事件频率-> {throttle}")

        return os.system(
            read_command(
                contents=[fastbotrunner_xctrunner, package_bundle_id, duration, throttle]
            )
        )
    else:
        raise Exception(f"请检查被测试包的bundle_id-> {args.bundle_id}")



print(read_command([1, 2, 3, 4]))