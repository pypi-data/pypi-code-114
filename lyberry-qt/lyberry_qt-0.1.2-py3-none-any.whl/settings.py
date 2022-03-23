from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.uic import loadUi

from lyberry_qt.helpers import relative_path
from lyberry_api import settings

app_settings = settings.settings

class SettingsScreen(QtWidgets.QDialog):
    change_url = pyqtSignal()

    def __init__(self, lbry):
        super(SettingsScreen, self).__init__()
        loadUi(relative_path('designer/settings.ui'), self)
        self.url = 'about:settings'
        self._lbry = lbry
        
        self.row = 0
        self.inputs = []
        self.labels = []
        for key in app_settings:
            self.add_input(key, app_settings[key])

        self.apply_button.clicked.connect(self.apply)

    def apply(self, something_else):
        settings.apply()
        self.reapply_settings()

    def reapply_settings(self):
        self._lbry.lbrynet_api = app_settings['lbrynet_api']
        self._lbry.comment_api = app_settings['comment_api']
        self._lbry.lighthouse_api = app_settings['lighthouse_api']
    
    def add_input(self, key, value):
        label = QtWidgets.QLabel()
        label.setText(key)
        self.formLayout.setWidget(self.row, QtWidgets.QFormLayout.LabelRole, label)
        self.labels.append(label)

        inputbox = {}
        if type(value) == str:
            inputbox = QtWidgets.QLineEdit()
            inputbox.setText(value)
        elif type(value) == int:
            inputbox = QtWidgets.QSpinBox()
            inputbox.setValue(value)
        else:
            inputbox = QtWidgets.QLineEdit()
            inputbox.setText(str(value))
            inputbox.setEnabled(False)
            print(f'Config {key} is of unsupported type: {type(value)}')
        self.formLayout.setWidget(self.row, QtWidgets.QFormLayout.FieldRole, inputbox)
        def update_setting():
            app_settings[label.text()] = inputbox.text()
        inputbox.editingFinished.connect(update_setting)
        self.inputs.append(inputbox)

        self.row += 1

class AccountsScreen(QtWidgets.QDialog):
    change_url = pyqtSignal()

    def __init__(self, lbry):
        super(AccountsScreen, self).__init__()
        loadUi(relative_path('designer/account.ui'), self)
        self._lbry = lbry
        self.url = 'about:accounts'
        for account in self._lbry.accounts:
            self._add_account_to_list(account)

        self.add_acc_button.clicked.connect(lambda: self.add_account())

    def add_account(self):
        try:
            account = self._lbry.add_account(
                self.edit_name.text(),
                self.edit_priv_key.text())
        except ValueError:
            print('invalid key!')
            return

        self._add_account_to_list(account)

    def _add_account_to_list(self, account):
        label = QtWidgets.QLabel()
        label.setText(account_to_html(account))
        self.acc_list_section.addWidget(label)
        if not account.is_default:
            default_button = QtWidgets.QPushButton()
            default_button.clicked.connect(account.set_as_default)
            default_button.setText(f'Set {account.name} as the default account')
            self.acc_list_section.addWidget(default_button)

            remove_button = QtWidgets.QPushButton()
            remove_button.clicked.connect(lambda: account.remove())
            remove_button.setText(f'Remove {account.name}')
            self.acc_list_section.addWidget(remove_button)

def account_to_html(account):
    return f'''
<h2>{account.name}{" - Default" if account.is_default else ""}</h2>
<p>
id: {account.id}
<br>
public key: {account.public_key}
</p>
'''

