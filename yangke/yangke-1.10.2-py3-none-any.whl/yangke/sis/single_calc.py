from yangke.web.flaskserver import start_server_app, logger
from yangke.sis.sis_io import run, pred, get_煤耗, get_气耗


def deal(args):
    action = args.get("Action")
    result = eval("{}(args)".format(action))
    return result


def calculate(args):
    """
    后台计算服务的计算函数
    :param args:
    :return:
    """
    try:
        # 获取前端传入的数据
        power = float(args.get("power"))
        flow_heat = float(args.get("heat"))
        p_env = float(args.get("p_env") or 98)
        t_env = float(args.get("t0"))
        humid = float(args.get("humid") or 60) / 100
        p_gas = float(args.get("p_gas"))
        t_gas = float(args.get("t_gas"))
        flow_fgh = float(args.get("flow_fgh"))
        flow_tca = float(args.get("flow_tca"))
        flow_oh = float(args.get("flow_oh"))
        flow_rh = float(args.get("flow_rh"))

        result = {}
        hr1_min = 10000
        for pump in [2, 3]:
            for fun in [3, 4, 5]:
                eta1, hr1, p1 = pred(unit_num=1, power=power, flow_heat=flow_heat, p_env=p_env, t_env=t_env,
                                     humid=humid, p_gas=p_gas, t_gas=t_gas, flow_fgh=flow_fgh, flow_tca=flow_tca,
                                     flow_oh=flow_oh, flow_rh=flow_rh, pump=pump, fun=fun)
                eta1, hr1, p1 = eta1.item(), hr1.item(), p1.item()
                if hr1 < hr1_min:
                    hr1_min = hr1
                    气耗 = get_气耗(eta1, power, 47748.32)
                    煤耗 = get_煤耗(气耗, 47748.32)
                    result.update({"p": p1, "hr": hr1, "eta": eta1, "pump": pump, "fun": fun,
                                   "coal": 煤耗, "gas": 气耗})

        # 返回计算结果给前端
        return result

    except (TypeError, ValueError):
        logger.warning("类型转换错误")
        return {"error": "类型转换错误，calculate函数接受参数类型见提示",
                }


def start_server():
    run()  # 启动定时执行
    start_server_app(deal=deal,
                     example_url="http://127.0.0.1:5000/?Action=calculate&power=400&heat=100&fluegas1=100000&"
                                 "fluegas2=100000&ti1=600&ti2=600&to1=100&to2=101.2&t0=20.14&humid=63.2")


if __name__ == "__main__":
    start_server()
