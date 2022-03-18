# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashColorful(Component):
    """A DashColorful component.
A color picker powered by react-colorful
A toggle button is included or can be disabled with ``toggleable=False``.
Common style aspects goes on the container of the picker, hidden by default.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- active (boolean; optional):
    Show the color picker.

- as_string (boolean; optional):
    The value will always be a string, usable directly in styles.
    ``toggle_button_color`` requires a string value or hex type.

- class_name (string; optional)

- style (boolean | number | string | dict | list; optional)

- toggle_button (a list of or a singular dash component, string or number; optional):
    Content of the toggle button.

- toggle_button_color (boolean; default True):
    Use a square with background color from the value as the toggle
    button.

- toggle_direction (a value equal to: 'top', 'top-left', 'top-right', 'left', 'right', 'bottom', 'bottom-left', 'bottom-right'; default 'top-left'):
    Direction to open the color picker on toggle.

- toggle_on_choose (boolean; default True):
    Close the color picker when a value is selected.

- toggle_on_choose_delay (number; default 2500):
    Delay before closing the modal when the.

- toggleable (boolean; default True):
    Add a toggle button to activate the color picker.

- type (a value equal to: 'hex', 'rgb', 'rgba', 'hsl', 'hsla', 'hsv', 'hsva'; default 'hex'):
    Type of color.

- value (string; optional):
    Current color value."""
    @_explicitize_args
    def __init__(self, value=Component.UNDEFINED, type=Component.UNDEFINED, toggleable=Component.UNDEFINED, toggle_button=Component.UNDEFINED, toggle_on_choose=Component.UNDEFINED, toggle_on_choose_delay=Component.UNDEFINED, toggle_direction=Component.UNDEFINED, active=Component.UNDEFINED, toggle_button_color=Component.UNDEFINED, as_string=Component.UNDEFINED, class_name=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'active', 'as_string', 'class_name', 'style', 'toggle_button', 'toggle_button_color', 'toggle_direction', 'toggle_on_choose', 'toggle_on_choose_delay', 'toggleable', 'type', 'value']
        self._type = 'DashColorful'
        self._namespace = 'dash_colorful'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'active', 'as_string', 'class_name', 'style', 'toggle_button', 'toggle_button_color', 'toggle_direction', 'toggle_on_choose', 'toggle_on_choose_delay', 'toggleable', 'type', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashColorful, self).__init__(**args)
