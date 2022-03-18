import pandas as pd
import nlopt
import numpy as np
from datetime import datetime, timedelta


def budget_allocator(df, name_date_column, medias, all_features, date_get_budget, model, spents, response_get_budget,
                     lower_bounds, upper_bounds, maxeval, df_aggregated, algoritm='LD_MMA'):
    def getVals(df, name_date_column, all_features, date_get_budget):
        # last_week = datetime.strftime(datetime.today() - timedelta(7), '%Y-%m-%d')

        full_row = df.loc[df[name_date_column] == date_get_budget]
        row = full_row[all_features].copy()

        return row

    def myFunc(x, grad=[]):
        data = {}

        for m in medias:
            data[m] = [x[medias.index(m)]]

        dic = pd.DataFrame.from_dict(data)

        new_df = getVals(df, name_date_column, all_features, date_get_budget).copy()

        for column in dic:
            new_df[column] = dic[column].iloc[0]

        return model.predict(new_df)[0]

    if algoritm == 'GN_DIRECT':
        opt = nlopt.opt(nlopt.GN_DIRECT, len(medias))
    elif algoritm == 'LD_SLSQP':
        opt = nlopt.opt(nlopt.LD_SLSQP, len(medias))
    elif algoritm == 'GN_ISRES':
        opt = nlopt.opt(nlopt.GN_ISRES, len(medias))
    elif algoritm == 'GN_AGS':
        opt = nlopt.opt(nlopt.GN_AGS, len(medias))
    elif algoritm == 'LD_COBYLA':
        opt = nlopt.opt(nlopt.LD_COBYLA, len(medias))
    elif algoritm == 'GN_CRS2_LM':
        opt = nlopt.opt(nlopt.GN_CRS2_LM, len(medias))
    elif algoritm == 'G_MLSL':
        opt = nlopt.opt(nlopt.G_MLSL, len(medias))
    elif algoritm == 'GD_STOGO':
        opt = nlopt.opt(nlopt.GD_STOGO, len(medias))
    elif algoritm == 'GN_ESCH':
        opt = nlopt.opt(nlopt.GN_ESCH, len(medias))
    elif algoritm == 'LN_BOBYQA':
        opt = nlopt.opt(nlopt.LN_BOBYQA, len(medias))
    elif algoritm == 'LN_NEWUOA':
        opt = nlopt.opt(nlopt.LN_NEWUOA, len(medias))
    elif algoritm == 'LD_CCSAQ':
        opt = nlopt.opt(nlopt.LD_CCSAQ, len(medias))
    elif algoritm == 'AUGLAG':
        opt = nlopt.opt(nlopt.AUGLAG, len(medias))
    else:
        opt = nlopt.opt(nlopt.LD_MMA, len(medias))

    opt.set_lower_bounds(lower_bounds)
    opt.set_upper_bounds(upper_bounds)

    opt.set_max_objective(myFunc)
    opt.add_inequality_constraint(lambda z, grad: sum(z) - np.sum(spents), 1e-8)

    # rate of improvement, below which we are done
    opt.set_xtol_rel(1e-14)
    opt.set_maxeval(maxeval)

    budget_spents = opt.optimize(spents)

    budget_allocator_df = pd.DataFrame()
    budget_allocator_df['canale'] = medias
    for index, row in budget_allocator_df.iterrows():
        budget_allocator_df.at[index, 'actual_spend'] = spents[index]
        budget_allocator_df.at[index, 'optimal_spend'] = budget_spents[index]
        budget_allocator_df.at[index, 'actual_response'] = df_aggregated.loc[index, 'xDecompAgg']
        budget_allocator_df.at[index, 'optimal_response'] = budget_spents[index] * df_aggregated.loc[index, 'coef']
        budget_allocator_df.at[index, 'actual_total_spend'] = np.sum(spents)
        budget_allocator_df.at[index, 'optimal_total_spend'] = np.sum(budget_spents)
        budget_allocator_df.at[index, 'actual_total_response'] = response_get_budget
        budget_allocator_df.at[index, 'optimal_total_response'] = opt.last_optimum_value()

    return budget_allocator_df