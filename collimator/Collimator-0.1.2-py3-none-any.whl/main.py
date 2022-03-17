from os import path

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication

from .config import Config
from .controllers import GuiController, IndiController
from .indi_thread import IndiThread
from .windows import ConnectionWindow, ImageDisplayWindow, MarkerControlWindow


def main():
    config = Config()
    loaded_config = config.load()

    app = QApplication([])
    icon_path = path.join(path.dirname(__file__), "icon.png")
    app.setWindowIcon(QIcon(icon_path))

    gui_controller = GuiController()
    indi_controller = IndiController(gui_controller)
    indi_thread = IndiThread(indi_controller)
    indi_thread.start_thread()


    connection_window = ConnectionWindow(indi_controller)
    gui_controller.indi_control = connection_window.indi_control
    connection_window.show()

    marker_control_window = MarkerControlWindow()
    marker_control_window.marker_control.apply_loaded_config(loaded_config)
    marker_control_window.show()

    image_display_window = ImageDisplayWindow(marker_control_window.marker_control)
    gui_controller.image_display = image_display_window.image_display
    image_display_window.show()


    def save_callback():
        save_data = {}
        save_data.update(connection_window.indi_control.get_save_data())
        save_data.update(marker_control_window.marker_control.get_save_data())
        save_data["windows"] = {}
        save_data["windows"].update(connection_window.get_save_data())
        save_data["windows"].update(marker_control_window.get_save_data())
        save_data["windows"].update(image_display_window.get_save_data())
        config.save(save_data)


    marker_control_window.marker_control.save_callback = save_callback
    connection_window.indi_control.save_callback = save_callback

    connection_window.apply_loaded_config(loaded_config)
    marker_control_window.apply_loaded_config(loaded_config)
    image_display_window.apply_loaded_config(loaded_config)

    connection_window.save_callback = save_callback
    marker_control_window.save_callback = save_callback
    image_display_window.save_callback = save_callback

    gui_controller.setup_interval()
    config.save(None)
    config.setup_interval()

    app.exec()
