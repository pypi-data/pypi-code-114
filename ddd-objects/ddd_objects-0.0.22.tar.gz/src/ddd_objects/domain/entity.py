from typing import Optional
from time import time


class Entity:
    def get_json(self):
        raise NotImplementedError

class Expired(Entity):
    def __init__(self, life_time:Optional[int]=None) -> None:
        self.life_time = life_time
        if self.life_time is None:
            self.expired_time = None
        else:
            self.expired_time = time()+self.life_time

    @property
    def is_expired(self):
        if self.expired_time is None:
            return False
        else:
            return self.expired_time>time()
