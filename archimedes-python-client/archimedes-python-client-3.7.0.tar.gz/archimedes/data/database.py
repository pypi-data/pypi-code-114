import datetime
import json
from typing import List, Optional, Dict

from sqlalchemy.exc import ResourceClosedError

import archimedes
import pandas as pd
import numpy as np
import records
from archimedes.configuration import config


try:
    db_url = (
        f"postgresql://"
        f"{config.db.postgres_user}:"
        f"{config.db.postgres_pass}@"
        f"{config.db.postgres_host}:"
        f"{config.db.postgres_port}/"
        f"{config.db.postgres_dbname}"
    )
    db = records.Database(db_url=db_url)
except AttributeError as e:
    db = None
    db_error_msg = e


def list_ids(sort: bool = False):
    """List all the series ids available.

    Example:
        >>> archimedes.list_ids()
                                    series_id
        0   NP/NegativeProductionImbalancePrices
        1                      SN/FRRADownVolume
        ..                                   ...
        38                 NP/OrdinaryDownVolume
        39                    NP/SpecialUpVolume
    
    Args:
        sort (bool): False - return all series in one dataframe column, True - order dataframe by data-origin
    
    Returns:
        DataFrame with all available list_ids
    """
    if db is None:
        raise ValueError(db_error_msg)
    query = """
            SELECT distinct series_id from nordpool
            UNION
            SELECT distinct series_id from statnett
            """
    rows = db.query(query)
    ret = rows.export("df")

    if not sort:
        return ret
    
    # get list of data-sources and sort alphabetically
    data_sources = np.unique([ids.split("/")[0] for ids in ret.values.flatten()])
    data_sources = np.sort(data_sources)

    sorted_df = pd.DataFrame()
    for source in data_sources:
        source_ids = ret[pd.Series(ret.values.flatten()).str.startswith(source)]
        # sort series_ids alphabetically and reset dataframe index
        source_ids = source_ids.sort_values(by="series_id")
        source_ids = source_ids.reset_index(drop=True)
        # append column of series_ids to frame
        sorted_df = pd.concat([sorted_df, source_ids], axis=1)

    # set name of columns and replace nans with empty strings
    sorted_df.columns = data_sources
    sorted_df = sorted_df.fillna("")
    return sorted_df.copy()


def list_prediction_ids(composite_ids=False):
    """List all the prediction series ids available.

    Example:
        >>> archimedes.list_prediction_ids()
                                    series_id
        0   NP/NegativeProductionImbalancePrices
        1                      SN/FRRADownVolume
        ..                                   ...
        38                 NP/OrdinaryDownVolume
        39                    NP/SpecialUpVolume
    """
    if db is None:
        raise ValueError(db_error_msg)
    if composite_ids:
        query = """
        SELECT distinct composite_id from predictions
        """
    else:
        query = """
        SELECT distinct series_id from predictions
        """
    rows = db.query(query)
    return rows.export("df")


