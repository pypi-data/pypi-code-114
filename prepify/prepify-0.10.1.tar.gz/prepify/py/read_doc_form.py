from datetime import datetime
import json
from operator import iconcat
from pathlib import Path
import os

from natsort import natsorted
import PySimpleGUI as sg

import prepify.py.edit_settings as es
import prepify.py.foliation as fo



DISABLED = (
    'has_illumination',
    'has_lection',
    'has_icon',
    'has_commentary',
    'has_ektheses',
    'has_otmarks',
    'has_neume',
    'has_carpianus',
    'has_rubrication',
    'has_headings',
    'has_kephalaia',
    'has_euthalian_apparatus',
    'has_euthalian_marks',
    'has_canon_tables',
    'has_canon_marks',
)

def write_prep_file(filepath: str, to_save: dict, save_as: bool):
    destination = Path(filepath).as_posix()
    temp_name = datetime.now().strftime('%Y%j%H%M%f')
    temp_path = Path(filepath).parent.joinpath(temp_name)
    try:
        with open(temp_path, 'w', encoding='utf-8') as f:
            json.dump(to_save, f, ensure_ascii=False)
    except Exception as e:
        sg.popup_ok(f"Prepify doesn't seem to have permission to write a file to\n{temp_path.parent.as_posix()}.\nSaving to a non-cloud-based directory might work.\n(For David: {e}", "Cannot Save")
        return
    try:
        os.remove(destination)
    except Exception as e:
        print(f'{destination}\nmust not exist yet')
        # sg.popup_ok(f'There was a problem deleting the old file before writing the new one. David was not sure if this could happen, but just in case, you get this message instead of a crashing Prepify.\n{e}', title='Not sure what to say...')
        # return
    try:
        os.rename(temp_path.as_posix(), destination)
    except Exception as e:
        sg.popup_ok(f"Something screwy happend. The prepdoc was correctly saved as a temp file:\n{temp_path}\nbut Prepify was not allowed to rename the temp file to the desired name.\nI recommend trying again.\n(For David: {e}")
        return
    if save_as:
        sg.popup_ok(f"The prepdoc was succesfully saved.\n\n{destination}", title="Saved!")
    else:
        sg.popup_quick_message(f"The prepdoc was succesfully saved.\n\n{destination}")

def load_doc_data(values: dict, window: sg.Window):
    for key, value in values.items():
        if key == 'sections':
            key = 'foliation'
        elif key == 'has_icons':
            key = 'has_icon'
        elif key == 'icons_notes':
            key = 'icon_notes'
        elif key == 'guide_sheet':
            continue
        elif key in {'guide_sheet', 'project_folder'}:
            continue
        
        if isinstance(window[key], (sg.Input, sg.Multiline, sg.Checkbox, sg.Radio, sg.Spin)):
            window[key].update(value=value)
        elif isinstance(window[key], sg.Listbox):
            window[key].update(values=value)
        
    if values.get('foliation') or values.get('foliation') == []:
        foliation = fo.Foliation(values['foliation'])
    else:
        foliation = fo.Foliation(values['sections'])
    window['foliation'].update(values=foliation.as_sg_tree())
    return foliation

def get_doc_data(values: dict, window: sg.Window, foliation: fo.Foliation): # read form
    prepdoc = {}
    prepdoc['foliation'] = foliation.sections
    for key, value in values.items():
        if isinstance(window[key], sg.Listbox):
            prepdoc[key] = window[key].get_list_values()
        elif isinstance(window[key], (sg.Input, sg.Multiline, sg.Radio, sg.Checkbox, sg.Spin)):
            prepdoc[key] = value
    return prepdoc

def save_doc_data(values: dict, window: sg.Window, foliation: fo.Foliation, saved: bool = False, save_as: bool = False):
    settings = es.get_settings()
    to_save = get_doc_data(values, window, foliation)
    if save_as:
        save_path = sg.popup_get_file(
            '', no_window=True, file_types=(('CSNTM Files', '*.csntm'),), 
            initial_folder=settings.get('prepdoc_folder'), save_as=True)
        if not save_path:
            return
        es.update_settings('currently_saving', save_path)
    else:
        save_path = settings.get('currently_saving')
        if not saved:
            sg.popup_ok('First "Save As" by right-clicking (Windows) or two-finger-clicking (macOS) the "Save" button.')
            return
    write_prep_file(save_path, to_save, save_as)
    es.update_settings('prepdoc_folder', Path(save_path).parent.as_posix())
    return save_path

