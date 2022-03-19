from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measure:
	"""Measure commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measure", core, parent)

	def get(self, force: str = None) -> bool:
		"""SCPI: CALibration:ALL:[MEASure] \n
		Snippet: value: bool = driver.calibration.all.measure.get(force = '1') \n
		Starts all internal adjustments that do not need external measuring equipment. Note: If an external frequency converter
		R&S SZU is connected, the internal adjustments are blocked, and the R&S SMW generates an error message. \n
			:param force: string
			:return: measure: 0| 1| OFF| ON"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('force', force, DataType.String, None, is_optional=True))
		response = self._core.io.query_str(f'CALibration:ALL:MEASure? {param}'.rstrip())
		return Conversions.str_to_bool(response)
