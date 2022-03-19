from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Otime:
	"""Otime commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("otime", core, parent)

	def get_set(self) -> int:
		"""SCPI: DIAGnostic:INFO:OTIMe:SET \n
		Snippet: value: int = driver.diagnostic.info.otime.get_set() \n
		No command help available \n
			:return: set_py: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:INFO:OTIMe:SET?')
		return Conversions.str_to_int(response)

	def set_set(self, set_py: int) -> None:
		"""SCPI: DIAGnostic:INFO:OTIMe:SET \n
		Snippet: driver.diagnostic.info.otime.set_set(set_py = 1) \n
		No command help available \n
			:param set_py: No help available
		"""
		param = Conversions.decimal_value_to_str(set_py)
		self._core.io.write(f'DIAGnostic:INFO:OTIMe:SET {param}')

	def get_value(self) -> int:
		"""SCPI: DIAGnostic:INFO:OTIMe \n
		Snippet: value: int = driver.diagnostic.info.otime.get_value() \n
		Queries the operating hours of the instrument so far. \n
			:return: operation_time: integer Range: 0 to INT_MAX
		"""
		response = self._core.io.query_str('DIAGnostic:INFO:OTIMe?')
		return Conversions.str_to_int(response)