def load_from_saved(window: sg.Window, load_on_start: str = None, store_saved_path: bool = True):
    settings = es.get_settings()
    if load_on_start:
        file_path = load_on_start
    else:
        file_path = sg.popup_get_file(
            '', no_window=True, file_types=(('CSNTM Files', ('*.csntm', '*.json')),), 
            initial_folder=settings['prepdoc_folder'])
    if not file_path:
        return
    print(file_path)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            values = json.load(f)
    except Exception as e:
        sg.popup_ok(f'Could not open that file. See error below\n{e}')
        return
    if store_saved_path:
        es.update_settings('currently_saving', file_path)
        es.update_settings('prepdoc_folder', Path(file_path).parent.as_posix())
    foliation = load_doc_data(values, window)
    return foliation

def update_cf_intf(liste_entry: dict, window: sg.Window, ga: str, shelf: dict):
    '''Update the "Cf. INTF" tab values with offline data from
    INTF's database.'''
    window['intf_GA Number'].update(value=ga)
    window['intf_shelf'].update(value=shelf['shelfNumber'])
    window['intf_contents'].update(value=liste_entry.get('content_summary', ''))
    window['intf_date'].update(value=f"{liste_entry.get('originYear', {}).get('content', '')} {liste_entry.get('originYear', {}).get('early', '')}–{liste_entry.get('originYear', {}).get('late', '')}")
    window['intf_material'].update(value=liste_entry['material'])
    window['intf_leaves'].update(value=shelf['leavesCount'])
    window['intf_columns'].update(value=liste_entry.get('columns', ''))
    # format line count
    if liste_entry.get('lineCount', {}).get('lineCountMax', ''):
        line_count = f"{liste_entry['lineCount']['lineCountMin']}–{liste_entry['lineCount']['lineCountMax']}"
    else:
        line_count = liste_entry.get('lineCount', {}).get('lineCountMin', '')
    window['intf_lines'].update(value=line_count)
    # format width
    if liste_entry.get('width'):
        if liste_entry['width'].get('widthMax'):
            width = f"{liste_entry['width']['widthMin']}–{liste_entry['width']['widthMax']}"
        else:
            width = liste_entry['width'].get('widthMin')
    else:
        width = ''
    # format height
    if liste_entry.get('height'):
        if liste_entry['height'].get('heightMax'):
            height = f"{liste_entry['height']['heightMin']}–{liste_entry['height']['heightMax']}"
        else:
            height = liste_entry['height'].get('heightMin')
    else:
        height = ''
    if width == '' and height == '':
        dimensions = ''
    else:
        dimensions = f'{width} W\n{height} H'
    window['intf_dimensions'].update(value=dimensions)

def parse_dimensions(values):
    if values['width_min'] == values['width_max'] or values['width_max'] == 0:
        width = values['width_min']
    else:
        width = f'{values["width_min"]}–{values["width_max"]}'
    if values['height_min'] == values['height_max'] or values['height_max'] == 0:
        height = values['width_min']
    else:
        height = f'{values["height_min"]}–{values["height_max"]}'
    depth = f'{values["depth_bottom"]} (b) {values["depth_top"]} (t)'
    return width, height, depth

def format_content(values):
    content = ''
    options = (
        ('gospels', 'e'), 
        ('acts', 'a'), 
        ('catholic', 'c'), 
        ('paul', 'p'), 
        ('revelation', 'r'), 
        )
    for item in options:
        if values[f'biblical_content_{item[0]}']:
            content = f'{content.lstrip()}{item[1]}'
    if values['biblical_content_specific'] != '':
        content = f'{content}: {values["biblical_content_specific"]}'
    if values['biblical_content_incomplete']:
        content = f'{content} †'
    return content

def format_date(values):
    if values['exact_year?']:
        date = values['exact_year']
    elif values['date_range_start'] == 0 and values['date_range_end'] == 0:
        date = '—'
    else:
        date = f'{values["date_range_start"]}–{values["date_range_end"]}'
    return date

def format_material(values):
    for m in ('papyrus', 'parchment', 'paper'):
        if values[m]:
            break
    else:
        m = '—'
    return m

