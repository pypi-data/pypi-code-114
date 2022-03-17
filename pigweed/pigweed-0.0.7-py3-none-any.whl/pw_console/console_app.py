# Copyright 2021 The Pigweed Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""ConsoleApp control class."""

import asyncio
import builtins
import functools
import logging
import os
from pathlib import Path
import sys
from threading import Thread
from typing import Any, Callable, Iterable, List, Optional, Tuple, Union

from jinja2 import Environment, FileSystemLoader, make_logging_undefined
from prompt_toolkit.clipboard.pyperclip import PyperclipClipboard
from prompt_toolkit.layout.menus import CompletionsMenu
from prompt_toolkit.output import ColorDepth
from prompt_toolkit.application import Application
from prompt_toolkit.filters import Condition
from prompt_toolkit.styles import (
    DynamicStyle,
    merge_styles,
)
from prompt_toolkit.layout import (
    ConditionalContainer,
    Float,
    Layout,
)
from prompt_toolkit.widgets import FormattedTextToolbar
from prompt_toolkit.widgets import (
    MenuContainer,
    MenuItem,
)
from prompt_toolkit.key_binding import KeyBindings, merge_key_bindings
from prompt_toolkit.history import (
    FileHistory,
    History,
    ThreadedHistory,
)
from ptpython.layout import CompletionVisualisation  # type: ignore
from ptpython.key_bindings import (  # type: ignore
    load_python_bindings, load_sidebar_bindings,
)

from pw_console.console_prefs import ConsolePrefs
from pw_console.help_window import HelpWindow
from pw_console.command_runner import CommandRunner
import pw_console.key_bindings
from pw_console.log_pane import LogPane
from pw_console.log_store import LogStore
from pw_console.pw_ptpython_repl import PwPtPythonRepl
from pw_console.python_logging import all_loggers
from pw_console.quit_dialog import QuitDialog
from pw_console.repl_pane import ReplPane
import pw_console.style
import pw_console.widgets.checkbox
import pw_console.widgets.mouse_handlers
from pw_console.window_manager import WindowManager

_LOG = logging.getLogger(__package__)

# Fake logger for --test-mode
FAKE_DEVICE_LOGGER_NAME = 'pw_console_fake_device'
_FAKE_DEVICE_LOG = logging.getLogger(FAKE_DEVICE_LOGGER_NAME)
# Don't send fake_device logs to the root Python logger.
_FAKE_DEVICE_LOG.propagate = False

MAX_FPS = 15
MIN_REDRAW_INTERVAL = (60.0 / MAX_FPS) / 60.0


class FloatingMessageBar(ConditionalContainer):
    """Floating message bar for showing status messages."""
    def __init__(self, application):
        super().__init__(
            FormattedTextToolbar(
                (lambda: application.message if application.message else []),
                style='class:toolbar_inactive',
            ),
            filter=Condition(
                lambda: application.message and application.message != ''))


def _add_log_handler_to_pane(logger: Union[str, logging.Logger],
                             pane: 'LogPane',
                             level_name: Optional[str] = None) -> None:
    """A log pane handler for a given logger instance."""
    if not pane:
        return
    pane.add_log_handler(logger, level_name=level_name)


def get_default_colordepth(
        color_depth: Optional[ColorDepth] = None) -> ColorDepth:
    # Set prompt_toolkit color_depth to the highest possible.
    if color_depth is None:
        # Default to 24bit color
        color_depth = ColorDepth.DEPTH_24_BIT

        # If using Apple Terminal switch to 256 (8bit) color.
        term_program = os.environ.get('TERM_PROGRAM', '')
        if sys.platform == 'darwin' and 'Apple_Terminal' in term_program:
            color_depth = ColorDepth.DEPTH_8_BIT

    # Check for any PROMPT_TOOLKIT_COLOR_DEPTH environment variables
    color_depth_override = os.environ.get('PROMPT_TOOLKIT_COLOR_DEPTH', '')
    if color_depth_override:
        color_depth = ColorDepth(color_depth_override)
    return color_depth


