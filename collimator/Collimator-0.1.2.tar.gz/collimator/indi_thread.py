import time
from threading import Thread

from .controllers import IndiController


class IndiThread:
    QUEUE_READ_INTERVAL = 0.1  # s

    def __init__(self, indi_controller: IndiController) -> None:
        self.indi_controller = indi_controller

    def main_loop(self):
        while True:
            self.indi_controller.read_queue()
            time.sleep(self.QUEUE_READ_INTERVAL)

    def start_thread(self):
        thread = Thread(target=self.main_loop, daemon=True)
        thread.start()
