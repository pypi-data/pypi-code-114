# -*- coding: utf-8 -*-
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
from yangke.pytorch.mytorch import DataFitterNet, train_model

models = {}
dbp_api: Optional[dll_file.DllMode] = None

tag_des_write = {
    "N1TC_P_Best_Con"     : "#1凝汽器最佳真空",
    "N1TC_Way_CirPump_Run": "#1循泵最佳运行台数",
    "N1TC_Way_CoolFan_Run": "#1机力塔风机最佳运行台数",
    "N1TC_Coal_Saving_Run": "#1优化后预计节省标煤量",

    "N2TC_P_Best_Con"     : "#2凝汽器最佳真空",
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
    "N1DSJ.TCS110GM015ND04_AV" : "#1大气压力",
    "N1TS_T_CicWiA"            : "#1凝汽器进口循环水温度",
    "N1DCS.10PAB11CP101"       : "#1凝汽器进口循环水压力",
    "N1TS_T_CicWoA"            : "#1凝汽器出口循环水温度",
    "N1DCS.10PAB21CP101"       : "#1凝汽器出口循环水压力",
    "N1TS_P_Pex"               : "#1背压",
    "N1PC_Q_SUPPLHEAT_GJ"      : "#1供热能量",
    "N1GS_W_G"                 : "#1燃机功率",
    "N1TS_W_G"                 : "#1汽机功率",
    "N1PS_W_G"                 : "#1机组功率",
    "N1TC_DT_CirWater"         : "#1循环水温升",
    "N1TC_W_CIRPUMP"           : "#1循泵总功率",
    "N1TC_W_LitaMachineFan"    : "#1机力塔风机总功率",
    "N1TC_N_HetLoad"           : "#1凝汽器热负荷",
    "N1TC_TTD_Con"             : "#1凝汽器端差",
    "N1TC_P_Res_Con"           : "#1凝汽器汽阻",
    "N1TC_ConWaterSC"          : "#1凝汽器过冷度",
    "N1TC_Eff_Con"             : "#1凝汽器效率",
    "N1TC_E_Clear_Con"         : "#1凝汽器实时清洁度",
    "N1PC_W_Con_Sys"           : "#1冷端消耗总功率",
    "N1PC_Eff_Unit"            : "#1联合循环效率",
    "N1PC_RW_PECEle"           : "#1厂用电率",
    "N1PC_R_FuelExpendGE"      : "#1供电气耗",
    # "": "#1供热流量",
    # "": "#1FGH进气压力",
    # "": "#1FGH进气温度",
    # "": "#1FGH进水流量",
    # "": "#1TCA进水流量",
    # "": "#1过热减温水流量",
    # "": "#1再热减温水流量",

    # "N1DCS.TCS110RCAOG_B120_01": "#2环境湿度",  # 画面上两台机组相同
    "N2DSJ.TCS220GM015ND04_AV" : "#2大气压力",
    "N2TS_T_CicWiA"            : "#2凝汽器进口循环水温度",
    "N2DCS.20PAB11CP101"       : "#2凝汽器进口循环水压力",  # 画面点号错误
    "N2TS_T_CicWoA"            : "#2凝汽器出口循环水温度",
    "N2DCS.20PAB21CP101"       : "#2凝汽器出口循环水压力",  # 画面错误
    "N2DCS.10CJA02EC109"       : "#2背压",
    "N2PC_Q_SUPPLHEAT_GJ"      : "#2供热能量",
    "N2GS_W_G"                 : "#2燃机功率",
    "N2TS_W_G"                 : "#2汽机功率",
    "N2PS_W_G"                 : "#2机组功率",
    "N2TC_DT_CirWater"         : "#2循环水温升",
    "N2TC_W_CIRPUMP"           : "#2循泵总功率",
    "N2TC_W_LitaMachineFan"    : "#2机力塔风机总功率",
    "N2TC_N_HetLoad"           : "#2凝汽器热负荷",
    "N2TC_TTD_Con"             : "#2凝汽器端差",
    "N2TC_P_Res_Con"           : "#2凝汽器汽阻",
    "N2TC_ConWaterSC"          : "#2凝汽器过冷度",
    "N2TC_Eff_Con"             : "#2凝汽器效率",
    "N2TC_E_Clear_Con"         : "#2凝汽器实时清洁度",
    "N2PC_W_Con_Sys"           : "#2冷端消耗总功率",
    "N2PC_Eff_Unit"            : "#2联合循环效率",
    "N2PC_RW_PECEle"           : "#2厂用电率",
    "N2DCS.TCS220RCAOG_B018_02": "#2燃气体积流量",  # Nm3/h
    "N2PC_R_FuelExpendGE"      : "#2供电气耗",
    # "": "#2供热流量",
}


