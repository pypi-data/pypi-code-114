import PySimpleGUI as sg

def enforce_spin(values: dict, window: sg.Window):
    for value in ['number', 'written_from', 'written_to']:
        if not values[value].isnumeric() or values[value] == '0':
            window[value].update(value='')

def hide_unhide(folio_type: str, window: sg.Window):
    if folio_type in {'Front Inside Cover', 'Back Inside Cover'}:
        n = False
        f = False
        t = False
        e = False
        s = False
    elif folio_type in {'Foliated', 'Paginated'}:
        if folio_type == 'Foliated':
            e = False
        else:
            e = True
        n = False
        f = True
        t = True
        s = False
    elif folio_type == 'Unnumbered':
        n = True
        f = False
        t = False
        e = False
        s = False
    elif folio_type == 'Single Folio Side':
        n = False
        f = True
        t = False
        e = False
        s = True
    window['number_title'].update(visible=n)
    window['number'].update(visible=n)
    window['written_range_title'].update(visible=f)
    window['written_from'].update(visible=f)
    window['n-dash'].update(visible=t)
    window['written_to'].update(visible=t)
    window['even_on_recto'].update(visible=e)
    window['single_folio_a'].update(visible=s)
    window['single_folio_b'].update(visible=s)
    window['supplemental_folio'].update(visible=s)

def edit_foliation_window(
            folio_type: str, 
            number: str = '', 
            written_from: str = '', 
            written_to: str = '', 
            even_on_recto: bool = False, 
            single_folio_a: bool = False,
            single_folio_b: bool = False,
            supplemental: bool = False
    ):
    # initial state
    
    cat = [
        'Front Inside Cover',
        'Back Inside Cover',
        'Unnumbered',
        'Foliated',
        'Paginated',
        'Single Folio Side'
        ]
    four = (4, 1)
    layout = [
        [sg.Drop(cat, default_value=folio_type, k='folio_type', readonly=True, enable_events=True, expand_x=True)],
        [
            sg.pin(sg.T('Number: ', key='number_title', visible=False)),
            sg.pin(sg.Input('', k='number', size=four, enable_events=True, visible=False, expand_x=True), shrink=False, expand_x=True),
        ],
        [
            sg.pin(sg.T('Written: ', key='written_range_title', visible=False)),
            sg.pin(sg.Input('', k='written_from', size=four, enable_events=True, visible=False)),
            sg.pin(sg.T('–', key='n-dash', visible=False)),
            sg.pin(sg.Input('', k='written_to', size=four, enable_events=True, visible=False)),
        ],
        [sg.pin(sg.Checkbox('Even on Recto (rare)', key='even_on_recto', visible=False))],
        [
            sg.pin(sg.Radio('A side', 'single_folio_side', default=False, key='single_folio_a', enable_events=True, visible=False)),
            sg.pin(sg.Radio('B side', 'single_folio_side', default=False, key='single_folio_b', enable_events=True, visible=False))
            ],
        [sg.pin(sg.Checkbox('Supplemental', key='supplemental_folio', visible=False))],
        [sg.Button('Submit', bind_return_key=True, expand_x=True), sg.Button('Cancel', expand_x=True)],
    ]

    window = sg.Window('Add Subsection', layout).finalize()
    hide_unhide(folio_type, window)
    while True:
        event, values = window.read()
        if event in {'Cancel', None, sg.WINDOW_CLOSED}:
            window.close()
            return
        elif event == 'Submit':
            window.close()
            return values
        elif event in {'number', 'written_from', 'written_to'}:
            enforce_spin(values, window)
        elif event == 'folio_type':
            hide_unhide(values['folio_type'], window)
