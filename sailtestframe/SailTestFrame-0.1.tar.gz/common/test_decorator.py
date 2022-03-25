# @Time : 2022/3/9 3:26 PM 
# @Author : SailYang
from functools import wraps


class Test:
    """
    enabled 是否启动使用标签挑选测试用例，默认启动
    tag 用户自定义标签
    """

    def __init__(self, tag=None, enabled=True):
        self.enabled = enabled
        self.tag = tag

    def __call__(self, func):
        # @wraps的作用是防止传进来的func 变成了wrapper的__name__,__doc__，因为传进来的func 最后返回的是wrapper
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        # 给原测试函数添加属性，以便测试框架判断当前测试函数是否为测试用例
        setattr(wrapper, "__test_tag__", self.tag)
        setattr(wrapper, "__test_case_type__", "__Test_Case__")
        setattr(wrapper, "__test_case_enabled__", self.enabled)
        return wrapper


class SetUpTest(object):
    def __init__(self, enabled=True):
        self.enabled = enabled

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        # 给原测试函数添加属性，以方便测试框架判断当前测试函数是否为测试用例的前置函数
        setattr(wrapper, "__test_case_fixture_type__", "__setUp__")
        setattr(wrapper, "__test_case_fixture_enabled__", self.enabled)
        return wrapper


class TearDownTest(object):
    def __init__(self, enabled=True):
        self.enabled = enabled

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        # 给原测试函数添加属性，以方便测试框架判断当前测试函数是否为测试用例的后置函数
        setattr(wrapper, "__test_case_fixture_type__", "__teardown__")
        setattr(wrapper, "__test_case_fixture_enabled__", self.enabled)
        return wrapper
