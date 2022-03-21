from .nucleus import Nucleus
import numpy as np
from scipy.optimize import curve_fit
from typing import Iterable

# Precalculations
PRECAL_POW = [0] + [(2. * i - 5.) / 3. for i in range(1, 6)]

# Chapter characteristics
# Chapter number:   1  2  3  4  5  6  7  8  9 10 11
TOT_NUM = np.array([2, 3, 4, 3, 4, 5, 6, 4, 5, 6, 5])
INI_NUM = np.array([1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 1])
FIN_NUM = TOT_NUM - INI_NUM
TOT_LEN = TOT_NUM * 5
INI_LEN = INI_NUM * 5
FIN_LEN = FIN_NUM * 5
CHPT = np.zeros((np.amax(INI_NUM), np.amax(FIN_NUM)), dtype=int)
for i in range(11):
    CHPT[INI_NUM[i] - 1, FIN_NUM[i] - 1] = i + 1


class Rate:
    def __init__(self):
        self._chapter = None
        self._initial = None
        self._final = None
        self._dset = None
        self._rtype = None  # blank or n / r / w
        self._reverse = None  # True or False
        self._Q = 0.  # MeV
        self._a = np.empty(7)

    def __repr__(self):
        return "{} <{}_{}{}>".format(self.reaction, self.dset, self.rtype,
                                     "_v" if self.reverse else "")

    def __hash__(self):
        return hash(self.__repr__() + str(np.sum(self._a)))

    def __lt__(self, other):
        if not self.chapter == other.chapter:
            return self.chapter < other.chapter
        else:
            return self.initial[0] < other.initial[0]

    @staticmethod
    def __check_lines(lines):
        try:
            not_all_str = any(not isinstance(line, str) for line in lines)
            if len(lines) != 4 or not_all_str:
                return False
        except TypeError:
            return False
        return True

    @staticmethod
    def __handle_nuclei(nucl):
        """
        Check that 'nucl' is iterable of Nucleus or strings.
        Return numpy array of Nucleus objects.
        """
        if nucl is None:
            return None
        if isinstance(nucl, Nucleus):
            return np.array([nucl])
        if isinstance(nucl, str):
            return np.array([Nucleus(nucl)])
        for i in range(len(nucl)):
            if isinstance(nucl[i], str):
                nucl[i] = Nucleus(nucl[i])
            elif not isinstance(nucl[i], Nucleus):
                raise ValueError("Argument must be string or Nucleus")
        return np.array(nucl)

    @staticmethod
    def __fit_rvals(T9_vs_rval: np.ndarray) -> np.ndarray:
        def fit_func(T9, a0, a1, a2, a3, a4, a5, a6):
            coefs = [a0, a1, a2, a3, a4, a5, a6]
            return Rate.__calc_ln_rval(T9, coefs)

        rvals = np.log(T9_vs_rval[:, 1] + np.finfo(float).eps)
        T9s = T9_vs_rval[:, 0]

        fit, cov = curve_fit(fit_func, T9s, rvals)
        f_vec = np.array([Rate.__calc_ln_rval(T9, fit) for T9 in T9s])
        err = np.linalg.norm(rvals - f_vec) / np.linalg.norm(rvals)
        return fit, err

    @staticmethod
    def __calc_ln_rval(T9: float, coefs: Iterable[float]) -> float:
        rez = coefs[6] * np.log(T9)
        for i in range(6):
            rez += coefs[i] * np.power(T9, PRECAL_POW[i])
        return rez

    @property
    def chapter(self):
        return self._chapter

    @property
    def initial(self):
        return self._initial

    @property
    def final(self):
        return self._final

    @property
    def reaction(self):
        rez = self._initial[0].name
        for nuc in self._initial[1:]:
            rez += " + " + nuc.name
        rez += " -> " + self._final[0].name
        for nuc in self._final[1:]:
            rez += " + " + nuc.name
        return rez

    @property
    def dset(self):
        return self._dset

    @property
    def rtype(self):
        return self._rtype

    @property
    def reverse(self):
        return self._reverse

    @property
    def Q(self):
        return self._Q

    def init_by_lines(self, lines):
        """
        Initialize rate by REACLIB file format lines.
        """
        if not Rate.__check_lines(lines):
            raise ValueError("Rate should be initialized with a list of 4 "
                             "lines in REACLIB format.")

        # Extract chapter
        try:
            self._chapter = int(lines[0])
        except ValueError:
            raise ValueError("Wrong chapter format:\n\t" + lines[0])

        # Parse reaction
        nuclei = parse_reaction_reaclib(lines[1][5:35], self.chapter)
        self._initial = nuclei[0]
        self._final = nuclei[1]

        # Extract set label, reaction type, reverse flag and Q
        self._dset = lines[1][43:47].replace(' ', '')
        self._rtype = lines[1][47]
        # For some reason in original REACLIB there are undocumented flags
        # if self._type not in (" ", "n", "r", "w"):
        #     raise ValueError()
        self._reverse = (lines[1][48] == "v")
        self._Q = np.double(lines[1][52:65])

        # Extract rate approximation
        self._a = np.empty(7)
        self._a = np.zeros(7)
        param_line = lines[2][:-23] + lines[3][:-35]
        for i in range(7):
            self._a[i] = np.double(param_line[13*i:13+13*i])

    def init_by_values(self, reaction=None, initial=None, final=None,
                       nuclei=None, chapter=None, dset=None, rtype=None,
                       reverse=None, Q=0., rvals=None):
        """
        Initialize rate by values.
        """
        self._dset = dset
        self._rtype = rtype
        self._reverse = reverse
        self._Q = Q

        if reaction is not None:
            self._initial, self._final = parse_reaction_natural(reaction)
            self._chapter = CHPT[len(self.initial) - 1, len(self.final) - 1]
        elif initial is not None or final is not None:
            self._initial = Rate.__handle_nuclei(initial)
            self._final = Rate.__handle_nuclei(final)
            if not isinstance(self, RateFilter):
                self._chapter = CHPT[len(self.initial) - 1,
                                     len(self.final) - 1]
        elif nuclei is not None and chapter is not None:
            nuclei = Rate.__handle_nuclei(nuclei)
            ini_n = None
            try:
                ini_n = INI_NUM[chapter - 1]
            except KeyError:
                raise ValueError("Unknown chapter: '{}'".format(chapter))
            self._initial, self._final = nuclei[:ini_n], nuclei[ini_n:]
            self._chapter = chapter
        elif not isinstance(self, RateFilter):
            raise ValueError("Reaction or initial and final nuclei or "
                             "all nuclei and chapter must be given.")
        if self.initial is not None:
            self._initial = np.sort(self.initial)
        if self.final is not None:
            self._final = np.sort(self.final)

        self._a[:] = 0.
        if isinstance(rvals, float):
            # Setting constant rate
            if np.isclose(rvals, 0.) or np.isnan(rvals):
                raise ValueError("Reaction should not have zero or nan rate")
            self._a[0] = np.log(rvals)
        elif isinstance(rvals, np.ndarray) and rvals.shape[1] == 2:
            self._a, err = Rate.__fit_rvals(rvals)
            return err
        elif not isinstance(self, RateFilter):
            raise ValueError("Rate values must be a float scalar for "
                             "constant rate or numpy ndarray T9 vs rate")

    def ln_rval(self, T9):
        """
        Get REACLIB rate parameterization exponent value at given T9.
        """
        if self.is_constant():
            return self._a[0]
        return Rate.__calc_ln_rval(T9, self._a)

    def rval(self, T9):
        """
        Get REACLIB rate parameterization value at given T9.
        """
        return np.exp(self.ln_rval(T9))

    def is_constant(self):
        """
        Check if rate doesn't depend on T9.
        """
        all_zeros = not np.any(self._a[1:])
        return all_zeros

    def reaclib_format(self):
        """
        Return 4 lines in REACLIB format.
        """
        lines = []
        lines.append(str(self.chapter) + "\n")

        line = " " * 5
        nuclei = list(self.initial) + list(self.final)
        for n in nuclei:
            line += "{0:>5s}".format(n.name)
        free_space = 5 * (6 - len(nuclei)) + 8
        dset_str = "" if self.dset is None else self.dset
        rtype_str = "" if self.rtype is None else self.rtype
        reverse_str = "v" if self.reverse else " "
        line += "{0:8s}{1:>4s}{2:>1s}{3:>1s}{4:3s}{5:>12.5e}{6:10s}".format(
            " " * free_space, dset_str, rtype_str, reverse_str, " " * 3,
            self.Q, " " * 10
        )
        lines.append(line + "\n")

        line = ""
        for coef in self._a:
            line += "{0:>13.6e}".format(coef)
        lines.append(line[:52] + " " * 22 + "\n")
        lines.append(line[52:] + " " * 35 + "\n")
        return lines


