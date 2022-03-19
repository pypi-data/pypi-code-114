from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wsignal:
	"""Wsignal commands group definition. 21 total commands, 5 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wsignal", core, parent)

	@property
	def dpcch(self):
		"""dpcch commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpcch'):
			from .Dpcch import Dpcch
			self._dpcch = Dpcch(self._core, self._cmd_group)
		return self._dpcch

	@property
	def dpdch(self):
		"""dpdch commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpdch'):
			from .Dpdch import Dpdch
			self._dpdch = Dpdch(self._core, self._cmd_group)
		return self._dpdch

	@property
	def pcpch(self):
		"""pcpch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcpch'):
			from .Pcpch import Pcpch
			self._pcpch = Pcpch(self._core, self._cmd_group)
		return self._pcpch

	@property
	def prach(self):
		"""prach commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import Prach
			self._prach = Prach(self._core, self._cmd_group)
		return self._prach

	@property
	def trigger(self):
		"""trigger commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	# noinspection PyTypeChecker
	def get_btype(self) -> enums.Ts25141WsbLkScen:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:BTYPe \n
		Snippet: value: enums.Ts25141WsbLkScen = driver.source.bb.w3Gpp.ts25141.wsignal.get_btype() \n
		Selects the type of blocking scenario and determines the type of interfering signal and its level. \n
			:return: btype: WIDE| COLocated| NARRow
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:BTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141WsbLkScen)

	def set_btype(self, btype: enums.Ts25141WsbLkScen) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:BTYPe \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.set_btype(btype = enums.Ts25141WsbLkScen.COLocated) \n
		Selects the type of blocking scenario and determines the type of interfering signal and its level. \n
			:param btype: WIDE| COLocated| NARRow
		"""
		param = Conversions.enum_scalar_to_str(btype, enums.Ts25141WsbLkScen)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:BTYPe {param}')

	def get_dc_ratio(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DCRatio \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.wsignal.get_dc_ratio() \n
		Sets channel power ratio of DPCCH to DPDCH. \n
			:return: dc_ratio: float Range: -80 to 80
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:DCRatio?')
		return Conversions.str_to_float(response)

	def set_dc_ratio(self, dc_ratio: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DCRatio \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.set_dc_ratio(dc_ratio = 1.0) \n
		Sets channel power ratio of DPCCH to DPDCH. \n
			:param dc_ratio: float Range: -80 to 80
		"""
		param = Conversions.decimal_value_to_str(dc_ratio)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:DCRatio {param}')

	def get_frequency(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:FREQuency \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.wsignal.get_frequency() \n
		The command sets the RF frequency of the wanted signal. \n
			:return: frequency: float Range: 100E3 to 6E9
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, frequency: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:FREQuency \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.set_frequency(frequency = 1.0) \n
		The command sets the RF frequency of the wanted signal. \n
			:param frequency: float Range: 100E3 to 6E9
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:FREQuency {param}')

	# noinspection PyTypeChecker
	def get_oband(self) -> enums.Ts25141WsoPband:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:OBANd \n
		Snippet: value: enums.Ts25141WsoPband = driver.source.bb.w3Gpp.ts25141.wsignal.get_oband() \n
		Selects the operating band of the base station for 'Wideband Blocking'. The operating band is required for calculation of
		power levels and interferer modulation. \n
			:return: oband: I| II| III| IV| V| VI
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:OBANd?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141WsoPband)

	def set_oband(self, oband: enums.Ts25141WsoPband) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:OBANd \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.set_oband(oband = enums.Ts25141WsoPband.I) \n
		Selects the operating band of the base station for 'Wideband Blocking'. The operating band is required for calculation of
		power levels and interferer modulation. \n
			:param oband: I| II| III| IV| V| VI
		"""
		param = Conversions.enum_scalar_to_str(oband, enums.Ts25141WsoPband)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:OBANd {param}')

	def get_power(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:POWer \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.wsignal.get_power() \n
		Sets the RF level of the wanted signal. \n
			:return: power: float
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:POWer?')
		return Conversions.str_to_float(response)

	def set_power(self, power: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:POWer \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.set_power(power = 1.0) \n
		Sets the RF level of the wanted signal. \n
			:param power: float
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:POWer {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.ts25141.wsignal.get_state() \n
		Enables/disables the generation of the wanted signal. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:STATe \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.set_state(state = False) \n
		Enables/disables the generation of the wanted signal. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:STATe {param}')

	def clone(self) -> 'Wsignal':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Wsignal(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
