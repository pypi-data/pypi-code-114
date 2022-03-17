from PyQt6.QtWidgets import QVBoxLayout, QWidget

from .widgets import ImageDisplay, IndiControl, MarkerControl


class BaseWindow(QWidget):
    name = None
    save_position = True
    save_size = False

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.save_callback = None

    def get_save_data(self):
        size = self.size()
        position = self.pos()
        config = {self.name: {}}
        if self.save_position:
            config[self.name]["position"] = {
                "x": position.x(),
                "y": position.y(),
            }

        if self.save_size:
            config[self.name]["size"] = {
                "width": size.width(),
                "height": size.height(),
            }
        return config

    def resizeEvent(self, event):
        if self.save_callback:
            self.save_callback()

    def moveEvent(self, event):
        if self.save_callback:
            self.save_callback()

    def apply_loaded_config(self, data):
        windows = data.get("windows", {})
        config = windows.get(self.name, {})
        position = config.get("position", None)
        size = config.get("size", None)

        if size:
            self.resize(size["width"], size["height"])

        if position:
            self.move(position["x"], position["y"])


class ConnectionWindow(BaseWindow):
    name = "indi-connection"

    def __init__(self, indi_controller, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.indi_control = IndiControl(indi_controller)
        self.layout.addWidget(self.indi_control)


class MarkerControlWindow(BaseWindow):
    name = "marker-control"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.marker_control = MarkerControl()
        self.layout.addWidget(self.marker_control)


class ImageDisplayWindow(BaseWindow):
    name = "image-display"
    save_size = True

    def __init__(self, marker_control, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.image_display = ImageDisplay(marker_control)
        self.layout.addWidget(self.image_display)
