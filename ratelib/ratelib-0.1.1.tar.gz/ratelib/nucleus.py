import os
import re
import numpy as np

# Create element vs Z dictationary
PYRLIB_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(PYRLIB_PATH, "data")
EL_VS_Z = {}
Z_VS_EL = ["n"]
with open(os.path.join(DATA_PATH, "elements.txt")) as fd:
    for line in fd:
        Z, element = line.split()
        EL_VS_Z[element.lower()] = int(Z)
        Z_VS_EL.append(element.lower())


class MetaStableError(ValueError):
    """
    Exception for meta stable states that are temporarily unsupported
    """
    pass


class Nucleus:
    """
    Class for nucleus participating in reaction
    """
    def __init__(self, name=None, A=None, Z=None, N=None):
        self._A = np.nan
        self._Z = np.nan

        if name is not None:
            # Default initialisation by name string
            self.__init_by_descr(name)
        elif A is not None or Z is not None or N is not None:
            # Initialization with numbers
            self.__init_by_numbers(A=A, Z=Z, N=N)
        else:
            raise ValueError("Provide nucleus name or nuclear numbers.")

    def __init_by_descr(self, descr):
        re_str = r'^([A-Za-z]{1,2})([-\*]*)(\d{0,3})$'
        descr = descr.replace(' ', '')
        parse_results = re.search(re_str, descr)
        if not parse_results:
            # Undiscovered elements
            re_str = r'^([Cc]\d)([-\*]*)(\d{3})'
            parse_results = re.search(re_str, descr)
            if not parse_results:
                raise ValueError("Failed to parse: '{}'".format(descr))

        if parse_results.group(2) != "":
            msg = "Meta stable states are not supported: '{}'.".format(descr)
            raise MetaStableError(msg)

        element = parse_results.group(1).lower()
        # TODO: refactor
        if parse_results.group(3):
            self._Z = EL_VS_Z[element]
            self._A = int(parse_results.group(3))
        elif element == "n":
            self._Z = 0
            self._A = 1
        elif element == "p":
            self._Z = 1
            self._A = 1
        elif element == "d":
            self._Z = 1
            self._A = 2
        elif element == "t":
            self._Z = 1
            self._A = 3
        else:
            raise ValueError("A was not provided: '{}'".format(descr))

    def __init_by_numbers(self, A=None, Z=None, N=None):
        none_num = (A, Z, N).count(None)
        if none_num > 1:
            raise ValueError("Provide at least 2 values: A, Z or N")
        self._A = A if A is not None else Z + N
        self._Z = Z if Z is not None else A - N
        if self._A < self._Z or self.Z < 0:
            raise ValueError("Mass number too small:"
                             "A = {}, Z = {}".format(self._A, self._Z))

    def __repr__(self):
        if self.Z > 1 or self.A > 3:
            return "{}{}".format(Z_VS_EL[self.Z], self.A)
        elif self.A == 1:
            return "n" if self.Z == 0 else "p"
        elif self.A == 2 and self.Z == 1:
            return "d"
        elif self.A == 3 and self.Z == 1:
            return "t"
        else:
            raise ValueError("Unknown nucleus with A = {} and "
                             "Z = {}.".format(self.A, self.Z))

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return (self.A == other.A) and (self.Z == other.Z)

    def __lt__(self, other):
        if not self.Z == other.Z:
            return self.Z < other.Z
        else:
            return self.A < other.A

    @property
    def A(self):
        return self._A

    @property
    def Z(self):
        return self._Z

    @property
    def N(self):
        return self.A - self.Z

    @property
    def element(self):
        return Z_VS_EL[self.Z]

    @property
    def name(self):
        return self.__repr__()

    def relative(self, dZ=0, dN=0):
        """
        Return Nucleus relative to self.
        """
        Z = self.Z + dZ
        N = self.N + dN
        return Nucleus(Z=Z, N=N)

    def neighbours(self):
        """
        Get array of 8 nearest nuclei
        """
        rez = []
        for dZ in range(-1, 2):
            for dN in range(-1, 2):
                if dZ == 0 and dN == 0:
                    continue
                rez.append(self.relative(dZ=dZ, dN=dN))
        return np.array(rez)
