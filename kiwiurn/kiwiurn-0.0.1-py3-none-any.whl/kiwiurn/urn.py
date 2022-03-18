import random
from typing import Dict


class Urn:
    def __init__(self, counters=Dict[str, int]):
        """Creates an urn filled with tokens.

        counter should be a dictionary with labels, e.g.
        {'black': 5, 'white': 3, 'red': 2}
        represents an urn with 5 black tokens, 3 white tokens, and 2 red tokens.
        """
        self._counters = []
        for key, count in counters.items():
            self._counters += [key]*count

    def draw_with_replacement(self):
        return random.choice(self._counters)

    def _tally(self):
        counter = {}
        for element in self.counters:
            counter[element] = counter.get(element, 0) + 1
        return counter

    def __repr__(self):
        types = self.token_types()
        return f'Urn with {len(types)} token types: {types}'

    def token_types(self):
        return set(self._counters)

    def total_number_of_tokens(self):
        return len(self._counters)



BWUrn1 = Urn({'black': 4, 'white': 5})
BWUrn2 = Urn({'black': 8, 'white': 13})
BWUrn3 = Urn({'black': 15, 'white': 12})
BWUrn4 = Urn({'black': 25, 'white': 21})

RGBUrn1 = Urn({'red': 5, 'green': 6, 'blue': 5})
RGBUrn2 = Urn({'red': 25, 'green': 23, 'blue': 25})
