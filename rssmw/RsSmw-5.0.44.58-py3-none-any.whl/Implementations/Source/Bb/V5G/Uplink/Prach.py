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
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PRACh:CONFiguration \n
		Snippet: value: int = driver.source.bb.v5G.uplink.prach.get_configuration() \n
		No command help available \n
			:return: configuration: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PRACh:CONFiguration?')
		return Conversions.str_to_int(response)

	def set_configuration(self, configuration: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PRACh:CONFiguration \n
		Snippet: driver.source.bb.v5G.uplink.prach.set_configuration(configuration = 1) \n
		No command help available \n
			:param configuration: No help available
		"""
		param = Conversions.decimal_value_to_str(configuration)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:PRACh:CONFiguration {param}')

	def get_foffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PRACh:FOFFset \n
		Snippet: value: int = driver.source.bb.v5G.uplink.prach.get_foffset() \n
		No command help available \n
			:return: frequency_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PRACh:FOFFset?')
		return Conversions.str_to_int(response)

	def set_foffset(self, frequency_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PRACh:FOFFset \n
		Snippet: driver.source.bb.v5G.uplink.prach.set_foffset(frequency_offset = 1) \n
		No command help available \n
			:param frequency_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(frequency_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:PRACh:FOFFset {param}')

	def get_rset(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PRACh:RSET \n
		Snippet: value: bool = driver.source.bb.v5G.uplink.prach.get_rset() \n
		No command help available \n
			:return: restricted_set: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:UL:PRACh:RSET?')
		return Conversions.str_to_bool(response)

	def set_rset(self, restricted_set: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:UL:PRACh:RSET \n
		Snippet: driver.source.bb.v5G.uplink.prach.set_rset(restricted_set = False) \n
		No command help available \n
			:param restricted_set: No help available
		"""
		param = Conversions.bool_to_str(restricted_set)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:UL:PRACh:RSET {param}')
