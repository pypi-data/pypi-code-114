"""Exercise ThirdChapter"""
import logging
from configparser import ConfigParser
from dataclasses import dataclass, field
import numpy as np

from utils.log import InternalLogger
from utils.math import is_parallel


@dataclass
class Result:
    """
    Object that encapsulates the distance results

        Params
        ------
        distance: float
            distance between E and the line DB
        ab_length: float
            current length of AB
        cd_length: float
            current length of CD
    """
    distance: float = field(default=None)
    ab_length: float = field(default=None)
    cd_length: float = field(default=None)

    def __str__(self):
        return f'({self.distance},{self.ab_length},{self.cd_length})'


@dataclass
class Resolution:
    """
    General object for resolutions. Here we should be able to use the results
    """
    raw_results = list()
    result = Result

    def plot(self):
        pass

    def get_config(self):
        pass


@dataclass
class ThreeCSix(Resolution):
    """
    Produce an object of the problem ThirdChapter.

        Parameters
        ----------

        position_a: ndarray
            position A, position of the first(upper) duct
        position_e: ndarray
            position E, position of the thermometer
        position_c: ndarray
            position C, position of the second(lower) duct
        lambda_ab: ndarray
            unitary vector AB
        lambda_cd: ndarray
            unitary vector CD
        upper_range: float
            upper part of the range that determines the size of A and the size C
        lower_range: float
            lower part of the range that determines the size of A and the size C
        step: float,optional
            step to move on the range, also determines the precision of the answer

        Methods
        -------
        get_minimal_distance()

        calculate_distance_e_db()

        solve()

        Examples
        --------
        Solve the problem with the default values

        >> from numpy import array
        >> a = ThirdChapter(
                array([0.0, 4, 96]),
                array([90.0, 52.0, 0.0]),
                array([120.0, 36.0, 100.0]),
                array([7/9, -4/9, 4/9]),
                array([-7/9, 4/9, -4/9]),
                36.0,
                9.0
            )
        >> print(a.solve())

        (80.67809762705207,36.0,36.0)
    """
    # Unit
    # TODO Implement conversion and use of [pint](https://pint.readthedocs.io/en/0.6/numpy.html)

    logger: InternalLogger = field()

    # Position of the first duct
    position_a: np.ndarray = field(default=np.array([0.0, 96.0, 4.0]))

    # Position of the thermometer
    position_e: np.ndarray = field(default=np.array([90.0, 52.0, 0.0]))

    # Position of the second duct
    position_c: np.ndarray = field(default=np.array([120.0, 36.0, 100.0]))

    lambda_ab: np.ndarray = field(default=np.array([7 / 9, -4 / 9, 4 / 9]))
    lambda_cd: np.ndarray = field(default=np.array([-7 / 9, 4 / 9, -4 / 9]))

    upper_range: float = field(default=36.0)
    lower_range: float = field(default=9.0)

    range: np.ndarray = field(init=False)

    step: float = field(default=1.0)

    def __post_init__(self):
        self.range = np.arange(self.lower_range, self.upper_range + self.step, self.step)

        # Check if lambda_ab and lambda_cd are parallels
        if not is_parallel(self.lambda_ab, self.lambda_cd):
            self.logger.log(f"{self.lambda_ab} and {self.lambda_cd} should be parallel", logging.DEBUG)

            raise Exception(f"{self.lambda_ab} and {self.lambda_cd} should be parallel")

    def get_minimal_distance(self, values: list[Result]) -> Result:
        """
        Get minimal distance on a list of results
        :param values: list of results from the distance of e from the line DB
        :type values: list[Result]
        """
        minimal_result = None

        for value in values:
            self.logger.log(str(value), logging.DEBUG)

            dist = value.distance
            ab_length = value.ab_length
            cd_length = value.cd_length

            if minimal_result is None:
                minimal_result = Result(dist, ab_length, cd_length)

            if dist < minimal_result.distance:
                minimal_result.distance = dist
                minimal_result = Result(dist, ab_length, cd_length)

        self.logger.log(f"minimal_distance: {minimal_result}", logging.DEBUG)
        return minimal_result

    def calculate_distance_e_db(self, ab_length: float, cd_length: float) -> Result:
        """
        Calculate the distance between the E point and the line DB
        :param ab_length: the current length of AB
        :type ab_length: float
        :param cd_length: the current length of CD
        :type cd_length: float
        :return: Result(a,b,distance)
        """

        # Get the vector for the value of AB over the unitary vector lambda AB
        ab_vector = ab_length * self.lambda_ab
        self.logger.log(f"ab_vector = {ab_vector}", logging.DEBUG)

        # Get the vector for the value of C over the unitary vector lambda CD
        cd_vector = cd_length * self.lambda_cd
        self.logger.log(f"cd_vector = {cd_vector}", logging.DEBUG)

        r_a = self.position_a
        r_c = self.position_c
        r_e = self.position_e
        self.logger.log(f"r_a = {r_a}", logging.DEBUG)
        self.logger.log(f"r_c = {r_c}", logging.DEBUG)
        self.logger.log(f"r_e = {r_e}", logging.DEBUG)

        # Get r_b and r_d
        r_b = ab_vector + r_a
        r_d = cd_vector + r_c
        self.logger.log(f"r_b = {r_b}", logging.DEBUG)
        self.logger.log(f"r_d = {r_d}", logging.DEBUG)

        # Get r_db and r_de
        r_db = r_b - r_d
        r_de = r_e - r_d

        self.logger.log(f"r_db = {r_db}", logging.DEBUG)
        self.logger.log(f"r_de = {r_db}", logging.DEBUG)

        # Get the lambda DB value
        lambda_db = r_db / (np.sqrt(np.vdot(r_db, r_db)))
        self.logger.log(f"λ_db = {lambda_db}", logging.DEBUG)

        line_e = np.cross(lambda_db, r_de)
        self.logger.log(f"line_e = {line_e}", logging.DEBUG)

        # Get the distance of the E Point to the DB line
        distance_e = np.sqrt(np.vdot(line_e, line_e))

        return Result(distance_e, ab_length, cd_length)

    def get_config(self) -> ConfigParser:
        """
        Return basic configuration to populate a configuration
        :return: ConfigParser
        """
        config = ConfigParser()

        config["positions"] = {
            "position_a_x": self.position_a[0],
            "position_a_y": self.position_a[1],
            "position_a_z": self.position_a[2],

            "position_e_x": self.position_e[0],
            "position_e_y": self.position_e[1],
            "position_e_z": self.position_e[2],

            "position_c_x": self.position_c[0],
            "position_c_y": self.position_c[1],
            "position_c_z": self.position_c[2],
        }

        config["lambdas"] = {
            "lambda_ab_x": self.lambda_ab[0],
            "lambda_ab_y": self.lambda_ab[1],
            "lambda_ab_z": self.lambda_ab[2],

            "lambda_cd_x": self.lambda_cd[0],
            "lambda_cd_y": self.lambda_cd[1],
            "lambda_cd_z": self.lambda_cd[2]
        }

        config["range"] = {
            "upper_range": self.upper_range,
            "lower_range": self.lower_range,
            "step": self.step
        }

        return config

    def solve(self) -> Result:
        """
        Solves the basic exercise and set the results' field
        :return: Result
        """

        # Loops by all possibilites for the size of a and c determined by the range
        values = []
        for ab_length in self.range:
            for cd_length in self.range:
                distance_e = self.calculate_distance_e_db(ab_length, cd_length)
                self.logger.log(f"distance_e: {distance_e}", logging.DEBUG)
                values.append(Result(distance_e.distance, ab_length, cd_length))

        self.raw_results = values

        self.result = self.get_minimal_distance(values)

        return self.result


