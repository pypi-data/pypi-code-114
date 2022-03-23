import pandas as pd
from .WOE import WOE

class Category(WOE):
    """
    类别型变量的分箱
    """
    def __init__(self, variables, target, fill_pos=False):
        """
        # 类别型变量初始化
        :param variables: 待分箱变量
        :param target: 标签列
        :param fill_pos: 是否在分箱中未包含 1 标签的情况下，全部 1 标签数量自增 1 默认为 False
        """
        # 继承 WOE Object
        super(Category, self).__init__(variables, target, fill_pos=fill_pos)
        self.cutoffpoint = 'category'
        # bins_type 用于标定子类来源
        self.bins_type = 'category'

    def WoeIV(self, ):
        """
        计算类别型变量的 woe & iv
        :return: res 结果表
        """
        # bins groupby bucket
        Bucket = pd.DataFrame({
            'variables': self.variables,
            'target': self.target,
            'Bucket': self.variables,
        }).groupby('Bucket', as_index=True)
        # 计算 woe iv
        self.woe_iv_res(Bucket)
        # 增加 cutoffpoint 列
        # self.res['cutoffpoint'] = self.cutoffpoint
        return self.res

