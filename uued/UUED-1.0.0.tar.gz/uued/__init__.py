import time

SEQUENCE_BITS = 12
WORKER_ID_BITS = 5
DATACENTER_ID_BITS = 5

TIMESTAMP_LEFT_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS + DATACENTER_ID_BITS

class Generator:
    def __init__(self, epoch: int):
        self.seq = 100
        self._last_ep = 0
        self.ep = epoch

    def increment(self):
        cur_ep = str((time.time()) * 1000)

        _fake_ep = int(cur_ep.split('.')[0])

        ep = _fake_ep - (int(self.ep * 1000))

        self._last_ep = ep

        if self.seq == 999:
            self.seq = 100

        self.seq += 1

        ret = str((ep << TIMESTAMP_LEFT_SHIFT) | self.seq)

        return int(ret[6:])
    
    def __str__(self):
        return str(self.increment())
