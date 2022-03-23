from ..Utils import pd, np


def lift(df_score, bins=20, score_name='score', target_name='target'):
    """
    描述：计算模型结果的lift
    :param df_score:
    :param bins:
    :param score_name:
    :param target_name:
    :return:
    """
    df_score["buckets"] = pd.cut(df_score[score_name], bins=np.linspace(0, 100, bins + 1), include_lowest=True)

    df_buckets = df_score.groupby('buckets').agg({'uuid': 'count', target_name: 'sum'})
    df_buckets['good'] = df_buckets.uuid - df_buckets.target

    df_buckets['cum_total'] = df_buckets.uuid.cumsum() / df_buckets.uuid.sum()
    df_buckets['cum_bad'] = df_buckets.target.cumsum() / df_buckets.target.sum()
    df_buckets['cum_good'] = df_buckets.good.cumsum() / df_buckets.good.sum()
    df_buckets['ks'] = df_buckets.cum_bad / df_buckets.cum_good
    df_buckets['lift'] = df_buckets.cum_bad / df_buckets.cum_total
    return df_buckets