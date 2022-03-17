

class ParamError(BaseException): ...  # 参数错误

class SetAttrError(BaseException): ...  # 对象不可修改

class NeedNotExecute:  # 不需要执行
    def __init__(self, reason=''): self.reason = reason
    def __str__(self): return self.reason
    def __bool__(self): return True


# 未传递(的参数)
class UnGive(int): ...
ungive = UnGive(0)

# 全集
class UniSet(int): ...
uniset = UniSet(1)

# 空集
class EmpSet(int): ...
empset = EmpSet(0)

# 整数0
class Int0(int): ...
int0 = Int0(0)

# 正无穷大
class PInf(float): ...
pinf = PInf('inf')
