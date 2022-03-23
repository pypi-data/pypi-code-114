from ..Utils import np, pd, tqdm_notebook

from .WoeCategory import Category
from .WoeCutOffPoint import CutOffPoint
from .WoeFrequency import Frequency
from .FixWOE import FixWoeBins

from IPython.display import display


def Rebins(col_name, bins, df, target_name='target'):
    """
    描述：指定分箱阈值进行重分箱。
    :param col_name:
    :param bins:
    :param df:
    :param target_name:
    :return:
    """
    target, x = df[target_name], df[col_name]
    cut = CutOffPoint(x, target, cutoffpoint=bins, fill_pos=True)
    df_rebin_woe = cut.WoeIV()
    if hasattr(df_rebin_woe, 'cutoffpoint'):
        df_rebin_woe = df_rebin_woe.drop('cutoffpoint', axis=1)
    df_rebin_woe = FillBinScore(df_rebin_woe, col_name='var_name')
    disp_cols = ['var_name', 'total', 'bad', 'min_bin', 'max_bin', 'bad_rate', 'woe', 'woe_score', 'iv_value']
    df_rebin_woe = df_rebin_woe[disp_cols].style.bar(
        subset=['bad_rate', 'woe', 'woe_score'],
        align='mid',
        color=['#d65f5f', '#5fba7d'],
    )
    display(df_rebin_woe)

def IntScore(score):
    """
    将数值分数按 5 取整
    :param score: 浮点型分数
    :return: 按 5 取整分数
    """
    basic_score = np.arange(0, 101, 5)
    return basic_score[np.argmin(np.abs(score - basic_score))]

def FillBins(group, sort_by):
    """
    描述：

    参数：
    :param group:
    :param sort_by:
    :return:

    示例：

    """
    group.loc[:, 'woe_score'], group.loc[:, 'woe_score_int'] = -1, -1

    group = group.reset_index(drop=True)
    group.sort_values(by='woe', inplace=True)

    # select non inf data
    index = (-np.isinf(group.woe)).tolist()
    woe = group.woe[index]

    # order or not order
    diff = woe[1:] - woe[:-1]
    if np.all(diff >= 0) or np.all(diff <= 0):
        order = True
    else:
        order = False

    neg_woe = -woe
    woe_score = (neg_woe - neg_woe.min()) / (neg_woe.max() - neg_woe.min())
    group.loc[index, 'woe_score'] = woe_score * 100
    group.loc[index, 'woe_score_int'] = group.woe_score.apply(IntScore)
    group.loc[:, 'order'] = order
    return group.sort_values(by=sort_by)

def FillBinScore(data, col_name, sort_by="min_bin"):
    '''
    fill woe score in bins
    :param data: woe result
    :param col_name: feature name
    :return:
    '''
    df_new_woe = pd.DataFrame()
    for groupName, group in data.groupby(col_name):
        group = group.copy()
        group = FillBins(group, sort_by)
        if len(group) == 0:
            df_new_woe = group
        else:
            df_new_woe = df_new_woe.append(group)
    return df_new_woe

def WOEBatch(df, columns_name, target_name, WOEFun=Frequency, bins=5):
    """
    描述：批量计算WOE IV值

    参数：
    :param df:
    :param columns_name:
    :param target_name:
    :param bins: [int, dict]
        {col_name, cutoffpoint}
    :return:

    示例：
    >>> df_woe, faulted_cols = WOEBatch(
    >>>     df, columns_name=df.drop('target', axis=1).columns,
    >>>     target_name='target')
    """
    print(f'Samples shape: {df.shape}.')
    faulted_cols = []
    df_woe = pd.DataFrame()
    for col_name in tqdm_notebook(columns_name, desc='计算WOE'):
        try:
            if WOEFun == Category:
                woe = WOEFun(df[col_name], df[target_name])
            elif WOEFun == CutOffPoint:
                indexBins = bins.get(col_name)
                woe = WOEFun(df[col_name], df[target_name], cutoffpoint=indexBins, fill_pos=True)
            else:
                woe = WOEFun(df[col_name], df[target_name], bins=bins)
            if len(df_woe) == 0:
                df_woe = woe.WoeIV()
            else:
                df_woe = df_woe.append(woe.WoeIV())
        except:
            faulted_cols.append(col_name)

    df_woe = FillBinScore(df_woe, col_name='var_name')

    # 修正WOE分箱
    df_woe = FixWoeBins(df_woe)

    if len(faulted_cols) == 0:
        return df_woe, None
    else:
        return df_woe, faulted_cols