def format_lines(values):
    if values['lines_max'] == 0 or values['lines_min'] == values['lines_max']:
        lines = values['lines_min']
    else:
        lines = f'{values["lines_min"]}–{values["lines_max"]}'
    if lines == 0:
        lines = '—'
    return lines

def load_cf_csntm(values: dict, window: sg.Window):
    window['csntm_GA Number'].update(value=values['ga_number'])
    window['csntm_shelf'].update(value=values['shelf_number'])
    content = format_content(values)
    window['csntm_contents'].update(value=content)
    date = format_date(values)
    window['csntm_date'].update(value=date)
    # material
    material = format_material(values)
    window['csntm_material'].update(value=material)
    # leaves
    window['csntm_leaves'].update(value=values['number_of_leaves'])
    window['csntm_columns'].update(value=values['number_of_columns'])
    # lines
    lines = format_lines(values)
    window['csntm_lines'].update(value=lines)
    # dimensions
    width, height, depth = parse_dimensions(values)
    if width == '' and height == '':
        dimensions = ''
    else:
        dimensions = f'{width} cm W\n{height} cm H\n{depth} cm D'
    window['csntm_dimensions'].update(value=dimensions)

def add_former_institute(values: dict, window: sg.Window):
    previous_owners = window['former_owners'].get_list_values()
    owner = values['previous_owner']
    place = values['previous_place']
    shelf = values['previous_shelf']
    date = values['date_sold']
    if owner == place == shelf == '':
        sg.popup_ok('At least one value is required between owner, place, and shelf.', title='Missing Value')
        return
    elif owner == place == '':
        new_entry = f'Shelf Number: {shelf} — {date}'
    elif owner == shelf == '':
        new_entry = f'Place: {place} — {date}'
    elif place == shelf == '':
        new_entry = f'Owner: {owner} — {date}'
    elif owner == '':
        new_entry = f'({place}): {shelf} — {date}'
    elif place == '':
        new_entry = f'{owner}: {shelf} — {date}'
    elif shelf == '':
        new_entry = f'{owner} ({place}) — {date}'
    else:
        new_entry = f'{owner} ({place}): {shelf} — {date}'
    previous_owners.append(new_entry)
    window['former_owners'].update(values=previous_owners)

def remove_selected_from_listbox(values: dict, window, key: str):
    listbox_contents = window[key].get_list_values()
    new_list = []
    for item in listbox_contents:
        if item in values[key]:
            continue
        new_list.append(item)
    window[key].update(values=new_list)

def add_toc_entry(values: dict, window: sg.Window):
    toc = window['table_of_contents'].get_list_values()
    toc.append(values['toc_entry'])
    window['table_of_contents'].update(values=toc)
    window['toc_entry'].update('')

def sort_toc(window):
    items = window['table_of_contents'].get_list_values()
    items = natsorted(items)
    window['table_of_contents'].update(values=items)

def decolor_buttons(window, sections: list[dict]):
    for section in ('Frontmatter', 'Body', 'Backmatter'):
        window[section].update(button_color='#046380')
        window[section].update(disabled=False)
    for section in sections:
        if section['main_section']:
            try:
                window[section['main_section']].update(button_color='#05a366')
            except KeyError:
                pass

def hide_all_folio_options(window):
    window['number_title'].update(visible=False)
    window['number'].update(visible=False)
    window['number'].update(value='')
    window['written_from'].update(visible=False)
    window['written_from'].update(value='')
    window['n-dash'].update(visible=False)
    window['written_to'].update(visible=False)
    window['written_to'].update(value='')
    window['Insert after Selected'].update(visible=False)
    window['written_range_title'].update(visible=False)
    window['even_on_recto'].update(visible=False)
    window['single_folio_a'].update(value=False)
    window['single_folio_b'].update(value=False)
    window['single_folio_a'].update(visible=False)
    window['single_folio_b'].update(visible=False)
    window['supplemental_folio'].update(visible=False)
    window['supplemental_folio'].update(value=False)

