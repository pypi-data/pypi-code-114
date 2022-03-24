# -*- coding: utf-8 -*-
import os.path
import random
import time
import traceback
from datetime import datetime
from typing import Optional

import numpy as np
import torch

from yangke.base import execute_function_by_interval, get_settings, execute_function_every_day
from yangke.common.config import logger
import yangke.sis.dll_file as dll_file
from yangke.pytorch.mytorch import DataFitterNet
from ruamel import yaml

models = {}
dbp_api: Optional[dll_file.DllMode] = None

tag_des_write = {
    "N1TC_P_Best_Con": "#1凝汽器最佳真空",
    "N1TC_Way_CirPump_Run": "#1循泵最佳运行台数",
    "N1TC_Way_CoolFan_Run": "#1机力塔风机最佳运行台数",
    "N1TC_Coal_Saving_Run": "#1优化后预计节省标煤量",

    "N2TC_P_Best_Con": "#2凝汽器最佳真空",
    "N2TC_Way_CirPump_Run": "#2循泵最佳运行台数",
    "N2TC_Way_CoolFan_Run": "#2机力塔风机最佳运行台数",
    "NPTC_Coal_Saving_Run": "#2优化后预计节省标煤量",
}


def get_tag_value(snapshot, tag_description):
    try:
        result = float(snapshot[tag_description][0])
    except KeyError:
        logger.warning(f"快照中不包括名为[{tag_description}]的变量，返回None")
        result = None
    return result


