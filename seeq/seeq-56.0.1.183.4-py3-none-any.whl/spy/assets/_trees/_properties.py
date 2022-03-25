import copy
import re
import types

import numpy as np
import pandas as pd

from seeq.sdk import *
from seeq.spy import _common, _login, _metadata
from seeq.spy._errors import *
from seeq.spy._session import Session
from seeq.spy.assets._trees import _constants, _match, _path, _utils
from seeq.spy.workbooks._item import Item


def apply_friendly_name(df) -> None:
    if 'Friendly Name' not in df.columns or df['Friendly Name'].isnull().all():
        _common.put_properties_on_df(df, types.SimpleNamespace(modified_items=set()))
        return

    # If we are changing the names of items in a dataframe whose paths are dependent on one another, then
    # record those dependencies so we can modify paths afterwards as well
    relationships = path_relationships(df)

    modified_items = set()
    for i in df.index:
        if pd.isnull(df.loc[i, 'Friendly Name']):
            continue
        if _match.is_column_value_query(df.loc[i, 'Friendly Name']):
            new_name = _match.fill_column_values(df.loc[i], df.loc[i, 'Friendly Name'])
        else:
            new_name = df.loc[i, 'Friendly Name']
        if pd.isnull(new_name):
            continue
        df.loc[i, 'Name'] = new_name
        if _common.present(df.loc[i], 'ID'):
            modified_items.add(df.loc[i, 'ID'])

    recover_relationships(df, relationships)
    _common.put_properties_on_df(df, types.SimpleNamespace(modified_items=modified_items))


def path_relationships(df) -> dict:
    """
    Return a dict of dicts indicating via integers how the paths of the input rows are dependent on one another.

    Example:
        df = pd.DataFrame([{
            'Path': 'Root', 'Name': 'Item 1'
        }, {
            'Path': 'Root >> Item 1', 'Name': 'Item 2'
        }])

        output = {
            1: { # 1 refers here to the row in df with index 1, i.e., Item 2
                1: 0 # 1 refers here to the item in Item 2's path with index 1, i.e. 'Item 1'
                     # 0 refers here to the index of Item 1's row in df
            }
        }
    """
    if len(df) == 0 or 'Name' not in df.columns:
        return None
    temp_df = df[['Name']].copy()
    temp_df['Path'] = df.apply(_path.determine_path, axis=1)
    full_paths = list(temp_df.apply(_path.get_full_path, axis=1).apply(_common.path_string_to_list))
    relationships = dict()
    # This is O(n^2) but it's not a core feature
    for i, this in enumerate(full_paths):
        if this == [''] or len(this) == 0:
            continue
        for j, other in enumerate(full_paths):
            if other == ['']:
                continue
            # If the full path "other" begins with the full path "this", then we mark that
            # the (len(this) - 1)th element in "other"'s path is equal to "this"
            if len(other) > len(this) and other[:len(this)] == this:
                if j not in relationships:
                    relationships[j] = dict()
                relationships[j][len(this) - 1] = i
    return relationships


def recover_relationships(df, relationships) -> None:
    """
    Takes a list of relationships (in the format described in _path_relationships) and modifies paths in
    df to reflect those relationships
    """
    if relationships is None:
        return
    for i, path_ref_dict in relationships.items():
        path = _path.determine_path(df.loc[i])
        path_list = _common.path_string_to_list(path) if path else []
        for j, reference in path_ref_dict.items():
            if 0 <= reference < len(df) and 0 <= j < len(path_list):
                path_list[j] = df.loc[reference, 'Name']
        df.loc[i, 'Path'] = _common.path_list_to_string(path_list)
    if 'Asset' in df.columns:
        df.drop(columns='Asset', inplace=True)


