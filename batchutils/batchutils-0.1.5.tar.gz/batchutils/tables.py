import pandas as pd


def concat_dataframes(*df_list):
    """Concatenate Pandas dataframe objects serialized in Hail Batch.

    Parameters
    ----------
    df_list : unpacked list
        dataframe objects serialized in Batch

    Examples
    --------
    >>> concat_df_obj_list = []
    >>> for index, grouped_list in enumerate(grouped(200, df_obj_list)):
    >>>     j = b.new_python_job(name=f'concat-dataframes_{index}')
    >>>     j.image('gcr.io/daly-neale-sczmeta/hailgenetics-python-dill-pandas:0.1.0')
    >>>     df = j.call(concat_dataframes, *grouped_list)
    >>>     concat_df_obj_list.append(df)
    """
    df = pd.concat(df_list, axis=0)
    return(df)


def export_dataframes(*df_list):
    """Concatenate and export a list of Pandas dataframe objects 
    serialized in Hail Batch.

    Parameters
    ----------
    df_list : unpacked list
        dataframe objects serialized in Batch

    Examples
    --------
    >>> j = b.new_python_job(name='export-dataframes-all')
    >>> j.image('gcr.io/daly-neale-sczmeta/hailgenetics-python-dill-pandas:0.1.0')
    >>> result = j.call(concat_dataframes, *df_obj_list)
    >>> b.write_output(result.as_str(), outfile_path)
    """
    df = pd.concat(df_list, axis=0)
    return(df.to_csv(header=True, index=False, sep='\t'))


def export_joined_dataframes(df1, key, how='outer', *df_list):
    """Concatenate a list of Pandas dataframe objects serialized in Hail Batch.
    Join with another dataframe on a key and export to file.
    
    Parameters
    ----------
    df1 : Batch Python object
        Dataframe as Batch Python object
    key : str
        Key on which to join dataframes
    how : str, optional
        Type of join, by default 'outer'

    Examples
    --------
    >>> j = b.new_python_job(name='join-and-export-dataframes-all')
    >>> j.image('gcr.io/daly-neale-sczmeta/hailgenetics-python-dill-pandas:0.1.0')
    >>> result = j.call(concat_dataframes, df1, key, how='outer', *df_obj_list)
    >>> b.write_output(result.as_str(), outfile_path)
    """
    df2 = pd.concat(df_list, axis=0)
    df = pd.merge(df1, df2, how=how, on=key)
    return(df.to_csv(header=True, index=False, sep='\t'))


def export_concat_dataframes(df1, *df_list):
    """Concatenate a list of Pandas dataframe objects serialized in Hail Batch.
    Join with another dataframe on a key and export to file.
    
    Parameters
    ----------
    df1 : Batch Python object
        Dataframe as Batch Python object

    Examples
    --------
    >>> j = b.new_python_job(name='join-and-export-dataframes-all')
    >>> j.image('gcr.io/daly-neale-sczmeta/hailgenetics-python-dill-pandas:0.1.0')
    >>> result = j.call(export_concat_dataframes, df1, *df_obj_list)
    >>> b.write_output(result.as_str(), outfile_path)
    """
    df2 = pd.concat(df_list, axis=0)
    df1 = df1.reset_index(drop=True)
    df2 = df2.reset_index(drop=True)
    df = pd.concat([df1, df2], axis=1)
    return(df.to_csv(header=True, index=False, sep='\t'))
