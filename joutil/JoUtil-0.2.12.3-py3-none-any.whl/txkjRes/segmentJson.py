# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from ..utils.JsonUtil import JsonUtil
from ..utils.FileOperationUtil import FileOperationUtil
from .segmentObj import SegmentObj


class SegmentJson(object):


    def __init__(self):

        self.version = ""
        self.imageWidth = ""
        self.imageHeight = ""
        self.shapes = []
        self.imagePath = ""
        self.lineColor = ""
        self.fillColor = ""
        self.imageData = ""
        self.flags = ""

    def parse_json_info(self, json_path):
        """解析 json 的信息"""

        a = JsonUtil.load_data_from_json_file(json_path)
        # parse attr
        self.version = a["version"] if "version" in a else ""
        self.imageWidth = a["imageWidth"] if "imageWidth" in a else ""
        self.imageHeight = a["imageHeight"] if "imageWidth" in a else ""
        self.imagePath = a["imagePath"] if "imagePath" in a else ""
        self.lineColor = a["lineColor"] if "lineColor" in a else ""
        self.fillColor = a["fillColor"] if "fillColor" in a else ""
        self.imageData = a["imageData"] if "imageData" in a else ""
        self.flags = a["flags"] if "flags" in a else ""
        # parse shape
        for each_shape in a["shapes"]:
            each_label = each_shape["label"] if "label" in each_shape else ""
            each_shape_points = each_shape["points"] if "points" in each_shape else []
            each_type = each_shape["shape_type"] if "shape_type" in each_shape else ""
            each_obj = SegmentObj(label=each_label, points=each_shape_points, shape_type=each_type)
            self.shapes.append(each_obj)

    def print_as_fzc_format(self):
        """按照防振锤的格式进行打印"""
        for each_shape in self.shapes:
            print(each_shape.get_format_list())




if __name__ == "__main__":

    json_dir = r"C:\data\004_绝缘子污秽\val\json"

    a = SegmentJson()

    for each_json_path in FileOperationUtil.re_all_file(json_dir, endswitch=['.json']):

        a.parse_json_info(each_json_path)

        break

    a.print_as_fzc_format()