tag_des_read = {  # 可读参数，部分也可以写入，但不建议从该程序中写入
    "N1DCS.TCS110RCAOG_B120_01": "#1环境湿度",
    "N1DCS.TCS110RCAOG_B116_01": "#1环境温度",
    "N1DSJ.TCS110GM015ND04_AV": "#1大气压力",
    "N1TS_T_CicWiA": "#1凝汽器进口循环水温度",
    "N1DCS.10PAB11CP101": "#1凝汽器进口循环水压力",
    "N1TS_T_CicWoA": "#1凝汽器出口循环水温度",
    "N1DCS.10PAB21CP101": "#1凝汽器出口循环水压力",
    "N1TS_P_Pex": "#1背压",
    "N1PC_Q_SUPPLHEAT_GJ": "#1供热能量",
    "N1GS_W_G": "#1燃机功率",
    "N1TS_W_G": "#1汽机功率",
    "N1PS_W_G": "#1机组功率",
    "N1TC_DT_CirWater": "#1循环水温升",
    "N1TC_W_CIRPUMP": "#1循泵总功率",
    "N1TC_W_LitaMachineFan": "#1机力塔风机总功率",
    "N1TC_N_HetLoad": "#1凝汽器热负荷",
    "N1TC_TTD_Con": "#1凝汽器端差",
    "N1TC_P_Res_Con": "#1凝汽器汽阻",
    "N1TC_ConWaterSC": "#1凝汽器过冷度",
    "N1TC_Eff_Con": "#1凝汽器效率",
    "N1TC_E_Clear_Con": "#1凝汽器实时清洁度",
    "N1PC_W_Con_Sys": "#1冷端消耗总功率",
    "N1PC_Eff_Unit": "#1联合循环效率",
    "N1PC_RW_PECEle": "#1厂用电率",
    "N1PC_R_FuelExpendGE": "#1供电气耗",

    "N1PC_F_HeatSupply": "#1供热流量",
    "N1DCS.TCS110RCAOG_B009_01": "#1FGH进气压力",
    "N1DCS.TCS110RCAOG_B113_04": "#1FGH进气温度",
    "N1DCS.TCS110RCAOM_D164_01": "#1FGH进水流量",  # 取自Fual Gas Diagram
    "N1DCS.TCS110RCAOM_D454_01": "#1TCA进水流量",  # 取自TCA Cooler
    "N1DCS.10LAE90CFX3": "#1过热减温水流量",
    "N1DCS.10LAF80CF101_CAL": "#1再热减温水流量",

    # "N1DCS.TCS110RCAOG_B120_01": "#2环境湿度",  # 画面上两台机组相同
    "N2DSJ.TCS220GM015ND04_AV": "#2大气压力",
    "N2TS_T_CicWiA": "#2凝汽器进口循环水温度",
    "N2DCS.20PAB11CP101": "#2凝汽器进口循环水压力",  # 画面点号错误
    "N2TS_T_CicWoA": "#2凝汽器出口循环水温度",
    "N2DCS.20PAB21CP101": "#2凝汽器出口循环水压力",  # 画面错误
    "N2DCS.10CJA02EC109": "#2背压",
    "N2PC_Q_SUPPLHEAT_GJ": "#2供热能量",
    "N2GS_W_G": "#2燃机功率",
    "N2TS_W_G": "#2汽机功率",
    "N2PS_W_G": "#2机组功率",
    "N2TC_DT_CirWater": "#2循环水温升",
    "N2TC_W_CIRPUMP": "#2循泵总功率",
    "N2TC_W_LitaMachineFan": "#2机力塔风机总功率",
    "N2TC_N_HetLoad": "#2凝汽器热负荷",
    "N2TC_TTD_Con": "#2凝汽器端差",
    "N2TC_P_Res_Con": "#2凝汽器汽阻",
    "N2TC_ConWaterSC": "#2凝汽器过冷度",
    "N2TC_Eff_Con": "#2凝汽器效率",
    "N2TC_E_Clear_Con": "#2凝汽器实时清洁度",
    "N2PC_W_Con_Sys": "#2冷端消耗总功率",
    "N2PC_Eff_Unit": "#2联合循环效率",
    "N2PC_RW_PECEle": "#2厂用电率",
    "N2PC_R_FuelExpendGE": "#2供电气耗",
    "N2PC_F_HeatSupply": "#2供热流量",
    "N2DCS.TCS220RCAOG_B009_01": "#2FGH进气压力",
    "N2DCS.TCS220RCAOG_B113_04": "#2FGH进气温度",
    "N2DCS.TCS220RCAOM_D164_01": "#2FGH进水流量",  # 取自Fual Gas Diagram
    "N2DCS.TCS220RCAOM_D454_01": "#2TCA进水流量",  # 取自TCA Cooler
    "N2DCS.20LAE90CFX3": "#2过热减温水流量",
    "N2DCS.20LAF80CF101_CAL": "#2再热减温水流量",

    "N1DCS.TCS110RCAOG_B018_02": "#1天然气流量",  # Nm3/h
    "N2DCS.TCS220RCAOG_B018_02": "#2天然气流量",  # Nm3/h

    "N1DCS.AILCA385": "循泵1-A电流",
    "N1DCS.AILCB377": "循泵1-B电流",
    "N1DCS.AILCB385": "循泵1-C电流",
    "N1DCS.AILCA409": "风机1-A电流",
    "N1DCS.AILCA417": "风机1-B电流",
    "N1DCS.AILCB401": "风机1-C电流",
    "N1DCS.AILCB409": "风机1-D电流",
    "N1DCS.AILCB417": "风机1-E电流",
    "N2DCS.AILCA385": "循泵2-A电流",
    "N2DCS.AILCB377": "循泵2-B电流",
    "N2DCS.AILCB385": "循泵2-C电流",
    "N2DCS.AILCA409": "风机2-A电流",
    "N2DCS.AILCA417": "风机2-B电流",
    "N2DCS.AILCB401": "风机2-C电流",
    "N2DCS.AILCB409": "风机2-D电流",
    "N2DCS.AILCB417": "风机2-E电流",
}


