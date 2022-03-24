# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 08:19:32 2022

@author: Tyler Blume
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit
import optuna.integration.lightgbm as lgb
import optuna
from scipy import stats
import lightgbm as gbm
import warnings
from LazyProphet.LinearBasisFunction import LinearBasisFunction
from LazyProphet.FourierBasisFunction import FourierBasisFunction
warnings.filterwarnings("ignore")


class LazyProphet:
    
    def __init__(self,
                 seasonal_period=None,
                 fourier_order=10,
                 n_basis=10,
                 ar=None,
                 ma_windows=None,
                 decay=None,
                 scale=True,
                 weighted=True,
                 decay_average=False,
                 linear_trend=None,
                 boosting_params=None):
        self.exogenous = None
        if seasonal_period is not None:
            if not isinstance(seasonal_period, list):
                seasonal_period = [seasonal_period]
        self.seasonal_period = seasonal_period
        self.scale = scale
        if ar is not None:
            if not isinstance(ar, list):
                ar = [ar]
        self.ar = ar
        if ma_windows is not None:
            if not isinstance(ma_windows, list):
                ma_windows = [ma_windows]
        self.ma_windows = ma_windows
        self.fourier_order = fourier_order
        self.decay = decay
        self.n_basis = n_basis
        self.weighted = weighted
        self.component_dict = {}
        self.decay_average = decay_average
        self.linear_trend = linear_trend
        if boosting_params is None:
            self.boosting_params = {
                                    "objective": "regression",
                                    "metric": "rmse",
                                    "verbosity": -1,
                                    "boosting_type": "gbdt",
                                    "seed": 42,
                                    'linear_tree': False,
                                    'learning_rate': .15,
                                    'min_child_samples': 5,
                                    'num_leaves': 31,
                                    'num_iterations': 50
                                }
        else:
            self.boosting_params = boosting_params

    def linear_test(self, y):
        y = y.copy().reshape((-1,))
        xi = np.arange(1, len(y) + 1)
        xi = xi**2
        slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
        trend_line = slope*xi*r_value + intercept
        if self.linear_trend is None:
            n_bins = (1 + len(y)**(1/3) * 2)
            splitted_array = np.array_split(y.reshape(-1,), int(n_bins))
            mean_splits = np.array([np.mean(i) for i in splitted_array])
            asc_array = np.sort(mean_splits)
            desc_array = np.flip(asc_array)
            if all(asc_array == mean_splits):
                growth = True
            elif all(desc_array == mean_splits):
                growth = True
            else:
                growth = False
            if (r_value > .9 and growth):
                self.linear_trend = True
            else:
                self.linear_trend = False
        self.slope = slope * r_value
        self.penalty = r_value
        self.intercept = intercept
        return trend_line

    def get_piecewise(self, y):
        self.lbf = LinearBasisFunction(n_changepoints=self.n_basis,
                                  decay=self.decay,
                                  weighted=self.weighted)
        basis = self.lbf.get_basis(y)
        return basis

    def get_harmonics(self, y, seasonal_period):
        self.fbf = FourierBasisFunction(self.fourier_order)
        basis = self.fbf.get_harmonics(y, seasonal_period)
        return basis

    @staticmethod
    def shift(xs, n):
        e = np.empty_like(xs)
        if n >= 0:
            e[:n] = np.nan
            e[n:] = xs[:-n]
        else:
            e[n:] = np.nan
            e[:n] = xs[-n:]
        return e

    @staticmethod
    def moving_average(y, window):
        y = pd.Series(y.reshape(-1,))
        ma = np.array(y.rolling(window).mean())
        return ma.reshape((-1, 1))

    def build_input(self, y, exogenous=None):
        X = np.arange(len(y))
        X = X.reshape((-1, 1))
        if self.n_basis is not None:
            if len(y) <= self.n_basis - 1:
                self.n_basis = len(y) - 1
            self.basis = self.get_piecewise(y)
            X = np.append(X, self.basis, axis=1)
            self.component_dict['basis'] = self.basis
        if self.seasonal_period:
            for period in self.seasonal_period:
                harmonics = self.get_harmonics(y, period)
                self.component_dict['harmonics ' + str(period)] = harmonics
                X = np.append(X, harmonics, axis=1)
        if self.exogenous is not None:
            X = np.append(X, exogenous, axis=1)
        if self.ar is not None:
            for ar_order in self.ar:
                shifted_y = self.scaled_y.copy()
                shifted_y = LazyProphet.shift(shifted_y, ar_order)
                X = np.append(X, shifted_y.reshape(-1, 1), axis=1)
        if self.ma_windows is not None:
            for ma_order in self.ma_windows:
                ma = LazyProphet.moving_average(self.scaled_y, ma_order)
                X = np.append(X, ma, axis=1)
        return X

    def scale_input(self, y):
        self.scaler = StandardScaler()
        self.scaler.fit(np.asarray(y).reshape(-1, 1))
        self.scaled_y = y.copy()
        self.scaled_y = self.scaler.transform(self.scaled_y.reshape(-1, 1))

    def fit(self, y, X=None):
        self.exogenous = X
        y = np.array(y)
        self.og_y = y
        if self.linear_trend is None or self.linear_trend:
            fitted_trend = self.linear_test(y)
        if self.linear_trend:
            y = np.subtract(y, fitted_trend)
        #TODO: Should we disable here?
        # if self.linear_trend:
        #     self.ar = None
        #     self.decay = None
        if self.scale:
            self.scale_input(y)
        else:
            self.scaled_y = y.copy()
        self.X = self.build_input(self.scaled_y)
        self.model_obj = gbm.LGBMRegressor(**self.boosting_params)
        self.model_obj.fit(self.X, self.scaled_y.reshape(-1, ))
        #commented out from basic feature selection
        # self.columns = pd.Series(lp_model.model_obj.feature_importances_).sort_values().index[-100:]
        # self.model_obj.fit(self.X[:, self.columns], self.scaled_y.reshape(-1, ))
        fitted = self.model_obj.predict(self.X).reshape(-1,1)
        if self.scale:
            fitted = self.scaler.inverse_transform(fitted)
        if self.linear_trend:
            fitted = np.add(fitted.reshape(-1,1), fitted_trend.reshape(-1,1))
        return fitted

    def recursive_predict(self, X, forecast_horizon):
        self.future_X = X
        #TODO: This is just...horrible
        predictions = []
        self.full = self.scaled_y.copy()
        if self.ar is not None:
            self.future_X = np.append(self.future_X,
                                      np.zeros((len(X), len(self.ar))),
                                      axis=1)
        if self.ma_windows is not None:
            self.future_X = np.append(self.future_X,
                                      np.zeros((len(X), len(self.ma_windows))),
                                      axis=1)
        for step in range(forecast_horizon):
            if self.ar is not None:
                for i, ar_order in enumerate(self.ar):
                    column_slice = -len(self.ar) + i
                    if step < ar_order:
                        self.future_X[step, column_slice] = self.scaled_y[-ar_order + step]
                    else:
                        self.future_X[step, column_slice] = predictions[-ar_order]
            if self.ma_windows is not None:
                for i, ma_window in enumerate(self.ma_windows):
                    column_slice = -len(self.ma_windows) + i
                    ma = np.mean(self.full[-ma_window:])
                    self.future_X[step, column_slice] = ma
            recursive_X = self.future_X[step, :].reshape(1, -1)
            predictions.append(self.model_obj.predict(recursive_X))
            self.full = np.append(self.full, predictions[-1])
        return np.array(predictions)

    def predict(self, forecast_horizon, future_X=None):
        X = np.arange(forecast_horizon) + len(self.scaled_y)
        X = X.reshape((-1, 1))
        if self.n_basis is not None:
            basis = self.lbf.get_future_basis(self.component_dict['basis'],
                                          forecast_horizon,
                                          average=self.decay_average)
            X = np.append(X, basis, axis=1)
        if self.seasonal_period:
            for period in self.seasonal_period:
                harmonics = self.component_dict['harmonics ' + str(period)]
                future_harmonics = self.fbf.get_future_harmonics(harmonics,
                                                                 forecast_horizon,
                                                                 period)
                X = np.append(X, future_harmonics, axis=1)
        if self.exogenous is not None:
            X = np.append(X, future_X, axis=1)
        if self.ar is not None or self.ma_windows is not None:
            predicted = self.recursive_predict(X, forecast_horizon)
        else:
            predicted = self.model_obj.predict(X)
        predicted = predicted.reshape(-1,1)
        if self.scale == True:
            predicted = self.scaler.inverse_transform(predicted)
        if self.linear_trend:
            linear_trend = [i for i in range(0, forecast_horizon)]
            linear_trend = np.reshape(linear_trend, (len(linear_trend), 1))
            linear_trend += len(self.scaled_y) + 1
            linear_trend = linear_trend**2
            linear_trend = np.multiply(linear_trend, self.slope*self.penalty) + self.intercept
            predicted = np.add(predicted, linear_trend.reshape(-1,1))
        return predicted

    def init_opt_params(self):
            self.opt_params = {
                                    "objective": "regression",
                                    "metric": "rmse",
                                    "verbosity": -1,
                                    "boosting_type": "gbdt",
                                    "seed": 42,
                                    'linear_tree': False,
                                }

    def tree_optimize(self, y, exogenous=None, cv_splits=3, test_size=None):
        self.init_opt_params()
        if self.n_basis is not None:
            if len(y) <= self.n_basis - 1:
                self.n_basis = len(y) - 1
        self.exogenous = exogenous
        y = np.array(y)
        self.og_y = y
        if self.linear_trend:
            fitted_trend = self.linear_test(y)
            y = np.subtract(y, fitted_trend)
        # if self.linear_trend:
        #     self.ar = None
        #     self.decay = None
        if self.scale:
            self.scale_input(y)
        else:
            self.scaled_y = y.copy()
        self.X = self.build_input(self.scaled_y)
        study_tuner = optuna.create_study(direction='minimize')
        dtrain = lgb.Dataset(self.X, label=self.scaled_y)
        optuna.logging.set_verbosity(optuna.logging.CRITICAL)
        tscv = TimeSeriesSplit(n_splits=cv_splits, test_size=test_size)
        tuner = lgb.LightGBMTunerCV(self.opt_params,
                                    dtrain,
                                    study=study_tuner,
                                    verbose_eval=False,
                                    early_stopping_rounds=10,
                                    seed = 42,
                                    folds=tscv,
                                    num_boost_round=500,
                                    show_progress_bar=False
                                    )
        
        tuner.run()
        best_params = tuner.best_params
        self.model_obj = gbm.LGBMRegressor(**best_params)
        self.model_obj.fit(self.X, self.scaled_y)
        fitted = self.model_obj.predict(self.X).reshape(-1,1)
        if self.scale:
            fitted = self.scaler.inverse_transform(fitted)
        if self.linear_trend:
            fitted = np.add(fitted.reshape(-1,1), fitted_trend.reshape(-1,1))
        return fitted
