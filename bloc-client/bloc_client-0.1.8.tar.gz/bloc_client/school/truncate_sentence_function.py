import time
from enum import Enum
from typing import List

from bloc_client.value_type import ValueType
from bloc_client.bloc_client import BlocClient
from bloc_client.function_opt import FunctionOpt
from bloc_client.function_run_log import LogLevel
from bloc_client.select_options import SelectOption
from bloc_client.function_run_opt import FunctionRunOpt
from bloc_client.formcontrol_type import FormControlType
from bloc_client.function_interface import FunctionInterface
from bloc_client.function_run_queue import FunctionRunMsgQueue
from bloc_client.function_ipt import FunctionIpt, IptComponent


class CutWay(Enum):
    head = "head"
    tail = "tail"


class CutSentence(FunctionInterface):
    def ipt_config(self) -> List[FunctionIpt]:
        return [
            FunctionIpt(
                key="sentence",
                display="随便输",
                must=True,
                components=[
                    IptComponent(
                        value_type=ValueType.strValueType,
                        formcontrol_type=FormControlType.FormControlTypeTextArea,
                        hint="输入吧，用来测试python-client的节点而已",
                        default_value="hi bloc_client_python sdk",
                        allow_multi=False,
                    )
                ]
            ),
            FunctionIpt(
                key="cut_way",
                display="截断设置",
                must=True,
                components=[
                    IptComponent(
                        value_type=ValueType.strValueType,
                        formcontrol_type=FormControlType.FormControlTypeSelect,
                        hint="截断方式",
                        default_value="",
                        allow_multi=False,
                        select_options=[
                            SelectOption(label="头部", value="head"),
                            SelectOption(label="尾部", value="tail"),
                        ]
                    ),
                    IptComponent(
                        value_type=ValueType.intValueType,
                        formcontrol_type=FormControlType.FormControlTypeInput,
                        hint="截断的长度",
                        default_value=10,
                        allow_multi=False,
                    ),
                ]
            )
        ]
    
    def opt_config(self) -> List[FunctionOpt]:
        return [
            FunctionOpt(
                key="sentence",
                description="truncationed sentence",
                value_type=ValueType.strValueType,
                is_array=False)
        ]
    
    def all_process_stages(self) -> List[str]:
        return ["完成解析参数", "开始截断", "完成截断"]
    
    def run(
        self, 
        ipts: List[FunctionIpt], 
        queue: FunctionRunMsgQueue
    ) -> FunctionRunOpt:
        queue.report_log(LogLevel.info, "startstartstartstartstartstartstart")

        sentence = ipts[0].components[0].value
        if not sentence:
            queue.report_function_run_finished_opt(
                FunctionRunOpt(
                    suc=False, intercept_below_function_run=True,
                    error_msg=f"not allow blank sentence")
            )
            return

        try:
            cut_way = CutWay(ipts[1].components[0].value)
        except ValueError:
            queue.report_function_run_finished_opt( 
                FunctionRunOpt(
                    suc=False, intercept_below_function_run=True,
                    error_msg=f"""cut_way({ipts[1].components[0].value}) not in {list(map(lambda c: c.value, CutWay))}"""
                )
            )
            return

        cut_length = ipts[1].components[1].value
        if cut_length <=0:
            queue.report_function_run_finished_opt(
                FunctionRunOpt(
                    suc=False, intercept_below_function_run=True,
                    error_msg="cut_length must > 0"
                )
            )
            return

        if cut_way == CutWay.head:
            cuted_sentence = sentence[:cut_length]
        else:
            cuted_sentence = sentence[len(sentence)-cut_length:]
        queue.report_function_run_finished_opt(
            FunctionRunOpt(
                suc=True, 
                optKey_map_data={
                    'sentence': cuted_sentence
                }
            )
        )


if __name__ == "__main__":
    client = BlocClient.new_client("")
    client.test_run_function(
        CutSentence(),
        [
            ["xxxxxxx"],
            ["head", 2]
        ],
    )
