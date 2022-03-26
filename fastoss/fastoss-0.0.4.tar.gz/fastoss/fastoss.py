#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import oss2
import envx
import sys
import os

"""
SDK文档：https://help.aliyun.com/document_detail/32026.html

存储类型介绍：https://help.aliyun.com/document_detail/51374.html
标准存储:standard-archives
低频访问:infrequent-archives
归档存储:archives（需要取回）
冷归档存储:cold-archives（需要取回）


"""


def percentage(
        consumed_bytes,
        total_bytes
):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')
        sys.stdout.flush()


def make_con_info(
        env_file_name: str = 'oss.env'
):
    # ---------------- 固定设置 ----------------
    inner_env = envx.read(file_name=env_file_name)
    con_info = {
        "access_key_id": inner_env.get('access_key_id'),
        "access_key_secret": inner_env.get('access_key_secret'),
        "endpoint": inner_env.get('endpoint'),
        "bucket_name": inner_env.get('bucket_name')
    }
    # ---------------- 固定设置 ----------------
    return con_info


class Basics:
    def __init__(
            self,
            access_key_id: str = None,
            access_key_secret: str = None,
            endpoint: str = None,
            bucket_name: str = None,
            con_info: dict = None  # 优先使用
    ):
        if con_info is None:
            self.access_key_id = access_key_id
            self.access_key_secret = access_key_secret
            self.endpoint = endpoint
            self.endpoint_url = "http://%s" % endpoint
            self.bucket_name = bucket_name
        else:
            self.access_key_id = con_info.get('access_key_id')
            self.access_key_secret = con_info.get('access_key_secret')
            self.endpoint = con_info.get('endpoint')
            self.endpoint_url = "http://%s" % con_info.get('endpoint')
            self.bucket_name = con_info.get('bucket_name')
        # 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行

    def get_auth_bucket(
            self
    ):
        return oss2.Bucket(
            oss2.Auth(
                self.access_key_id,
                self.access_key_secret
            ),
            self.endpoint_url,
            self.bucket_name
        )

    def upload_file(
            self,
            key: str,
            filename: str,
    ):
        # filename是本地文件名，key是云文件key
        # key='云上座右铭.txt', filename='本地座右铭.txt'
        # 注意要拼接结果地址
        self.get_auth_bucket().put_object_from_file(
            key=key,
            filename=filename
        )
        return 'http://%s.%s/%s' % (self.bucket_name, self.endpoint, key)

    def upload_content(
            self,
            key,
            content
    ):
        # filename是本地文件名，key是云文件key
        # key='云上座右铭.txt', filename='本地座右铭.txt'
        # 注意要拼接结果地址
        self.get_auth_bucket().put_object(
            key=key,
            data=content
        )
        return 'http://%s.%s/%s' % (self.bucket_name, self.endpoint, key)

    def show_bucket(
            self,
            limit=None
    ):
        # [打印]列举Bucket下10个Object，并打印它们的最后修改时间、文件名
        if limit is None:
            for i, object_info in enumerate(oss2.ObjectIterator(self.get_auth_bucket())):
                print("{0} {1}".format(object_info.last_modified, object_info.key))
        else:
            for i, object_info in enumerate(oss2.ObjectIterator(self.get_auth_bucket())):
                print("{0} {1}".format(object_info.last_modified, object_info.key))
                if i >= (limit - 1):
                    break

    def get_bucket_list(
            self,
            limit=None
    ):
        # [返回]列举Bucket下10个Object，并打印它们的最后修改时间、文件名
        bucket_list = list()
        if limit is None:
            for i, object_info in enumerate(oss2.ObjectIterator(self.get_auth_bucket())):
                bucket_list.append({'last_modified': object_info.last_modified, "object_key": object_info.key})
        else:
            for i, object_info in enumerate(oss2.ObjectIterator(self.get_auth_bucket())):
                bucket_list.append({'last_modified': object_info.last_modified, "object_key": object_info.key})
                if i >= (limit - 1):
                    break
        return bucket_list

    def get_content(
            self,
            key
    ):
        return self.get_auth_bucket().get_object(key).read().decode('utf-8')

    def download(
            self,
            key: str,
            filename: str = None,
            path: str = None
    ):
        if filename is None:
            local_file_name = key
        else:
            local_file_name = filename

        if path is None:
            local_file_dir = local_file_name
        else:
            local_file_dir = os.path.join(path, local_file_name)

        return self.get_auth_bucket().get_object_to_file(
                key=key,
                filename=local_file_dir,
                progress_callback=percentage
            )


def upload_file(
        key: str,
        file_dir: str,
        con_info: dict = None,  # 若指定，将优先使用
        env_file_name: str = 'oss.env',
):
    """
    上传文件
    """
    # ---------------- 固定设置 ----------------
    if con_info is None:
        con_info = make_con_info(env_file_name=env_file_name)
    else:
        pass
    # ---------------- 固定设置 ----------------
    oss_basics = Basics(con_info=con_info)
    return oss_basics.upload_file(key=key, filename=file_dir)


def download(
        key: str,
        file_dir: str = None,
        path: str = None,
        con_info: dict = None,  # 若指定，将优先使用
        env_file_name: str = 'oss.env',
):
    """
    上传文件
    """
    # ---------------- 固定设置 ----------------
    if con_info is None:
        con_info = make_con_info(env_file_name=env_file_name)
    else:
        pass
    # ---------------- 固定设置 ----------------
    oss_basics = Basics(con_info=con_info)
    return oss_basics.download(key=key, filename=file_dir, path=path)