def load_model(机组编号, para):
    """
    按需加载神经网络模型

    :param 机组编号: 以后不同的机组可以有不同的预测模型，目前两台机使用同一个模型
    :param para:
    :return:
    """
    if 机组编号 not in [1, 2]:
        logger.warning("机组编号错误")
        return None
    if models.get(para) is not None:
        return models.get(para)
    else:
        output = get_settings("output")
        zip_dict = dict(zip(output.get("para"), output.get("save_path")))
        model_path = zip_dict.get(para)
        model = DataFitterNet.load_yk(model_path)
        models[para] = model
        return model


def pred(机组编号, power, flow_heat, p_env, t_env, humid, p_gas,
         t_gas, flow_fgh, flow_tca, flow_oh, flow_rh, pump, fun):
    model1 = load_model(机组编号, "循环效率")
    model2 = load_model(机组编号, "循环热耗率")
    model3 = load_model(机组编号, "背压")
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
    天然气热值 = 47748.32  # kJ/kg
    当前运行背压1 = float(get_tag_value(snapshot, "#1背压") or 8)
    当前运行背压2 = float(get_tag_value(snapshot, "#2背压") or 8)
    当前循泵台数1 = float(get_tag_value(snapshot, "#1循泵台数") or 3)
    当前循泵台数2 = float(get_tag_value(snapshot, "#2循泵台数") or 3)
    当前风机台数1 = float(get_tag_value(snapshot, "#1风机台数") or 5)
    当前风机台数2 = float(get_tag_value(snapshot, "#2风机台数") or 5)
    power1 = float(get_tag_value(snapshot, "#1机组功率") or 400)
    power2 = float(get_tag_value(snapshot, "#2机组功率") or 400)
    flow_heat1 = float(get_tag_value(snapshot, "#1供热流量") or 0)
    flow_heat2 = float(get_tag_value(snapshot, "#2供热流量") or 0)
    p_env1 = float(get_tag_value(snapshot, "#1大气压力") or 98)
    p_env2 = float(get_tag_value(snapshot, "#2大气压力") or 98)
    t_env1 = float(get_tag_value(snapshot, "#1环境温度") or 0)
    t_env2 = float(get_tag_value(snapshot, "#1环境温度") or 0)
    humid1 = float(get_tag_value(snapshot, "#1环境湿度") or 0.3)
    humid2 = float(get_tag_value(snapshot, "#1环境湿度") or 0.3)
    p_gas1 = float(get_tag_value(snapshot, "#1FGH进气压力") or 3.8)
    p_gas2 = float(get_tag_value(snapshot, "#2FGH进气压力") or 3.8)
    t_gas1 = float(get_tag_value(snapshot, "#1FGH进气温度") or 18)
    t_gas2 = float(get_tag_value(snapshot, "#2FGH进气压力") or 18)
    flow_fgh1 = float(get_tag_value(snapshot, "#1FGH进水流量") or 32.3)
    flow_fgh2 = float(get_tag_value(snapshot, "#2FGH进水流量") or 32.3)
    flow_tca1 = float(get_tag_value(snapshot, "#1TCA进水流量") or 115.6)
    flow_tca2 = float(get_tag_value(snapshot, "#2TCA进水流量") or 115.6)
    flow_oh1 = float(get_tag_value(snapshot, "#1过热减温水流量") or 0)
    flow_oh2 = float(get_tag_value(snapshot, "#2过热减温水流量") or 0)
    flow_rh1 = float(get_tag_value(snapshot, "#1再热减温水流量") or 0)
    flow_rh2 = float(get_tag_value(snapshot, "#2再热减温水流量") or 0)

    result = {}
    now_state_dict = {}
    hr1_min = hr2_min = 10000
    for pump in [2, 3]:
        for fun in [3, 4, 5]:
            eta1, hr1, p1 = pred(机组编号=1, power=power1, flow_heat=flow_heat1, p_env=p_env1, t_env=t_env1, humid=humid1,
                                 p_gas=p_gas1, t_gas=t_gas1, flow_fgh=flow_fgh1, flow_tca=flow_tca1, flow_oh=flow_oh1,
                                 flow_rh=flow_rh1, pump=pump, fun=fun)
            eta2, hr2, p2 = pred(机组编号=2, power=power2, flow_heat=flow_heat2, p_env=p_env2, t_env=t_env2, humid=humid2,
                                 p_gas=p_gas2, t_gas=t_gas2, flow_fgh=flow_fgh2, flow_tca=flow_tca2, flow_oh=flow_oh2,
                                 flow_rh=flow_rh2, pump=pump, fun=fun)
            eta1, hr1, p1 = eta1.item(), hr1.item(), p1.item()
            eta2, hr2, p2 = eta2.item(), hr2.item(), p2.item()
            if hr1 < hr1_min:
                hr1_min = hr1
                气耗 = get_气耗(eta1, power1, 天然气热值)
                煤耗 = get_煤耗(气耗, 天然气热值)
                result.update({"p1"   : p1, "hr1": hr1, "eta1": eta1, "pump1": pump, "fun1": fun,
                               "coal1": 煤耗, "gas1": 气耗})
            if hr2 < hr2_min:
                hr2_min = hr2
                气耗 = get_气耗(eta2, power2, 天然气热值)
                煤耗 = get_煤耗(气耗, 天然气热值)
                result.update({"p2"   : p2, "hr2": hr2, "eta2": eta2, "pump2": pump, "fun2": fun,
                               "coal2": 煤耗, "gas2": 气耗})
            if pump == 当前循泵台数1 and fun == 当前风机台数1:
                气耗 = get_气耗(eta1, power1, 天然气热值)
                煤耗 = get_煤耗(气耗, 天然气热值)
                now_state_dict.update({
                    "p1"   : p1, "hr1": hr1, "eta2": eta1, "pump1": pump, "fun1": fun,
                    "coal1": 煤耗, "gas1": 气耗
                })
            if pump == 当前循泵台数2 and fun == 当前风机台数2:
                气耗 = get_气耗(eta2, power2, 天然气热值)
                煤耗 = get_煤耗(气耗, 天然气热值)
                now_state_dict.update({
                    "p2"   : p2, "hr2": hr2, "eta2": eta2, "pump2": pump, "fun2": fun,
                    "coal2": 煤耗, "gas2": 气耗
                })

    节省煤量1 = (now_state_dict["coal1"] - result["coal1"]) * power1  # kg/h
    节省煤量2 = (now_state_dict["coal2"] - result["coal2"]) * power2  # kg/h
    ret = dbp_api.write_snapshot_double(tags=list(tag_des_write.keys()),
                                        values=[result["p1"], result["pump1"], result["fun1"], 节省煤量1,
                                                result["p2"], result["pump2"], result["fun2"], 节省煤量2, ])
    # dbp_api.get_his_value(["N2TC_TTD_Con", "N1TC_DT_CirWater"])


def update_model():
    global models
    from yangke.pytorch.mytorch import re_train
    re_train(data_file=r"E:\热工院\新建文件夹\summary5.csv")
    models = {}  # 将models置为空，则load_model方法会自动重新加载模型


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


if __name__ == "__main__":
    run()
