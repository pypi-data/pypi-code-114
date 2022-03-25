# -*- coding: utf-8  -*-
# -*- author: jokker -*-


class PrintUtil(object):

    @staticmethod
    def print(data):
        """用我习惯的方式进行打印"""

        if isinstance(data, list):
            PrintUtil.print_list(data)
        else:
            raise TypeError("type : {0}  not support".format(type(data)))

    @staticmethod
    def print_list(data):
        """打印列表"""
        for index, each in enumerate(data):
            print(index, each)










