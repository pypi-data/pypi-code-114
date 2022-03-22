import wcorr
import pandas as pd


def re_weight_with_limit(w, w_limit):
    wl =  w.sum() * w_limit
    if (w > wl).sum():
        w_over_at = w >= wl
        w_le_limit_at = w < wl
        w_over_limit = wl * w_over_at
        w_over = w * w_over_at - w_over_limit
        w_le_limit = w * w_le_limit_at
        re_weight_w = w_over_limit + w_le_limit + w_over.sum() * (w_le_limit / w_le_limit.sum())
        return re_weight_with_limit(re_weight_w, w_limit)
    else:
        return w


def profit_func(
    data,
    pred="pred",
    long_profit="long_profit_fwd1",
    short_profit="short_profit_fwd1",
    weight="w",
    cost=0.0,
    w_limit=1.,
    **kwargs,
):
    data["wl"] = re_weight_with_limit(data[weight], w_limit)
    long_profit = (
        (data[pred] > 0).astype(int) * (data[long_profit] - cost) * data["wl"]
    )
    short_profit = (
        (data[pred] < 0).astype(int) * (data[short_profit] - cost) * data["wl"]
    )
    return sum(long_profit + short_profit) / sum(data["wl"])

def profit_func_separate(
    data,
    pred="pred",
    long_profit="long_profit_fwd1",
    short_profit="short_profit_fwd1",
    weight="w",
    cost=0.0,
    w_limit=0.25,
    **kwargs,
):
    data["wl"] = re_weight_with_limit(data[weight], w_limit)
    long_profit = (
        (data[pred] > 0).astype(int) * (data[long_profit] - cost) * data["wl"]
    )
    short_profit = (
        (data[pred] < 0).astype(int) * (data[short_profit] - cost) * data["wl"]
    )
    long_w = sum((data[pred] > 0).astype(int) * data["wl"])
    short_w = sum((data[pred] < 0).astype(int) * data["wl"])
    return pd.Series({"profit": sum(long_profit + short_profit) / sum(data["wl"]), 
            "long_profit": (sum(long_profit) / sum(data["wl"])),
            "short_profit": (sum(short_profit) / sum(data["wl"])),
            "long_proportion": long_w / sum(data["wl"]),
                     })


def ic_func(data, pred="pred", label="label", weight="w", **kwargs):
    return wcorr.wspearman(data[pred], data[label], data[weight])


def get_n_largest_cond(
    data,
    amount_th=1e5,
    n=25,
    amount="Amount",
    dcol="Date",
    rank="pred_abs",
    rank_th=0,
    **kwargs,
):
    amount_cond = (data[amount] > amount_th) & (data[rank] > rank_th)
    return (
        data[amount_cond].groupby(dcol)[rank].nlargest(n).droplevel(2).index.swaplevel()
    )


def gen_daily_frame(data, func, dcol="Date", pred="pred", amount="Amount", **kwargs):
    data["pred_abs"] = data[pred].abs()
    data["w"] = data["pred_abs"] * data["Amount"]
    n_largest_cond = get_n_largest_cond(data, dcol=dcol, amount=amount, **kwargs)
    return data.loc[n_largest_cond].groupby(dcol).apply(lambda x: func(x, **kwargs))


def gen_daily_profit_df(data, idx_name="", **kwargs):
    frame = gen_daily_frame(data, func=profit_func, **kwargs)
    df = pd.DataFrame(frame, columns=["profit"])
    if idx_name:
        df["Set"] = idx_name
        df = df.reset_index().set_index(["Set", "Date"])
    return df

def gen_daily_profit_sep_df(data, idx_name="", **kwargs):
    frame = gen_daily_frame(data, func=profit_func_separate, **kwargs)
    df = pd.DataFrame(frame, columns=["profit", "long_profit", "short_profit", "long_proportion"])
    if idx_name:
        df["Set"] = idx_name
        df = df.reset_index().set_index(["Set", "Date"])
    return df

def gen_daily_profit_cum_df(data, idx_name="", **kwargs):
    frame = gen_daily_frame(data, func=profit_func_separate, **kwargs)
    df = pd.DataFrame(frame, columns=["profit", "long_profit", "short_profit", "long_proportion"])
    for col in ["profit", "long_profit", "short_profit"]:
        df[col] = df[col].cumsum()
        col_trim_profit = "_" + col.replace("profit", "").rstrip("_") if col.replace("profit", "") else ""
        df[f"drawdown{col_trim_profit}"] = (df[col] - df[col].cummax())
    if idx_name:
        df["Set"] = idx_name
        df = df.reset_index().set_index(["Set", "Date"])
    return df


def gen_daily_ic_df(data, idx_name="", n=650, **kwargs):
    frame = gen_daily_frame(data, func=ic_func, n=n, **kwargs)
    df = pd.DataFrame(frame, columns=["ic"])
    if idx_name:
        df["Set"] = idx_name
        df = df.reset_index().set_index(["Set", "Date"])
    return df


def concat_dfs(datas, col="profit", rolling_period=21, **kwargs):
    daily_profit = pd.DataFrame(pd.concat(datas), columns=[col])
    daily_profit[f"rolling_{col}"] = daily_profit.rolling(rolling_period)[col].mean()
    return daily_profit