class RateFilter(Rate):
    def __init__(self, reaction=None, initial=None, final=None, nuclei=None,
                 exact=False, chapter=None, dset=None, rtype=None,
                 reverse=None, filter_function=None):
        if nuclei is not None and chapter is None:
            raise ValueError("If nuclei are given, chapter is also needed")
        super().__init__()
        self.init_by_values(reaction=reaction, initial=initial, final=final,
                            nuclei=nuclei, chapter=chapter, dset=dset,
                            rtype=rtype, reverse=reverse)
        self._exact = exact if reaction is None else True
        self._func = filter_function

    @staticmethod
    def __atleast_one(ref, test):
        """
        Check that atleast one object from ref iterable presents
        in test iterable.
        """
        if ref is None:
            return False
        return any(n in test for n in ref)

    @staticmethod
    def __identical(arr1, arr2):
        """
        Check if two iterables are completely identical regardless of order.
        """
        if arr1 is None or arr2 is None:
            return False
        return np.array_equal(np.sort(arr1), np.sort(arr2))

    def __check_nuclei(self, r: Rate):
        """
        Check that given Rate's nuclei matchs search parameters.
        """
        if self.initial is None and self.final is None:
            return True
        if self._exact:
            initial_m = RateFilter.__identical(self.initial, r.initial)
            final_m = RateFilter.__identical(self.final, r.final)
            return initial_m and final_m
        else:
            initial_m = RateFilter.__atleast_one(self.initial, r.initial)
            final_m = RateFilter.__atleast_one(self.final, r.final)
            return initial_m or final_m

    def check_matches(self, r: Rate):
        """
        Check that given Rate matchs search parameters.
        """
        nuclei_m = self.__check_nuclei(r)
        chapter_m = (self.chapter is None or self.chapter == r.chapter)
        dset_m = (self.dset is None or self.dset == r.dset)
        rtype_m = (self.rtype is None or self.rtype == r.rtype)
        reverse_m = (self.reverse is None or self.reverse == r.reverse)
        function_m = (self._func is None or self._func(r))
        return nuclei_m and chapter_m and dset_m and rtype_m and reverse_m \
            and function_m


