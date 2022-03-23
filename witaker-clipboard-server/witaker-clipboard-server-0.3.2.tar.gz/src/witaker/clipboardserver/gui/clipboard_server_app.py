import re
import sys
import importlib.resources

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.behaviors import ToggleButtonBehavior

from witaker.clipboardserver import get_auth_marker, DEFAULT_SERVER_PORT, start_server_process, stop_server_process


class SettingsButton(ToggleButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(SettingsButton, self).__init__(**kwargs)

    def set_button_icons(self, active_icon, inactive_icon):
        self.active_icon = active_icon
        self.inactive_icon = inactive_icon
        self.source = self.inactive_icon

    def on_state(self, widget, value):
        if value == 'down':
            self.source = self.active_icon
        else:
            self.source = self.inactive_icon




class ClipboardServerApp(App):
    
    def __init__(self, **kwargs) :
        super(ClipboardServerApp, self).__init__(**kwargs)
        self.server_port = DEFAULT_SERVER_PORT
        self.server_is_running = False



    def on_toggle_settings(self, _button, value):
        if value == 'down':
            self.footer_pane.add_widget(self.settings_panel)
        elif value == 'normal':
            self.footer_pane.remove_widget(self.settings_panel)
        
    
    
    def stop_scheduled_tasks(self):
        print(f"Removing copy/paste queue scheduler : {self.queue_scheduler}")
        if (self.queue_scheduler):
            Clock.unschedule(self.queue_scheduler)
        if (self.remove_highlight_scheduler):
            self.remove_highlight_scheduler.cancel()


    def start_server(self):
        print("Starting server process")
        self.server_process = start_server_process(self.server_port)
        self.server_is_running = True

    def stop_server(self):
        print("Stopping server")
        stop_server_process(self.server_process)
        self.server_is_running = False


    def on_close_app(self, *args):
        self.stop_scheduled_tasks()
        self.stop_server()
        print("Closing Kivy app")
        self.stop()
        Window.close()
        self.release_resource_files()
        sys.exit(0)


    def copy_auth(self, button=None):        
        self.clipboard_util.copy_text_to_clipboard(self.auth_key, get_auth_marker(self.server_port, self.auth_key))

    def set_panel_background(self, panel, rgb_color):
        with panel.canvas.before:
            Color(rgb_color[0], rgb_color[1], rgb_color[2])
            panel.bg_rect = Rectangle(pos=panel.pos, size=panel.size)
            def update_rect(instance, value):
                instance.bg_rect.pos = instance.pos
                instance.bg_rect.size = instance.size
            # listen to size and position changes
            panel.bind(pos=update_rect, size=update_rect)

    def stop_or_start_server(self, button=None):
        if self.server_is_running:
            self.stop_server()
            self.server_status_panel.add_widget(self.server_port_text_input)
            self.server_port_text_input.text = str(self.server_port)
            self.server_status_label.text = 'Start server on http://localhost:'
            self.server_is_running = False
            self.stop_start_server_button.text = "Start"
        else:
            port = self.server_port_text_input.text.strip()
            MIN_PORT = 1024
            MAX_PORT = 65535
            error_red = "#AA0000"
            if re.match(r"^\d+$", port):
                port_num = int(port)
                if port_num >= MIN_PORT and port_num <= MAX_PORT:
                    self.server_port = port_num
                    self.start_server()
                    self.server_status_panel.remove_widget(self.server_port_text_input)
                    if self.error_label.text != '':
                        self.error_label.text = ''
                        self.main.remove_widget(self.error_label)
                    self.server_status_label.text = f"Server running on http://localhost:[color={self.port_blue}]{self.server_port}[/color]"
                    self.server_is_running = True
                    self.stop_start_server_button.text = "Stop"
                    self.copy_auth()
                else:
                    if self.error_label.text == '':
                        self.main.add_widget(self.error_label)
                    self.error_label.text = f"Please enter a number between [color={error_red}]{MIN_PORT}[/color] and [color={error_red}]{MAX_PORT}[/color] "
                    
            else:
                if self.error_label.text == '':
                        self.main.add_widget(self.error_label)
                self.error_label.text = f"Please enter a port number between [color={error_red}]{MIN_PORT}[/color] and [color={error_red}]{MAX_PORT}[/color] "

    def access_resource_files(self):        
        icon_names = ["copy-icon--active","witaker-clipboard-server","settings--inactive","copy-icon--inactive","settings--active"]

        for icon_name in icon_names:
            manager = importlib.resources.path('witaker.clipboardserver.gui.icons', f"{icon_name}.png")
            icon_path = manager.__enter__()
            
            self.importlib_resource_managers[icon_name] = (manager, icon_path)
            self.icons[icon_name] = str(icon_path)

    def release_resource_files(self):
        for icon_name in self.importlib_resource_managers.keys():
            manager, value = self.importlib_resource_managers[icon_name]
            manager.__exit__(None, value, None)

    
    def build(self):
        self.icons = {}
        self.importlib_resource_managers = {}
        self.access_resource_files()

        Window.bind(on_request_close=self.on_close_app)

        self.main = BoxLayout(orientation='vertical', padding=(10,10))      
        self.set_panel_background(self.main, [1, 1, 1])

        ## header
        self.header_panel = BoxLayout(orientation='horizontal', size_hint=(1, None), height=100)               
        
        title_image = Image(source=self.icons["witaker-clipboard-server"],  size_hint=(None, None), size=(300, 100))
        self.copy_icon_image = Image(source=self.icons["copy-icon--inactive"], size_hint=(None, None), size=(60,60), top=0) # , pos_hint={"top": 40})

        icon_panel = BoxLayout(orientation='vertical', size_hint=(None, 1), width=60)
        icon_panel.add_widget(self.copy_icon_image)
        icon_panel.add_widget(Widget(size_hint=(1, 0.2)))
        header_spacer = Widget(size_hint=(0.6, None), height=100)

        self.header_panel.add_widget(title_image)
        self.header_panel.add_widget(header_spacer)
        self.header_panel.add_widget(icon_panel)

        self.main.add_widget(self.header_panel)

        ## copied text
        self.text_color = "#a6a6a6"
        self.active_text_color = "#63ad1d"
        # self.clipboard_source = Label(text="CR Tool", bold=True, color=self.text_color, padding= (10, 5), halign="left", valign="top", size_hint=(1, None), height=24)
        # self.clipboard_source.bind(size=self.clipboard_source.setter('text_size'))    
        # self.main.add_widget(self.clipboard_source)

        self.copied_text = Label(text="Copied text...", color=self.text_color, padding= (10, 20), halign="left", valign="top", size_hint=(1, 0.6))
        self.copied_text.bind(size=self.copied_text.setter('text_size'))    
        self.main.add_widget(self.copied_text)


        ## footer
        self.port_blue = '#4646da'
        self.footer_pane = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40, spacing=40)
        self.button = SettingsButton(size_hint=(None, None), width=40, height=40)
        self.button.set_button_icons(self.icons["settings--active"], self.icons["settings--inactive"])
        self.button.bind(state=self.on_toggle_settings)

        self.settings_panel = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40, spacing=20)
        self.copy_auth_button = Button(text="Copy Auth", size_hint=(None, None), width=120, height=40, background_color="#63ad1d", background_normal='', color="#ffffff", bold=False)
        self.copy_auth_button.bind(on_press=self.copy_auth)
        self.server_status_wrapper_panel = BoxLayout(orientation='vertical', size_hint=(1, None), height=40)
        self.server_status_panel = BoxLayout(orientation='horizontal', size_hint=(1, None), height=26, spacing=10)
        self.server_status_label = Label(text=f"Server running on http://localhost:[color={self.port_blue}]{self.server_port}[/color]", color=self.text_color, font_size=20, halign="left", valign="top", size_hint=(1, None), height=26, markup=True)
        self.server_port_text_input = TextInput(text="", size_hint=(None, None), width=60, height=26, font_size=16, padding=(6,2))
        self.stop_start_server_button = Button(text="Stop", size_hint=(None, None), width=60, height=40, background_color="#63ad1d", background_normal='', color="#ffffff", bold=False)
        self.stop_start_server_button.bind(on_press=self.stop_or_start_server)
        settings_spacer = Widget(size_hint=(0.4, None), height=40)

        self.server_status_panel.add_widget(self.server_status_label)

        self.server_status_wrapper_panel.add_widget(Widget(size_hint=(1, None), height=7))
        self.server_status_wrapper_panel.add_widget(self.server_status_panel)
        self.server_status_wrapper_panel.add_widget(Widget(size_hint=(1, None), height=7))

        self.settings_panel.add_widget(self.copy_auth_button)
        self.settings_panel.add_widget(settings_spacer)
        self.settings_panel.add_widget(self.server_status_wrapper_panel)
        self.settings_panel.add_widget(self.stop_start_server_button)

        self.footer_pane.add_widget(self.button)

        self.error_label = Label(text="", color=self.text_color, font_size=20, halign="left", valign="top", size_hint=(1, None), height=24, markup=True)

        self.main.add_widget(self.footer_pane)


        self.queue_scheduler = Clock.schedule_interval(self.consumer_process_queue, 1)
        self.remove_highlight_scheduler = None

        return self.main

    def set_clipboard_util(self, util):
        self.clipboard_util = util

    def set_secret_auth_key(self, auth_key):
        self.auth_key = auth_key

    def set_queue(self, q):
        self.q = q

    def set_server_port(self, p):
        if not self.server_is_running:
            self.server_port = p

    def consumer_process_queue(self, dt=0):
        # while True:        
        if self.q.empty():
            return
        else:
            value = str(self.q.get())
            if value:
                if self.remove_highlight_scheduler:
                    self.remove_highlight_scheduler.cancel()
                    self.remove_highlight_scheduler = None
                self.copied_text.text = value
                self.copy_icon_image.source = self.icons["copy-icon--active"]
                self.copied_text.color = self.active_text_color
                self.remove_highlight_scheduler = Clock.schedule_once(self.remove_copy_highlights, 3)
                
    def remove_copy_highlights(self, dt=0):
        self.copy_icon_image.source = self.icons["copy-icon--inactive"]
        self.copied_text.color = self.text_color

        
        

    def on_start(self):
        self.start_server()
        self.copy_auth()


