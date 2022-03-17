import pandas as pd

def qcut(data, q = None, key = None, *args, **kwargs):
    '''
    data: pd.Series or pd.DataFrame. If DataFrame, must set key param.
    key: column name you select in data
    return: a list of split result by qcut.
    '''
    result_list = []
    
    if isinstance(data, pd.Series):
        tmp_series = data
    elif isinstance(data, pd.DataFrame) and key is not None:
        tmp_series = data[key]
    else:
        raise Exception('The param \'data\' must be pd.Series or pd.DataFrame. If DataFrame, must set key param.')

    result = pd.qcut(tmp_series, q, *args, *kwargs)

    if isinstance(q, list):
        len_q = len(q) 
    else:
        len_q = q

    if result.dtype == 'category':
        for i in result.drop_duplicates().sort_values():
            result_list.append(data[(tmp_series <= i.right) & (tmp_series > i.left)])
    else:
         for i in range(len_q):
            result_list.append(data[result == i])   
    return result_list