def process_properties(session: Session, df, status, existing_tree_df=None, pull_nodes=True,
                       keep_parent_column=False) -> pd.DataFrame:
    """
    Sanitize and pull item properties into an input dataframe. Steps in order:
    -- Pulls missing properties for items with ID provided
    -- Filters out properties not in _constants.dataframe_columns
    -- Determines tree depth
    -- Determines (if possible_tree_copy is True) if the input dataframe corresponds to an existing SPy tree
        -- If it is indeed a copy of a SPy tree, pulls in calculations from the original tree
        -- Otherwise, it converts all items with IDs into references
    -- Ensures all formula parameters are NAN or dict
    """
    df = df.reset_index(drop=True)

    df = df.apply(process_row_properties, axis=1,
                  session=session,
                  status=status,
                  pull_nodes=pull_nodes,
                  keep_parent_column=keep_parent_column)

    def _row_is_from_existing_tree(row):
        if existing_tree_df is None or not _common.present(row, 'ID'):
            return 'new'
        same_id_rows = existing_tree_df[existing_tree_df.ID.str.casefold() == row['ID'].casefold()]
        if len(same_id_rows) != 1:
            return 'new'
        if _common.present(row, 'Type') and row['Type'].casefold() != same_id_rows.Type.iloc[0].casefold():
            return 'new'
        if _common.present(row, 'Name') and row['Name'].casefold() != same_id_rows.Name.iloc[0].casefold():
            return 'modified'
        if _common.present(row, 'Path') and row['Path'].casefold() != same_id_rows.Path.iloc[0].casefold():
            return 'modified'
        return 'pre-existing'

    row_type = df.apply(_row_is_from_existing_tree, axis=1)
    modified_items = df.loc[row_type == 'modified', 'ID'] if 'ID' in df.columns else set()

    # For the nodes that originated from the pre-existing SPy tree we are modifying, we want to pull
    # pre-existing calculations directly.
    formulas_api = FormulasApi(session.client)
    metrics_api = MetricsApi(session.client)
    df.loc[row_type == 'pre-existing', :] = df.loc[row_type == 'pre-existing', :] \
        .apply(pull_calculation, axis=1, formulas_api=formulas_api, metrics_api=metrics_api)

    # For the nodes that originate from places other than the pre-existing SPy tree we are modifying,
    # we want to build references so we create and modify *copies* and not the original items.
    df.loc[row_type != 'pre-existing', :] = df.loc[row_type != 'pre-existing', :] \
        .apply(make_node_reference, axis=1, session=session, formulas_api=formulas_api, metrics_api=metrics_api)

    if 'Formula Parameters' in df.columns:
        df['Formula Parameters'] = df['Formula Parameters'].apply(formula_parameters_to_dict)

    _common.put_properties_on_df(df, types.SimpleNamespace(modified_items=modified_items))

    return df


# Note that the session argument is second in this special case because we call this from pd.DataFrame.apply(),
# which requires that row is the first argument.
def process_row_properties(row, session: Session, status, pull_nodes, keep_parent_column) -> pd.Series:
    if _common.present(row, 'ID') and pull_nodes:
        new_row = pull_node(session, row['ID'])
        _utils.increment_status_df(status, pulled_items=[new_row])
    else:
        new_row = pd.Series(index=_constants.dataframe_columns, dtype='object')

    # In case that properties are specified, but IDs are given, the user-given properties
    # override those pulled from Seeq
    for prop, value in row.items():
        if prop == 'Type' and _common.present(new_row, 'Type'):
            continue
        if prop in ['Path', 'Asset']:
            prop = 'Path'
            value = _path.determine_path(row)
        add_tree_property(new_row, prop, value)

    if not _common.present(new_row, 'Type') and not _common.present(new_row, 'Formula'):
        if _common.present(new_row, 'Measured Item'):
            new_row['Type'] = 'Metric'
        else:
            new_row['Type'] = 'Asset'

    if not _common.present(new_row, 'Path'):
        new_row['Path'] = ''
    new_row['Depth'] = new_row['Path'].count('>>') + 2 if new_row['Path'] else 1

    if keep_parent_column and _common.present(row, 'Parent'):
        new_row['Parent'] = row['Parent']

    return new_row


def make_node_reference(row, session: Session, formulas_api: FormulasApi, metrics_api: MetricsApi) -> pd.Series:
    row = row.copy()
    if _common.present(row, 'ID'):
        if _common.get(row, 'Type') in _constants.data_types and not is_reference(row):
            _metadata.build_reference(session, row)
        elif 'Metric' in _common.get(row, 'Type'):
            row = pull_calculation(row, formulas_api, metrics_api)
        if _common.present(row, 'ID'):
            row['Referenced ID'] = row['ID']
    row['ID'] = np.nan
    return row


def is_reference(row) -> bool:
    if not _common.get(row, 'Referenced ID') or not _common.get(row, 'Formula Parameters'):
        return False
    formula = _common.get(row, 'Formula')
    if formula is not None and re.match(r'^\$\w+$', formula):
        return True
    else:
        return False


