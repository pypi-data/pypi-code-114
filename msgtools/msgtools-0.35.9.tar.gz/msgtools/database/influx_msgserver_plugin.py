from msgtools.database.influxdb import InfluxDBConnection
from msgtools.lib.messaging import Messaging
from PyQt5 import QtCore, QtGui, QtWidgets

class InfluxServerPlugin(QtCore.QObject):
    statusUpdate = QtCore.pyqtSignal(str)
    messagereceived = QtCore.pyqtSignal(object)
    disconnected = QtCore.pyqtSignal(object)
    
    SUMMARY_FORMAT_STR = "Msgs: %d, Bytes In: %d, Bytes Out: %d, Mps In: %.0f, Bps In: %.0f, Bps Out: %.0f"

    def __init__(self, param):
        super(InfluxServerPlugin, self).__init__(None)
        
        # split up params, and use them to construct the DB connection.
        params = param.split("|")
        # an emptry string results in a len 1 array with an empty string,
        # which we'd like to treat as no parameters
        if len(params) == 1 and params[0] == '':
            params = []
        self.db = InfluxDBConnection(self, *params)

        # these are for interfacing to msgserver
        self.name = "InfluxDB"
        self.subscriptions = {}
        self.subMask = 0
        self.subValue = 0
        self.isHardwareLink = False
        self.statusLabel = QtWidgets.QLabel("influxdb %s:%d" % (self.db.hostname, self.db.port))
        self.summaryLabel = QtWidgets.QLabel(SUMMARY_FORMAT_STR % (0,0,0, 0.0,0.0,0.0))

        self.removeClient = QtWidgets.QPushButton("Remove")
        self.removeClient.pressed.connect(self.onDisconnected)

        # start a timer to print summary data peridically
        self.display_timer = QtCore.QTimer(self)
        self.display_timer.setInterval(10000)
        self.display_timer.timeout.connect(self.print_summary)
        self.display_timer.start()

    def onDisconnected(self):
        self.disconnected.emit(self)

    def widget(self, index):
        if index == 0:
            return self.removeClient
        if index == 1:
            return self.statusLabel
        if index == 2:
            return self.summaryLabel
        return None

    def start(self):
        pass
    
    def stop(self):
        pass
    
    # for msgserver telling us to send
    def sendMsg(self, hdr):
        msg = Messaging.MsgFactory(hdr)
        self.db.handle_message(msg)
    
    # for influxdb telling us to send
    def send_message(self, hdr):
        self.messagereceived.emit(hdr)
    
    def print_summary(self):
        (mi, bi, bo, mips, bips, bops) = self.db.compute_stats(self.display_timer.interval() / 1000.0)
        self.summaryLabel.setText(SUMMARY_FORMAT_STR % (mi, bi, bo, mips, bips, bops))

def PluginConnection(param=""):
    isp = InfluxServerPlugin(param)
    return isp

def PluginEnabled():
    return True

import collections
PluginInfo = collections.namedtuple('PluginInfo', ['name', 'enabled', 'connect_function'])
plugin_info = PluginInfo('InfluxDB', PluginEnabled, PluginConnection)
