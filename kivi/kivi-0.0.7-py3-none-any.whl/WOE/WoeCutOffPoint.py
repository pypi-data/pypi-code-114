from .WOE import WOE, pd

class CutOffPoint(WOE):
    """
    自定义分箱截断点 woe iv 计算方式
    """
    def __init__(self, variables, target, cutoffpoint, fill_pos=False, use_cutoffpoint='source'):
        """
        自定义分箱初始化
        :param variables: 待分箱变量
        :param target: 标签
        :param cutoffpoint: 分箱截断点
        :param fill_pos: 是否在分箱中未包含 1 标签的情况下，全部 1 标签数量自增 1 默认为 False
        :param use_cutoffpoint: 'source'汇总真实分箱截断点至结果表，'fix'汇总修正的分箱截断点至结果表, 默认为'source'
        """
        super(CutOffPoint, self).__init__(variables, target, fill_pos=fill_pos)
        self.cutoffpoint = cutoffpoint
        # bins_type 用于标定子类来源
        self.bins_type = 'cutoffpoint'
        # 使用自定义分箱截断点，
        self.use_cutoffpoint=use_cutoffpoint

    def WoeIV(self, ):
        """
        计算自定义型变量的 woe & iv
        :return: res 结果表
        """
        # 依据自定义的分箱截断点进行分箱，并返回修正分箱截断点
        value_cut, self.fix_cutoffpoint = pd.cut(
            self.variables, self.cutoffpoint, include_lowest=True, retbins=True)
        # 分箱与原值进行合并
        Bucket = pd.DataFrame({
            'variables': self.variables,
            'target': self.target,
            'Bucket': value_cut,
        }).groupby('Bucket', as_index=True)
        # 计算 woe iv
        self.woe_iv_res(Bucket)
        # 增加 cutoffpoint 列
        # if self.use_cutoffpoint == 'source':
        #     self.res['cutoffpoint'] = self.cutoffpoint
        # elif self.use_cutoffpoint == 'fix':
        #     self.res['cutoffpoint'] = self.fix_cutoffpoint
        return self.res