#%%
if __name__ == '__main__':
    #simple example
    from LazyProphet import LazyProphet as lp
    from sklearn.datasets import fetch_openml
    import matplotlib.pyplot as plt
    
    bike_sharing = fetch_openml("Bike_Sharing_Demand", version=2, as_frame=True)
    y = bike_sharing.frame['count']
    y = y[-400:].values
    
    lp_model = lp.LazyProphet(seasonal_period=[24, 168], #list means we use both seasonal periods
                              n_basis=4,
                              fourier_order=10,
                              ar=list(range(1,25)),
                              decay=.99
                              )
    fitted = lp_model.fit(y)
    predicted = lp_model.predict(100)
    
    plt.plot(y)
    plt.plot(np.append(fitted, predicted))
    plt.axvline(400)
    plt.show()

#%%
    import matplotlib.pyplot as plt
    import numpy as np
    from tqdm import tqdm
    import pandas as pd
    from LazyProphet  import LazyProphet as lp
    
    train_df = pd.read_csv(r'm4-monthly-train.csv')
    test_df = pd.read_csv(r'm4-monthly-test.csv')
    train_df.index = train_df['V1']
    train_df = train_df.drop('V1', axis = 1)
    test_df.index = test_df['V1']
    test_df = test_df.drop('V1', axis = 1)
    def smape(A, F):
        return 100/len(A) * np.sum(2 * np.abs(F - A) / (np.abs(A) +       np.abs(F)))
    smapes = []
    naive_smape = []
    # train_df = train_df.iloc[:1000, :]
    j = tqdm(range(len(train_df)))
    boosting_params = {
                            "objective": "regression",
                            "metric": "rmse",
                            "verbosity": -1,
                            "boosting_type": "gbdt",
                            "seed": 42,
                            'linear_tree': False,
                            'learning_rate': .15,
                            'min_child_samples': 5,
                            'num_leaves': 31,
                            'num_iterations': 50
                        }
    for row in j:
        y = train_df.iloc[row, :].dropna()
        y_test = test_df.iloc[row, :].dropna()
        j.set_description(f'{np.mean(smapes)}, {np.mean(naive_smape)}')
        lp_model = LazyProphet(scale=True,
                                seasonal_period=12,
                                n_basis=10,
                                fourier_order=5,
                                # ar=list(range(1, 4)),
                                decay=.99,
                                linear_trend=None,
                                decay_average=False,
                                boosting_params=boosting_params)
        fitted = lp_model.fit(y)
        predictions = lp_model.predict(len(y_test)).reshape(-1)
        smapes.append(smape(y_test.values,      pd.Series(predictions).clip(lower=0)))
        naive_smape.append(smape(y_test.values, np.tile(y.iloc[-1], len(y_test))))  
    print(np.mean(smapes))
    print(np.mean(naive_smape))