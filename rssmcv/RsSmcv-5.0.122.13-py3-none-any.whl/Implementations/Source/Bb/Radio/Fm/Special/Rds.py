from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rds:
	"""Rds commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rds", core, parent)

	def get_phase(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:[SPECial]:RDS:PHASe \n
		Snippet: value: float = driver.source.bb.radio.fm.special.rds.get_phase() \n
		Sets the phase offset of the suppressed 57 kHz carrier. \n
			:return: offset_rds: float Range: -180 to 180
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:SPECial:RDS:PHASe?')
		return Conversions.str_to_float(response)

	def set_phase(self, offset_rds: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:[SPECial]:RDS:PHASe \n
		Snippet: driver.source.bb.radio.fm.special.rds.set_phase(offset_rds = 1.0) \n
		Sets the phase offset of the suppressed 57 kHz carrier. \n
			:param offset_rds: float Range: -180 to 180
		"""
		param = Conversions.decimal_value_to_str(offset_rds)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:SPECial:RDS:PHASe {param}')
