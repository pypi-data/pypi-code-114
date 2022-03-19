from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Refsig:
	"""Refsig commands group definition. 7 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refsig", core, parent)

	@property
	def niot(self):
		"""niot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_niot'):
			from .Niot import Niot
			self._niot = Niot(self._core, self._cmd_group)
		return self._niot

	def get_epre(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:REFSig:EPRE \n
		Snippet: value: float = driver.source.bb.eutra.downlink.refsig.get_epre() \n
		Queries the RS Power per RE relative to Level Display. \n
			:return: rel_to_level_displ: float Range: -1e3 to 1e3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:REFSig:EPRE?')
		return Conversions.str_to_float(response)

	def get_fpower(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:REFSig:FPOWer \n
		Snippet: value: float = driver.source.bb.eutra.downlink.refsig.get_fpower() \n
		No command help available \n
			:return: first_power: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:REFSig:FPOWer?')
		return Conversions.str_to_float(response)

	def set_fpower(self, first_power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:REFSig:FPOWer \n
		Snippet: driver.source.bb.eutra.downlink.refsig.set_fpower(first_power = 1.0) \n
		No command help available \n
			:param first_power: No help available
		"""
		param = Conversions.decimal_value_to_str(first_power)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:REFSig:FPOWer {param}')

	def get_power(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:REFSig:POWer \n
		Snippet: value: float = driver.source.bb.eutra.downlink.refsig.get_power() \n
		Sets the reference signal power. \n
			:return: power: float Range: -80 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:REFSig:POWer?')
		return Conversions.str_to_float(response)

	def set_power(self, power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:REFSig:POWer \n
		Snippet: driver.source.bb.eutra.downlink.refsig.set_power(power = 1.0) \n
		Sets the reference signal power. \n
			:param power: float Range: -80 to 10
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:REFSig:POWer {param}')

	def get_prs(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:REFSig:PRS \n
		Snippet: value: str = driver.source.bb.eutra.downlink.refsig.get_prs() \n
		No command help available \n
			:return: prs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:REFSig:PRS?')
		return trim_str_response(response)

	def set_prs(self, prs: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:REFSig:PRS \n
		Snippet: driver.source.bb.eutra.downlink.refsig.set_prs(prs = '1') \n
		No command help available \n
			:param prs: No help available
		"""
		param = Conversions.value_to_quoted_str(prs)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:REFSig:PRS {param}')

	def get_sc_offset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:REFSig:SCOFfset \n
		Snippet: value: int = driver.source.bb.eutra.downlink.refsig.get_sc_offset() \n
		No command help available \n
			:return: sub_carr_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:REFSig:SCOFfset?')
		return Conversions.str_to_int(response)

	def set_sc_offset(self, sub_carr_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:REFSig:SCOFfset \n
		Snippet: driver.source.bb.eutra.downlink.refsig.set_sc_offset(sub_carr_offset = 1) \n
		No command help available \n
			:param sub_carr_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(sub_carr_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:REFSig:SCOFfset {param}')

	def get_spower(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:REFSig:SPOWer \n
		Snippet: value: float = driver.source.bb.eutra.downlink.refsig.get_spower() \n
		No command help available \n
			:return: symbol_power: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:REFSig:SPOWer?')
		return Conversions.str_to_float(response)

	def set_spower(self, symbol_power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:REFSig:SPOWer \n
		Snippet: driver.source.bb.eutra.downlink.refsig.set_spower(symbol_power = 1.0) \n
		No command help available \n
			:param symbol_power: No help available
		"""
		param = Conversions.decimal_value_to_str(symbol_power)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:REFSig:SPOWer {param}')

	def clone(self) -> 'Refsig':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Refsig(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