def get(
    series_ids: List[str],
    price_areas: List[str] = None,
    start: str = None,
    end: str = None,
    flatten_columns: bool = False,
    long_format: bool = False,
):
    """Get any number of time series.

    This function can be used to fetch time series from the Archimedes Database.
    To see which series are available, use `list_ids()`.

    Example:
        >>> archimedes.get(
        >>>     series_ids=["NP/AreaPrices"],
        >>>     price_areas=["NO1", "NO2"],
        >>>     start="2020-06-20T04:00:00+00:00",
        >>>     end="2020-06-28T04:00:00+00:00",
        >>> )
        series_id                 NP/AreaPrices
        price_area                          NO1   NO2
        from_dt
        2020-06-20T04:00:00+00:00          1.30  1.30
        2020-06-20T05:00:00+00:00          1.35  1.35
        ...                                 ...   ...
        2020-06-28T03:00:00+00:00          0.53  0.53
        2020-06-28T04:00:00+00:00          0.55  0.55

    Args:
        series_ids (List[str]): The series ids to get.
        price_areas (List[str], optional): The price areas to pick, all price areas if None. Defaults to None.
        start (str, optional): The first datetime to fetch (inclusive). Returns all if None. Defaults to None.
        end (str, optional): The last datetime to fetch (exclusive). Returns all if None. Defaults to None.
        flatten_columns (bool, optional): The column names are flattened if True. Defaults to False.
        long_format (str, optional): Should the dataframe be long (instead of wide). Defaults to False.

    Returns:
        DataFrame with all the time series data
    """
    if db == None:
        raise ValueError(db_error_msg)

    if isinstance(series_ids, str):
        series_ids = [series_ids]

    if isinstance(price_areas, str):
        price_areas = [price_areas]

    if start == None:
        start = archimedes.constants.DATE_LOW
    else:
        start = pd.to_datetime(start)

    if end == None:
        end = archimedes.constants.DATE_HIGH
    else:
        end = pd.to_datetime(end)

    query = """
    SELECT c.series_id, c.from_dt, c.price_area, c.value, c.version FROM (
        SELECT * FROM nordpool
        UNION
        SELECT * FROM statnett
    ) as c
    WHERE c.series_id IN :series_ids
    AND c.from_dt >= :start
    AND c.from_dt < :end
    """

    if price_areas is None:
        rows = db.query(
            query=query,
            series_ids=tuple(series_ids),
            start=start,
            end=end,
        )
    else:
        query = f"{query} AND c.price_area IN :price_areas"
        rows = db.query(
            query=query,
            series_ids=tuple(series_ids),
            price_areas=tuple(price_areas),
            start=start,
            end=end,
        )

    df = rows.export("df")

    row_count = df.shape[0]
    if row_count == 0:
        return df

    df["from_dt"] = pd.to_datetime(df["from_dt"])
    df = df.sort_values(by=["from_dt", "version"])

    if long_format:
        df = (
            df.groupby(["series_id", "from_dt", "price_area"]).agg("last").reset_index()
        )
        df.drop(["version"], axis=1, inplace=True)
        return df

    df = df.pivot_table(
        values="value",
        columns=["series_id", "price_area"],
        index="from_dt",
        aggfunc="last",
    )
    if flatten_columns:
        new_columns = ["/".join(list(column)) for column in df.columns]
        df.columns = new_columns
    df = df.astype(float)
    return df


def get_latest(
    series_ids: List[str],
    price_areas: List[str] = None,
    flatten_columns: bool = False,
):
    """Get the most recent data for any number of time series.

    This function is similar to `get()`, but only fetches data from the past 48 hours,
    potentially including future hours as well (as in the case of Spot price data).

    @TODO: Add an argument `hours` that allows the 'lookback' period to be extended
    to an arbitrary number of hours.

    Example:
        >>> # Calling this function at 2020-03-15T10:15:00
        >>> archimedes.get_latest(
        >>>     series_ids=["NP/AreaPrices", "NP/ConsumptionImbalancePrices"],
        >>>     price_areas=["NO1"],
        >>> )
        series_id                 NP/AreaPrices  NP/ConsumptionImbalancePrices
        price_area                          NO1                            NO1
        from_dt
        2020-03-14T04:11:00+00:00          1.30                           1.30
        2020-03-14T05:12:00+00:00          1.35                           1.35
        ...                                 ...                            ...
        2020-03-15T22:00:00+00:00          0.53                            NaN
        2020-03-15T23:00:00+00:00          0.55                            NaN

    Args:
        series_ids (List[str]): The series ids to get.
        price_areas (List[str], optional): The price areas to pick, all price areas if None. Defaults to None.
        flatten_columns (bool, optional): The column names are flattened if True. Defaults to False.

    Returns:
        DataFrame with all the time series data
    """
    now_dt = pd.Timestamp.now(tz="utc")
    start_dt = now_dt - datetime.timedelta(days=2)
    # +14 days should be enough in all cases now:
    end_dt = now_dt + datetime.timedelta(days=14)

    df = get(
        series_ids=series_ids,
        price_areas=price_areas,
        start=start_dt.isoformat(),
        end=end_dt.isoformat(),
        flatten_columns=flatten_columns,
    )

    return df


