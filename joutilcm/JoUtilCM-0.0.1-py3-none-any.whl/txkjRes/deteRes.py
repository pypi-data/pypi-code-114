# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import cv2
import copy
import time
import random
from flask import jsonify
import numpy as np
from abc import ABC
from PIL import Image
from .resBase import ResBase
from .deteObj import DeteObj
from .deteAngleObj import DeteAngleObj
from ..txkjRes.resTools import ResTools
from ..utils.JsonUtil import JsonUtil
from ..txkjRes.deteXml import parse_xml, save_to_xml
from ..utils.FileOperationUtil import FileOperationUtil

class DeteRes(ResBase, ABC):
    """检测结果"""

    def __init__(self, xml_path=None, assign_img_path=None, json_dict=None, log=None, redis_conn_info=None, img_redis_key=None):
        # 子类新方法需要放在前面
        self._alarms = []
        self._log = log
        super().__init__(xml_path, assign_img_path, json_dict, redis_conn_info=redis_conn_info, img_redis_key=img_redis_key)

    def __contains__(self, item):
        """是否包含元素"""

        if not(isinstance(item, DeteAngleObj) or isinstance(item, DeteObj)):
             raise TypeError("item should 被 DeteAngleObj or DeteObj")

        for each_dete_obj in self._alarms:
            if item == each_dete_obj:
                return True

        return False

    def __add__(self, other):
        """DeteRes之间进行相加"""

        if not isinstance(other, DeteRes):
            raise TypeError("should be DeteRes")

        for each_dete_obj in other.alarms:
            # 不包含这个元素的时候进行添加
            if each_dete_obj not in self:
                self._alarms.append(each_dete_obj)
        return self

    def __len__(self):
        """返回要素的个数"""
        return len(self._alarms)

    def __getitem__(self, index):
        """按照 index 取对应的对象"""
        return self._alarms[index]

    def __setattr__(self, key, value):
        """设置属性后执行对应"""
        object.__setattr__(self, key, value)
        #
        if key == 'img_path' and isinstance(value, str):
            self._parse_img_info()
        elif key == 'xml_path' and isinstance(value, str):
            self._parse_xml_info()
        elif key == 'json_dict' and isinstance(value, dict):
            self._parse_json_info()

    # ------------------------------------------ transform -------------------------------------------------------------

    def _parse_xml_info(self):
        """解析 xml 中存储的检测结果"""
        xml_info = parse_xml(self.xml_path)
        #
        if 'size' in xml_info:
            if 'height' in xml_info['size']:
                self.height = float(xml_info['size']['height'])
            if 'width' in xml_info['size']:
                self.width = float(xml_info['size']['width'])
        #
        if 'filename' in xml_info:
            self.file_name = xml_info['filename']
        #
        if 'path' in xml_info:
            self.img_path = xml_info['path']

        if 'folder' in xml_info:
            self.folder = xml_info['folder']

        # 解析 object 信息
        for each_obj in xml_info['object']:
            # bndbox
            if 'bndbox' in each_obj:
                bndbox = each_obj['bndbox']

                if not bndbox:
                    break

                # ------------------------------------------------------------------------------------------------------
                # fixme 恶心的代码，在同一后进行删除

                if 'xmin' in bndbox:
                    x_min, x_max, y_min, y_max = int(bndbox['xmin']), int(bndbox['xmax']), int(bndbox['ymin']), int(bndbox['ymax'])
                elif 'xMin' in bndbox:
                    x_min, x_max, y_min, y_max = int(bndbox['xMin']), int(bndbox['xMax']), int(bndbox['yMin']), int(bndbox['yMax'])
                else:
                    continue
                # ------------------------------------------------------------------------------------------------------

                if 'prob' not in each_obj: each_obj['prob'] = -1
                if 'id' not in each_obj: each_obj['id'] = -1
                if 'des' not in each_obj: each_obj['des'] = ''
                if each_obj['id'] in ['None', None]: each_obj['id'] = -1

                self.add_obj(x1=x_min, x2=x_max, y1=y_min, y2=y_max, tag=each_obj['name'], conf=float(each_obj['prob']), assign_id=int(each_obj['id']), describe=each_obj['des'])
            # robndbox
            if 'robndbox' in each_obj:
                bndbox = each_obj['robndbox']
                cx, cy, w, h, angle = float(bndbox['cx']), float(bndbox['cy']), float(bndbox['w']), float(bndbox['h']), float(bndbox['angle'])
                if 'prob' not in each_obj: each_obj['prob'] = -1
                if 'id' not in each_obj : each_obj['id'] = -1
                if 'des' not in each_obj : each_obj['des'] = ''
                # fixme 这块要好好修正一下，这边应为要改 bug 暂时这么写的
                if each_obj['id'] in ['None', None] : each_obj['id'] = -1
                self.add_angle_obj(cx, cy, w, h, angle, tag=each_obj['name'], conf=each_obj['prob'], assign_id=each_obj['id'], describe=each_obj['des'])

    def save_to_xml(self, save_path, assign_alarms=None):
        """保存为 xml 文件"""
        xml_info = {'size': {'height': str(self.height), 'width': str(self.width), 'depth': '3'},
                    'filename': self.file_name, 'path': self.img_path, 'object': [], 'folder': self.folder,
                    'segmented': "", 'source': ""}

        if assign_alarms is None:
            alarms = self._alarms
        else:
            alarms = assign_alarms
        #
        for each_dete_obj in alarms:
            # bndbox
            if isinstance(each_dete_obj, DeteObj):
                each_obj = {'name': each_dete_obj.tag, 'prob': str(each_dete_obj.conf), 'id':str(each_dete_obj.id), 'des':str(each_dete_obj.des),
                            'bndbox': {'xmin': str(int(each_dete_obj.x1)), 'xmax': str(int(each_dete_obj.x2)),
                                       'ymin': str(int(each_dete_obj.y1)), 'ymax': str(int(each_dete_obj.y2))}}
                xml_info['object'].append(each_obj)
            # robndbox
            elif isinstance(each_dete_obj, DeteAngleObj):
                each_obj = {'name': each_dete_obj.tag, 'prob': str(each_dete_obj.conf), 'id': str(int(each_dete_obj.id)), 'des':str(each_dete_obj.des),
                            'robndbox': {'cx': str(each_dete_obj.cx), 'cy': str(each_dete_obj.cy),
                                         'w': str(each_dete_obj.w), 'h': str(each_dete_obj.h),'angle': str(each_dete_obj.angle)}}
                xml_info['object'].append(each_obj)

        # 保存为 xml
        save_to_xml(xml_info, xml_path=save_path)

    def add_obj(self, x1, y1, x2, y2, tag, conf=-1, assign_id=-1, describe=''):
        """快速增加一个检测框要素"""
        one_dete_obj = DeteObj(x1=x1, y1=y1, x2=x2, y2=y2, tag=tag, conf=conf, assign_id=assign_id, describe=describe)
        self._alarms.append(one_dete_obj)

