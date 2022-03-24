class Files:
    """ahk代码文件模型的注册中心

    参考了django.apps.registry.Apps的实现
    """
    def __init__(self):
        self.all_files = {}
        self.all_funcs = {}

    def register_file(self, ahk):
        self.all_files[ahk.__name__] = ahk

    def register_func(self, func: callable):
        self.all_funcs[func.__name__] = func


files = Files()