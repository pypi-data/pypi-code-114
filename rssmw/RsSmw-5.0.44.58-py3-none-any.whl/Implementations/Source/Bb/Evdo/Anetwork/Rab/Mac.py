from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mac:
	"""Mac commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mac", core, parent)

	def get_index(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:RAB:MAC:INDex \n
		Snippet: value: int = driver.source.bb.evdo.anetwork.rab.mac.get_index() \n
		For physical layer, subtype 3 only sets the RAB MAC Index. \n
			:return: index: integer Range: 4 to 127
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:ANETwork:RAB:MAC:INDex?')
		return Conversions.str_to_int(response)

	def set_index(self, index: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:RAB:MAC:INDex \n
		Snippet: driver.source.bb.evdo.anetwork.rab.mac.set_index(index = 1) \n
		For physical layer, subtype 3 only sets the RAB MAC Index. \n
			:param index: integer Range: 4 to 127
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:ANETwork:RAB:MAC:INDex {param}')
