from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Awgn:
	"""Awgn commands group definition. 6 total commands, 3 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("awgn", core, parent)

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def rblock(self):
		"""rblock commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rblock'):
			from .Rblock import Rblock
			self._rblock = Rblock(self._core, self._cmd_group)
		return self._rblock

	@property
	def rpDetection(self):
		"""rpDetection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpDetection'):
			from .RpDetection import RpDetection
			self._rpDetection = RpDetection(self._core, self._cmd_group)
		return self._rpDetection

	def get_cn_ratio(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:AWGN:CNRatio \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.awgn.get_cn_ratio() \n
		Sets/queries the carrier/noise ratio. \n
			:return: cn_ratio: float Range: -50 to 45
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:AWGN:CNRatio?')
		return Conversions.str_to_float(response)

	def set_cn_ratio(self, cn_ratio: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:AWGN:CNRatio \n
		Snippet: driver.source.bb.w3Gpp.ts25141.awgn.set_cn_ratio(cn_ratio = 1.0) \n
		Sets/queries the carrier/noise ratio. \n
			:param cn_ratio: float Range: -50 to 45
		"""
		param = Conversions.decimal_value_to_str(cn_ratio)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:AWGN:CNRatio {param}')

	def get_en_ratio(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:AWGN:ENRatio \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.awgn.get_en_ratio() \n
		Sets/queries the ratio of bit energy to noise power density. \n
			:return: en_ratio: float Range: 0 to 20
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:AWGN:ENRatio?')
		return Conversions.str_to_float(response)

	def set_en_ratio(self, en_ratio: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:AWGN:ENRatio \n
		Snippet: driver.source.bb.w3Gpp.ts25141.awgn.set_en_ratio(en_ratio = 1.0) \n
		Sets/queries the ratio of bit energy to noise power density. \n
			:param en_ratio: float Range: 0 to 20
		"""
		param = Conversions.decimal_value_to_str(en_ratio)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:AWGN:ENRatio {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:AWGN:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.ts25141.awgn.get_state() \n
		Enables/disables the generation of the AWGN signal. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:AWGN:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:AWGN:STATe \n
		Snippet: driver.source.bb.w3Gpp.ts25141.awgn.set_state(state = False) \n
		Enables/disables the generation of the AWGN signal. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:AWGN:STATe {param}')

	def clone(self) -> 'Awgn':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Awgn(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
