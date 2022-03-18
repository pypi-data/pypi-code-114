from prophet.plot import plot_plotly, plot_components_plotly
from prophet import Prophet
from cassandra.references.load_holidays import load_holidays
import pandas as pd


def prophet(df, name_date_column, name_target_column, window_start = '', window_end = '', national_holidays_abbreviation = 'IT', future_dataframe_periods = 14, plot_prophet = True):

    # Read the CSV on holidays
    csv_holiday = load_holidays()

    # Select the holidays according to the country that interests me
    condition = (csv_holiday['country'] == national_holidays_abbreviation)
    holidays = csv_holiday.loc[condition, ['ds', 'holiday']]

    # Create a DF with the only two columns for Prophet
    prophet_df = df[[name_date_column, name_target_column]]

    # Rename the columns for Prophet
    prophet_df = prophet_df.rename(columns={name_date_column: 'ds', name_target_column: 'y'})

    # Instance and fit Prophet
    prophet_m = Prophet(weekly_seasonality=True, yearly_seasonality=True, holidays=holidays)
    prophet_m.add_seasonality(name='monthly', period=30.5, fourier_order=5)
    prophet_m.fit(prophet_df)

    future = prophet_m.make_future_dataframe(periods=future_dataframe_periods)

    forecast = prophet_m.predict(future)
    forecast[['ds', 'yhat', 'trend', 'yearly', 'monthly', 'weekly', 'holidays', 'additive_terms',
              'multiplicative_terms']].tail()

    sub_prophet_df = forecast[['ds', 'trend', 'yearly', 'monthly', 'weekly', 'holidays']]
    sub_prophet_df = sub_prophet_df.rename(columns={'ds': name_date_column})

    if plot_prophet:
        plot_components_plotly(prophet_m, forecast)

    df[name_date_column] = pd.to_datetime(df[name_date_column])
    sub_prophet_df[name_date_column] = pd.to_datetime(sub_prophet_df[name_date_column])

    full_df = pd.merge(df, sub_prophet_df, how='inner', on=name_date_column)

    if window_start:
        full_df.drop(full_df[full_df[name_date_column] < window_start].index, inplace=True)
    if window_end:
        full_df.drop(full_df[full_df[name_date_column] > window_end].index, inplace=True)


    return full_df




