import copy
import random
from collections import OrderedDict
from typing import Optional

import numpy as np
import optuna
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from torch.utils.tensorboard import SummaryWriter

from yangke.base import get_settings, YkDict
from yangke.common.config import logger
from yangke.common.fileOperate import read_csv_ex
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


class DataSetFitting(Dataset):
    def __init__(self, data_source, x_title=None, y_title=None):
        """
        构建数据集

        :param data_source: 数据源，可以为settings.yaml文件配置，也可以是pd.DataFrame对象
        :param x_title: 输入参数的列标题，如果从配置文件加载，则可以为None
        :param y_title: 输出参数的列标题，如果从配置文件加载，则可以为None
        """
        self.dataframe = None
        if isinstance(data_source, pd.DataFrame):
            self.dataframe = data_source
            self.x_title = x_title or []
            self.y_title = y_title or []
        elif isinstance(data_source, YkDict):
            files = data_source.get_settings("dataset.data_file")
            self.x_title = data_source.get("input")
            self.y_title = data_source.get_settings("output.para")
            for file in files:
                ext = file.get("type")
                filename = file.get("name")
                if ext == "csv":
                    data_frame = read_csv_ex(filename)
                else:
                    data_frame = pd.read_excel(filename)
                if self.dataframe is not None and data_frame is not None:
                    self.dataframe = pd.concat([self.dataframe, data_frame], axis=0, ignore_index=True)
                else:
                    self.dataframe = self.dataframe or data_frame

            # 删除某些行
            self.drop_by_condition(data_source.get_settings("dataset.drop"))

        # 仅保留x,y相关的数据列，删除其他列
        titles = self.x_title.copy()
        titles.extend(self.y_title)
        self.dataframe = self.dataframe[titles]

        # 数据标准化
        self.mean = self.dataframe.mean()
        self.std = self.dataframe.std()
        self.dataframe_std = self.standard(self.dataframe)
        # self.dataframe_std[self.y_title] = self.dataframe[self.y_title]

    def set_standard(self, mean, std):
        """
        设置数据的归一化参数，在初始化部分数据时，直接从部分数据集得到的归一化参数可能出现偏差，这里提供一种外部设置的方法

        :param mean:
        :param std:
        :return:
        """
        self.mean = mean
        self.std = std
        self.dataframe_std = self.standard(self.dataframe)

    def standard(self, df):
        """
        数据标准化

        :param df: Dataframe(num, input_and_output_dim)
        :return:
        """
        # Dataframe和Series运算的前提是：Dataframe的列标题和Series的索引名必须一一对应，而不仅仅看维度，否则可能会出错，
        return (df - self.mean) / self.std  # mean Series (input_and_output_dim,)

    def standard_reverse(self, out):
        """
        将预测结果反标准化

        :param out:
        :return:
        """
        return out * self.std[self.y_title] + self.mean[self.y_title]

    def __getitem__(self, index):
        """
        DataSet子类必须实现的方法，用于根据索引返回一条数据，数据类型需要是Tensor

        :param index:
        :return:
        """
        single_item = self.dataframe_std.iloc[index, :]
        x = torch.from_numpy(single_item[self.x_title].to_numpy()).to(torch.float32)
        y = torch.from_numpy(single_item[self.y_title].to_numpy()).to(torch.float32)
        return x, y

    def __len__(self):
        """
        DataSet子类必须实现的方法，用于获取DataSet的大小

        :return:
        """
        return self.dataframe.shape[0]

    def get_size(self):
        return self.dataframe.shape[0]

    def drop_by_condition(self, conditions):
        for cond in conditions:
            if list(cond.keys())[0] == "or":
                for co in cond.get("or"):
                    if "<=" in co:
                        title, value = tuple(co.split("<="))
                        title = str(title).strip()
                        value = float(value)
                        self.dataframe = self.dataframe[self.dataframe[title] > value]  # 删除小于的行 = 保留大于的行
                    elif ">=" in co:
                        title, value = tuple(co.split(">="))
                        title = str(title).strip()
                        value = float(value)
                        self.dataframe = self.dataframe[self.dataframe[title] < value]  # 删除小于的行 = 保留大于的行
                    elif "<" in co:
                        title, value = tuple(co.split("<"))
                        title = str(title).strip()
                        value = float(value)
                        self.dataframe = self.dataframe[self.dataframe[title] >= value]  # 删除小于的行 = 保留大于的行
                    elif ">" in co:
                        title, value = tuple(co.split(">"))
                        title = str(title).strip()
                        value = float(value)
                        self.dataframe = self.dataframe[self.dataframe[title] <= value]  # 删除大于的行 = 保留小于的行

    def split_set(self, 比例1, 比例2=None, 比例3=None):
        """
        按照指定的比例将数据集分割，一般用于将总体数据集分割为训练集，测试集，验证集等

        :param 比例1:
        :param 比例2:
        :param 比例3:
        :return:
        """
        if 比例3 is not None:
            assert 比例1 + 比例2 + 比例3 == 1, "数据集比例之和不为1"
            size = self.get_size()
            size1, size2 = int(比例1 * size), int(比例2 * size)
            set1, set2, set3 = torch.utils.data.random_split(self, [size1, size2, size - size1 - size2])
            return set1, set2, set3
        elif 比例2 is not None:
            if 比例1 + 比例2 < 1:
                return self.split_set(比例1, 比例2, 1 - 比例1 - 比例2)
            else:
                size = self.get_size()
                size1 = int(比例1 * size)
                return torch.utils.data.random_split(self, [size1, size - size1])
        else:
            size = self.get_size()
            size1 = int(比例1 * size)
            return torch.utils.data.random_split(self, [size1, size - size1])