def parse_reaction_reaclib(reaction: str, chapter: int):
    """
    Extract initial and final nuclei from REACLIB reaction notation
    with given chapter number.
    Return numpy arrays of initial and final Nucleus objects.
    """
    tot_l = None
    ini_l = None
    fin_l = None
    try:
        tot_l = TOT_LEN[chapter - 1]
        ini_l = INI_LEN[chapter - 1]
        fin_l = FIN_LEN[chapter - 1]
    except KeyError:
        raise ValueError("Unknown chapter: '{}'".format(chapter))
    ini_str = reaction[:ini_l]
    fin_str = reaction[ini_l:tot_l]
    ini_nuc = [Nucleus(ini_str[i:i + 5]) for i in range(0, ini_l, 5)]
    fin_nuc = [Nucleus(fin_str[i:i + 5]) for i in range(0, fin_l, 5)]
    return np.array(ini_nuc), np.array(fin_nuc)


def parse_reaction_natural(reaction: str):
    """
    Extract initial and final nuclei from natural reaction notion, e.g.
    'n15 + p -> c12 + he4'.
    Return numpy arrays of initial and final Nucleus objects.
    """
    ini_str, fin_str = reaction.split(" -> ")
    ini_nuc = [Nucleus(n) for n in ini_str.split(" + ")]
    fin_nuc = [Nucleus(n) for n in fin_str.split(" + ")]
    return np.array(ini_nuc), np.array(fin_nuc)
