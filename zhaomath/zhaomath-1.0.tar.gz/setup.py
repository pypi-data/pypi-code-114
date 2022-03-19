from distutils.core import setup
import zhaomath.module_a1
setup(
    name="zhaomath",
    version="1.0",
    description="自定义函数",
    author="zhao",
    author_email="zhao@163.com",
    py_modules=["zhaomath.module_a1", "zhaomath.module_a2"]
)