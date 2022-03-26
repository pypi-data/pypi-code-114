import shutil
import os
import sys
import cv2

os.system('git clone https://huggingface.co/spaces/nielsr/dit-document-layout-analysis')
os.system("git clone https://github.com/microsoft/unilm.git")
# shutil.move('DIT-document-layout-analysis/Base-RCNN-FPN.yml','Base-RCNN-FPN.yml' ) CHECK FILE IS IN OR NOT
# os.system('pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu102/torch1.9/index.html')
os.system('git clone https://github.com/facebookresearch/detectron2.git')
os.rename("detectron2","detectron")
shutil.move('detectron/detectron2', 'detectron2')
# import detectron2
sys.path.append("unilm")
from unilm.dit.object_detection.ditod.config import add_vit_config
import torch
from detectron2.config import CfgNode as CN
from detectron2.config import get_cfg
from detectron2.utils.visualizer import ColorMode, Visualizer
from detectron2.data import MetadataCatalog
from detectron2.engine import DefaultPredictor

# # Step 1: instantiate config
cfg = get_cfg()
add_vit_config(cfg)
cfg.merge_from_file("cascade_dit_base.yml")

# Step 2: add model weights URL to config

cfg.MODEL.WEIGHTS = "https://layoutlm.blob.core.windows.net/dit/dit-fts/publaynet_dit-b_cascade.pth"

# cfg.MODEL.WEIGHTS = "https://layoutlm.blob.core.windows.net/dit/dit-fts/publaynet_dit-b_mrcnn.pth"
cfg.MODEL.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Step 4: define model
predictor = DefaultPredictor(cfg)


def analyze_image(img):
    md = MetadataCatalog.get(cfg.DATASETS.TEST[0])
    if cfg.DATASETS.TEST[0]=='icdar2019_test':
        md.set(thing_classes=["table"])
    else:
        md.set(thing_classes=["text","title","list","table","figure"])
    cv2.imwrite('before_visulazise.png', img)
    output = predictor(img)["instances"]
    v = Visualizer(img[:, :, ::-1],
                    md,
                    scale=1.0,
                    instance_mode=ColorMode.SEGMENTATION)
    result = v.draw_instance_predictions(output.to("cpu"))
    result_image = result.get_image()[:, :, ::-1]
    cv2.imwrite('after_visulazise.png', result_image)
    return result_image