def pull_calculation(row, formulas_api: FormulasApi, metrics_api: MetricsApi) -> pd.Series:
    if _common.get(row, 'Type') in _constants.calculated_types and _common.present(row, 'ID'):
        row = row.copy()
        formula_output = formulas_api.get_item(id=row['ID'])  # type: FormulaItemOutputV1
        row['Formula'] = formula_output.formula
        row['Formula Parameters'] = [
            '%s=%s' % (p.name, p.item.id if p.item else p.formula) for p in formula_output.parameters
        ]
    elif 'Metric' in _common.get(row, 'Type') and _common.present(row, 'ID'):
        row = row.copy()
        row['Type'] = 'Metric'

        def str_from_scalar_value_output(scalar_value_output):
            # noinspection PyProtectedMember
            return Item._str_from_scalar_value_dict(Item._dict_from_scalar_value_output(scalar_value_output)).strip()

        def set_metric_value_if_present(column_name, val):
            if val is not None:
                if isinstance(val, ScalarValueOutputV1):
                    row[column_name] = str_from_scalar_value_output(val)
                elif isinstance(val, ItemPreviewWithAssetsV1):
                    row[column_name] = val.id
                else:
                    row[column_name] = val

        metric = metrics_api.get_metric(id=row['ID'])  # type: ThresholdMetricOutputV1
        set_metric_value_if_present('Aggregation Function', metric.aggregation_function)
        set_metric_value_if_present('Bounding Condition', metric.bounding_condition)
        set_metric_value_if_present('Bounding Condition Maximum Duration', metric.bounding_condition_maximum_duration)
        set_metric_value_if_present('Duration', metric.duration)
        set_metric_value_if_present('Measured Item', metric.measured_item)
        set_metric_value_if_present('Metric Neutral Color', metric.neutral_color)
        set_metric_value_if_present('Number Format', metric.number_format)
        set_metric_value_if_present('Period', metric.period)
        set_metric_value_if_present('Process Type', metric.process_type)
        if metric.thresholds:
            thresholds_dict = dict()
            for threshold in metric.thresholds:  # type: ThresholdOutputV1
                # Key can be 'HiHi#FF0000' or 'HiHi'
                key = threshold.priority.name
                if threshold.priority.color:
                    key += threshold.priority.color
                # Value could get pulled as an ID or as a string-ified value
                value = ''
                if not threshold.is_generated and threshold.item:
                    value = threshold.item.id
                elif threshold.value is not None:
                    if isinstance(threshold.value, ScalarValueOutputV1):
                        value = str_from_scalar_value_output(threshold.value)
                    else:
                        value = threshold.value
                if key and value:
                    thresholds_dict[key] = value
            row['Thresholds'] = thresholds_dict

    return row


def pull_node(session: Session, node_id) -> pd.Series:
    """
    Returns a dataframe row corresponding to the item given by node_id
    """
    items_api = _login.get_api(session, ItemsApi)

    item_output = items_api.get_item_and_all_properties(id=node_id)  # type: ItemOutputV1
    node = pd.Series(index=_constants.dataframe_columns, dtype='object')

    # Extract only the properties we use
    node['Name'] = item_output.name
    node['Type'] = item_output.type
    node['ID'] = item_output.id  # If this should be a copy, it'll be converted to 'Referenced ID' later
    for prop in item_output.properties:  # type: PropertyOutputV1
        add_tree_property(node, prop.name, prop.value)
    if 'Metric' in node['Type']:
        node = pull_calculation(node, _login.get_api(session, FormulasApi), _login.get_api(session, MetricsApi))

    return node


def add_tree_property(properties, key, value) -> pd.Series:
    """
    If the property is one which is used by SPy Trees, adds the key+value pair to the dict.
    """
    if key in _constants.dataframe_columns:
        value = _common.none_to_nan(value)
        if isinstance(value, str) and key in ['Cache Enabled', 'Archived', 'Enabled', 'Unsearchable']:
            # Ensure that these are booleans. Otherwise Seeq Server will silently ignore them.
            value = (value.lower() == 'true')
        if key not in properties or not (pd.api.types.is_scalar(value) and pd.isnull(value)):
            properties[key] = value
    return properties


def formula_parameters_to_dict(formula_parameters) -> dict:
    if isinstance(formula_parameters, dict) or (pd.api.types.is_scalar(formula_parameters) and pd.isnull(
            formula_parameters)):
        return formula_parameters

    if isinstance(formula_parameters, str):  # formula_parameters == 'x=2b17adfd-3308-4c03-bdfb-bf4419bf7b3a'
        # handle an empty string case
        if len(formula_parameters) == 0:
            return dict()
        else:
            formula_parameters = [formula_parameters]

    if isinstance(formula_parameters, pd.Series):
        formula_parameters = formula_parameters.tolist()

    formula_dictionary = dict()
    if isinstance(formula_parameters, list):  # formula_parameters == ['x=2b17adfd-3308-4c03-bdfb-bf4419bf7b3a', ...]
        for param in formula_parameters:  # type: str
            split_list = param.split('=')  # ['x', '2b17...']
            if len(split_list) != 2:
                raise SPyException(f'Formula Parameter: {param} needs to be in the format \'paramName=inputItem\'.')
            formula_dictionary[split_list[0].strip()] = split_list[1].strip()
    return formula_dictionary  # output == {'x': '2b17adfd-3308-4c03-bdfb-bf4419bf7b3a'}