def get_predictions(
    series_ids: List[str],
    start: str = None,
    end: str = None,
    ref_dt: str = None,
    price_area: str = None,
) -> List:
    """Get any number of predictions

    This function can be used to fetch predictions from the Archimedes Database.

    Unlike `archimedes.get`, this will return a list, not a dataframe.

    @TODO: It could be that this function should also return a pd.DataFrame,
    where the user can choose whether to have the 'wide' or 'long' format returned.

    Example:
        >>> archimedes.get_predictions(
            series_ids=["PX/rk-naive"],
            start="2020"
        )
        >>> [...]

    Args:
        series_ids (List[str]): The series ids to get.
        start (str, optional):
            The first datetime to fetch (inclusive). Returns all if None. Defaults to None.
        end (str, optional):
            The last datetime to fetch (exclusive). Returns all if None. Defaults to None.
        ref_dt (str, optional):
            The reference datetime, eg. what was the time of the latest RK price?
        price_area (str, optional):
            The price area, eg. "NO2"

    Returns:
        List with all the prediction data
    """
    if db == None:
        raise ValueError(db_error_msg)

    if isinstance(series_ids, str):
        series_ids = [series_ids]

    if start == None:
        start = archimedes.constants.DATE_LOW
    else:
        start = pd.to_datetime(start)

    if end == None:
        end = archimedes.constants.DATE_HIGH
    else:
        end = pd.to_datetime(end)

    query = """
    SELECT
        from_dt,
        version,
        value,
        attributes->>'ref_dt' as ref_dt,
        attributes->>'model_version' as model_version,
        attributes->>'hours_ahead' as hours_ahead,
        attributes->>'price' as price,
        attributes->>'price_area' as price_area
    FROM predictions as c
    WHERE c.series_id IN :series_ids
    AND c.from_dt >= :start
    AND c.from_dt < :end
    """

    params = {"series_ids": tuple(series_ids), "start": start, "end": end}

    if ref_dt != None:
        ref_dt = pd.to_datetime(ref_dt).isoformat()
        query += " AND c.attributes->>'ref_dt' = :ref_dt"
        params["ref_dt"] = ref_dt

    if price_area != None:
        query += " AND c.attributes->>'price_area' = :price_area"
        params["price_area"] = price_area

    rows = db.query(query, **params)

    data = json.loads(rows.export("json"))

    for d in data:
        d["from_dt"] = pd.to_datetime(d["from_dt"])
        d["ref_dt"] = pd.to_datetime(d["ref_dt"])
        d["hours_ahead"] = pd.to_timedelta(d["hours_ahead"])
        d["price"] = float(d["price"]) if d["price"] else None
        d["value"] = float(d["value"])

    return data


def get_predictions_ref_dts():
    """Get which ref_dts are available.

    ref_dt == prediction_build_dt
    Users views in the database.

    Returns:
        List[Dict]
    """
    if db == None:
        raise ValueError(db_error_msg)
    import time

    start = time.time()
    query = """
    SELECT * FROM v_predictions_ref_dts
    LIMIT 10
    """
    rows = db.query(query)
    end = time.time()
    print(f"database.py->get_predictions_ref_dts timing: {end - start}")
    # return_value = [record.as_dict() for record in rows.all()]
    return_value = json.loads(rows.export("json"))
    # from pprint import pprint
    # pprint(return_value)
    return return_value


