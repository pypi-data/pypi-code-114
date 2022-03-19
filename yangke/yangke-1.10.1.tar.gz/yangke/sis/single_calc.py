from yangke.web.flaskserver import start_server_app, logger
from yangke.sis.sis_io import run


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
        power_load = float(args.get("power"))
        heat_load = float(args.get("heat"))
        flowrate_fluegas_1 = float(args.get("fluegas1"))
        flowrate_fluegas_2 = float(args.get("fluegas2"))
        t_fluegas_in1 = float(args.get("ti1"))
        t_fluegas_in2 = float(args.get("ti2"))
        t_fluegas_out1 = float(args.get("to1"))
        t_fluegas_out2 = float(args.get("to2"))
        t_env = float(args.get("t0"))
        humid = float(args.get("humid"))
        logger.debug(f"{power_load=}")
        logger.debug(f"{humid=}")
        # 进行计算

        # 返回计算结果给前端
        return {"p": 7, "save_coal": -0.1, "type_pump": [2, 2], "type_tower": [4, 4]}

    except (TypeError, ValueError):
        logger.warning("类型转换错误")
        return {"error"   : "类型转换错误，calculate函数接受参数类型见提示",
                "power"   : "float, nonnull",
                "heat"    : "float, nonnull",
                "fluegas1": "float, nonnull",
                "fluegas2": "float, nonnull",
                "ti1"     : "float, nonnull",
                "ti2"     : "float, nonnull",
                "to1"     : "float, nonnull",
                "to2"     : "float, nonnull",
                "t0"      : "float, nonnull",
                "humid"   : "float, nonnull",
                }


def start_server():
    run()  # 启动定时执行
    start_server_app(deal=deal,
                     example_url="http://127.0.0.1:5000/?Action=calculate&power=400&heat=100&fluegas1=100000&"
                                 "fluegas2=100000&ti1=600&ti2=600&to1=100&to2=101.2&t0=20.14&humid=63.2")


if __name__ == "__main__":
    start_server()

