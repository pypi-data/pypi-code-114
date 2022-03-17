# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary
'''
TabbedPanel
============

Test of the widget TabbedPanel.
'''

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.core.window import Window

import my_globals as g

Builder.load_string("""
#:import g my_globals
<Test>:
    # size_hint: .5, .5
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    TabbedPanelItem:
        text: 'Commands'
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: 'Save'
                id: bt_save
                on_press: 
                    print('Save pressed')
                    g.config['sample']['period'] = float(spin_sample_period.text)
                    g.config['sample']['size'] = int(spin_sample_size.text)
                    g.config['log']['max'] = int(spin_log_max.text)
                    g.config['proc']['method'] = spin_proc_method.text
                    print(g.config)                    
                    root.on_config_file('save')               
            Button:
                text: 'Load'
                on_press: 
                    print('Load pressed')
                    root.on_config_file('load')               
            Button:
                text: 'Close'
                on_press: 
                    print('Close pressed')
                                    
            Button:
                text: 'Test'
                on_press: 
                    self.text = self.text + '@'
                    bt_save.text = '***'
                    g.config['sample']['period'] = 100
                    print(g.config)
                    print('not implemented ****')
            Button:
                text: 'Blank'
            Button:
                text: 'Blank'
            Button:
                text: 'Blank'
                
                
    TabbedPanelItem:
        text: 'Config'
        BoxLayout:
            orientation: 'vertical'

            Label:
                text: 'Sample Period(ms):'
            Spinner:
                id: spin_sample_period
                text: '1.0'
                values: '0.25', '0.5', '1.0', '2.0', '5.0'

            Label:
                text: 'Sample Size:'
            Spinner:
                id: spin_sample_size
                text: '8'
                values: '4', '8', '16', '32'

            Label:
                text: 'Max # of logs:'
            Spinner:
                id: spin_log_max
                text: '10'
                values: '20', '50', '100', '1000'

            Label:
                text: 'Post processing:'
            Spinner:
                id: spin_proc_method
                text: 'MEAN'
                values: 'MEAN', 'MEDIAN'

            Label:
                text: 'Blank:'
            Spinner:
                id: spin_blank1
                text: '0'
                values: '0', '1', '2'
            Label:
                text: 'Blank:'
            Spinner:
                id: spin_blank2
                text: '0'
                values: '0', '1', '2'

                
    TabbedPanelItem:
        text: 'Help'
        RstDocument:
            text:
                '\\n'.join(("Hello world", "-----------",
                "You are in the third tab."))

""")


class Test(TabbedPanel):
    def on_config_file(self, cmd):
        dic = g.config
        # print(__name__, 'dic:', dic)
        jo = json.dumps(dic, ensure_ascii=True)  # 한글금지
        # print(__name__, 'json:', jo)

        conf_filename = 'config_app.json'

        # if cmd is 'save':
        #     with open(conf_filename, 'w') as f:
        #         json.dump(jo, f, indent=4)  # indent 안먹힌다
        #         print(__name__, 'config json to file:', jo)
        #
        # if cmd is 'load':
        #     with open(conf_filename, 'r') as f:
        #         jo = json.load(f)
        #         print(__name__, 'config json from file:', jo)

        if cmd is 'save':
            # 'wt' 를 사용하면 더러워진다 그리고 숫자를 스트링 처리한다
            with open(conf_filename, 'w') as f:
                # json --> file
                json.dump(jo, f)  # indent 안먹힌다
                print(__name__, 'save config to file:', jo)

        if cmd is 'load':
            with open(conf_filename, 'r') as f:
                # file --> json
                jo = json.load(f)
                print(__name__, 'load config from file:', jo)
                # json --> python dic
                dic = json.loads(jo)
                g.config = dic
                print(g)


    # def foo1(self):
    #     print('foo...')
    #     self.config_file(cmd='save')

    # def on_config_file(self, cmd):

    pass


class TabbedPanelApp(App):
    def build(self):
        return Test()


import json

if __name__ == '__main__':
    app = TabbedPanelApp()
    # Window.size = (320, 480)  # good TFT, 3.5"
    Window.size = (320, 400)  # good TFT, 3.5"
    Window.top = 0
    Window.left = 0
    app.run()
