from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mset:
	"""Mset commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mset", core, parent)

	def get_mtype(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:GBAS:MSET:MTYPe \n
		Snippet: value: str = driver.source.bb.gbas.mset.get_mtype() \n
		Queries the used modulation. \n
			:return: mtype: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:MSET:MTYPe?')
		return trim_str_response(response)

	def get_symbol_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:MSET:SRATe \n
		Snippet: value: float = driver.source.bb.gbas.mset.get_symbol_rate() \n
		Queries the used sample rate. \n
			:return: srate: float Range: 10.49E3 to 10.51E3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:MSET:SRATe?')
		return Conversions.str_to_float(response)