def _adjust(result, now, unit_num, better=True):
    if better:
        if result[f"p{unit_num}"] > now[f"p{unit_num}"]:  # 预测背压需小于当前背压
            result[f"p{unit_num}"] = now[f"p{unit_num}"] * 0.99
            if result[f"pump{unit_num}"] == now[f"pump{unit_num}"]:  # 背压预测结果大于运行，但风机还开得多，则需要
                if result[f"fun{unit_num}"] - now[f"fun{unit_num}"] > 1:  # 将背压预测结果修正到小于运行，风机数量
                    result[f"fun{unit_num}"] = now[f"fun{unit_num}"] + 1  # 限制到运行+1

        if result[f"hr{unit_num}"] > now[f"hr{unit_num}"]:
            result[f"hr{unit_num}"] = now[f"hr{unit_num}"] * 0.9975  # 预测热耗要更小
        if result[f"eta{unit_num}"] < now[f"eta{unit_num}"]:
            result[f"eta{unit_num}"] = now[f"eta{unit_num}"] * 1.0025
    else:
        if result[f"p{unit_num}"] < now[f"p{unit_num}"]:  # 预测背压需小于当前背压
            result[f"p{unit_num}"] = now[f"p{unit_num}"] * 1.01
            if result[f"pump{unit_num}"] == now[f"pump{unit_num}"]:
                if now[f"fun{unit_num}"] - result[f"fun{unit_num}"] > 1:
                    result[f"fun{unit_num}"] = now[f"fun{unit_num}"] - 1
        if result[f"hr{unit_num}"] < now[f"hr{unit_num}"]:
            result[f"hr{unit_num}"] = now[f"hr{unit_num}"] * 1.0025  # 预测热耗要更小
        if result[f"eta{unit_num}"] > now[f"eta{unit_num}"]:
            result[f"eta{unit_num}"] = now[f"eta{unit_num}"] * 0.9975


def adjust_result(result, now, unit_num=1):
    if now[f"pump{unit_num}"] == 0 and now[f"fun{unit_num}"] == 0:  # 说明该机停机
        return

    # 如果优化后运行方式等于当前运行方式，则让优化结果=当前结果
    if result[f"pump{unit_num}"] == now[f"pump{unit_num}"] and result[f"fun{unit_num}"] == now[f"fun{unit_num}"]:
        result[f"hr{unit_num}"] = now.get(f"hr{unit_num}")
        result[f"p{unit_num}"] = now.get(f"p{unit_num}")
        result[f"eta{unit_num}"] = now.get(f"eta{unit_num}")

    #
    if result[f"pump{unit_num}"] > now[f"pump{unit_num}"]:
        if result[f"fun{unit_num}"] >= now[f"fun{unit_num}"]:
            _adjust(result, now, unit_num, better=True)
    elif result[f"pump{unit_num}"] < now[f"pump{unit_num}"]:
        if result[f"fun{unit_num}"] <= now[f"fun{unit_num}"]:
            _adjust(result, now, unit_num, False)
    else:
        if result[f"fun{unit_num}"] > now[f"fun{unit_num}"]:
            _adjust(result, now, unit_num, better=True)
        elif result[f"fun{unit_num}"] < now[f"fun{unit_num}"]:
            _adjust(result, now, unit_num, better=False)
        if now[f"fun{unit_num}"] - result[f"fun{unit_num}"] > 1:  # 限制优化结果和实时运行风机台数之差小于2，防止超调
            result[f"fun{unit_num}"] = now[f"fun{unit_num}"] - 1
        if result[f"fun{unit_num}"] - now[f"fun{unit_num}"] > 1:
            result[f"fun{unit_num}"] = now[f"fun{unit_num}"] + 1


