__version__ = '1.2'

import os
import shutil
import time

try:
    import jnius
    from jnius import autoclass

except KeyError:
    os.environ['JDK_HOME'] = "/usr/lib/jvm/java-1.8.0-openjdk-amd64"
    os.environ['JAVA_HOME'] = "/usr/lib/jvm/java-1.8.0-openjdk-amd64"
    import jnius
    from jnius import autoclass

from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform

from threading import Thread
import webbrowser

SERVICE_NAME = u'{packagename}.Service{servicename}'.format(
    packagename=u'org.kivy.eisenradio',
    servicename=u'Eisenradio'
)

KV = '''
BoxLayout:
    orientation: 'vertical'
    ScrollView:
        Label:
            id: label
            background_color: 0.40, 1.16, 1.66, 1
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.size[0], None
            verdana: True

    BoxLayout:
        size_hint_y: None
        height: '200sp'
        Button:
            background_color: 1.51, 0.51, 0.51, 1
            text: 'Eisenradio Browser!'
            verdana: True
            on_press: app.browser()

'''
service = ''
is_android = 'ANDROID_STORAGE' in os.environ
if is_android:
    activity = autoclass('org.kivy.android.PythonActivity').mActivity
    Context = autoclass('android.content.Context')
    ConnectivityManager = autoclass('android.net.ConnectivityManager')
    con_mgr = activity.getSystemService(Context.CONNECTIVITY_SERVICE)
    conn_wifi = con_mgr.getNetworkInfo(ConnectivityManager.TYPE_WIFI).isConnectedOrConnecting()
    conn_mobile = con_mgr.getNetworkInfo(ConnectivityManager.TYPE_MOBILE).isConnectedOrConnecting()

    TelephonyManager = autoclass('android.telephony.TelephonyManager')
    conn_ts = activity.getSystemService(Context.TELEPHONY_SERVICE)
    conn_sim = conn_ts.getSimState(TelephonyManager.SIM_STATE_READY)
    # mob_data = Settings.Secure.getInt(getContentResolver(), "mobile_data", 1) == 1;

from jnius import autoclass

if platform == "android":
    service = autoclass(SERVICE_NAME)
    mActivity = autoclass(u'org.kivy.android.PythonActivity').mActivity
    argument = ''
    service.start(mActivity, argument)


class EisenradioApp(App):
    def build(self):
        self.root = Builder.load_string(KV)
        if is_android:
            if self.root:
                if conn_wifi:
                    self.root.ids.label.text += '\n\n{}'.format('    Network:   WIFI available')
                else:
                    self.root.ids.label.text += '\n\n{}'.format('    Network:   WIFI disconnected    <--')

                if conn_ts:
                    self.root.ids.label.text += '\n\n{}'.format('    SIM card:   ready ')
                else:
                    self.root.ids.label.text += '\n\n{}'.format('    SIM card:   not ready    <--')

        return self.root

    def browser(self):
        self.create_folder()
        self.thread = Thread(
            target=webbrowser.open,
            args=['http://localhost:5050'],
            daemon=True
        )
        self.thread.start()

        if self.root:
            self.root.ids.label.text += '\n\n{}'.format('    Browser started    http://localhost:5050')

    def create_folder(self):

        if platform == 'android':
            # noinspection PyUnresolvedReferences
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
            db_path_music = '/storage/emulated/0/Music/Eisenradio'
            self.make_folder(db_path_music)
            source_file = os.path.dirname(os.path.abspath(__file__)) + '//eisenradio_android.db'
            dst_file = db_path_music + '//eisenradio_android.db'
            try:
                if not os.path.exists(dst_file):
                    shutil.copyfile(source_file, dst_file)
                    # debug msg
                    print('\n\t---> DB copyfile(source_file, dst_file), SUCCESS <---\n')
            except FileExistsError:
                pass

    @staticmethod
    def make_folder(this_folder):
        try:
            os.makedirs(this_folder)
        except FileExistsError:
            pass


eisen_radio = EisenradioApp()
eisen_radio.create_folder()

if __name__ == '__main__':
    EisenradioApp().run()