class DataFitterNet(torch.nn.Module):
    def __init__(self, settings, trial=None):
        """
        一个用于数据拟合的神经网络类库，神经网络架构通过settings.yaml文件进行配置

        :param settings:
        :param trial: 使用optuna超参数调优时会传入该参数
        """
        super(DataFitterNet, self).__init__()
        cfg = settings.get("networks")  # 获取神经网络结构信息
        self.settings = settings
        self.trial = trial
        self.cfg = cfg
        self.in_num = 0  # 输入层神经元个数，对应输入参数的个数
        self.out_num = 1
        train_settings = settings.get_settings("networks.train") or {}
        self.lr = float(train_settings.get("learning_rate") or 1e-3)
        self.epochs = int(train_settings.get("epochs") or 10)
        self.batch_size = int(train_settings.get("batch_size") or 64)
        if settings.get_settings("networks.loss_fn.type") == "MSE":
            self.loss_fn = nn.MSELoss(reduction="mean")
        elif settings.get_settings("networks.loss_fn.type").lower() == "max":
            from yangke.stock.prediction.pytorch_pred_stock import MAXLoss
            self.loss_fn = MAXLoss()
        else:
            self.loss_fn = nn.CrossEntropyLoss()
        self.mean: Optional[pd.Series] = None
        self.std: Optional[pd.Series] = None
        self.x_title = []
        self.y_title = []
        self.max_err = 0
        self.average_err = 0

        _cell_num_last_layer = 0  # 循环中记录上一层神经网络的输出个数
        i = 1
        layer_dict = OrderedDict()
        for layer in cfg.get("layers"):  # 从配置中拿到神经网络各层的信息，进而构建神经网络
            _type = layer.get("type")
            _cell_num = 1
            if _type == "input":  # 输入/输出层的神经元个数可以根据输入/输出参数个数自动确定
                _cell_num = layer.get("cell_num") or 10
                if layer.get("cell_num") == "auto" or layer.get("cell_num") is None:
                    self.in_num = len(settings.get("input"))
                    _cell_num = self.in_num
                else:
                    self.in_num = int(layer.get("cell_num") or 10)
                    _cell_num = self.in_num
            elif _type == "linear":
                bias = layer.get("bias") or True
                _cell_num = self.get_para_of_optuna_str(layer.get("cell_num") or 10, f"cell_num{i}")
                layer_dict[f"layer{i}"] = nn.Linear(_cell_num_last_layer, _cell_num, bias=bias)
            elif _type == "relu":
                layer_dict[f"layer{i}"] = nn.ReLU()
                _cell_num = _cell_num_last_layer  # 激活函数输入输出个数不变
            # elif _type == 'softmax':
            #     self.layers.append(nn.Softmax())
            elif _type == "sigmoid":
                layer_dict[f"layer{i}"] = nn.Sigmoid()
                _cell_num = _cell_num_last_layer
            elif _type == "dropout":
                p = self.get_para_of_optuna_str(layer.get('rate'), "dropout_rate")
                layer_dict[f"layer{i}"] = nn.Dropout(p=p)
                _cell_num = _cell_num_last_layer
            elif _type == "output":  # 输入/输出层的神经元个数可以根据输入/输出参数个数自动确定
                if settings.get_settings("output.type") == "single_output":
                    if layer.get("cell_num") != "auto" and int(layer.get("cell_num")) != 1:
                        logger.warning("数据集使用single_output，但神经网络模型输出层单元个数不为1，忽略神经网络输出单元个数设置！")
                    self.out_num = 1
                elif layer.get("cell_num") == "auto" or layer.get("cell_num") is None:
                    self.out_num = len(settings.get("output"))
                else:
                    self.out_num = layer.get("cell_num")
                bias = layer.get("bias") or True
                layer_dict[f"layer{i}"] = nn.Linear(_cell_num_last_layer, self.out_num, bias=bias)

            _cell_num_last_layer = _cell_num
            i = i + 1

        self.net = nn.Sequential(layer_dict)
        weight_decay = self.get_para_of_optuna_str(settings.get_settings("networks.optimizer.weight_decay") or 0,
                                                   "weight_decay")
        if settings.get_settings("networks.optimizer.type") == "adam":
            self.optimizer = torch.optim.Adam(self.parameters(), lr=self.lr, weight_decay=weight_decay)
        else:
            self.optimizer = torch.optim.SGD(self.parameters(), lr=self.lr, weight_decay=weight_decay)

    def forward(self, x):
        out = self.net(x)
        return out

    def set_standard(self, mean, std, x_title, y_title):
        self.mean = mean
        self.std = std
        self.x_title = x_title
        self.y_title = y_title

    def standard_reverse(self, tensor, flag="y"):
        """
        将预测结果反标准化

        :param tensor: 反标准化的数据
        :param flag: 反标准化的变量类型，x表示对输入变量进行反标准换，y表示对输出变量
        :return:
        """
        if len(self.y_title) != 1:
            logger.error("暂不支持输出变量个数大于1的神经网络")
        if flag == "x":
            para = tensor.cpu().data.numpy()  # 必须加.data，否则在需要求导的Tensor上直接调用numpy()方法会出错
            std = self.std[self.x_title].to_numpy()
            mean = self.mean[self.x_title].to_numpy()
        elif flag == "y":
            para = tensor.cpu().data.numpy()
            std = self.std[self.y_title].to_numpy()
            mean = self.mean[self.y_title].to_numpy()
        else:  # "all"包括x和y
            para = tensor.cpu().data.numpy()
            std = self.std.to_numpy()
            mean = self.mean.to_numpy()
        result = para * std + mean
        result = torch.from_numpy(result)
        return result

    def prediction(self, x):
        """
        预测指定输入参数

        :param x: x.shape = torch.Size([batch_size, input_dim])
        :return:
        """
        mean = torch.from_numpy(self.mean[self.x_title].to_numpy())
        std = torch.from_numpy(self.std[self.x_title].to_numpy())
        x = (x - mean) / std  # 输入数据归一化
        x = x.to(torch.float32)
        self.eval()
        y = self.net(x)
        return self.standard_reverse(y)

    def save_yk(self, path):
        checkpoint = {
            'mean'                : self.mean,
            'std'                 : self.std,
            'x_title'             : self.x_title,
            'y_title'             : self.y_title,
            'model_state_dict'    : self.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict(),
            'max_err'             : self.max_err,
            'average_err'         : self.average_err,
            'settings'            : self.settings
        }
        torch.save(checkpoint, path)

    @staticmethod
    def load_yk(path):
        checkpoint = torch.load(path)
        model = DataFitterNet(checkpoint.get("settings"))
        model.set_standard(checkpoint['mean'], checkpoint['std'], checkpoint['x_title'], checkpoint['y_title'])
        model.max_err = checkpoint['max_err']
        model.average_err = checkpoint['average_err']
        model.load_state_dict(checkpoint['model_state_dict'])
        model.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        return model

    def __str__(self):
        str1 = super(DataFitterNet, self).__str__()
        return str1[:-1] + "  (Optimizer): " + self.optimizer.__str__().replace("\n", "\n  ", 1).replace("\n",
                                                                                                         "\n  ") + "\n)"

    def device(self):
        return next(self.parameters()).device

    def train_loop(self, data_loader):
        size = len(data_loader.dataset)
        self.train()
        loss = 0
        is_tqdm = self.settings.get_settings("print.tqdm")
        if is_tqdm:
            from tqdm import tqdm
            pbar = tqdm(data_loader)
        else:
            pbar = data_loader
            pbar.set_set_description = print
        for batch, (x, y) in enumerate(pbar):
            x = x.to(self.device())
            y = y.to(self.device())
            pred = self.net(x)
            loss = self.loss_fn(pred, y)
            self.optimizer.zero_grad()  # 每一次训练梯度要清零
            loss.backward()
            self.optimizer.step()

            if batch % 10 == 0:
                loss, current = loss.item(), batch * len(x)
                pbar.set_description(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}-{self.y_title}]")

        return loss

    def test_loop(self, data_loader):
        num_batches = len(data_loader)
        size = len(data_loader.dataset)
        test_loss = 0
        self.eval()
        relative_err = 0
        max_err = 0
        with torch.no_grad():
            for x, y in data_loader:
                x = x.to(self.device())
                y = y.to(self.device())
                pred = self.net(x)
                test_loss += self.loss_fn(pred, y).item()
                pred = self.standard_reverse(pred)
                y = self.standard_reverse(y)
                # max_err = max(max_err, (abs(pred-y)/abs(y)).max(0))  # tensor.max()返回最大值,tensor.max(0)返回最大值和索引
                max_err = max(max_err, (abs(pred - y) / abs(y)).max())
                relative_err = ((pred - y).abs() / y.abs()).sum() + relative_err

        test_loss /= num_batches
        relative_err = relative_err / size
        logger.debug(f"测试集预测结果({self.y_title[0]}): 平均损失为{test_loss:>8f}")
        return relative_err, max_err

    def start_train(self, train_dataloader, test_dataloader, writer=None):
        """
        开始模型训练
        :param train_dataloader:
        :param test_dataloader:
        :param writer: tensorboard的记录器
        :return:
        """
        relative_err = []  # 预测结果的相对误差
        if writer is None:
            writer = SummaryWriter(f'./runs/{self.y_title[0]}')  # 可视化数据存放在这个文件夹
        writer.add_graph(self, torch.rand([1, self.in_num], device=self.device()))
        for t in range(self.epochs):
            print(f"-------------------------Epoch {t + 1}-------------------------------")
            train_loss = self.train_loop(train_dataloader)
            current_err, max_err = self.test_loop(test_dataloader)
            relative_err.append(current_err)
            logger.debug(f"最大相对误差为{max_err.item():>8f}，平均相对误差为：{current_err:>8f}")
            # ------------------------- 损失曲线图 ---------------------------------
            writer.add_scalar('train/损失', train_loss, t)
            writer.add_scalar('test/平均误差', current_err, t)
            writer.add_scalar('test/最大误差', max_err, t)
            # ------------------------- 损失曲线图 ---------------------------------
            # ------------------------- 权重直方图 ---------------------------------
            for i, (name, param) in enumerate(self.named_parameters()):
                if 'bn' not in name:
                    writer.add_histogram(name + "_data", param, t)
                    writer.add_histogram(name + "_grad", param.grad, t)
            # ------------------------- 权重直方图 ---------------------------------
            try:
                if current_err < 0.01 and max_err < 0.01 and t >= 10:
                    self.max_err = max_err
                    self.average_err = current_err
                    break
            except IndexError:  # 当relative_err列表长度小于3时，会报IndexError错误，此处忽略错误继续训练
                pass
            self.max_err = max_err
            self.average_err = current_err
            if self.trial is not None:
                self.trial.report(self.average_err, t)
                if self.trial.should_prune():
                    raise optuna.TrialPruned
        logger.debug(f"测试集预测结果的相对误差随epoch的变化为：{[x.item() for x in relative_err]}")
        writer.close()
        return self.average_err

    def get_para_type(self, p):
        if isinstance(p, list):
            result = "int"
            for p_ in p:
                if self.get_para_type(p_) == "float":
                    result = "float"
                elif self.get_para_type(p_) == "str":
                    result = "str"
            return result
        else:
            if str(p).isnumeric():  # 小数的isnumeric()方法返回的是false
                return "int"
            else:
                try:
                    _ = eval(p)
                    return "float"
                except NameError:
                    return "str"

    def get_para_of_optuna_str(self, string, name):
        result = 0
        if str(string).startswith("optuna"):
            p1 = string.replace("optuna(", "").replace(")", "")
            p_list = p1.split(",")
            type1 = self.get_para_type(p_list)
            if type1 == "float":
                step = None if len(p_list) == 2 else float(p_list[2])
                result = self.trial.suggest_float(name, float(p_list[0]), float(p_list[1]), step=step)
            elif type1 == "int":
                step = None if len(p_list) == 2 else int(p_list[2])
                result = self.trial.suggest_int(name, int(p_list[0]), int(p_list[1]), step=step)
        else:
            result = string
        return result


