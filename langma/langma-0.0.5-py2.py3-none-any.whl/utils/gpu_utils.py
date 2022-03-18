# *_*coding:utf-8 *_*
from __future__ import absolute_import, division, print_function
from langma.utils.logutil import logger


def check_gpu_tf():
    import tensorflow as tf

    logger.info(tf.__version__)

    logger.info(f'GPU可用：{tf.config.list_physical_devices("GPU")}')


def check_gpu_torch():
    import torch

    logger.info(torch.__version__)

    logger.info(f'GPU可用：{torch.cuda.is_available()}')


if __name__ == '__main__':
    check_gpu_tf()
    # check_gpu_torch()
