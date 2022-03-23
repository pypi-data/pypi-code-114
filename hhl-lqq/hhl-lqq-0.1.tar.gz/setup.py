from setuptools import setup,find_packages
setup(
    name="hhl-lqq",
    version="0.1",
    author="hhl",
    description="黄慧琳 梁琪琪 钟香琴",
#url="ckh.handsome.com", 此网站需要存在且未被占用
    packages = find_packages("hhl"), # 模块的保存目录
    package_dir = {"":"hhl"}, # 告诉 setuptools 包都在 ckh 下
    package_data = {
# 定义打包除了 .py 之外的文件类型，此处 .py 其实可以不写
# 定义完成打包的部署文件后，进行程序的执行，执行时可以设置多种类型的包
# 打包
# 打包完成后，会生成两个类型的包
#都保存在 dist 目录中
#复制一份 .whl 文件，重命名为 .zip 或 .rar
    "":[".txt",".info","*.properties",".py"],
# 包含 data 文件夹下所有的 *.dat 文件
    "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)
