#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: load.py
# Author: Haoyu Lu
# Mail: lhy1998@ruc.edu.cn
# Created Time:  2022-3-18 19:17:34
#############################################


import argparse
import torch
import sys 
sys.path.append("..")

from models import build_network
from utils.config import cfg_from_yaml_file, cfg

def load_wenlan_model(load_checkpoint='../wenlan-video-model.pth', device='cpu'):
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg_file', type=str, default='cfg/moco_box.yml')

    args = parser.parse_args()
    cfg_from_yaml_file(args.cfg_file, cfg)

    cfg.MODEL.IMG_SIZE = 384
    cfg.MODEL.IS_EXTRACT = True
    cfg.DATASET.TEST_SET = 'test'

    model = build_network(cfg.MODEL)
    model.load_state_dict(torch.load(load_checkpoint))

    model = model.to(device)
    model.eval()

    return model