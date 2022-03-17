import os

from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt6.QtCore import QPoint, QRect
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtWidgets import (
    QComboBox,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from .markers import BaseMarkerControl, CenterControl, CircleControl


class IndiControl(QWidget):
    def __init__(self, indi_controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.indi_controller = indi_controller
        self.save_callback = None

        layout = QVBoxLayout()

        host_input = QLineEdit()
        host_input.setText("localhost")
        host_label = QLabel("&Host:")
        host_label.setBuddy(host_input)

        port_input = QLineEdit()
        port_input.setText("7624")
        port_label = QLabel("&Port:")
        port_label.setBuddy(port_input)

        connect_button = QPushButton("Connect")
        connect_button.clicked.connect(self.connect)

        camera_selector = QComboBox()
        camera_selector.addItems(["a"])
        camera_label = QLabel("&Camera:")
        camera_label.setBuddy(camera_selector)

        expose_time_input = QLineEdit()
        expose_time_input.setText("0.1")
        expose_time_label = QLabel("&Expose time:")
        expose_time_label.setBuddy(expose_time_input)

        expose_button = QPushButton("Expose")
        expose_button.clicked.connect(self.expose)

        log_view = QPlainTextEdit()

        layout.addWidget(port_label)
        layout.addWidget(port_input)

        layout.addWidget(host_label)
        layout.addWidget(host_input)

        layout.addWidget(connect_button)

        layout.addWidget(camera_label)
        layout.addWidget(camera_selector)

        layout.addWidget(expose_time_label)
        layout.addWidget(expose_time_input)

        layout.addWidget(expose_button)

        layout.addWidget(log_view)

        self.setLayout(layout)

        self.host_input = host_input
        self.port_input = port_input
        self.camera_selector = camera_selector
        self.expose_time_input = expose_time_input
        self.log_view = log_view

    def connect(self):
        host = self.host_input.text()
        port = int(self.port_input.text())
        self.indi_controller.connect(host, port)

    def update_camera_list(self, cameras):
        current_camera = self.camera_selector.currentText()

        for i in range(self.camera_selector.count()):
            self.camera_selector.removeItem(i)
        self.camera_selector.addItems(cameras)

        if current_camera in cameras:
            self.camera_selector.setCurrentIndex(cameras.index(current_camera))

    def insert_log_line(self, msg):
        self.log_view.insertPlainText(msg)

    def expose(self):
        camera = self.camera_selector.currentText()
        time = self.expose_time_input.text()
        self.indi_controller.expose(camera, time)

    def get_save_data(self):
        data = {"indi": {}}
        return data


class ImageDisplay(QWidget):
    def __init__(self, marker_control, *args, **kwargs) -> None:

        filename = os.path.join(os.path.dirname(__file__), "welcome.png")
        self.image = Image.open(filename)
        self.marker_control = marker_control
        self.marker_control.needs_repaint_callback = self.needs_repaint

        super().__init__(*args, **kwargs)

    def update_image(self, image):
        self.image = image
        self.update()

    def resize_img(self, img):

        orignal_ratio = img.width / img.height

        if orignal_ratio > 1.0:
            new_width = max(self.width(), 300)
            scale = new_width / img.width
            new_height = scale * img.height
        else:
            new_height = max(self.height(), 300)
            scale = new_height / img.height
            new_width = scale * img.width

        newsize = (int(new_width), int(new_height))
        return img.resize(newsize)

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)

        resized_image = self.resize_img(self.image)
        qt_image = ImageQt(resized_image)
        img_pixmap = QPixmap.fromImage(qt_image)
        canvas_rect = QRect(QPoint(0, 0), img_pixmap.size())
        paint.drawPixmap(canvas_rect, img_pixmap)

        # optional
        # paint.setRenderHint(QPainter.Antialiasing)

        for marker in self.get_markers():
            marker.paint(paint, canvas_rect)

        paint.end()

    def get_markers(self):
        return self.marker_control.get_controls_to_paint()

    def needs_repaint(self, marker_control, sender):
        self.update()


class MarkerControl(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        layout = QVBoxLayout()

        marker_controls_placeholder = QVBoxLayout()

        center_control = CenterControl(on_change=self.center_marker_changed)

        add_circle_button = QPushButton("Add circle")
        add_circle_button.clicked.connect(self.add_circle_clicked)

        layout.addWidget(center_control)
        layout.addLayout(marker_controls_placeholder)
        layout.addWidget(add_circle_button)

        self.setLayout(layout)
        self.marker_controls_placeholder = marker_controls_placeholder
        self.controls = []
        self.center_control = center_control
        self.needs_repaint_callback = None
        self.save_callback = None

    def add_circle_clicked(self):
        circle_control = CircleControl(
            on_remove=self.remove_control, on_change=self.marker_changed
        )
        circle_control.center_offset = self.center_control.offset
        self.marker_controls_placeholder.addWidget(circle_control)
        self.controls.append(circle_control)
        self.marker_changed(circle_control)

    def marker_changed(self, sender):
        if self.needs_repaint_callback:
            self.needs_repaint_callback(self, sender)

        if self.save_callback:
            self.save_callback()

    def center_marker_changed(self, sender):
        for control in self.controls:
            control.center_offset = sender.offset

        if self.needs_repaint_callback:
            self.needs_repaint_callback(self, sender)

        if self.save_callback:
            self.save_callback()

    def remove_control(self, sender):
        idx = self.controls.index(sender)
        del self.controls[idx]
        sender.deleteLater()
        self.marker_changed(sender)

    def get_controls_to_paint(self):
        return [self.center_control] + self.controls

    def apply_loaded_config(self, loaded_config):
        for c in loaded_config["markers"]:
            if c["type"] == self.center_control.name:
                self.center_control.apply_config(c)
                self.center_marker_changed(self.center_control)
            else:
                marker = BaseMarkerControl.from_config(
                    c, on_remove=self.remove_control, on_change=self.marker_changed
                )
                marker.center_offset = self.center_control.offset
                self.marker_controls_placeholder.addWidget(marker)
                self.controls.append(marker)
                self.marker_changed(marker)

    def get_save_data(self):
        controls = [self.center_control] + self.controls
        data = {"markers": [ctrl.to_config() for ctrl in controls]}
        return data
