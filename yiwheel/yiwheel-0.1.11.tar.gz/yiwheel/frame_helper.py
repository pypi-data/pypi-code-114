from pandas import DataFrame


def get_a_value_from_frame(df: DataFrame, col1, v, col2):
    """
    获取一个 DataFrame 中一列 col1 第一个值为 v 的哪一行, 列为 col2 的值
    :param df: DataFrame
    :param col1: 第一个列名
    :param v: 一个格子的值
    :param col2: 第二个列名
    :return: 另一个格子的值
    """
    index = (df[df[col1] == v]).index[0]
    return df.loc[index, col2]
