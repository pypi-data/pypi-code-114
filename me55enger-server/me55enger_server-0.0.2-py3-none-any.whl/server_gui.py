import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QLabel, QTableView, QDialog, QPushButton, QLineEdit, \
    QFileDialog, QApplication


def gui_create_model(database):
    list_users = database.active_users_list()

    list_table = QStandardItemModel()
    list_table.setHorizontalHeaderLabels(['Имя клиента', 'IP-адрес', 'Порт', 'Время подключения'])

    for row in list_users:
        user, ip, port, time = row
        user = QStandardItem(user)
        user.setEditable(False)
        ip = QStandardItem(ip)
        ip.setEditable(False)
        port = QStandardItem(str(port))
        port.setEditable(False)

        time = QStandardItem(str(time.replace(microsecond=0)))
        time.setEditable(False)
        list_table.appendRow([user, ip, port, time])
    return list_table


def create_stat_model(database):
    hist_list = database.message_history()

    list_table = QStandardItemModel()
    list_table.setHorizontalHeaderLabels(
        ['Имя клиента', 'Последний раз входил', 'Сообщений отправлено', 'Сообщений получено'])

    for row in hist_list:
        user, last_seen, sent, received = row
        user = QStandardItem(user)
        user.setEditable(False)
        last_seen = QStandardItem(str(last_seen.replace(microsecond=0)))
        last_seen.setEditable(False)
        sent = QStandardItem(str(sent))
        sent.setEditable(False)
        received = QStandardItem(str(received))
        received.setEditable(False)
        list_table.appendRow([user, last_seen, sent, received])
    return list_table


class MainWindow(QMainWindow):
    """ Main window. """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction('Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        self.refresh_button = QAction('Обновить список', self)
        self.config_button = QAction('Настройки сервера', self)
        self.show_history_button = QAction('История клиентов', self)

        self.statusBar()

        self.toolbar = self.addToolBar('MainBar')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(self.refresh_button)
        self.toolbar.addAction(self.show_history_button)
        self.toolbar.addAction(self.config_button)

        self.setFixedSize(800, 600)
        self.setWindowTitle('Messaging Server v0.000001a')

        self.label = QLabel('Список подключённых клиентов:', self)
        self.label.setFixedSize(240, 15)
        self.label.move(10, 25)

        self.active_clients_tabel = QTableView(self)
        self.active_clients_tabel.setFixedSize(780, 400)
        self.active_clients_tabel.move(10, 45)

        self.show()


class HistoryWindow(QDialog):
    """ Users history window. """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Статистика клиентов')
        self.setFixedSize(600, 700)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.close_button = QPushButton('Закрыть', self)
        self.close_button.move(250, 650)
        self.close_button.clicked.connect(self.close)

        self.history_table = QTableView(self)
        self.history_table.setFixedSize(580, 620)
        self.history_table.move(10, 10)

        self.show()


class ConfigWindow(QDialog):
    """ Settings window. """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(365, 260)
        self.setWindowTitle('Настройки сервера')

        self.db_path_label = QLabel('Путь до файла базы данных:', self)
        self.db_path_label.setFixedSize(240, 15)
        self.db_path_label.move(10, 10)

        self.db_path = QLineEdit(self)
        self.db_path.setFixedSize(250, 20)
        self.db_path.move(10, 30)
        self.db_path.setReadOnly(True)

        self.db_path_select = QPushButton('Обзор...', self)
        self.db_path_select.move(275, 28)

        def open_file_dialog():
            global dialog
            dialog = QFileDialog(self)
            path = dialog.getExistingDirectory().replace('/', '\\')
            self.db_path.clear()
            self.db_path.insert(path)

        self.db_path_select.clicked.connect(open_file_dialog)

        self.db_file_label = QLabel('Имя файла базы данных:', self)
        self.db_file_label.setFixedSize(180, 15)
        self.db_file_label.move(10, 68)

        self.db_file = QLineEdit(self)
        self.db_file.setFixedSize(150, 20)
        self.db_file.move(200, 66)

        self.port_label = QLabel('Номер порта для соединения:', self)
        self.port_label.setFixedSize(180, 15)
        self.port_label.move(10, 108)

        self.port = QLineEdit(self)
        self.port.setFixedSize(150, 20)
        self.port.move(200, 108)

        self.ip_label = QLabel('С какого IP принимаем соединения:', self)
        self.ip_label.setFixedSize(180, 15)
        self.ip_label.move(10, 148)

        self.ip_label_note = QLabel(' оставьте это поле пустым, чтобы\nпринимать соединения с любых адресов.', self)
        self.ip_label_note.setFixedSize(500, 30)
        self.ip_label_note.move(10, 168)

        self.ip = QLineEdit(self)
        self.ip.setFixedSize(150, 20)
        self.ip.move(200, 148)

        self.save_button = QPushButton('охранить', self)
        self.save_button.move(190.220)

        self.close_button = QPushButton('Закрыть', self)
        self.close_button.move(275, 220)
        self.close_button.clicked.connect(self.close)

        self.show()


if __name__ == '__main__':
    test_window = 'main'  # main / cfg / hist

    if test_window == 'main':
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.statusBar().showMessage('Test Statusbar Message')
        test_list = QStandardItemModel(main_window)
        test_list.setHorizontalHeaderLabels(['Имя клиента', 'IP-адрес', 'Порт', 'Время подключения'])
        test_list.appendRow(
            [QStandardItem('test1'), QStandardItem('192.168.0.7'), QStandardItem('12345'), QStandardItem('20:20:20')])
        test_list.appendRow(
            [QStandardItem('test2'), QStandardItem('192.168.0.9'), QStandardItem('54321'), QStandardItem('20:21:22')])
        main_window.active_clients_tabel.setModel(test_list)
        main_window.active_clients_tabel.resizeColumnsToContents()
        app.exec()
    elif test_window == 'cfg':
        app = QApplication(sys.argv)
        dial = ConfigWindow()
        app.exec()
    elif test_window == 'hist':
        app = QApplication(sys.argv)
        window = HistoryWindow()
        test_list = QStandardItemModel(window)
        test_list.setHorizontalHeaderLabels(
            ['Имя клиента', 'Последний раз входил', 'Отправлено', 'Получено'])
        test_list.appendRow(
            [QStandardItem('test1'), QStandardItem('Fri Feb 25 20:20:20 2022'), QStandardItem('2'), QStandardItem('3')])
        test_list.appendRow(
            [QStandardItem('test2'), QStandardItem('Fri Feb 25 20:21:22 2022'), QStandardItem('7'), QStandardItem('4')])
        window.history_table.setModel(test_list)
        window.history_table.resizeColumnsToContents()
        app.exec()
