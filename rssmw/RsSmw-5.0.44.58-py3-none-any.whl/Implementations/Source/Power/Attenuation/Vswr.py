from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vswr:
	"""Vswr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vswr", core, parent)

	def get(self, vswr: float) -> float:
		"""SCPI: [SOURce]:POWer:ATTenuation:VSWR \n
		Snippet: value: float = driver.source.power.attenuation.vswr.get(vswr = 1.0) \n
		No command help available \n
			:param vswr: No help available
			:return: vswr: No help available"""
		param = Conversions.decimal_value_to_str(vswr)
		response = self._core.io.query_str(f'SOURce:POWer:ATTenuation:VSWR? {param}')
		return Conversions.str_to_float(response)
