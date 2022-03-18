import mcstatus
import threading
try:
    import winsound
except ImportError:
    winsound = None
import time
import enum


class Status(enum.Enum):
    OFFLINE = 0
    ONLINE = 1


class Beeper(threading.Thread):
    def run(self) -> None:
        # FIXME this is silent on Linux
        if winsound:
            for _ in range(5):
                winsound.Beep(1000, 200)

    @staticmethod
    def beep():
        Beeper().start()


def main():
    try:
        server = mcstatus.MinecraftServer('connect.2b2t.org')
        last_status = Status.ONLINE
        while True:
            try:
                status = server.status()
            except IOError:
                print('status: offline')
                last_status = Status.OFFLINE
                time.sleep(0.5)
                continue

            if last_status == Status.OFFLINE:
                Beeper.beep()
            last_status = Status.ONLINE
            print(f'status: online players: {status.players.online} latency: {status.latency:.2f}')
            time.sleep(2)
    except KeyboardInterrupt:
        pass  # Ignore Ctrl-C event


if __name__ == '__main__':
    main()
