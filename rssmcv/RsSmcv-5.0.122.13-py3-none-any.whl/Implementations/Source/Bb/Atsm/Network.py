from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("network", core, parent)

	def get_id(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ATSM:NETWork:ID \n
		Snippet: value: int = driver.source.bb.atsm.network.get_id() \n
		Sets the network ID for the watermark. The network ID is a three-digit value in hexadecimal format. \n
			:return: netw_id: integer Range: 0 to 4095
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:NETWork:ID?')
		return Conversions.str_to_int(response)

	def set_id(self, netw_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:NETWork:ID \n
		Snippet: driver.source.bb.atsm.network.set_id(netw_id = 1) \n
		Sets the network ID for the watermark. The network ID is a three-digit value in hexadecimal format. \n
			:param netw_id: integer Range: 0 to 4095
		"""
		param = Conversions.decimal_value_to_str(netw_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:NETWork:ID {param}')