def optimize():
    global dbp_api
    try:
        snapshot = dbp_api.get_snapshot(tags=list(tag_des_read.keys()),
                                        tag_description=list(tag_des_read.values()),
                                        need_detail=False)
    except:
        init_dbp_api()
        snapshot = {}

    # print(snapshot.T)
    logger.debug("Start Optimize... 寻优开始")
    天然气热值 = 47748.32  # kJ/kg
    当前运行背压1 = float(get_tag_value(snapshot, "#1背压") or 8)
    当前运行背压2 = float(get_tag_value(snapshot, "#2背压") or 8)

    当前循泵台数1, 当前循泵台数2 = get_循泵运行台数(snapshot)
    当前风机台数1, 当前风机台数2 = get_风机运行台数(snapshot)
    power1 = float(get_tag_value(snapshot, "#1机组功率") or 400)
    power2 = float(get_tag_value(snapshot, "#2机组功率") or 400)
    flow_heat1 = float(get_tag_value(snapshot, "#1供热流量") or 0)
    flow_heat2 = float(get_tag_value(snapshot, "#2供热流量") or 0)
    p_env1 = float(get_tag_value(snapshot, "#1大气压力") or 980) / 10
    p_env2 = float(get_tag_value(snapshot, "#2大气压力") or 980) / 10
    t_env1 = float(get_tag_value(snapshot, "#1环境温度") or 0)
    t_env2 = t_env1
    humid1 = float(get_tag_value(snapshot, "#1环境湿度") or 30) / 100
    humid2 = humid1
    p_gas1 = float(get_tag_value(snapshot, "#1FGH进气压力") or 3.8)
    p_gas2 = float(get_tag_value(snapshot, "#2FGH进气压力") or 3.8)
    t_gas1 = float(get_tag_value(snapshot, "#1FGH进气温度") or 18)
    t_gas2 = float(get_tag_value(snapshot, "#2FGH进气温度") or 18)
    flow_fgh1 = float(get_tag_value(snapshot, "#1FGH进水流量") or 32.3)
    flow_fgh2 = float(get_tag_value(snapshot, "#2FGH进水流量") or 32.3)
    flow_tca1 = float(get_tag_value(snapshot, "#1TCA进水流量") or 115.6)
    flow_tca2 = float(get_tag_value(snapshot, "#2TCA进水流量") or 115.6)
    flow_oh1 = float(get_tag_value(snapshot, "#1过热减温水流量") or 0)
    flow_oh2 = float(get_tag_value(snapshot, "#2过热减温水流量") or 0)
    flow_rh1 = float(get_tag_value(snapshot, "#1再热减温水流量") or 0)
    flow_rh2 = float(get_tag_value(snapshot, "#2再热减温水流量") or 0)
    flow_gas1 = float(get_tag_value(snapshot, "#1天然气流量") or 40000)
    flow_gas2 = float(get_tag_value(snapshot, "#2天然气流量") or 40000)

    # -------------------------- 循环求取最优结果 --------------------------------
    result = {}
    now_state_dict = {}
    hr1_min = hr2_min = 10000
    for pump in [2, 3]:  # 遍历循泵和风机的所有可能组合
        for fun in [2, 3, 4, 5]:
            if 当前循泵台数1 == 0 or 当前风机台数1 == 0:
                eta1, hr1, p1 = 0, 0, 0
            else:
                eta1, hr1, p1 = pred(unit_num=1, power=power1, flow_heat=flow_heat1, p_env=p_env1, t_env=t_env1,
                                     humid=humid1, p_gas=p_gas1, t_gas=t_gas1, flow_fgh=flow_fgh1, flow_tca=flow_tca1,
                                     flow_oh=flow_oh1, flow_rh=flow_rh1, pump=pump, fun=fun)
                eta1, hr1, p1 = eta1.item(), hr1.item(), p1.item()
                hr1 = 3600 / eta1
            if 当前循泵台数2 == 0 or 当前风机台数2 == 0:
                eta2, hr2, p2 = 0, 0, 0
            else:
                eta2, hr2, p2 = pred(unit_num=2, power=power2, flow_heat=flow_heat2, p_env=p_env2, t_env=t_env2,
                                     humid=humid2, p_gas=p_gas2, t_gas=t_gas2, flow_fgh=flow_fgh2, flow_tca=flow_tca2,
                                     flow_oh=flow_oh2, flow_rh=flow_rh2, pump=pump, fun=fun)
                eta2, hr2, p2 = eta2.item(), hr2.item(), p2.item()
                hr2 = 3600 / eta2
            if hr1 < hr1_min:
                hr1_min = hr1
                result.update({"p1": p1, "hr1": hr1, "eta1": eta1, "pump1": pump, "fun1": fun})
            if hr2 < hr2_min:
                hr2_min = hr2
                result.update({"p2": p2, "hr2": hr2, "eta2": eta2, "pump2": pump, "fun2": fun})
            if pump == 当前循泵台数1 and fun == 当前风机台数1:
                flow_gas = flow_gas1 * 0.7192  # kg/h，0.7192是天然气密度
                气耗 = flow_gas / power1  # kg/h/MW = g/kW.h
                煤耗 = get_煤耗(气耗, 天然气热值)  # g/kWh
                eta1_true = power1 * 1000 / 47748.32 / (flow_gas / 3600)  # kW/(kJ/kg*kg/s)
                hr1_true = 3600 / eta1_true
                now_state_dict.update({  # hr和eta的预测值用于显示，真实值用于保存并以后训练
                    "p1": 当前运行背压1, "hr1": hr1, "eta1": eta1, "pump1": pump, "fun1": fun,
                    "coal1": 煤耗, "gas1": 气耗, "eta1_t": eta1_true, "hr1_t": hr1_true
                })
            if pump == 当前循泵台数2 and fun == 当前风机台数2:
                flow_gas = flow_gas2 * 0.7192  # kg/h
                气耗 = flow_gas / power2  # kg/h/MW =g/kW.h
                煤耗 = get_煤耗(气耗, 天然气热值)  # g/kW.h
                eta2_true = power2 * 1000 / 47748.32 / (flow_gas / 3600)
                hr2_true = 3600 / eta2_true
                now_state_dict.update({
                    "p2": 当前运行背压2, "hr2": hr2, "eta2": eta2, "pump2": pump, "fun2": fun,
                    "coal2": 煤耗, "gas2": 气耗, "eta2_t": eta2_true, "hr2_t": hr2_true
                })

    if result["hr1"] == 0:  # 停机状态
        result["pump1"] = result["fun1"] = 0
        气耗1 = 煤耗1 = 0
        now_state_dict["pump1"] = 0
        now_state_dict["fun1"] = 0
        now_state_dict["coal1"] = 0
    if result["hr2"] == 0:  # 停机状态
        result["pump2"] = result["fun2"] = 0
        气耗2 = 煤耗2 = 0
        now_state_dict["pump2"] = 0
        now_state_dict["fun2"] = 0
        now_state_dict["coal2"] = 0
    adjust_result(result, now_state_dict, 1)
    adjust_result(result, now_state_dict, 2)
    if result["hr1"] > 2000:
        气耗1 = get_气耗(result["eta1"], power1, 天然气热值)
        煤耗1 = get_煤耗(气耗1, 天然气热值)
    if result["hr2"] > 2000:
        气耗2 = get_气耗(result["eta2"], power1, 天然气热值)
        煤耗2 = get_煤耗(气耗1, 天然气热值)
    result.update({"coal1": 煤耗1, "gas1": 气耗1, "coal2": 煤耗2, "gas2": 气耗2})

    煤耗降低1 = now_state_dict["coal1"] - result["coal1"]
    煤耗降低2 = now_state_dict["coal2"] - result["coal2"]
    节省煤量1 = 煤耗降低1 * power1  # kg/h
    节省煤量2 = 煤耗降低2 * power2  # kg/h

    if dbp_api is not None:
        ret = dbp_api.write_snapshot_double(tags=list(tag_des_write.keys()),
                                            values=[result["p1"], result["pump1"], result["fun1"], 节省煤量1,
                                                    result["p2"], result["pump2"], result["fun2"], 节省煤量2, ])
    # dbp_api.get_his_value(["N2TC_TTD_Con", "N1TC_DT_CirWater"])


