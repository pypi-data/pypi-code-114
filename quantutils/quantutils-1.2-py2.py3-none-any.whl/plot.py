import numpy as np
import seaborn as sns


def plot_daily_frame(data, col="", year_n=250):
    sns.set(rc={"figure.figsize": (12, 8)})
    # sns.set_style("white")
    if not col:
        col = data.columns[0]
    sets = data.index.get_level_values(0).unique()
    profit_max = data[col].max()
    profit_mean = data[col].mean()
    profit_std = data[col].std()
    year_rolling = data.rolling(year_n)[col].mean()
    for i, s in enumerate(sets):
        df_set = data.loc[s]
        df_set_mean = df_set[col].mean()
        df_set_std = df_set[col].std()
        p = sns.lineplot(data=df_set, style="white")
        p.plot(year_rolling.loc[s], color="black")
        p.axvline(df_set.index.max(), color="g")
        p.axhline(0, color="r")
        p.axhline(profit_mean, color="w")
        p.text(
                df_set.index[-1],
                profit_max,
                f"{s}\n\nmean:{df_set_mean: .05f}\nstd:{df_set_std: .05f}",
                ha="right",
                va="center",
                color="r",
            )
        if i == 0:
            p.set_title(f"mean: {profit_mean: 0.4f} std: {profit_std: 0.4f}")
            p.text(
                df_set.index[0],
                profit_mean,
                f"{profit_mean: .04f}",
                ha="right",
                va="center",
                color="b",
            )


def plot_daily_frame_cum(data, cols=["profit", "long_profit", "short_profit"], year_n=250, cost=0.007, costr_col="long_proportion", figsize=(12, 8)):
    data_ = data.copy()
    data[cols[0]] = data[cols[0]] - cost
    data[cols[1]] = data[cols[1]] - (cost * data[costr_col])
    data[cols[2]] = data[cols[2]] - (cost * (1 - data[costr_col]))
    # sns.set_style("white")
    for col in cols:
        data[col] = data[col].cumsum()
        data[col.replace("profit", "drawdown")] = (data[col] - data[col].cummax())
    
    col = cols[0]
    fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [2, 1]}, sharex=True, figsize=figsize)
    sets = data.index.get_level_values(0).unique()
    sets_mean_arr = []
    sets_std_arr = []
    for i, s in enumerate(sets):
        df_set = data.loc[s]
        df_set_ = data_.loc[s]
        df_set_mean = df_set_[col].mean()
        df_set_std = df_set_[col].std()
        sets_mean_arr.append(df_set_mean)
        sets_std_arr.append(df_set_std)
        profit_max = df_set["profit"].max()
        p = sns.lineplot(data=df_set[["profit", "long_profit", "short_profit"]], style="white", ax=axs[0])
        p.axvline(df_set.index.max(), color="g")
        p.axhline(0, color="r")
        #p.axhline(df_set_mean, color="w")
        p.text(
                df_set.index[-1],
                0,
                f"{s}\n\nmean:{df_set_mean: .05f}\nstd:{df_set_std: .05f}",
                ha="right",
                va="center",
                color="r",
            )
        p1 = sns.lineplot(data=df_set[["drawdown", "long_drawdown", "short_drawdown"]], style="white", ax=axs[1])

    profit_mean = np.mean(sets_mean_arr)
    profit_std = np.mean(sets_std_arr)
    p.set_title(f"mean: {profit_mean: 0.4f} std: {profit_std: 0.4f}")
    fig.tight_layout()