def _get_predictions_UNRELEASED(
    series_ids: List[str],
    start: str = None,
    end: str = None,
    long_format: bool = True,
    rename_columns: Dict = None,
) -> pd.DataFrame:  # A replacement for get_predictions
    # Include create_composite_id in imports
    """Get any number of predictions

    This function can be used to fetch predictions from the Archimedes Database.

    Unlike `archimedes.get`, this will return a list, not a dataframe.

    @TODO: It could be that this function should also return a pd.DataFrame,
    where the user can choose whether to have the 'wide' or 'long' format returned.

    Example:
        >>> archimedes.get_predictions(
            series_ids=["PX/rk-naive"],
            start="2020"
        )
        >>> [...]

    Args:
        series_ids (List[str]): The series ids to get.
        start (str, optional):
            The first datetime to fetch (inclusive). Returns all if None. Defaults to None.
        end (str, optional):
            The last datetime to fetch (exclusive). Returns all if None. Defaults to None.
        long_format (str, optional):
            Should the dataframe be long (instead of wide). Defaults to True.

    Returns:
        Dataframe with all the prediction data
    """
    if db == None:
        raise ValueError(db_error_msg)

    if isinstance(series_ids, str):
        series_ids = [series_ids]

    if start == None:
        start = archimedes.constants.DATE_LOW
    else:
        start = pd.to_datetime(start)

    if end == None:
        end = archimedes.constants.DATE_HIGH
    else:
        end = pd.to_datetime(end)

    query = """
    SELECT * FROM predictions as c
    WHERE c.series_id IN :series_ids
    AND c.from_dt >= :start
    AND c.from_dt < :end
    """
    rows = db.query(query, series_ids=tuple(series_ids), start=start, end=end)

    df = rows.export("df")

    row_count = df.shape[0]
    if row_count == 0:
        return df

    df["from_dt"] = pd.to_datetime(df["from_dt"])
    df.drop(["created_at", "composite_id", "to_dt"], axis=1, inplace=True)
    attributes_df = pd.json_normalize(df["attributes"])
    df.drop(["attributes"], axis=1, inplace=True)
    for column in attributes_df.columns:
        if column in ["from_dt", "model_name", "value_description"]:
            pass
        elif column in ["hours_ahead"]:
            df[column] = pd.to_timedelta(attributes_df[column])
        elif column in ["ref_dt"]:
            df[column] = pd.to_datetime(attributes_df[column])
        elif column in ["price_area", "model_version"]:
            df[column] = attributes_df[column]
        elif column in ["quantile"]:
            df[column] = attributes_df[column]
            # df[column] = attributes_df[column].fillna("exp")
            # df[column] = df[column].apply(lambda x: x if x == "exp" else f"{int(x)}%")
        else:
            print("there was an error")
            print(column)
            raise ValueError("Uncaught column in attributes named: " + column)
        # TODO: add column using create_composite_id

    # TODO: return different format if format="wide"

    if rename_columns != None:
        for key, value in rename_columns.items():
            df[value] = df[key]
            df.drop([key], axis=1, inplace=True)

    # lst = [record.as_dict() for record in rows.all()]
    # return lst
    return df


def store_prediction(
    series_id: str,
    value: float,
    version: int,
    from_dt: pd.Timestamp,
    attributes: Optional[Dict] = None,
    composite_id: str = None,
):
    """Store a prediction

    Example:
        >>> # @TODO: Add example.

    @TODO:
        Include 'model' and / or 'model version' as arguments.

    Args:
        project_name (str): The name of the project
        model_name (str): The name of the model used to make the prediction
        target_dt (pd.Timestamp): The hour of the prediction
        last_data_dt (pd.Timestamp): The hour of the last available data used to make the prediction
        predicted_value (float): The value that has been predicted
        prediction_dt (pd.Timestamp, optional): The time at which the prediction was made
        target_series_id (str, optional): The Archimedes series id corresponding to the predicted value
    """
    if db == None:
        raise ValueError(db_error_msg)

    if attributes == None:
        attributes = {}

    for k, v in attributes.items():
        if isinstance(v, (pd.Timestamp, pd.Timedelta)):
            attributes[k] = v.isoformat()

    query = """
    INSERT INTO predictions (from_dt, value, version, attributes, series_id, composite_id)
    VALUES (:from_dt, :value, :version, :attributes, :series_id, :composite_id)
    """

    try:
        db.query(
            query,
            from_dt=from_dt,
            value=value,
            version=version,
            attributes=json.dumps(attributes),
            series_id=series_id,
            composite_id=composite_id,
        )
    except ResourceClosedError:
        # This is expected for records library when inserting
        pass
    return True
