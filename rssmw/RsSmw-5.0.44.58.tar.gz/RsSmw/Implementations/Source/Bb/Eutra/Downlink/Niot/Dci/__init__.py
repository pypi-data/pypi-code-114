from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dci:
	"""Dci commands group definition. 36 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dci", core, parent)

	@property
	def alloc(self):
		"""alloc commands group. 28 Sub-classes, 0 commands."""
		if not hasattr(self, '_alloc'):
			from .Alloc import Alloc
			self._alloc = Alloc(self._core, self._cmd_group)
		return self._alloc

	def get_awa_round(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:AWARound \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.niot.dci.get_awa_round() \n
		If enabled, the NPDSCH allocations are relocated at the beginning of the ARB sequence to ensure a consistent signal. \n
			:return: alloc_wrap_around: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:AWARound?')
		return Conversions.str_to_bool(response)

	def set_awa_round(self, alloc_wrap_around: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:AWARound \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.set_awa_round(alloc_wrap_around = False) \n
		If enabled, the NPDSCH allocations are relocated at the beginning of the ARB sequence to ensure a consistent signal. \n
			:param alloc_wrap_around: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(alloc_wrap_around)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:AWARound {param}')

	def get_nalloc(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:NALLoc \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.dci.get_nalloc() \n
		Sets the number of configurable DCIs. \n
			:return: no_alloc: integer Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:NALLoc?')
		return Conversions.str_to_int(response)

	def set_nalloc(self, no_alloc: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:NALLoc \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.set_nalloc(no_alloc = 1) \n
		Sets the number of configurable DCIs. \n
			:param no_alloc: integer Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(no_alloc)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:NALLoc {param}')

	def clone(self) -> 'Dci':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dci(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