def update_settings(unit_num, file="settings.yml"):
    settings = get_settings(setting_file="settings.yaml")
    paths = settings["output"]["save_path"]
    paths_new = [path.replace(".dat", f"{unit_num}.dat") for path in paths]
    settings["output"]["save_path"] = paths_new
    with open(file, "w") as f:
        yaml.dump(dict(settings), f, Dumper=yaml.RoundTripDumper)


def update_model():
    global models
    from yangke.pytorch.mytorch import re_train
    logger.debug("------------------开始更新模型----------------------")
    # api = init_dbp_api()
    # api.get_his_value("N1GS_W_G")
    # todo 将读入的历史数据写入"D:\lengduan\data\retrain.csv"
    update_settings(unit_num=1, file="settings.yml")  # 将yml文件中模型的路径更改为1号机组的模型，然后训练一遍
    re_train(data_file=r"D:\lengduan\data\retrain1.csv")
    update_settings(unit_num=2, file="settings.yml")
    re_train(data_file=r"D:\lengduan\data\retrain2.csv")
    models = {}  # 将models置为空，则load_model方法会自动重新加载模型
    logger.debug("------------------更新模型结束----------------------")


def run():
    """
    开始持续性任务
    :return:
    """
    global dbp_api
    try:
        init_dbp_api()
        execute_function_by_interval(optimize, minute=0, second=60)  # 每10s执行一次optimize()方法
        execute_function_every_day(update_model, hour=1, minute=0, second=0)
    except:
        time.sleep(10)  # 发生错误后，等待10s再次尝试
        traceback.print_exc()
        run()
    finally:
        ret = dbp_api.dis_connect()
        dbp_api.close()


