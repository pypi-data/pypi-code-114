from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prach:
	"""Prach commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prach", core, parent)

	def get_configuration(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:PRACh:CONFiguration \n
		Snippet: value: int = driver.source.bb.oneweb.uplink.prach.get_configuration() \n
		Sets the PRACH configuration number. \n
			:return: configuration: integer Range: 0 to 63
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:UL:PRACh:CONFiguration?')
		return Conversions.str_to_int(response)

	def set_configuration(self, configuration: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:PRACh:CONFiguration \n
		Snippet: driver.source.bb.oneweb.uplink.prach.set_configuration(configuration = 1) \n
		Sets the PRACH configuration number. \n
			:param configuration: integer Range: 0 to 63
		"""
		param = Conversions.decimal_value_to_str(configuration)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:PRACh:CONFiguration {param}')

	def get_foffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:PRACh:FOFFset \n
		Snippet: value: int = driver.source.bb.oneweb.uplink.prach.get_foffset() \n
		Sets the prach-FrequencyOffset nRAPRBoffset \n
			:return: frequency_offset: integer Range: 0 to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:UL:PRACh:FOFFset?')
		return Conversions.str_to_int(response)

	def set_foffset(self, frequency_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:PRACh:FOFFset \n
		Snippet: driver.source.bb.oneweb.uplink.prach.set_foffset(frequency_offset = 1) \n
		Sets the prach-FrequencyOffset nRAPRBoffset \n
			:param frequency_offset: integer Range: 0 to dynamic
		"""
		param = Conversions.decimal_value_to_str(frequency_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:PRACh:FOFFset {param}')

	def get_rset(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:PRACh:RSET \n
		Snippet: value: bool = driver.source.bb.oneweb.uplink.prach.get_rset() \n
		Enables/disables using of a restricted preamble set. \n
			:return: restricted_set: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:UL:PRACh:RSET?')
		return Conversions.str_to_bool(response)

	def set_rset(self, restricted_set: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:PRACh:RSET \n
		Snippet: driver.source.bb.oneweb.uplink.prach.set_rset(restricted_set = False) \n
		Enables/disables using of a restricted preamble set. \n
			:param restricted_set: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(restricted_set)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:PRACh:RSET {param}')
