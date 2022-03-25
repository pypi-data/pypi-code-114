from pydantic.dataclasses import dataclass
import magnumapi.commons.json_file as json_file

from magnumapi.optimization.config.OptimizationConfig import OptimizationConfig
from magnumapi.optimization.config.ParallelAnsysConfig import ParallelAnsysConfig


@dataclass
class ParallelOptimizationConfig(OptimizationConfig):
    """Class for parallel optimization config used for the genetic algorithm.

    Attributes:
       ansys (ParallelAnsysConfig): parallel ANSYS config

    """
    ansys: ParallelAnsysConfig

    def __str__(self) -> str:
        return super().__str__() + "\nansys: \n\n%s" % self.ansys

    @staticmethod
    def initialize_config(json_path: str) -> "ParallelOptimizationConfig":
        """ Static method initializing an optimization config from a json file

        :param json_path: a path to a json file with config
        :return: initialized OptimizationConfig instance
        """
        data = json_file.read(json_path)

        return ParallelOptimizationConfig(**data)
