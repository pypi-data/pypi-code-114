from datetime import datetime, timedelta


def getBudget(df, name_date_column, medias, date_get_budget):
    full_row = df.loc[df[name_date_column] == date_get_budget]

    spents = []

    for m in medias:
        spents.append(full_row[m].values[0])

    response = full_row['revenue'].values[0]
    return spents, response


def getVals(df, name_date_column, all_features, date_get_budget):

    full_row = df.loc[df[name_date_column] == date_get_budget]
    row = full_row[all_features].copy()

    return row
