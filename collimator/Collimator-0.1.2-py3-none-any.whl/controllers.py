from __future__ import annotations

import queue
from dataclasses import dataclass
from datetime import datetime
from io import BytesIO
from typing import Any, Dict, List

from astropy.io import fits
from PIL import Image
from PyQt6.QtCore import QTimer

from .indi_client import IndiClient


@dataclass
class Message:
    method: str
    args: List[Any]
    kwargs: Dict[str, Any]


class Controller:
    class Methods:
        def __init__(self, controller: Controller) -> None:
            self.controller = controller

    def __init__(self) -> None:
        self._q = queue.Queue()
        self._target = self.Methods(self)
        self._read_queue()

    def _read_queue(self):
        try:
            while True:
                msg = self._q.get_nowait()
                try:
                    getattr(self._target, msg.method)(*msg.args, **msg.kwargs)
                except Exception as e:
                    print(e)
        except queue.Empty:
            pass

    def _add_to_queue(self, msg: Message):
        self._q.put(msg)

    def __getattr__(self, name: str) -> Any:
        def inner_fun(*args, **kwargs):
            self._add_to_queue(Message(method=name, args=args, kwargs=kwargs))

        return inner_fun


class GuiController(Controller):
    INTERVAL = 200  # ms

    def __init__(self) -> None:
        self.indi_control = None
        self.image_display = None
        self.timer = None
        super().__init__()

    def setup_interval(self):
        timer = QTimer()
        timer.timeout.connect(self._read_queue)
        timer.setInterval(self.INTERVAL)
        timer.start()
        self.timer = timer

    class Methods(Controller.Methods):
        def log(self, text):
            time = datetime.now().isoformat()
            self.controller.indi_control.insert_log_line(f"[{time}] {text}\n")

        def update_camera_selector(self, cameras):
            self.controller.indi_control.update_camera_list(cameras)

        def update_image(self, data, format):
            if format.lower() == ".fits":
                stream = BytesIO(data)
                fitsarray = fits.getdata(stream)

                # fitsarray -= fitsarray.min()
                # fitsarray += 255/fitsarray.max()
                # fitsarray = fitsarray.astype("uint8")

                image = Image.fromarray(fitsarray)
            else:
                stream = BytesIO(data)
                image = Image.open(stream)

            print(image)
            self.controller.image_display.update_image(image)


class IndiController(Controller):
    def __init__(self, gui_controller: GuiController) -> None:
        self.client = None
        self.gui_controller = gui_controller
        super().__init__()

    def read_queue(self):
        self._read_queue()

    class Methods(Controller.Methods):
        def connect(self, host, port):
            if self.controller.client:
                self.controller.client.disconnect()
                self.controller.gui_controller.log("Disconnected previous connection")
            self.controller.gui_controller.log(f"Connecting to {host}:{port}...")
            try:
                self.controller.client = IndiClient(self.controller.gui_controller)
                self.controller.client.connect(host, port)
            except Exception as e:
                self.controller.gui_controller.log(f"Connection error: {e}")
            self.controller.gui_controller.log(f"Connected to {host}:{port}")

        def disconnect(self):
            if self.controller.client:
                self.controller.client.disconnect()
                self.controller.gui_controller.log("Disconnected previous connection")

        def expose(self, camera, time):
            self.controller.client.ensure_connected(camera)
            self.controller.client.expose(camera, time)