def format_formula_parameters(df, status) -> pd.DataFrame:
    """
    For each applicable row in the dataframe, resolve formula parameters from relative path to full path. If the
    referred item does not exist in the dataframe, error.
    :param df: The internal _dataframe to transform for _metadata.push().
    :param status: The status object if an error is encountered.
    :return: A deep copy of the original dataframe, but with fully resolved formula parameters.
    """
    output_df = df.copy()

    output_formula_parameters_column = pd.Series(np.nan, index=output_df.index, dtype='object')

    # Takes relative-path formula parameters and changes them to full path for the ensuing push call
    for idx, row in output_df[output_df['Formula Parameters'].notnull()].iterrows():
        formula_parameters = copy.deepcopy(row['Formula Parameters'])

        for name, item in row['Formula Parameters'].items():
            if not isinstance(item, str) or _common.is_guid(item):
                continue
            item_full_path = _path.get_full_path({'Path': row['Path'], 'Name': item})

            resolved_path, _ = resolve_node_reference(row, item, output_df)
            if resolved_path is None:
                # Validation prevents this error from being raised
                e = SPyValueError(f"Issue resolving formula parameters for item at '{row.Path} >> "
                                  f"{row.Name}'. No matches were found for '{item_full_path}'.")
                status.exception(e, throw=True)
            formula_parameters[name] = resolved_path

        output_formula_parameters_column[idx] = formula_parameters

    output_df['Formula Parameters'] = output_formula_parameters_column
    return output_df


def format_metric_parameters(df) -> pd.DataFrame:
    """
    For each applicable row in the dataframe, resolve the Measured Item and Bounding Condition from relative path
    to full path. Also converts Threshold values from relative path to full row dict.
    :param df: The internal _dataframe to transform for _metadata.push().
    :return: A deep copy of the original dataframe, but with fully resolved Metric references.
    """
    output_df = df.copy()

    output_measured_items_column = pd.Series(np.nan, index=output_df.index, dtype='object')
    output_bounding_conditions_column = pd.Series(np.nan, index=output_df.index, dtype='object')
    output_thresholds_column = pd.Series(np.nan, index=output_df.index, dtype='object')

    for idx, row in output_df[output_df['Type'].str.contains('Metric').fillna(False)].iterrows():
        if not pd.isnull(row['Measured Item']):
            resolved_path, _ = resolve_node_reference(row, row['Measured Item'], output_df)
            if resolved_path:
                output_measured_items_column[idx] = resolved_path
            else:
                output_measured_items_column[idx] = row['Measured Item']

        if not pd.isnull(row['Bounding Condition']):
            resolved_path, _ = resolve_node_reference(row, row['Bounding Condition'], output_df)
            if resolved_path:
                output_bounding_conditions_column[idx] = resolved_path
            else:
                output_bounding_conditions_column[idx] = row['Bounding Condition']

        if not pd.isnull(row['Thresholds']):
            thresholds = copy.deepcopy(row['Thresholds'])

            for key, threshold in row['Thresholds'].items():
                if not isinstance(threshold, str) or _common.is_guid(threshold):
                    continue
                resolved_path, resolved_row = resolve_node_reference(row, threshold, output_df)
                if resolved_path:
                    # Use a dict so _push can differentiate a string Threshold and a reference to another item
                    thresholds[key] = {
                        'Name': resolved_row['Name'],
                        'Path': resolved_row['Path']
                    }

            output_thresholds_column[idx] = thresholds

    output_df['Measured Item'] = output_measured_items_column
    output_df['Bounding Condition'] = output_bounding_conditions_column
    output_df['Thresholds'] = output_thresholds_column
    return output_df


def resolve_node_reference(current_row, referenced_item, df) -> (str, pd.Series):
    """
    Finds the item in the tree that is referenced as an input parameter by current_row.
    E.G. if a calculation 'Cooling Tower >> Area A >> Too Hot' references 'Sensors >> Temperature',
    the 'Cooling Tower >> Area A >> Sensors >> Temperature' row will be returned if it exists.

    :param current_row: The item row being evaluated that contains the reference.
    :param referenced_item: The name or path+name of the item being referenced. Must be at or below the current_row
    asset level.
    :param df: The entire tree dataframe
    :return: The full path string of the referenced item and its row, or None if not found.
    """
    item_full_path = _path.get_full_path({'Path': current_row['Path'], 'Name': referenced_item})
    for _, other_row in df.iterrows():
        if other_row is current_row:
            continue
        if _match.is_node_match(item_full_path, other_row):
            return _path.get_full_path(other_row), other_row
    return None, None