class OptunaModel:
    def __init__(self, settings):
        self.settings = copy.deepcopy(settings)
        self.settings["networks"] = copy.deepcopy(settings.get_settings("optuna.networks"))
        self.n_trials = int(settings.get_settings("optuna.networks.n_trials") or 10)
        self.device = 'cpu'
        self.mean = None
        self.std = None
        self.x_title = None
        self.y_title = None
        self.train_loader = None
        self.test_loader = None

    def optimize(self):
        study_name = "model_study3"
        study = optuna.create_study(study_name=study_name, direction="minimize",
                                    storage=f'sqlite:///{study_name}.db', load_if_exists=True)
        study.optimize(self.objective, n_trials=self.n_trials)
        trial = study.best_trial
        logger.debug(f"最优模型的损失为{trial.value}")
        logger.debug(f"最优模型的参数为{trial.params}")
        df = study.trials_dataframe()
        print(df)
        self.visualization(study_name)

    @staticmethod
    def visualization(study_name):
        study = optuna.create_study(study_name=study_name, direction="minimize",
                                    storage='sqlite:///example.db', load_if_exists=True)
        optuna.visualization.plot_contour(study).show()
        optuna.visualization.plot_optimization_history(study).show()
        optuna.visualization.plot_param_importances(study).show()

    def start_train(self, train_loader, test_loader):
        self.train_loader = train_loader
        self.test_loader = test_loader
        return self.optimize()

    def objective(self, trial):
        model = DataFitterNet(self.settings, trial).to(self.device)
        model.set_standard(self.mean, self.std, self.x_title, self.y_title)
        logger.debug("try model:")
        print(model)
        loss = model.start_train(self.train_loader, self.test_loader)
        return loss

    def to(self, device):
        self.device = device
        return self

    def set_standard(self, mean, std, x_title, y_title):
        self.mean = mean
        self.std = std
        self.x_title = x_title
        self.y_title = y_title


