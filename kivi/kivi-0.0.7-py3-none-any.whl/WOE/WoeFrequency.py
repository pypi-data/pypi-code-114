from .WOE import WOE, pd

class Frequency(WOE):
    """
    等频分箱 woe iv 计算方式
    """
    def __init__(self, variables, target, bins, fill_pos=False):
        """
        等频分箱初始化
        :param variables: 待分箱变量
        :param target: 标签
        :param bins: 分箱数量
        :param fill_pos: 是否在分箱中未包含 1 标签的情况下，全部 1 标签数量自增 1 默认为 False
        """
        super(Frequency, self).__init__(variables, target, bins, fill_pos=fill_pos)

    def WoeIV(self, ):
        """
        计算自定义型变量的 woe & iv
        :param return: res 结果表
        """
        Bucket = pd.DataFrame({
            'variables': self.variables,
            'target': self.target,
            'Bucket': pd.qcut(self.variables, self.bins, duplicates='drop')
        }).groupby('Bucket', as_index=True)
        self.woe_iv_res(Bucket)
        return self.res
