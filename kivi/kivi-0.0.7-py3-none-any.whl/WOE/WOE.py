from ..Utils import np, pd, logging

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(message)s')

from ..Utils.utils import sameLength

class WOE:
    """
    WOE Object 为全部 WOE 的基础类函数，其方法被全部其他分箱方式调用
    """
    def __init__(
            self, variables, target,
            bins=None, var_name=None,
            fill_pos=False, all_feature=False):
        """
        初始化
        :param variables: 待分箱变量
        :param target: 标签
        :param bins: 分箱数量
        :param var_name: 变量名称
        :param fill_pos: 是否在分箱中未包含 1 标签的情况下，全部 1 标签数量自增 1 默认为 False
        :param all_feature: 是否为全变量模式进行分箱，为 Pearson 分箱设计，默认为 False
        """
        self.fill_pos = fill_pos
        # 是否存在变量的名称，存在使用原名，不存在使用变量 var_name
        if hasattr(variables, 'name'):
            self.var_name = variables.name
        else:
            self.var_name = var_name
        # 非全变量模式
        if not all_feature:
            # 检查变量与标签是否为同一长度
            if sameLength(variables, target):
                Exception(ValueError, 'variable and target Must be the same length!')
            # 变量名称、分箱数、基础计数
            self.name = variables.name
            self.bins = bins
            self._basic_count(target)
            # 拆分字段中的空箱与数值
            self.justMiss, notMiss = self.findMissData(variables, target)
            self.variables = notMiss.variables
            self.target = notMiss.target

    def findMissData(self, variables, target):
        """
        拆分空值数据与非空值数据
        :param variables: 分箱变量
        :param taget: 标签
        """
        df = pd.DataFrame({"variables": variables, "target": target})
        # 如果变量为数值型变量，则检查是否存在正负无穷的数值，即是否存在 infinite，
        # 一般在此处去除 infinite 的数据
        if pd.api.types.is_number(df.variables):
            df = df[-np.isinf(df.variables)]
        justMiss = df[df.variables.isna()]
        notMiss = df[df.variables.notna()]
        # 返回纯空值数据，非空值数据
        return justMiss, notMiss

    def _basic_count(self, target):
        """
        基础统计方法
        :param target: 标签列
        :return: None
        """
        # 样本量、bad 样本量
        self.total, self.bad = target.count(), target.sum()
        # good 样本量
        self.good = self.total - self.bad
        # 样本长度
        self.sampleLength = len(target)

    def __res(self, Bucket, ):
        """
        基本结果表
        :param Bucket: class groupby
        :return: None
        """
        # 非空分箱的结果表
        self.res = pd.DataFrame({
            # min_bin, max_bin 调整为分箱的临界值，而非子分箱的最大最小值
            'min_bin': Bucket.variables.min(),
            'max_bin': Bucket.variables.max(),
            'bad': Bucket.target.sum(),
            'good': Bucket.target.count()-Bucket.target.sum(),
            'total': Bucket.target.count(),
        })
        # 空箱
        self.nan_res = pd.DataFrame()
        if len(self.justMiss) != 0:
            self.nan_res = pd.DataFrame({
                'min_bin': [np.nan],
                'max_bin': [np.nan],
                "bad": self.justMiss.sum().target,
                'total': self.justMiss.count().target,
            })

    def calculate_woe(self, res):
        """
        依据结果表，计算woe
        :param res: res 结果表
        :return: res 结果表
        """
        # 如果存在 fill_pos==True, 则需要对分箱中未包含 1 标签的情况下，全部 1 标签数量自增 1
        if self.fill_pos and (0 in res.bad.tolist()):
            res.bad = res.bad + 1
        elif  self.fill_pos and (0 in res.good.tolist()):
            res.good = res.good + 1
        # 每个箱中坏样本所占总样本数的比例
        res['bad_rate'] = res['bad'] / res['total']
        # 每个箱中坏样本所占坏样本总数的比例
        res['badattr'] = res['bad'] / self.bad
        # 每个箱中好样本所占好样本总数的比例
        res['goodattr'] = res['good'] / self.good
        # 计算每个箱体的woe值
        res['woe'] = np.log(res['badattr'] / res['goodattr'])
        res['iv'] = (res['badattr'] - res['goodattr']) * res['woe']
        # 对箱体从大到小进行排序
        res = (res.sort_values(by='min_bin')).reset_index(drop=True)
        return res

    def woe_iv_res(self, Bucket):
        """
        计算 iv 值
        :param Bucket: class groupby bins value
        :return: None
        """
        # 初始化 res 表
        self.__res(Bucket=Bucket)
        # 计算 woe 值
        self.res = self.calculate_woe(self.res)
        # 计算字段的缺失率
        missing_rate = 1 - (self.res.total.sum() / self.sampleLength)
        # 如果变量存在空值
        if len(self.justMiss) != 0:
            # 计算空值结果表
            self.nan_res = self.calculate_woe(self.nan_res)
            # 汇总空值与非空的值的计算结果表
            self.res = self.res.append(self.nan_res)
        # 计算分箱的 iv 值
        self.res['iv_value'] = self.res.iv[-np.isinf(self.res.iv)].sum()
        self.res['missing_rate'] = missing_rate
        # 给定变量名称
        self.res['var_name'] = self.var_name
        # 重置结果表 index
        self.res.reset_index(drop=True, inplace=True)
