# @Time : 2022/3/6 6:06 PM 
# @Author : SailYang
import importlib.util
import inspect
import os
import sys

from ddt import mk_test_name


class DiscoverTestCases:

    def __init__(self, target_file_or_file=None):
        """
        指定测试用例开始查找目录，如果没有指定，则分配固定目录
        """
        # if not target_file_or_file:
        #     self.test_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests')
        # else:
        self.test_file = target_file_or_file

    def recursive_file_parser(self, file_path):
        file_lists = []
        # os.listdir 列出子级文件和文件夹名字，仅列出次级
        files = os.listdir(file_path)
        for f in files:
            f_p = os.path.join(file_path, f)
            if os.path.isdir(f_p):
                self.recursive_file_parser(f_p)
            else:
                if f_p.endswith(".py"):
                    """
                    os.path.join方法有三种情况：
                    1)如果个组件首字母不包含"/"，函数会自动加上
                    2)如果一个组件是另一个组件的绝对路径，在它之前的所有组件会被舍弃
                    3)如果最后一个组件为空，则自动生成"/"结尾
                    """
                    # 这里file_path可能是f_P的绝对路径前部分，会自动被舍弃掉
                    file_lists.append(os.path.join(file_path, f_p))
        return file_lists

    def find_test_module(self):
        """
        根据指定文件查找到测试文件名并将其导入
        :return: 返回mod_ref 测试文件列表
        """
        mod_ref = []
        module_name_list = []
        module_file_paths = []

        if os.path.isdir(self.test_file):
            # 递归查找目标文件夹下的 .py 文件

            all_files = self.recursive_file_parser(self.test_file)

            # 将测试文件名查找出来并放在list中（不包括文件拓展名）

            for item in all_files:
                module_name_list.append(inspect.getmodulename(item))
                module_file_paths.append(item)

        # 如果提供的路径就是测试文件
        elif os.path.isfile(self.test_file):
            module_name_list = [inspect.getmodulename(self.test_file)]
            module_file_paths = [self.test_file]

        """
        zip(a,b)返回值为对象，需要将返回值转成list(),结构为[(测试数据1,测试数据2),(测试数据3),(测试数据4)]
        """
        for module_name, module_file_path in zip(module_name_list, module_file_paths):
            try:
                # importlib 可以通过仅传入文件名和其路径就可以导入模块
                # spec_from_file_location()接受文件名和路径，返回导入模块名
                module_spec = importlib.util.spec_from_file_location(module_name, module_file_path)

                # 通过module_from_spec方法可以判断 传入的模块是否存在，如果存在返回该模块对象，反之返回None
                module = importlib.util.module_from_spec(module_spec)

                # 通过loader.exec_module方法 传入模块对象，将模块导入项目环境
                module_spec.loader.exec_module(module)

                """
                sys.modules 是一个全局字典，每当导入新模块就会记录模块名字，
                并且起到了缓存作用，当再次导入相同模块时会从字典中查找从而加快程序运行速度
                """
                # 将module_name和module导入模块以字典的形式存入到sys.modules全局字典中
                sys.modules[module_name] = module
                mod_ref.append(module)
            except ImportError:
                raise ImportError(f'Module:{self.test_file} can not imported')
        return mod_ref

    def find_tests(self, mod_ref):
        """
        遍历上一步查找到的测试模块，过滤出符合条件的测试用例
        :param mod_ref: 入参，测试文件列表
        :return:返回测试用例集合
        """
        test_cases = []
        for module in mod_ref:

            # inspect.getmembers() 可以获取对象的成员属性，可以传入模块，类，实例，函数，方法
            # 返回数据如：class,method,function,generator,tracback,frame,code,builtin，返回值为(name,value)的列表组合
            # inspect.isclass() 判断传入对象是否为类，但这里是嵌套inspect.getmembers()使用，所以无需加()
            """
            inspect.isclass 无需调用方法，去掉括号。主要用于当做过滤条件
            inspect.isclass() 是否是类
            这里的module在data_provider装饰器中添加了__data_Provider__属性，并且 '__data_Provider__'  = test_data
            """
            cls_members = inspect.getmembers(module, inspect.isclass)

            for cls in cls_members:
                cls_name, cls_code_objects = cls

                # 通过dir类对象，返回类中的类方法和属性
                # 查找仅"tests"开头的测试用例的对象，即tests_suspect
                for func_name in dir(cls_code_objects):
                    # if func_name.startswith('tests'):
                    # tests_suspect 为测试方法对象
                    tests_suspect = getattr(cls_code_objects, func_name)

                    if getattr(tests_suspect, "__test_case_type__", None) == "__Test_Case__":

                        if getattr(tests_suspect, "__test_case_enabled__", None):
                            # 获取测试函数__test_tag__属性的值
                            tag_filter = getattr(tests_suspect, "__test_tag__", None)
                            # 判断测试用例是否存在 __data_Provider__ 属性
                            if hasattr(tests_suspect, "__data_Provider__"):
                                """
                                setattr(func, "__data_Provider__", test_data)
        
                                getattr(tests_suspect, "__data__Provider__") 由此可知这里获取test_data，
                                test_data就是数据驱动装饰器传入的数据参数
                                """
                                # 把传入的数据参数进行枚举分组

                                for i, v in enumerate(getattr(tests_suspect, "__data_Provider__")):
                                    # mk_test_name为ddt工具提供的方法，用于生成新的测试用例名称

                                    new_test_name = mk_test_name(tests_suspect.__name__, getattr(v, "__name__", v), i)

                                    # 将测试函数的Tag，测试类，新生成的测试用名称，测试数据组成一条测试用例供测试框架后续调用
                                    test_cases.append((tag_filter, cls_code_objects, new_test_name, tests_suspect, v))
                            else:

                                # 当没有 __data__Provider 属性直接返回原测试用例
                                test_cases.append((tag_filter, cls_code_objects, func_name, tests_suspect, None))
        return test_cases
