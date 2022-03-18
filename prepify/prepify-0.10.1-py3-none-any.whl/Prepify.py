from pathlib import Path
import platform
import sys

import PySimpleGUI as sg

import prepify.py.document_layout as dl
# import prepify.py.export_to_docx as ed
import prepify.py.read_doc_form as rdf
import prepify.py.foliation as fo
import prepify.py.guide_sheet as gs
import prepify.py.load_liste as ll
from prepify.py import package
import prepify.py.quires as qu
from prepify.py import edit_settings as es
from prepify.py import edit_foliation_window as efw
from prepify.py import tips

__VERSION = '0.10.1'

if platform.system() == 'Windows':
    WINDOWS = True
    WINDOW_SIZE = (1000, 800)
    RIGHT_CLICK = '<Button-3>'
else:
    WINDOW_SIZE = (600, 400)
    WINDOWS = False
    RIGHT_CLICK = '<Button-2>'

def set_bindings(window: sg.Window):
    window['toc_entry'].bind('<Return>', '-toc')
    window['written_to'].bind('<Return>', '-submit')
    window['written_from'].bind('<Return>', '-submit')
    window['number'].bind('<Return>', '-submit')
    window['quire_to'].bind('<Return>', '-submit')
    window['quire_note'].bind('<Return>', '-submit')
    window['previous_owner'].bind('<Return>', '-submit')
    window['previous_place'].bind('<Return>', '-submit')
    window['previous_shelf'].bind('<Return>', '-submit')
    window['date_sold'].bind('<Return>', '-submit')
    window['ga_number'].bind('<Return>', '-submit')
    window['added_contents'].bind('<Return>', '-submit')

