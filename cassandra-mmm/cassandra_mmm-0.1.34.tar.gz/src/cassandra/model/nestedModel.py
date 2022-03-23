from cassandra.model.linear import linear
from cassandra.model.logLinear import logLinear
from cassandra.model.ridge import ridge


def nestedModel(df, X_columns, y_column, model_regression = 'linear', metric = ['rsq', 'nrmse', 'mape'], return_metric = False):
    metrics_values = {}
    name_model = 'Nested Model for ' + y_column

    X = df[X_columns]
    y = df[y_column]

    if model_regression == 'linear':
        if return_metric:
            result, model, metrics_values = linear(df, X, y, y_column, name_model, metric = metric, return_metric = return_metric)
        else:
            result, model = linear(df, X, y, y_column, name_model, metric = metric, return_metric = return_metric)

    elif model_regression == 'logLinear':
        if return_metric:
            result, model, metrics_values = logLinear(df, X, y, y_column, name_model, metric=metric,
                                                   return_metric=return_metric)
        else:
            result, model = linear(df, X, y, y_column, name_model, metric=metric, return_metric=return_metric)

    elif model_regression == 'ridge':
        if return_metric:
            result, model, metrics_values = ridge(df, X, y, y_column, name_model, metric=metric,
                                                   return_metric=return_metric)
        else:
            result, model = linear(df, X, y, y_column, name_model, metric=metric, return_metric=return_metric)

    if metrics_values:
        return result, model, metrics_values
    else:
        return result, model



def mainNestedModel(sub_df, sub_X_columns, sub_y_column, X_columns, y_column, sub_model_regression = 'linear', sub_metric = ['rsq', 'nrmse', 'mape'], return_sub_metric = False, model_regression = 'linear', metric = ['rsq', 'nrmse', 'mape'], return_metric = False):
    metrics_values = {}
    if return_sub_metric == True:
        sub_result, sub_model, sub_metric_values = nestedModel(sub_df, sub_X_columns, sub_y_column, sub_model_regression, sub_metric, return_sub_metric)
    else:
        sub_result, sub_model = nestedModel(sub_df, sub_X_columns, sub_y_column, sub_model_regression, sub_metric)

    df = sub_result

    df[sub_y_column] = sub_result['prediction']
    X = df[X_columns]
    y = df[y_column]

    name_model = model_regression + ' for ' + y_column

    if model_regression == 'linear':
        if return_metric:
            result, model, metrics_values = linear(df, X, y, y_column, name_model, metric=metric,
                                                   return_metric=return_metric)
        else:
            result, model = linear(df, X, y, y_column, name_model, metric=metric, return_metric=return_metric)

    elif model_regression == 'logLinear':
        if return_metric:
            result, model, metrics_values = logLinear(df, X, y, y_column, name_model, metric=metric,
                                                      return_metric=return_metric)
        else:
            result, model = linear(df, X, y, y_column, name_model, metric=metric, return_metric=return_metric)

    elif model_regression == 'ridge':
        if return_metric:
            result, model, metrics_values = ridge(df, X, y, y_column, name_model, metric=metric,
                                                  return_metric=return_metric)
        else:
            result, model = linear(df, X, y, y_column, name_model, metric=metric, return_metric=return_metric)

    if metrics_values:
        return result, model, metrics_values, sub_result, sub_model, sub_metric_values
    else:
        return result, model, sub_result, sub_model