class ConsoleApp:
    """The main ConsoleApp class that glues everything together."""

    # pylint: disable=too-many-instance-attributes,too-many-public-methods
    def __init__(
        self,
        global_vars=None,
        local_vars=None,
        repl_startup_message=None,
        help_text=None,
        app_title=None,
        color_depth=None,
        extra_completers=None,
        prefs=None,
    ):
        self.prefs = prefs if prefs else ConsolePrefs()
        self.color_depth = get_default_colordepth(color_depth)

        # Create a default global and local symbol table. Values are the same
        # structure as what is returned by globals():
        #   https://docs.python.org/3/library/functions.html#globals
        if global_vars is None:
            global_vars = {
                '__name__': '__main__',
                '__package__': None,
                '__doc__': None,
                '__builtins__': builtins,
            }

        local_vars = local_vars or global_vars

        # Setup the Jinja environment
        self.jinja_env = Environment(
            # Load templates automatically from pw_console/templates
            loader=FileSystemLoader(Path(__file__).parent / 'templates'),
            # Raise errors if variables are undefined in templates
            undefined=make_logging_undefined(
                logger=logging.getLogger(__package__), ),
            # Trim whitespace in templates
            trim_blocks=True,
            lstrip_blocks=True,
        )

        self.repl_history_filename = self.prefs.repl_history
        self.search_history_filename = self.prefs.search_history

        # History instance for search toolbars.
        self.search_history: History = ThreadedHistory(
            FileHistory(self.search_history_filename))

        # Event loop for executing user repl code.
        self.user_code_loop = asyncio.new_event_loop()

        self.app_title = app_title if app_title else 'Pigweed Console'

        # Top level UI state toggles.
        self.load_theme(self.prefs.ui_theme)

        # Pigweed upstream RST user guide
        self.user_guide_window = HelpWindow(self, title='User Guide')
        self.user_guide_window.load_user_guide()

        # Top title message
        self.message = [('class:logo', self.app_title), ('', '  ')]

        self.message.extend(
            pw_console.widgets.checkbox.to_keybind_indicator(
                'Ctrl-p',
                'Search Menu',
                functools.partial(pw_console.widgets.mouse_handlers.on_click,
                                  self.open_command_runner_main_menu),
                base_style='class:toolbar-button-inactive',
            ))
        # One space separator
        self.message.append(('', ' '))

        # Auto-generated keybindings list for all active panes
        self.keybind_help_window = HelpWindow(self, title='Keyboard Shortcuts')

        # Downstream project specific help text
        self.app_help_text = help_text if help_text else None
        self.app_help_window = HelpWindow(self,
                                          additional_help_text=help_text,
                                          title=(self.app_title + ' Help'))
        self.app_help_window.generate_help_text()

        self.prefs_file_window = HelpWindow(self, title='.pw_console.yaml')
        self.prefs_file_window.load_yaml_text(
            self.prefs.current_config_as_yaml())

        # Used for tracking which pane was in focus before showing help window.
        self.last_focused_pane = None

        # Create a ptpython repl instance.
        self.pw_ptpython_repl = PwPtPythonRepl(
            get_globals=lambda: global_vars,
            get_locals=lambda: local_vars,
            color_depth=self.color_depth,
            history_filename=self.repl_history_filename,
            extra_completers=extra_completers,
        )
        self.input_history = self.pw_ptpython_repl.history

        self.repl_pane = ReplPane(
            application=self,
            python_repl=self.pw_ptpython_repl,
            startup_message=repl_startup_message,
        )
        self.pw_ptpython_repl.use_code_colorscheme(self.prefs.code_theme)

        if self.prefs.swap_light_and_dark:
            self.toggle_light_theme()

        # Window panes are added via the window_manager
        self.window_manager = WindowManager(self)
        self.window_manager.add_pane_no_checks(self.repl_pane)

        # Top of screen menu items
        self.menu_items = self._create_menu_items()

        self.quit_dialog = QuitDialog(self)

        # Key bindings registry.
        self.key_bindings = pw_console.key_bindings.create_key_bindings(self)

        # Create help window text based global key_bindings and active panes.
        self._update_help_window()

        self.command_runner = CommandRunner(
            self,
            width=self.prefs.command_runner_width,
            height=self.prefs.command_runner_height,
        )

        self.floats = [
            # Top message bar
            Float(
                content=FloatingMessageBar(self),
                top=0,
                right=0,
                height=1,
            ),
            # Centered floating help windows
            Float(
                content=self.prefs_file_window,
                top=2,
                bottom=2,
                # Callable to get width
                width=self.prefs_file_window.content_width,
            ),
            Float(
                content=self.app_help_window,
                top=2,
                bottom=2,
                # Callable to get width
                width=self.app_help_window.content_width,
            ),
            Float(
                content=self.user_guide_window,
                top=2,
                bottom=2,
                # Callable to get width
                width=self.user_guide_window.content_width,
            ),
            Float(
                content=self.keybind_help_window,
                top=2,
                bottom=2,
                # Callable to get width
                width=self.keybind_help_window.content_width,
            ),
            # Completion menu that can overlap other panes since it lives in
            # the top level Float container.
            Float(
                xcursor=True,
                ycursor=True,
                content=ConditionalContainer(
                    content=CompletionsMenu(
                        scroll_offset=(lambda: self.pw_ptpython_repl.
                                       completion_menu_scroll_offset),
                        max_height=16,
                    ),
                    # Only show our completion if ptpython's is disabled.
                    filter=Condition(
                        lambda: self.pw_ptpython_repl.completion_visualisation
                        == CompletionVisualisation.NONE),
                ),
            ),
            Float(
                content=self.command_runner,
                # Callable to get width
                width=self.command_runner.content_width,
                **self.prefs.command_runner_position,
            ),
            Float(
                content=self.quit_dialog,
                top=2,
                left=2,
            ),
        ]

        # prompt_toolkit root container.
        self.root_container = MenuContainer(
            body=self.window_manager.create_root_container(),
            menu_items=self.menu_items,
            floats=self.floats,
        )

        # NOTE: ptpython stores it's completion menus in this HSplit:
        #
        # self.pw_ptpython_repl.__pt_container__()
        #   .children[0].children[0].children[0].floats[0].content.children
        #
        # Index 1 is a CompletionsMenu and is shown when:
        #   self.pw_ptpython_repl
        #     .completion_visualisation == CompletionVisualisation.POP_UP
        #
        # Index 2 is a MultiColumnCompletionsMenu and is shown when:
        #   self.pw_ptpython_repl
        #     .completion_visualisation == CompletionVisualisation.MULTI_COLUMN
        #

        # Setup the prompt_toolkit layout with the repl pane as the initially
        # focused element.
        self.layout: Layout = Layout(
            self.root_container,
            focused_element=self.pw_ptpython_repl,
        )

        # Create the prompt_toolkit Application instance.
        self.application: Application = Application(
            layout=self.layout,
            key_bindings=merge_key_bindings([
                # Pull key bindings from ptpython
                load_python_bindings(self.pw_ptpython_repl),
                load_sidebar_bindings(self.pw_ptpython_repl),
                self.window_manager.key_bindings,
                self.key_bindings,
            ]),
            style=DynamicStyle(lambda: merge_styles([
                self._current_theme,
                # Include ptpython styles
                self.pw_ptpython_repl._current_style,  # pylint: disable=protected-access
            ])),
            style_transformation=self.pw_ptpython_repl.style_transformation,
            enable_page_navigation_bindings=True,
            full_screen=True,
            mouse_support=True,
            color_depth=self.color_depth,
            clipboard=PyperclipClipboard(),
            min_redraw_interval=MIN_REDRAW_INTERVAL,
        )

    def get_template(self, file_name: str):
        return self.jinja_env.get_template(file_name)

    def run_pane_menu_option(self, function_to_run):
        # Run the function for a particular menu item.
        return_value = function_to_run()
        # It's return value dictates if the main menu should close or not.
        # - True: The main menu stays open. This is the default prompt_toolkit
        #   menu behavior.
        # - False: The main menu closes.

        # Update menu content. This will refresh checkboxes and add/remove
        # items.
        self.update_menu_items()
        # Check if the main menu should stay open.
        if not return_value:
            # Keep the main menu open
            self.focus_main_menu()

    def open_new_log_pane_for_logger(
            self,
            logger_name: str,
            level_name='NOTSET',
            window_title: Optional[str] = None) -> None:
        pane_title = window_title if window_title else logger_name
        self.run_pane_menu_option(
            functools.partial(self.add_log_handler,
                              pane_title, [logger_name],
                              log_level_name=level_name))

    def set_ui_theme(self, theme_name: str) -> Callable:
        call_function = functools.partial(
            self.run_pane_menu_option,
            functools.partial(self.load_theme, theme_name))
        return call_function

    def set_code_theme(self, theme_name: str) -> Callable:
        call_function = functools.partial(
            self.run_pane_menu_option,
            functools.partial(self.pw_ptpython_repl.use_code_colorscheme,
                              theme_name))
        return call_function

    def update_menu_items(self):
        self.menu_items = self._create_menu_items()
        self.root_container.menu_items = self.menu_items

    def open_command_runner_main_menu(self) -> None:
        self.command_runner.set_completions()
        if not self.command_runner_is_open():
            self.command_runner.open_dialog()

    def open_command_runner_loggers(self) -> None:
        self.command_runner.set_completions(
            window_title='Open Logger',
            load_completions=self._create_logger_completions)
        if not self.command_runner_is_open():
            self.command_runner.open_dialog()

    def _create_logger_completions(self) -> List[Tuple[str, Callable]]:
        completions: List[Tuple[str, Callable]] = [
            (
                'root',
                functools.partial(self.open_new_log_pane_for_logger,
                                  '',
                                  window_title='root'),
            ),
        ]

        all_logger_names = sorted([logger.name for logger in all_loggers()])

        for logger_name in all_logger_names:
            completions.append((
                logger_name,
                functools.partial(self.open_new_log_pane_for_logger,
                                  logger_name),
            ))
        return completions

    def _create_menu_items(self):
        themes_submenu = [
            MenuItem('Toggle Light/Dark', handler=self.toggle_light_theme),
            MenuItem('-'),
            MenuItem(
                'UI Themes',
                children=[
                    MenuItem('Default: Dark', self.set_ui_theme('dark')),
                    MenuItem('High Contrast',
                             self.set_ui_theme('high-contrast-dark')),
                    MenuItem('Nord', self.set_ui_theme('nord')),
                    MenuItem('Nord Light', self.set_ui_theme('nord-light')),
                    MenuItem('Moonlight', self.set_ui_theme('moonlight')),
                ],
            ),
            MenuItem(
                'Code Themes',
                children=[
                    MenuItem('Code: pigweed-code',
                             self.set_code_theme('pigweed-code')),
                    MenuItem('Code: pigweed-code-light',
                             self.set_code_theme('pigweed-code-light')),
                    MenuItem('Code: material',
                             self.set_code_theme('material')),
                    MenuItem('Code: gruvbox-light',
                             self.set_code_theme('gruvbox-light')),
                    MenuItem('Code: gruvbox-dark',
                             self.set_code_theme('gruvbox-dark')),
                    MenuItem('Code: tomorrow-night',
                             self.set_code_theme('tomorrow-night')),
                    MenuItem('Code: tomorrow-night-bright',
                             self.set_code_theme('tomorrow-night-bright')),
                    MenuItem('Code: tomorrow-night-blue',
                             self.set_code_theme('tomorrow-night-blue')),
                    MenuItem('Code: tomorrow-night-eighties',
                             self.set_code_theme('tomorrow-night-eighties')),
                    MenuItem('Code: dracula', self.set_code_theme('dracula')),
                    MenuItem('Code: zenburn', self.set_code_theme('zenburn')),
                ],
            ),
        ]

        file_menu = [
            # File menu
            MenuItem(
                '[File]',
                children=[
                    MenuItem('Open Logger',
                             handler=self.open_command_runner_loggers),
                    MenuItem(
                        'Log Table View',
                        children=[
                            MenuItem(
                                '{check} Hide Date'.format(
                                    check=pw_console.widgets.checkbox.
                                    to_checkbox_text(
                                        self.prefs.hide_date_from_log_time,
                                        end='')),
                                handler=functools.partial(
                                    self.run_pane_menu_option,
                                    functools.partial(
                                        self.toggle_pref_option,
                                        'hide_date_from_log_time')),
                            ),
                            MenuItem(
                                '{check} Show Source File'.format(
                                    check=pw_console.widgets.checkbox.
                                    to_checkbox_text(
                                        self.prefs.show_source_file, end='')),
                                handler=functools.partial(
                                    self.run_pane_menu_option,
                                    functools.partial(self.toggle_pref_option,
                                                      'show_source_file')),
                            ),
                            MenuItem(
                                '{check} Show Python File'.format(
                                    check=pw_console.widgets.checkbox.
                                    to_checkbox_text(
                                        self.prefs.show_python_file, end='')),
                                handler=functools.partial(
                                    self.run_pane_menu_option,
                                    functools.partial(self.toggle_pref_option,
                                                      'show_python_file')),
                            ),
                            MenuItem(
                                '{check} Show Python Logger'.format(
                                    check=pw_console.widgets.checkbox.
                                    to_checkbox_text(
                                        self.prefs.show_python_logger,
                                        end='')),
                                handler=functools.partial(
                                    self.run_pane_menu_option,
                                    functools.partial(self.toggle_pref_option,
                                                      'show_python_logger')),
                            ),
                        ]),
                    MenuItem('-'),
                    MenuItem(
                        'Themes',
                        children=themes_submenu,
                    ),
                    MenuItem('-'),
                    MenuItem('Exit', handler=self.exit_console),
                ],
            ),
        ]

        edit_menu = [
            MenuItem(
                '[Edit]',
                children=[
                    MenuItem('Paste to Python Input',
                             handler=self.repl_pane.
                             paste_system_clipboard_to_input_buffer),
                    MenuItem('-'),
                    MenuItem('Copy all Python Output',
                             handler=self.repl_pane.copy_all_output_text),
                    MenuItem('Copy all Python Input',
                             handler=self.repl_pane.copy_all_input_text),
                ],
            ),
        ]

        view_menu = [
            MenuItem(
                '[View]',
                children=[
                    #         [Menu Item             ][Keybind  ]
                    MenuItem('Focus Next Window/Tab   Ctrl-Alt-n',
                             handler=self.window_manager.focus_next_pane),
                    #         [Menu Item             ][Keybind  ]
                    MenuItem('Focus Prev Window/Tab   Ctrl-Alt-p',
                             handler=self.window_manager.focus_previous_pane),
                    MenuItem('-'),

                    #         [Menu Item             ][Keybind  ]
                    MenuItem('Move Window Up         Ctrl-Alt-Up',
                             handler=functools.partial(
                                 self.run_pane_menu_option,
                                 self.window_manager.move_pane_up)),
                    #         [Menu Item             ][Keybind  ]
                    MenuItem('Move Window Down     Ctrl-Alt-Down',
                             handler=functools.partial(
                                 self.run_pane_menu_option,
                                 self.window_manager.move_pane_down)),
                    #         [Menu Item             ][Keybind  ]
                    MenuItem('Move Window Left     Ctrl-Alt-Left',
                             handler=functools.partial(
                                 self.run_pane_menu_option,
                                 self.window_manager.move_pane_left)),
                    #         [Menu Item             ][Keybind  ]
                    MenuItem('Move Window Right   Ctrl-Alt-Right',
                             handler=functools.partial(
                                 self.run_pane_menu_option,
                                 self.window_manager.move_pane_right)),
                    MenuItem('-'),

                    #         [Menu Item             ][Keybind  ]
                    MenuItem('Shrink Height            Alt-Minus',
                             handler=functools.partial(
                                 self.run_pane_menu_option,
                                 self.window_manager.shrink_pane)),
                    #         [Menu Item             ][Keybind  ]
                    MenuItem('Enlarge Height               Alt-=',
                             handler=functools.partial(
                                 self.run_pane_menu_option,
                                 self.window_manager.enlarge_pane)),
                    MenuItem('-'),

                    #         [Menu Item             ][Keybind  ]
                    MenuItem('Shrink Column                Alt-,',
                             handler=functools.partial(
                                 self.run_pane_menu_option,
                                 self.window_manager.shrink_split)),
                    #         [Menu Item             ][Keybind  ]
                    MenuItem('Enlarge Column               Alt-.',
                             handler=functools.partial(
                                 self.run_pane_menu_option,
                                 self.window_manager.enlarge_split)),
                    MenuItem('-'),

                    #         [Menu Item            ][Keybind  ]
                    MenuItem('Balance Window Sizes       Ctrl-u',
                             handler=functools.partial(
                                 self.run_pane_menu_option,
                                 self.window_manager.balance_window_sizes)),
                ],
            ),
        ]

        window_menu = self.window_manager.create_window_menu()

        help_menu_items = [
            MenuItem(self.user_guide_window.menu_title(),
                     handler=self.user_guide_window.toggle_display),
            MenuItem(self.keybind_help_window.menu_title(),
                     handler=self.keybind_help_window.toggle_display),
            MenuItem('-'),
            MenuItem('View Key Binding Config',
                     handler=self.prefs_file_window.toggle_display),
        ]

        if self.app_help_text:
            help_menu_items.extend([
                MenuItem('-'),
                MenuItem(self.app_help_window.menu_title(),
                         handler=self.app_help_window.toggle_display)
            ])

        help_menu = [
            # Info / Help
            MenuItem(
                '[Help]',
                children=help_menu_items,
            ),
        ]

        return file_menu + edit_menu + view_menu + window_menu + help_menu

    def focus_main_menu(self):
        """Set application focus to the main menu."""
        self.application.layout.focus(self.root_container.window)

    def focus_on_container(self, pane):
        """Set application focus to a specific container."""
        # Try to focus on the given pane
        try:
            self.application.layout.focus(pane)
        except ValueError:
            # If the container can't be focused, focus on the first visible
            # window pane.
            self.window_manager.focus_first_visible_pane()

    def toggle_light_theme(self):
        """Toggle light and dark theme colors."""
        # Use ptpython's style_transformation to swap dark and light colors.
        self.pw_ptpython_repl.swap_light_and_dark = (
            not self.pw_ptpython_repl.swap_light_and_dark)
        if self.application:
            self.focus_main_menu()

    def toggle_pref_option(self, setting_name):
        self.prefs.toggle_bool_option(setting_name)

    def load_theme(self, theme_name=None):
        """Regenerate styles for the current theme_name."""
        self._current_theme = pw_console.style.generate_styles(theme_name)
        if theme_name:
            self.prefs.set_ui_theme(theme_name)

    def _create_log_pane(self,
                         title: str = '',
                         log_store: Optional[LogStore] = None) -> 'LogPane':
        # Create one log pane.
        log_pane = LogPane(application=self,
                           pane_title=title,
                           log_store=log_store)
        self.window_manager.add_pane(log_pane)
        return log_pane

    def load_clean_config(self, config_file: Path) -> None:
        self.prefs.reset_config()
        self.prefs.load_config_file(config_file)

    def apply_window_config(self) -> None:
        self.window_manager.apply_config(self.prefs)

    def refresh_layout(self) -> None:
        self.window_manager.update_root_container_body()
        self.update_menu_items()
        self._update_help_window()

    def add_log_handler(
            self,
            window_title: str,
            logger_instances: Union[Iterable[logging.Logger], LogStore],
            separate_log_panes: bool = False,
            log_level_name: Optional[str] = None) -> Optional[LogPane]:
        """Add the Log pane as a handler for this logger instance."""

        existing_log_pane = None
        # Find an existing LogPane with the same window_title.
        for pane in self.window_manager.active_panes():
            if isinstance(pane, LogPane) and pane.pane_title() == window_title:
                existing_log_pane = pane
                break

        log_store: Optional[LogStore] = None
        if isinstance(logger_instances, LogStore):
            log_store = logger_instances

        if not existing_log_pane or separate_log_panes:
            existing_log_pane = self._create_log_pane(title=window_title,
                                                      log_store=log_store)

        if isinstance(logger_instances, list):
            for logger in logger_instances:
                _add_log_handler_to_pane(logger, existing_log_pane,
                                         log_level_name)

        self.refresh_layout()
        return existing_log_pane

    def _user_code_thread_entry(self):
        """Entry point for the user code thread."""
        asyncio.set_event_loop(self.user_code_loop)
        self.user_code_loop.run_forever()

    def start_user_code_thread(self):
        """Create a thread for running user code so the UI isn't blocked."""
        thread = Thread(target=self._user_code_thread_entry,
                        args=(),
                        daemon=True)
        thread.start()

    def _update_help_window(self):
        """Generate the help window text based on active pane keybindings."""
        # Add global mouse bindings to the help text.
        mouse_functions = {
            'Focus pane, menu or log line.': ['Click'],
            'Scroll current window.': ['Scroll wheel'],
        }

        self.keybind_help_window.add_custom_keybinds_help_text(
            'Global Mouse', mouse_functions)

        # Add global key bindings to the help text.
        self.keybind_help_window.add_keybind_help_text('Global',
                                                       self.key_bindings)

        self.keybind_help_window.add_keybind_help_text(
            'Window Management', self.window_manager.key_bindings)

        # Add activated plugin key bindings to the help text.
        for pane in self.window_manager.active_panes():
            for key_bindings in pane.get_all_key_bindings():
                help_section_title = pane.__class__.__name__
                if isinstance(key_bindings, KeyBindings):
                    self.keybind_help_window.add_keybind_help_text(
                        help_section_title, key_bindings)
                elif isinstance(key_bindings, dict):
                    self.keybind_help_window.add_custom_keybinds_help_text(
                        help_section_title, key_bindings)

        self.keybind_help_window.generate_help_text()

    def toggle_log_line_wrapping(self):
        """Menu item handler to toggle line wrapping of all log panes."""
        for pane in self.window_manager.active_panes():
            if isinstance(pane, LogPane):
                pane.toggle_wrap_lines()

    def focused_window(self):
        """Return the currently focused window."""
        return self.application.layout.current_window

    def command_runner_is_open(self) -> bool:
        return self.command_runner.show_dialog

    def command_runner_last_focused_pane(self) -> Any:
        return self.command_runner.last_focused_pane

    def modal_window_is_open(self):
        """Return true if any modal window or dialog is open."""
        if self.app_help_text:
            return (self.app_help_window.show_window
                    or self.keybind_help_window.show_window
                    or self.prefs_file_window.show_window
                    or self.user_guide_window.show_window
                    or self.quit_dialog.show_dialog
                    or self.command_runner.show_dialog)
        return (self.keybind_help_window.show_window
                or self.prefs_file_window.show_window
                or self.user_guide_window.show_window
                or self.quit_dialog.show_dialog
                or self.command_runner.show_dialog)

    def exit_console(self):
        """Quit the console prompt_toolkit application UI."""
        self.application.exit()

    def redraw_ui(self):
        """Redraw the prompt_toolkit UI."""
        if hasattr(self, 'application'):
            # Thread safe way of sending a repaint trigger to the input event
            # loop.
            self.application.invalidate()

    async def run(self, test_mode=False):
        """Start the prompt_toolkit UI."""
        if test_mode:
            background_log_task = asyncio.create_task(self.log_forever())

        try:
            unused_result = await self.application.run_async(
                set_exception_handler=True)
        finally:
            if test_mode:
                background_log_task.cancel()

    async def log_forever(self):
        """Test mode async log generator coroutine that runs forever."""
        message_count = 0
        # Sample log line format:
        # Log message [=         ] # 100

        # Fake module column names.
        module_names = ['APP', 'RADIO', 'BAT', 'USB', 'CPU']
        while True:
            if message_count > 32 or message_count < 2:
                await asyncio.sleep(1)
            bar_size = 10
            position = message_count % bar_size
            bar_content = " " * (bar_size - position - 1) + "="
            if position > 0:
                bar_content = "=".rjust(position) + " " * (bar_size - position)
            new_log_line = 'Log message [{}] # {}'.format(
                bar_content, message_count)
            if message_count % 10 == 0:
                new_log_line += (
                    ' Lorem ipsum \033[34m\033[1mdolor sit amet\033[0m'
                    ', consectetur '
                    'adipiscing elit.') * 8
            if message_count % 11 == 0:
                new_log_line += ' '
                new_log_line += (
                    '[PYTHON] START\n'
                    'In []: import time;\n'
                    '        def t(s):\n'
                    '            time.sleep(s)\n'
                    '            return "t({}) seconds done".format(s)\n\n')

            module_name = module_names[message_count % len(module_names)]
            _FAKE_DEVICE_LOG.info(new_log_line,
                                  extra=dict(extra_metadata_fields=dict(
                                      module=module_name, file='fake_app.cc')))
            message_count += 1


# TODO(tonymd): Remove this alias when not used by downstream projects.
def embed(
    *args,
    **kwargs,
) -> None:
    """PwConsoleEmbed().embed() alias."""
    # Import here to avoid circular dependency
    from pw_console.embed import PwConsoleEmbed  # pylint: disable=import-outside-toplevel
    console = PwConsoleEmbed(*args, **kwargs)
    console.embed()
