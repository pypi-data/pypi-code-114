# -*- coding: utf-8  -*-
# -*- author: jokker -*-


class SegmentObj(object):
    """一个分割对象"""

    def __init__(self, label="", points=None, shape_type="polygon"):
        self.label = label
        self.points = [] if points is None else points
        self.shape_type = shape_type
        self.flags = ""
        self.line_color = []
        self.fill_color = []

    def get_format_list(self):
        """获得格式化的输出"""
        return [self.label, len(self.points), self.shape_type]

    def do_print(self):
        """打印"""

        print("label : {0}".format(self.label))
        print("points count : {0}".format(len(self.points)))
        print("shape_type : {0}".format(self.shape_type))
        # print("flags : {0}".format(self.flags))
        # print("line_color : {0}".format(self.line_color))
        # print("fill_color : {0}".format(self.fill_color))