def load_model(unit_num, para):
    """
    按需加载神经网络模型

    :param unit_num: 以后不同的机组可以有不同的预测模型，目前两台机使用同一个模型
    :param para:
    :return:
    """

    if unit_num not in [1, 2]:
        logger.warning("机组编号错误")
        return None

    if models.get(f"{para}{unit_num}") is not None:
        return models.get(f"{para}{unit_num}")
    else:
        para = {"背压": "p", "循环效率": "eta", "循环热耗率": "hr"}.get(para)  # 写死以加快运行速度
        model_path = f"D:\\lengduan\\data\\model_{para}{unit_num}.dat"
        model = DataFitterNet.load_yk(model_path)
        models[para] = model
        return model


def pred(unit_num, power, flow_heat, p_env, t_env, humid, p_gas,
         t_gas, flow_fgh, flow_tca, flow_oh, flow_rh, pump, fun):
    model1 = load_model(unit_num, "循环效率")
    model2 = load_model(unit_num, "循环热耗率")
    model3 = load_model(unit_num, "背压")
    x = torch.from_numpy(np.array(
        [power, flow_heat, p_env, t_env, humid, p_gas, t_gas, flow_fgh, flow_tca, flow_oh, flow_rh, pump,
         fun])).view(1, 13)
    eta = model1.prediction(x)
    hr = model2.prediction(x)
    p = model3.prediction(x)
    return eta, hr, p


def init_dbp_api():
    global dbp_api
    try:
        dbp_api = dll_file.DllMode("172.22.191.211", "admin", "admin", 12085)
        return dbp_api
    except:
        logger.warning("RDB代理服务器连接失败")
        return None


def get_气耗(eta, power, ncv):
    """
    计算气耗

    :param eta: 循环效率，0~1
    :param power: 功率，MW
    :param ncv: 天然气低位热值，kJ/kg
    :return: g/kW.h
    """
    flow_gas = power * 1000 / eta / ncv  # kg/s
    flow_gas = flow_gas * 3600  # kg/h
    气耗 = flow_gas / power  # kg/h/kW =kg/kW.h
    return 气耗


def get_煤耗(气耗, ncv):
    """

    :param 气耗:
    :param ncv:
    :return: g/kW.h
    """
    # 标煤热值 = 29270  # kJ/kg
    return 气耗 * ncv / 29270  # g/kW.h


def get_循泵运行台数(snapshot):
    a1 = [float(get_tag_value(snapshot, "循泵1-A电流") or 0), float(get_tag_value(snapshot, "循泵1-B电流") or 0),
          float(get_tag_value(snapshot, "循泵1-C电流") or 0)]
    a2 = [float(get_tag_value(snapshot, "循泵2-A电流") or 0), float(get_tag_value(snapshot, "循泵2-B电流") or 0),
          float(get_tag_value(snapshot, "循泵2-C电流") or 0)]
    n1 = sum(i > 5 for i in a1)  # 如果循泵电流>5，认为循泵在运行
    n2 = sum(i > 5 for i in a2)
    return n1, n2


def get_风机运行台数(snapshot):
    a1 = [float(get_tag_value(snapshot, "风机1-A电流") or 0), float(get_tag_value(snapshot, "风机1-B电流") or 0),
          float(get_tag_value(snapshot, "风机1-C电流") or 0), float(get_tag_value(snapshot, "风机1-D电流") or 0),
          float(get_tag_value(snapshot, "风机1-E电流") or 0)]
    a2 = [float(get_tag_value(snapshot, "风机2-A电流") or 0), float(get_tag_value(snapshot, "风机2-B电流") or 0),
          float(get_tag_value(snapshot, "风机2-C电流") or 0), float(get_tag_value(snapshot, "风机2-D电流") or 0),
          float(get_tag_value(snapshot, "风机2-E电流") or 0)]
    n1 = sum(i > 5 for i in a1)
    n2 = sum(i > 5 for i in a2)
    return n1, n2


if __name__ == "__main__":
    run()
