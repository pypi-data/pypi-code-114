import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
def computeLinearRegression(XTrain, XTest, yTrain, yTest):
    from sklearn.linear_model import LinearRegression

    print("Computing Linear Regression...")
    regressor = LinearRegression()
    regressor.fit(XTrain, yTrain)
    yPred = regressor.predict(XTest)
    mae = mean_absolute_error(yTest, yPred)
    print(f"Mean absolute error: {mae}")


def RandomForestRegressor(XTrain, yTrain, XTest, yTest):
    from sklearn.ensemble import RandomForestRegressor
    model_forest = RandomForestRegressor()
    model_forest.fit(XTrain, yTrain)
    y_pred = model_forest.predict(XTest)
    mae = mean_absolute_error(yTest, y_pred)
    print(f"Mean absolute error: {mae}")