def main_loop(window: sg.Window, foliation: fo.Foliation):
    view_liste = False
    timeout = None
    liste_window = None
    saved = False
    args = sys.argv
    if len(args) > 1:
        load_on_start = args[1]
    else:
        load_on_start = None

    while True:
        
        if load_on_start:
            result = rdf.load_from_saved(window, load_on_start)
            if not result:
                continue
            foliation = result
            settings = es.get_settings()
            saved_path = settings.get('currently_saving')
            window.set_title(f"Prepify v{__VERSION}: {Path(saved_path).name}")
            saved = True
            load_on_start = False

        event, values = window.read(timeout=timeout)

        if event in [sg.WIN_CLOSED, None, sg.WIN_X_EVENT]:
            break

        elif event == 'New':
            answer = sg.popup_ok_cancel('Clear All Data and Startover?', title='Clear All')
            if answer == 'OK':
                new_doc = Path(__file__).parent.joinpath('resources/new.csntm').as_posix()
                foliation = rdf.load_from_saved(window, new_doc, store_saved_path=False)
                saved = False
                window.set_title(f"Prepify v{__VERSION}: NEW*")

        elif event == 'Save':
            rdf.save_doc_data(values, window, foliation, saved=saved)
        elif event == 'Save As':
            saved_path = rdf.save_doc_data(values, window, foliation, saved=saved, save_as=True)
            if saved_path:
                saved = True
                window.set_title(f"Prepify v{__VERSION}: {Path(saved_path).name}")

        elif event == 'Load from Saved File':
            result = rdf.load_from_saved(window)
            if not result:
                continue
            foliation = result
            settings = es.get_settings()
            saved_path = settings.get('currently_saving')
            window.set_title(f"Prepify v{__VERSION}: {Path(saved_path).name}")
            saved = True

        # PARSE PREP DOC
        elif event in {'number', 'written_from', 'written_to', 'single_folio_a', 'single_folio_b'}:
            fo.enforce_spin(values, window)
            if event == 'number':
                if values['number'] != '':
                    window['Insert after Selected'].update(visible=True)
                else:
                    window['Insert after Selected'].update(visible=False)
            elif event in {'written_from', 'written_to', 'single_folio_a', 'single_folio_b'}:
                if event in {'written_from', 'single_folio_a', 'single_folio_b'} and values['folio_type'] == 'Single Folio Side':
                    if (not values['single_folio_a'] and not values['single_folio_b']) or values['written_from'] == '':
                        window['Insert after Selected'].update(visible=False)
                    else:
                        window['Insert after Selected'].update(visible=True)
                elif values['written_from'] == '' or values['written_to'] == '':
                    window['Insert after Selected'].update(visible=False)
                    window['even_on_recto'].update(visible=False)
                else:
                    window['Insert after Selected'].update(visible=True)
                    if values['folio_type'] == 'Paginated':
                        window['even_on_recto'].update(visible=True)
                

        elif event in {'Add to Bottom', 'Insert after Selected', 'Insert at Beginning'}:
            fo.submit_section(values, window, foliation, event)
            rdf.hide_all_folio_options(window)

        elif event in {'written_to-submit', 'written_from-submit', 'number-submit'}:
            if not window['Insert after Selected'].visible:
                continue
            fo.submit_section(values, window, foliation, 'Insert after Selected')
            rdf.hide_all_folio_options(window)

        elif event == 'Remove Selected' and values['foliation'] != []:
            fo.remove_section(values, window, foliation)
            rdf.decolor_buttons(window, foliation.sections)

        elif event in {'Frontmatter', 'Body', 'Backmatter'}:
            fo.submit_main_section(values, window, event, foliation, 'Add')

        elif event in {'Frontmatter: Insert after Selected', 'Frontmatter: Insert at Beginning',
                        'Body: Insert after Selected', 'Body: Insert at Beginning',
                        'Backmatter: Insert after Selected', 'Backmatter: Insert at Beginning'}:
            items = event.split(': ')
            fo.submit_main_section(values, window, items[0], foliation, items[1])

        elif event == 'Other':
            fo.submit_other_section(values, window, foliation, 'Add')

        elif event in {'Other: Insert after Selected', 'Other: Insert at Beginning'}:
            items = event.split(': ')
            fo.submit_other_section(values, window, foliation, items[1])

        elif event == 'calculate' and foliation.sections != []:
            foliation.calculate_total_images(values, window)
        elif event == 'Create Spreadsheet' and foliation.sections != []:
            try:
                foliation.create_xslx()
                fo.open_excel()
            except IndexError:
                print('There are no folios to add')
        elif event == 'Create Decollated Spreadsheet':
            try:
                foliation.create_xslx(decollated=True)
                fo.open_excel()
            except IndexError:
                print('There are no folios to add')
        elif event == 'Create Decollated and Reverse "A" side':
            try:
                foliation.create_xslx(reverse_a_side=True)
                fo.open_excel()
            except IndexError:
                print('There are no folios to add')
        elif event == 'Decollate Existing Spreadsheet':
            try:
                if decollated := gs.decollate_existing_spreadsheet():
                    fo.open_excel(filename=decollated)
            except Exception as e:
                sg.popup_ok(f'Something David did not anticipate happened.\n{e}', title='Uhoh')

        elif event in {'Add Quire', 'quire_to-submit', 'quire_note-submit'}:
            qu.add_quire(values, window)
        elif event == 'remove_quire' and values['quire_structure'] != []:
            rdf.remove_selected_from_listbox(values, window, 'quire_structure')
        # elif event == 'Export to DOCX':
        #     data = rdf.get_doc_data(values, window)
        #     ed.to_docx(data)
        elif event in {'refresh_description', 'ga_number-submit'}:
            ll.load_cf_intf(values, window)
            rdf.load_cf_csntm(values, window)
        elif event == 'import_toc':
            gs.import_toc(window)
        elif event in {'add_toc', 'toc_entry-toc'}:
            rdf.add_toc_entry(values, window)
        elif event == 'remove_toc':
            rdf.remove_selected_from_listbox(values, window, 'table_of_contents')
        elif event == 'table_of_contents':
            rdf.reveal_add_contents(values, window)
        elif event == 'added_contents-submit':
            rdf.add_contents(values, window)

        elif event == 'package':
            package.package(values, window)
        elif event in {'add_former_institute', 'previous_owner-submit', 'previous_place-submit', 'previous_shelf-submit', 'date_sold-submit'}:
            rdf.add_former_institute(values, window)
        elif event == 'remove_former_institute':
            rdf.remove_selected_from_listbox(values, window, 'former_owners')
        elif event == 'sort_toc':
            rdf.sort_toc(window)
        elif event == 'Edit Selected':
            if len(values['foliation']) != 1:
                continue
            sel = foliation.get_section_by_index(values['foliation'][0])
            if not sel:
                continue
            if sel['main_section']:
                sg.popup_ok('Main Sections cannot be edited. Instead, replace and remove.', title='FYI')
                continue
            foliation_values = efw.edit_foliation_window(sel['foliation_type'], sel.get('number', ''), sel.get('written_from', ''), sel.get('written_to', ''))
            if not foliation_values:
                continue
            foliation_values['foliation'] = values['foliation']
            fo.submit_section(foliation_values, window, foliation, 'replace')

    # on exit
        elif event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, None, 'Exit', sg.WIN_X_EVENT):
            if sg.popup_yes_no('Do you really want to exit?', title='Confirm Exit') == 'Yes':
                break

        ##################
        # disable/enable #
        ##################
        elif event == 'exact_year?':
            has_exact_year = not values['exact_year?']
            window['exact_year'].update(disabled=has_exact_year)
        elif event in rdf.DISABLED:
            elem = event.replace('has_', '')
            elem = f'{elem}_notes'
            window[elem].update(disabled=not values[event])
        elif event in ('lectionary', 'continuous'):
            v = not values['lectionary']
            window['paschal'].update(disabled=v)
            window['sanctoral'].update(disabled=v)
            window['sk'].update(disabled=v)
            window['esk'].update(disabled=v)
            window['e'].update(disabled=v)
            window['k'].update(disabled=v)
        elif event == 'additional_nt_mss?':
            window['additional_nt_mss'].update(disabled=not values['additional_nt_mss?'])
        elif event == 'other_additional_mss?':
            window['other_additional_mss'].update(disabled=not values['other_additional_mss?'])
        elif event == 'folio_type':
            if values['folio_type'] == 'Single Folio Side':
                sg.popup_ok(tips.SINGLE_FOLIO_WARNING, title='Caution')
            rdf.hide_unhide_foliation(values, window)


        #####################
        # View Liste Window #
        #####################
        elif event == 'view_liste':
            view_liste = True
            timeout = 100
            liste_entry = ll.get_full_liste(values)
            liste_window = sg.Window('Full Liste Entry', ll.full_liste_layout(liste_entry), size=WINDOW_SIZE)
        if view_liste:
            ev2, _, = liste_window.read(timeout=100)
            if ev2 in ('Close', sg.WIN_CLOSED, sg.WIN_X_EVENT, None):
                liste_window.close()
                view_liste = False
                timeout = None
    try:
        liste_window.close()
    except:
        pass

def main():
    sg.set_options(font=('Helvetica', '14'), dpi_awareness=True)
    sg.theme('LightBrown3')
    window = sg.Window(
        f'Prepify v{__VERSION}: NEW*', dl.layout(WINDOWS), 
        resizable=True, 
        enable_close_attempted_event=True,
        debugger_enabled=False,
        ).finalize()
    set_bindings(window)
    foliation = fo.Foliation()
    
    # try:
    main_loop(window, foliation)
    # except Exception as e:
    #     print('Catastrophic Crash Caught')
    #     sg.popup_ok(f'Prepify crashed for a reason unknown to DF.\n(For David: {e})', title='BUMMER')
    try:
        window.close()
    except:
        pass # window already destroyed
    es.update_settings('currently_saving', None)

if __name__ == '__main__':
    main()
