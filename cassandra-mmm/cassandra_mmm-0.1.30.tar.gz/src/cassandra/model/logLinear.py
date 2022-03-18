import numpy as np
from modelEvaluation.evaluation import show_mape, show_nrmse, show_rsquared
from cassandra.data.trasformations.trasformations import create_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def logLinear(df, X, y, target, name_model, medias = [], organic = [], metric = ['rsq', 'nrmse', 'mape'], return_metric = False):
    metrics_values = {}
    logged_y = np.log(y)
    X_train, X_test, y_train, y_test = train_test_split(X, logged_y)

    if medias or organic:
        model = create_model(medias, organic, LinearRegression())
    else:
        model = LinearRegression()

    model.fit(X_train, y_train)

    #y_pred = np.exp(model.predict(X))  # Apply exponential function (inverse of natural log) to the predictions

    # Ask the model to predict on X_test without having Y_test
    # This will give you exact predicted values

    # We can use our NRMSE and MAPE functions as well

    # Create new DF not to edit the original one
    result = df

    # Create a new column with predicted values
    if medias or organic:
        result['prediction'] = model.predict(result)
    else:
        result['prediction'] = model.predict(X)

    # Get the NRMSE & MAPE values

    # Score returns the accuracy of the above prediction or R^2
    if 'rsq' in metric:
        rsq = show_rsquared(result[target], result['prediction'])
        if return_metric:
            metrics_values[name_model + '_rsq'] = rsq
        print(name_model, 'RSQ: ', rsq)

    # vedere se va tolto il log su result['revenue']
    if 'nrmse' in metric:
        nrmse_val = show_nrmse(np.log(result[target]), result['prediction'])
        if return_metric:
            metrics_values[name_model + '_nrmse'] = nrmse_val
        print(name_model, 'NRMSE: ', nrmse_val)

    if 'mape' in metric:
        mape_val = show_mape(np.log(result[target]), result['prediction'])
        if return_metric:
            metrics_values[name_model + '_mape'] = mape_val
        print(name_model, 'MAPE: ', mape_val)

    if metrics_values:
        return result, model, metrics_values
    else:
        return result, model