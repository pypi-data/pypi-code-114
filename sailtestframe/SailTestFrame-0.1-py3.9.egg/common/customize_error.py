# @Time : 2022/3/14 9:28 PM 
# @Author : SailYang

class RunTimeTooLong(Exception):
    def __init__(self, case_name, run_time):
        self.name = case_name
        self.value = run_time

    # 打印类实例会调用该方法
    def __str__(self):
        return f"Run Time Too Long Error:{self.name} run time - {self.value}s"
