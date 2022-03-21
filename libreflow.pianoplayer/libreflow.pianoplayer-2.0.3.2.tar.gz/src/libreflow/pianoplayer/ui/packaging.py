from kabaret.app.ui.gui.widgets.flow.flow_view import CustomPageWidget, QtWidgets, QtCore, QtGui
from kabaret.app import resources

from libreflow.resources.icons import libreflow as _
from ..resources.icons import gui as _, shotgrid as _


ICON_BY_STATUS = {
    'error': ('icons.gui', 'error'),
    'warning': ('icons.gui', 'warning'),
    'valid': ('icons.libreflow', 'available'),
}


class ShotItem(QtWidgets.QTreeWidgetItem):
    
    def __init__(self, tree, shot):
        super(ShotItem, self).__init__(tree)
        self._tree = tree
        self._shot = None
        self.set_shot(shot)
    
    def set_shot(self, shot):
        self._shot = shot
        self._update()

    def _update(self):
        self.setText(0, self._shot['sg_name'])

        icon = ICON_BY_STATUS[self._shot['status']]
        self.setIcon(1, QtGui.QIcon(resources.get_icon(icon)))
        icon = ('icons.gui', 'found')
        
        if self._shot['layout_src_path'] is None:
            icon = ('icons.gui', 'not_found')
            self.setToolTip(2, 'Not found on disk')
        
        self.setIcon(2, QtGui.QIcon(resources.get_icon(icon)))

        status = self._shot['layout_sg_status']
        self.setIcon(3, QtGui.QIcon(resources.get_icon(('icons.shotgrid', status))))
        self.setToolTip(3, status)

        icon = ('icons.gui', 'found')
        if self._shot['color_src_path'] is None:
            icon = ('icons.gui', 'not_found')
            self.setToolTip(4, 'Not found on disk')
        
        self.setIcon(4, QtGui.QIcon(resources.get_icon(icon)))

        status = self._shot['color_sg_status']
        self.setIcon(5, QtGui.QIcon(resources.get_icon(('icons.shotgrid', status))))
        self.setToolTip(5, status)

        flags = QtCore.Qt.ItemIsEnabled

        if self._shot['status'] != 'error' and self._shot['available']:
            flags |= QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable
            self.setCheckState(0, QtCore.Qt.Unchecked)

        self.setFlags(flags)
    
    def status(self):
        return self._shot['status']
    
    def is_selected(self):
        return self.checkState(0) == QtCore.Qt.Checked
    
    def to_dict(self):
        return self._shot


class ShotList(QtWidgets.QTreeWidget):
    
    def __init__(self, custom_widget, session):
        super(ShotList, self).__init__()
        self._custom_widget = custom_widget
        self.session = session

        self.setHeaderLabels(self.get_columns())
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        
        self.refresh()

        self.header().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
    
    def get_columns(self):
        return ('Shot', 'Status', 'LO files', 'LO status', 'CL files', 'CL status')
    
    def sizeHint(self):
        return QtCore.QSize(300, 500)
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            for item in self.selectedItems():
                if item.checkState(0) == QtCore.Qt.Unchecked:
                    item.setCheckState(0, QtCore.Qt.Checked)
                else:
                    item.setCheckState(0, QtCore.Qt.Unchecked)
    
    def refresh(self, refresh_data=False):
        self.clear()

        shots_data = self._custom_widget.get_shots_data(refresh_data)

        for shot in shots_data:
            ShotItem(self, shot)


class CreateShotPackagesWidget(CustomPageWidget):

    def get_shots_data(self, refresh_data=False):
        return self.session.cmds.Flow.call(
            self.oid, 'get_shots_data', [], dict(refresh=refresh_data)
        )
    
    def create_packages(self, shots_data, do_upload):
        self.session.cmds.Flow.call(
            self.oid, 'create_packages', [shots_data], dict(do_upload=do_upload)
        )

    def build(self):
        self.shot_list = ShotList(self, self.session)
        self.button_refresh = QtWidgets.QPushButton(
            QtGui.QIcon(resources.get_icon(('icons.gui', 'refresh'))), ''
        )
        self.button_refresh.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.button_refresh.setToolTip('Refresh list')
        self.checkbox_selectall = QtWidgets.QCheckBox('Select all')
        self.checkbox_upload = QtWidgets.QCheckBox('Upload now')
        self.button_create = QtWidgets.QPushButton('Create packages')
        
        glo = QtWidgets.QGridLayout()
        glo.addWidget(self.shot_list, 0, 0, 1, 5)
        glo.addWidget(self.button_create, 1, 4)
        glo.addWidget(self.checkbox_selectall, 1, 1)
        glo.addWidget(self.checkbox_upload, 1, 2)
        glo.addWidget(self.button_refresh, 1, 0)
        glo.setColumnStretch(3, 10)
        glo.setSpacing(2)
        self.setLayout(glo)

        self.checkbox_selectall.stateChanged.connect(self.on_checkbox_state_changed)
        self.button_refresh.clicked.connect(self.on_refresh_button_clicked)
        self.button_create.clicked.connect(self.on_create_button_clicked)

    def on_create_button_clicked(self):
        data = []
        for i in range(self.shot_list.topLevelItemCount()):
            item = self.shot_list.topLevelItem(i)

            if item.is_selected():
                data.append(item.to_dict())
        
        do_upload = self.checkbox_upload.checkState() == QtCore.Qt.Checked

        if data:
            self.create_packages(data, do_upload=do_upload)
            self.shot_list.refresh(refresh_data=True)
    
    def on_refresh_button_clicked(self):
        self.checkbox_selectall.setCheckState(QtCore.Qt.Unchecked)
        self.shot_list.refresh(refresh_data=True)
    
    def on_checkbox_state_changed(self, state):
        for i in range(self.shot_list.topLevelItemCount()):
            item = self.shot_list.topLevelItem(i)

            if item.status() != 'error':
                item.setCheckState(0, QtCore.Qt.CheckState(state))
    
    def _close_view(self):
        self.parentWidget().page.view.close()
