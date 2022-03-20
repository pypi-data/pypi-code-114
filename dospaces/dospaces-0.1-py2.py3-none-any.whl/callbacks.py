import os

from tqdm import tqdm


class ProgressPercentage(object):

    def __init__(self, filename):
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0

    def __call__(self, bytes_amount):
        with tqdm(total=self._size, desc='Upload progress') as t:
            self._seen_so_far += bytes_amount
            t.write('\r')
            t.update(self._seen_so_far)
