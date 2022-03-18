from pathlib import Path

import PySimpleGUI as sg
import pandas as pd

import prepify.py.edit_settings as es

def get_spreadsheet_data(excel_file):
    try:
        df = pd.read_excel(excel_file)
    except PermissionError:
        sg.popup_ok('Close or rename the Excel file first.', title='Excel File Already Open')
        return
    df = df.fillna('')
    return df.to_dict('records')

def create_toc(list_of_dicts: list):
    toc = []
    for row in list_of_dicts:
        if row['Contents'] in [None, '', 'NaN']:
            continue
        if row['Actual Folio'] == '':
            folio = row['Image #']
        else:
            folio = row['Actual Folio']
        toc.append(
            f'{folio}: {row["Contents"]}'
        )
    return toc

def import_toc(window: sg.Window):
    settings = es.get_settings()
    excel_file = sg.popup_get_file('', no_window=True, initial_folder=settings['excel_folder'], file_types=(('Excel File', '*.xlsx'),))
    if not excel_file:
        return
    excel_folder = Path(excel_file).parent.as_posix()
    es.update_settings('excel_folder', excel_folder)
    list_of_dicts = get_spreadsheet_data(excel_file)
    table_of_contents = create_toc(list_of_dicts)
    window['table_of_contents'].update(values=table_of_contents)
    return table_of_contents

def minimally_valid(values: dict, submitted):
    if submitted == []:
        sg.popup_ok('At least one item of foliation must be completed.', title='Not so fast...')
        return
    if values['ga_number'] == '' or values['csntm_id'] == '':
        sg.popup_ok('Both the GA Number and CSNTM ID must be entered.', title='Form Incomplete')
        return
    if values['guide_sheet'] == '':
        sg.popup_ok('The Guide Sheet is crucial for the imaging team and must be selected.', title='Guide Sheet Required')
        return
    if values['project_folder'] == '':
        sg.popup_ok('A Project Folder must be selected.\nThis is where the prepdoc files will be saved.', title='No Project Folder')
        return
    return True

def decollate_guide(temp_xlsx):
    folios = get_spreadsheet_data(temp_xlsx)
    if not folios:
        return
    guide_a = []
    guide_b = []
    for row in folios:
        if row['Image #'].endswith('a'):
            guide_a.append(row)
        elif row['Image #'].endswith('b'):
            guide_b.append(row)
    return guide_a + guide_b

def decollate_existing_spreadsheet():
    settings = es.get_settings()
    file_path = sg.popup_get_file(
        '', initial_folder=settings.get('prepdoc_folder'), 
        file_types=(('Excel Files', '*.xlsx'),),
        no_window=True)
    if not file_path:
        return
    try:
        decollated_dict = decollate_guide(file_path)
    except Exception as e:
        sg.popup_ok(f"Can't open that file for some reason. See below:\n{e}")
    df = pd.DataFrame.from_dict(decollated_dict)
    df.index += 1
    ####
    try:
        writer = pd.ExcelWriter(file_path.replace('.xlsx', '-decollated.xlsx'))
    except PermissionError:
        sg.popup_ok('Close or rename the open Excel file before generating another', title='File Write Denied')
        return
    except Exception as e:
        sg.popup_ok(f'This unexpected (by David) error happend:\n{e}')
    df.to_excel(writer, sheet_name='Guide', index=False, na_rep='')
    for column in df:
        column_length = max(df[column].astype(str).map(len).max(), len(column))
        col_idx = df.columns.get_loc(column)
        writer.sheets['Guide'].set_column(col_idx, col_idx, column_length)
    writer.save()
    return file_path
