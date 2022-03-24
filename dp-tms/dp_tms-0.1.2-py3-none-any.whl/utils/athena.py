"""Athena Query Utilities"""
import json
import datetime
import itertools

def get_date_n_days_ago(n_days: int):
    """get the date n_days ago relative to now()"""
    return (
        datetime.datetime.now() - datetime.timedelta(days = n_days)
    ).strftime('%Y-%m-%d')

def get_query_parameters(
    sources: list,
    mediums: list,
    view_ids: list,
    excl_landing_pages: list,
    start_date: str,
    end_date: str
):
    if isinstance(sources, str):
        sources = json.loads(sources)
    if isinstance(mediums, str):
        mediums = json.loads(mediums)
    if isinstance(view_ids, str):
        view_ids = json.loads(view_ids)
    if isinstance(excl_landing_pages, str):
        excl_landing_pages = json.loads(excl_landing_pages)

    if start_date.isdigit():
        start_date = get_date_n_days_ago(int(start_date))

    if end_date.isdigit():
        end_date = get_date_n_days_ago(int(end_date))

    return (
        sources,
        mediums,
        view_ids,
        excl_landing_pages,
        start_date,
        end_date
    )

def encode_list_as_list_of_strings(items: list):
    """
        Encodes a list as a String list of items for Athena query.
        
        Adding a list of items to athena query argument requires it to be
        encoded as a string encoded list
    """
    items = ["\'{ITEM}\'".format(ITEM=item) for item in items]
    return ",".join(items)

def encode_2Dlist_as_row_list_of_strings(items1, items2):
    """
        Encodes a 2 lists as a row list of items for Athena query.
        
        Adding a list of items to athena query argument requires it to be
        encoded as a string encoded list
    """
    all_combinations = []
    list1_permutations  = itertools.permutations(items1, len(items2))
    for each_permutation in list1_permutations:
        zipped = zip(each_permutation, items2)
        all_combinations += list(zipped)
    # print(all_combinations)
    items = ["ROW(\'{ITEM1}\', \'{ITEM2}\')".format(ITEM1=combo[0],ITEM2=combo[1]) for combo in all_combinations]
    return ",".join(items)
