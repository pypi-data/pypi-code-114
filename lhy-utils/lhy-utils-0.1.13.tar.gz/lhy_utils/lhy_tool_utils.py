# coding: utf-8
import math
import random
import re
import subprocess
import time
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import copy

import numpy as np


def read_gpu(return_least=False):
    import pynvml
    pynvml.nvmlInit()
    deviceCount = pynvml.nvmlDeviceGetCount()
    gpu_list = []
    for i in range(deviceCount):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
        name = pynvml.nvmlDeviceGetName(handle).decode()
        total = round(meminfo.total / 1024 ** 3, 2)
        used = round(meminfo.used / 1024 ** 3, 2)
        free = round(meminfo.free / 1024 ** 3, 2)
        information = {
            "id": i,
            "name": name,
            "total": total,
            "used": used,
            "free": free
        }
        gpu_list.append(information)
    if return_least:
        sort_gpu_list = copy.copy(gpu_list)
        sort_gpu_list.sort(key=lambda x: (x["used"], -x["id"]))
        least_id = sort_gpu_list[0]["id"]
        return gpu_list, least_id
    else:
        return gpu_list


def cut_list(target, batch_size):
    return [target[i:i + batch_size] for i in range(0, len(target), batch_size)]


def dict_set_value(input_data, args):
    assert len(args) == len(input_data.keys())
    for i, k in enumerate(input_data.keys()):
        input_data[k].append(args[i])


def l2_normalize(vecs):
    """l2标准化
    :param vecs: np.ndarray
    """
    norms = (vecs ** 2).sum(axis=1, keepdims=True) ** 0.5
    return vecs / np.clip(norms, 1e-8, np.inf)


def data_count(text_list, level="char"):
    """
    统计一个list的文本的长度
    """
    assert level in ["char", "word", "c", "w"]
    count_list = []
    for text in text_list:
        token_num = len(text.split()) if level[0] == "w" else len(text)
        count_list.append(token_num)
    counter = Counter(count_list)
    high_freq = counter.most_common(1)[0]
    result = {
        "min_length": min(count_list),
        "max_length": max(count_list),
        "ave_length": int(sum(count_list) / len(count_list)),
        "high_freq_length": high_freq[0],
        "high_freq_numbers": high_freq[1],
        "counter": counter
    }
    return result


def exec_shell(cmd):
    """打印并执行命令内容，并支持写入日志文件中
    Args:
        cmd: 执行命令的内容（str）
    Returns:
        status: 执行状态
    """
    print(cmd)
    regex = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}")
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
    while p.poll() is None:
        line = p.stdout.readline().strip().decode()
        if line:
            if re.search(regex, line) is None:
                print(line)
            else:
                print(line)
    status = p.returncode
    if status != 0:
        print(f'exec cmd failed. {cmd}')
    return status


class MultiProcessBase:
    """
    class MT(MultiProcessBase):
        @staticmethod
        def task(inputs):
            return [i ** 8 for i in inputs]
    m=MT().run()
    """

    def __init__(self, data, work_nums=4, batch_size=None, pool_type="t"):
        if batch_size:
            batch_size = batch_size
        else:
            batch_size = math.ceil(len(data) / work_nums)
        self.input_list = cut_list(data, batch_size)  # 每个进程的数据
        if pool_type == "t":
            self.pool = ThreadPoolExecutor(work_nums)
        else:
            self.pool = ProcessPoolExecutor(work_nums)

    @staticmethod
    def task(inputs):
        raise NotImplemented

    def run(self):
        obj_list = []
        for p_id in range(len(self.input_list)):
            r = self.pool.submit(self.task, self.input_list[p_id])
            obj_list.append(r)
        self.pool.shutdown()
        result_list = []
        for obj in obj_list:
            result_list.extend(obj.result())
        return result_list


class MultiThreadBar:
    """
    for i in MultiThreadBar(data, "te"):
        pass
    """

    def __init__(self, iter_data, desc=None):
        if not hasattr(iter_data, "__iter__"):
            raise ValueError("data必须是迭代器")
        self.data = iter_data
        self.length = len(iter_data)
        self.index = 0
        self.start_time = time.time()
        self.cost_time = 0
        self.time_step = 0
        self.last_time = 0
        self.msg = "\r"
        if desc:
            self.msg = self.msg + desc + ": "

    def update_time_step(self):
        self.cost_time = time.time() - self.start_time
        self.time_step = self.cost_time / self.index
        self.last_time = self.time_step * (self.length - self.index)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index != 0:
            self.update_time_step()
            print(f"{self.msg}{self.index} / {self.length - 1}, time: {int(self.cost_time)}s / {int(self.last_time)}s",
                  end="")
        else:
            print(f"{self.msg}{self.index} / {self.length - 1}", end="")
        if self.index == self.length:
            print(f"{self.msg}{self.index - 1} / {self.length - 1}, cost: {int(self.cost_time)}")
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