def train_model():
    """
    按照settings.yaml文件训练神经网络模型，并保存到settings.yaml指定的位置

    如果settings.networks没有定义具体的网络模型，但是settings.optuna.networks中定义了网络模型的寻优空间参数，则会自动使用
    Optuna库对模型超参数进行寻优，并将寻优结果得到的最有网络模型定义写入settings.yml文件中。再次调用该方法，则会使用寻优得到的
    网络模型架构进行数据拟合，将模型权值信息写入settings.output.save_path指定的路径中。

    如果settings.networks定义了具体的网络模型，则该方法只对定义的模型进行训练，将训练后的权值信息写入settings.output.save_path
    指定的路径中。

    如果该方法同时训练多个单输出模型，则模型架构的优化只会进行一次，即第一个模型架构的优化结果会应用于后续的多个单输出数据拟合任务。

    :return:
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    logger.info(f"使用{device}进行计算")
    settings = get_settings()
    if settings.get("networks") is not None:  # 如果存在networks的定义就直接使用该定义
        optimize_model = False
    elif settings.get("optuna") is not None:  # 如果存在optuna的设置，就使用该设置获取最有网络模型定义
        optimize_model = True
    else:
        logger.error("未找到模型设置信息，请确认！")
        return
    _settings_ = copy.deepcopy(settings)
    output = _settings_.get("output") or {}
    if output.get("type") == "single_output":
        paras = copy.deepcopy(output.get("para") or {})
        for i, para in enumerate(paras):
            output["para"] = [para]
            output["save_path"] = settings.get_settings("output.save_path")[i]
            model = OptunaModel(_settings_).to(device) if optimize_model else DataFitterNet(_settings_).to(device)
            print(model)
            dataset_all = DataSetFitting(_settings_)  # 获取所有的数据集
            model.set_standard(dataset_all.mean, dataset_all.std, dataset_all.x_title, dataset_all.y_title)
            part1 = float(_settings_.get_settings("dataset.data_training.proportion"))
            part2 = float(_settings_.get_settings("dataset.data_test.proportion"))
            train_set, test_set = dataset_all.split_set(part1, part2)  # 均已是归一化后的数据
            net_settings = _settings_.get_settings("optuna.networks") if optimize_model else _settings_.get("networks")
            batch_size = int(net_settings.get_settings("train.batch_size"))
            train_loader = DataLoader(dataset=train_set, batch_size=batch_size, shuffle=True)
            test_loader = DataLoader(dataset=test_set, batch_size=batch_size, shuffle=True)
            model.start_train(train_loader, test_loader)
            if not optimize_model:
                model.save_yk(output["save_path"])
            else:
                model.update_settings_file("settings.yml")
                train_model()
    # from yangke.core import runCMD
    # runCMD(f"tensorboard --logdir=runs/{para}")


def re_train(data_file):
    """
    在现有模型基础上再次训练

    :param data_file: 数据文件,csv文件
    :return:
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    logger.info(f"使用{device}再次训练")
    settings = get_settings()
    _settings_ = copy.deepcopy(settings)
    _settings_["dataset"]["data_file"] = data_file
    output = _settings_.get("output") or {}
    if output.get("type") == "single_output":
        paras = copy.deepcopy(output.get("para") or {})
        for i, para in enumerate(paras):
            output["para"] = [para]
            output["save_path"] = settings.get_settings("output.save_path")[i]
            model = DataFitterNet.load_yk(output["save_path"])
            print(model)
            dataset_all = DataSetFitting(_settings_)  # 获取所有的数据集
            dataset_all.set_standard(model.mean, model.std)
            part1 = _settings_.get_settings("dataset.data_training.proportion")
            part2 = _settings_.get_settings("dataset.data_test.proportion")
            train_set, test_set = dataset_all.split_set(part1, part2)  # 均已是归一化后的数据
            batch_size = _settings_.get_settings("networks.train.batch_size")
            train_loader = DataLoader(dataset=train_set, batch_size=batch_size, shuffle=True)
            test_loader = DataLoader(dataset=test_set, batch_size=batch_size, shuffle=True)
            model.start_train(train_loader, test_loader)

            model.save_yk(output["save_path"])


def setup_seed(seed=10):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)


if __name__ == "__main__":
    setup_seed()
    train_model()

"""
1. 同样的神经网络模型，使用MSELoss作为损失函数比MaxLoss做损失函数结果要好，例如：
使用MaxLoss，最大误差为0.376，平均误差为0.060
使用MSELoss，最大误差为0.302，平均误差为0.045    0.159 0.393
30个epoch
layers:
    - type: input  # 输入层
      cell_num: auto
    - type: linear  # 隐藏层
      cell_num: 30
      bias: True
    - type: sigmoid
    - type: linear  # 隐藏层
      cell_num: 128
      bias: True
    - type: dropout
      rate: 0.1
    - type: sigmoid
    - type: output  # 输出层
      cell_num: auto
"""
