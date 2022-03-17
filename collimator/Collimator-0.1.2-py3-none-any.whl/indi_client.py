from time import sleep

from indi.client.client import Client
from indi.device.properties.const import DriverInterface
from indi.message.const import State, SwitchState
from indi.transport.client import TCP

from .utils import sizeof_fmt


class IndiClient:
    def __init__(self, gui_controller) -> None:
        self.gui_controller = gui_controller
        self.cameras = []
        self.client = None

    def connect(self, host, port):
        control_connection = TCP(host, port)
        blob_connection = TCP(host, port)
        self.client = Client(control_connection, blob_connection)
        self.client.onevent(
            callback=self.device_discovered,
            vector="DRIVER_INFO",
            element="DRIVER_INTERFACE",
        )
        self.client.onevent(
            callback=self.expose_time_changed,
            vector="CCD_EXPOSURE",
            element="CCD_EXPOSURE_VALUE",
        )
        self.client.onevent(callback=self.blob_received, vector="CCD1", element="CCD1")
        self.client.start()

    def disconnect(self):
        self.client.stop()

    def device_discovered(self, event):
        if DriverInterface.CCD & int(event.new_value):
            camera = event.device.name
            if not camera in self.cameras:
                self.cameras.append(camera)
                self.gui_controller.update_camera_selector(self.cameras)
                self.gui_controller.log(f"Camera found: {camera}")

    def expose_time_changed(self, event):
        print(event)

    def blob_received(self, event):
        blob = event.element.value
        if not blob:
            return

        size = sizeof_fmt(len(blob))

        print(f"Got new image blob size={size} md5={blob.md5} format={blob.format}")
        print(event)
        if size:
            self.gui_controller.update_image(blob.binary, blob.format)

    def ensure_connected(self, camera):
        if self.client[camera]["CONNECTION"]["CONNECT"].value != SwitchState.ON:
            self.gui_controller.log(f"Connecting camera: {camera}")
            self.client[camera]["CONNECTION"]["CONNECT"].value = SwitchState.ON
            self.client[camera]["CONNECTION"].submit()
            self.client.waitforevent(
                device=camera,
                vector="CONNECTION",
                element="CONNECT",
                check=lambda e: e.element.value == SwitchState.ON
                and e.vector.state == State.OK,
            )
            sleep(2)
            self.gui_controller.log(f"Camera connected: {camera}")
        else:
            self.gui_controller.log(f"Camera already connected: {camera}")

    def expose(self, camera, time):
        self.client[camera]["CCD_EXPOSURE"]["CCD_EXPOSURE_VALUE"].value = time
        self.client[camera]["CCD_EXPOSURE"].submit()
