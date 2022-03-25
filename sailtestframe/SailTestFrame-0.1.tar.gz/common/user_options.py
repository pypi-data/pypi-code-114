# @Time : 2022/3/7 3:46 PM 
# @Author : SailYang
import argparse
import importlib.util
import os.path
import re
import shlex
import sys
from multiprocessing import cpu_count


def parser_options(user_options=None):
    parser = argparse.ArgumentParser(prog="testing",
                                     description="testing framework demo"
                                     )

    parser.add_argument("-env",
                        action="store",
                        default="qa",
                        dest="default_env",
                        metavar="target environment",
                        choices=['qa', 'prod'],
                        help='Specify test environment'
                        )

    parser.add_argument("-t",
                        action="store",
                        default=None,
                        dest="test_targets",
                        metavar="target run path/file",
                        help="Specify run path/file"
                        )

    parser.add_argument("-i",
                        action="store",
                        default=None,
                        dest="include_tags_any_match",
                        metavar="user provided tags,"
                                "string only,separate by comma without an spacing among all tags.if any user provided",
                        help="Select test cases to run by tags,separated by comma,no blank space among tag values"
                        )

    # 添加并发数目，默认为可用的CPU个数
    parser.add_argument("-n",
                        action="store",
                        type=int,
                        default=cpu_count(),
                        dest="test_thread_number",
                        metavar="int number",
                        help="Specify the number of testing thread run in parallel,default are cpu number."
                        )

    parser.add_argument("-r",
                        action="store",
                        type=int,
                        default=None,
                        dest="report_file",
                        metavar="store report bash file",
                        help="Specify report bash file."
                        )

    if not user_options:
        args = sys.argv[1:]
    else:
        args = shlex.split(user_options)

    # options是名字空间 <class 'argparse.Namespace'>
    options, un_known = parser.parse_known_args(args)

    def split(option_value):
        return None if option_value is None else re.split(r'[,]\s*', option_value)

    options.include_tags_any_match = split(options.include_tags_any_match)

    # 指定并发数目，默认为可用CPU个数
    options.test_thread_number = options.test_thread_number

    # 获取测试文件的绝对路径
    if options.test_targets:
        if not os.path.isdir(options.test_targets) and not os.path.isfile(options.test_targets):
            parser.error("test_targets must be a folder path or file path,"
                         "it either be absolute path or relative path,"
                         "if it is relative,it must relative to tests folder under your root folder ")
        # 判断test_targets是否为绝对路径
        if not os.path.isabs(options.test_targets):
            options.test_targets = os.path.abspath(options.test_targets)
        else:
            options.test_targets = options.test_targets

    if options.default_env:
        try:
            module_package = '.' + os.sep + 'configs' + os.sep + 'test_env'
            module_name = module_package + os.sep + f'{options.default_env}_env'
            module_file = f'{module_name}.py'

            # 获取测试用用例的文件名和文件路径，将其导入
            module_spec = importlib.util.spec_from_file_location(module_name, module_file)
            env = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(env)

            # 过滤掉文件中的各种变量，如以"__"的方法名或属性，并给options 命名空间添加config属性
            options.config = {item: getattr(env, item, None) for item in dir(env) if not item.startswith("__")}
        except ImportError:
            raise ImportError(f'Module:{module_name} can not imported')
    return options
