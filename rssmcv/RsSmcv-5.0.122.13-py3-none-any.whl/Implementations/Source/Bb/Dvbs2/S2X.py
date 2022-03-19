from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class S2X:
	"""S2X commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("s2X", core, parent)

	def get_chb(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:S2X:CHB \n
		Snippet: value: bool = driver.source.bb.dvbs2.s2X.get_chb() \n
		Enables or disables the chanel bonding. \n
			:return: chan_bonding: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:S2X:CHB?')
		return Conversions.str_to_bool(response)

	def set_chb(self, chan_bonding: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:S2X:CHB \n
		Snippet: driver.source.bb.dvbs2.s2X.set_chb(chan_bonding = False) \n
		Enables or disables the chanel bonding. \n
			:param chan_bonding: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(chan_bonding)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:S2X:CHB {param}')

	def get_sf(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:S2X:SF \n
		Snippet: value: bool = driver.source.bb.dvbs2.s2X.get_sf() \n
		Enables or disables the super frame. \n
			:return: super_frame: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:S2X:SF?')
		return Conversions.str_to_bool(response)

	def set_sf(self, super_frame: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:S2X:SF \n
		Snippet: driver.source.bb.dvbs2.s2X.set_sf(super_frame = False) \n
		Enables or disables the super frame. \n
			:param super_frame: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(super_frame)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:S2X:SF {param}')

	def get_value(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:S2X \n
		Snippet: value: bool = driver.source.bb.dvbs2.s2X.get_value() \n
		Enables S2-X features. \n
			:return: s_2_xstate: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:S2X?')
		return Conversions.str_to_bool(response)

	def set_value(self, s_2_xstate: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:S2X \n
		Snippet: driver.source.bb.dvbs2.s2X.set_value(s_2_xstate = False) \n
		Enables S2-X features. \n
			:param s_2_xstate: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(s_2_xstate)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:S2X {param}')
