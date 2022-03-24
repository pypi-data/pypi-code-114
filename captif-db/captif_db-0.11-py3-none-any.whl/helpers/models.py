import pandas as pd


__all__ = [
    "query_to_frame",
    "objects_to_frame",
]


def query_to_frame(query, index_col=None, include_hybrid=False) -> pd.DataFrame:
    """
    Convert the results of a SQLalchemy query into a DataFrame.

    :param query: SQLalchemy query object
    :param index_col: column to use for the index in the returned DataFrame, defaults to None
    :param include_hybrid: whether to include hybrid properties, defaults to False

    """
    if include_hybrid:
        return objects_to_frame(query.all(), include_hybrid=True)
    return drop_duplicate_columns(
        pd.read_sql(query.statement, query.session.bind, index_col=index_col)
    )


def objects_to_frame(objs, index_col=None, include_hybrid=False) -> pd.DataFrame:
    """
    Convert list of SQLalchemy ORM objects to a DataFrame.

    :param objs: list of objects returned from a SQLalchemy query or relationship property
    :param index_col: column to use for the index in the returned DataFrame, defaults to None
    :param include_hybrid: whether to include hybrid properties, defaults to False

    """
    return pd.DataFrame.from_records(
        [xx.as_dict(include_hybrid=include_hybrid) for xx in objs], index=index_col
    )


def drop_duplicate_columns(df):
    return df.loc[:, ~df.columns.duplicated()]