def hide_unhide_foliation(values: dict, window: sg.Window):
    if values['folio_type'] in {'Front Inside Cover', 'Back Inside Cover'}:
        window['number_title'].update(visible=False)
        window['number'].update(visible=False)
        window['number'].update(value='')
        window['written_from'].update(visible=False)
        window['written_from'].update(value='')
        window['n-dash'].update(visible=False)
        window['written_to'].update(visible=False)
        window['written_to'].update(value='')
        window['Insert after Selected'].update(visible=True)
        window['written_range_title'].update(visible=False)
        window['even_on_recto'].update(value=False)
        window['single_folio_a'].update(value=False)
        window['single_folio_b'].update(value=False)
        window['single_folio_a'].update(visible=False)
        window['single_folio_b'].update(visible=False)
        window['supplemental_folio'].update(visible=False)
        window['supplemental_folio'].update(value=False)
    elif values['folio_type'] == 'Unnumbered':
        window['written_from'].update(visible=False)
        window['written_from'].update(value='')
        window['written_to'].update(visible=False)
        window['written_to'].update(value='')
        window['number_title'].update(visible=True)
        window['number'].update(visible=True)
        window['number'].update(value='')
        window['n-dash'].update(visible=False)
        window['Insert after Selected'].update(visible=False)
        window['written_range_title'].update(visible=False)
        window['even_on_recto'].update(value=False)
        window['single_folio_a'].update(value=False)
        window['single_folio_b'].update(value=False)
        window['single_folio_a'].update(visible=False)
        window['single_folio_b'].update(visible=False)
        window['supplemental_folio'].update(visible=False)
        window['supplemental_folio'].update(value=False)
    elif values['folio_type'] in {'Foliated', 'Paginated'}:
        window['written_range_title'].update(visible=True)
        window['written_from'].update(visible=True)
        window['written_from'].update(value='')
        window['n-dash'].update(visible=True)
        window['written_to'].update(visible=True)
        window['written_to'].update(value='')
        window['number'].update(visible=False)
        window['number'].update(value='')
        window['Insert after Selected'].update(visible=False)
        window['even_on_recto'].update(visible=False)
        window['even_on_recto'].update(value=False)
        window['single_folio_a'].update(value=False)
        window['single_folio_b'].update(value=False)
        window['single_folio_a'].update(visible=False)
        window['single_folio_b'].update(visible=False)
        window['supplemental_folio'].update(visible=False)
        window['supplemental_folio'].update(value=False)
    elif values['folio_type'] == 'Single Folio Side':
        window['written_range_title'].update(visible=True)
        window['written_from'].update(visible=True)
        window['written_from'].update(value='')
        window['n-dash'].update(visible=False)
        window['written_to'].update(visible=False)
        window['written_to'].update(value='')
        window['number'].update(visible=False)
        window['number'].update(value='')
        window['Insert after Selected'].update(visible=False)
        window['even_on_recto'].update(visible=False)
        window['even_on_recto'].update(value=False)
        window['single_folio_a'].update(value=False)
        window['single_folio_b'].update(value=False)
        window['single_folio_a'].update(visible=True)
        window['single_folio_b'].update(visible=True)
        window['supplemental_folio'].update(visible=True)
        window['supplemental_folio'].update(value=False)

def reveal_add_contents(values: dict, window: sg.Window):
    if len(values['table_of_contents']) != 1:
        window['add_contents_label'].update('')
        window['added_contents'].update(visible=False)
        return
    table_of_contents = window['table_of_contents'].get_list_values()
    i = window['table_of_contents'].get_indexes()[0]
    selection = table_of_contents[i]
    if ':' in selection:
        window['add_contents_label'].update('Add Contents:')
        window['added_contents'].update(visible=True)
        window['table_of_contents'].set_value(i)
        window['added_contents'].update(selection)
        window['added_contents'].set_focus()

    else:
        window['add_contents_label'].update(value='Add Contents:')
        window['added_contents'].update(visible=True)
        window['table_of_contents'].set_value(i)
        window['added_contents'].update('')
        window['added_contents'].set_focus()

def add_contents(values: dict, window: sg.Window):
    if len(values['table_of_contents']) != 1:
        return
    table_of_contents = window['table_of_contents'].get_list_values()
    i = window['table_of_contents'].get_indexes()[0]
    selection = table_of_contents[i]
    if values['added_contents'] == '':
        return
    if ':' in selection:
        new_selection = values['added_contents']
    else:
        new_selection = f"{selection}: {values['added_contents']}"
    table_of_contents[i] = new_selection
    window['table_of_contents'].update(values=table_of_contents)
    window['added_contents'].update(value='')
    window['added_contents'].update(visible=False)
    window['add_contents_label'].update('')
