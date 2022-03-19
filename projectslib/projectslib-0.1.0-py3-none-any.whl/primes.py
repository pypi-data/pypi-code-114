import math
import itertools

flatten_iter = itertools.chain.from_iterable


class Primes(object):
    def __init__(self):
        self.primes = [2]
        self.sieve = {1}
        self.i = -1
        self.n = 2

    def _extend_sieve(self):
        old_n = self.n
        self.n *= 2
        prime_candidates = range(3, self.n + 1, 2)
        sieve_end = max(self.sieve)
        # print(sieve_end)

        def sieve_check_start(q, sieve_end):
            qmult = math.ceil(sieve_end / q)
            return q * qmult if qmult % 2 == 1 else q * (qmult + 1)

        self.sieve |= set(
            flatten_iter(
                range(
                    max(q ** 2, sieve_check_start(q, sieve_end)),
                    self.n + 1,
                    2 * q,
                )
                for q in prime_candidates
            )
        )
        # print(sorted(self.sieve))
        self.primes += [
            p for p in range(old_n + 1, self.n + 1, 2) if p not in self.sieve
        ]

    def _extend_to_n(self, n):
        while n >= self.n:
            self._extend_sieve()

    def __next__(self):
        self.i += 1
        while self.i >= len(self.primes):
            self._extend_sieve()

        return self.primes[self.i]

    def is_prime(self, p):
        self._extend_to_n(p)
        return p % 2 == 1 and p not in self.sieve

    def prime_factors(self, n):
        dividend = n
        self._extend_to_n(n)
        prime_factors = []
        while dividend not in self.primes:
            for p in self.primes:
                if dividend % p == 0:
                    dividend = dividend // p
                    prime_factors.append(p)
                    break
        prime_factors.append(dividend)
        return sorted(prime_factors)
