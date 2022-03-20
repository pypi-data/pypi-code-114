""" Internal RNG helper """

from .iqs import _iqs
import time

_rng = _iqs.RandomNumberGenerator()
_rng_seed = int(time.time())
_rng.SetSeedStreamPtrs(_rng_seed)
