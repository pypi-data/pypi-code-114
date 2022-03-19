import setuptools


name = 'cqh_file'
long_description = """信息
====================================================

command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

serve
-------------------------------------------------

opts:

* ``port`` ,  端口,默认是8081
* ``dir`` , 要目录
* ``timeout``, 默认值为60s, 内存缓存的超时时间

eg:

    sudo /home/vagrant/envs/default/bin/cqh_file --port=8081 --dir=/www/backup/path


client
-------------------------------------------------------

目的是为了下载服务器的dir

opts:

* ``url``, 地址
* ``dir``, 本地保存的目录
* ``sleep``,  睡眠时间,默认是300s



eg::

    cqh_file client --url='http://127.0.0.1:8081' --dir=/tmp/backup1

    python -m cqh_file client --url="http://192.168.146.129:8081" --dir="D:\\backup"

"""



version = "0.0.16"

setuptools.setup(
    name=name,  # Replace with your own username
    version=version,
    author="chenqinghe",
    author_email="1832866299@qq.com",
    description="cqh utils function",
    long_description=long_description,
    long_description_content_type='',
    url="https://github.com/chen19901225/cqh_util",
    packages=setuptools.find_packages(),
    install_requires=[
        "click",
        "tornado",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    entry_points={
        "console_scripts": [
            "cqh_file=cqh_file.run:cli",
        ],
    },
    python_requires='>=3.6',
    include_package_data=True
)