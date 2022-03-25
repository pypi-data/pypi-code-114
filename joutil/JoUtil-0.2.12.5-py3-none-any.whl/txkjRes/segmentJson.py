# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import cv2
from labelme import utils
from ..utils.JsonUtil import JsonUtil
from ..utils.FileOperationUtil import FileOperationUtil
from .segmentObj import SegmentObj
import numpy as np

# todo 从 mask 得到 points，可以指定 point 中的点的个数，这样就能直接将 分割出来的结果直接转为 json 输入的结果的样式



class SegmentJson(object):

    def __init__(self, json_path=None):

        self.version = ""
        self.image_width = ""
        self.image_height = ""
        self.shapes = []
        self.image_path = ""
        self.line_color = ""
        self.fill_color = ""
        self.image_data = None
        self.flags = ""
        self.json_path = json_path
        self.mask = None

    def parse_json_info(self, json_path=None, parse_img=False, parse_mask=False):
        """解析 json 的信息, 可以选择是否解析 img 和 mask"""

        if json_path:
            a = JsonUtil.load_data_from_json_file(json_path)
        else:
            a = JsonUtil.load_data_from_json_file(self.json_path)
        # parse attr
        self.version = a["version"] if "version" in a else ""
        self.image_width = a["imageWidth"] if "imageWidth" in a else ""
        self.image_height = a["imageHeight"] if "imageWidth" in a else ""
        self.image_path = a["imagePath"] if "imagePath" in a else ""
        self.line_color = a["lineColor"] if "lineColor" in a else ""
        self.fill_color = a["fillColor"] if "fillColor" in a else ""
        # fixme 需要拿到 img 才知道图像的大小，属性中的图像大小可能出问题
        if parse_img or parse_mask:
            self.image_data = utils.img_b64_to_arr(a["imageData"]) if "imageData" in a else ""
        self.flags = a["flags"] if "flags" in a else ""
        # parse shape
        label_name_dict = {}
        lables_dict = {}
        value_index = 1
        for each_shape in a["shapes"]:
            each_label = each_shape["label"] if "label" in each_shape else ""
            # strip number
            each_label_no_number = each_label.strip("0123456789")
            # fixme label_no_number 是 Jo12 应该是 Jo， yo2 应该是 yo
            if each_label_no_number not in lables_dict:
                lables_dict[each_label_no_number] = value_index
                value_index += 1
            label_name_dict[each_label] = lables_dict[each_label_no_number]
            #
            each_shape_points = each_shape["points"] if "points" in each_shape else []
            each_type = each_shape["shape_type"] if "shape_type" in each_shape else ""
            each_obj = SegmentObj(label=each_label_no_number, points=each_shape_points, shape_type=each_type, mask_value=each_label_no_number)
            self.shapes.append(each_obj)

        # parse mask
        if parse_mask:
            self.mask, _ = utils.shapes_to_label(self.image_data.shape, a["shapes"], label_name_dict)

    def save_mask(self, save_path=None):
        """将 mask 保存为图片文件"""
        # fixme 最好不要保存，保存后的结果比较大，还不如临时读取
        np.save(save_path, self.mask.astype(np.bool))

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















