from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfRignal:
	"""IfRignal commands group definition. 14 total commands, 3 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifRignal", core, parent)

	@property
	def cw(self):
		"""cw commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_cw'):
			from .Cw import Cw
			self._cw = Cw(self._core, self._cmd_group)
		return self._cw

	@property
	def modulated(self):
		"""modulated commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_modulated'):
			from .Modulated import Modulated
			self._modulated = Modulated(self._core, self._cmd_group)
		return self._modulated

	@property
	def setting(self):
		"""setting commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	# noinspection PyTypeChecker
	def get_bandwidth(self) -> enums.FilterWidth:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:BWIDth \n
		Snippet: value: enums.FilterWidth = driver.source.bb.w3Gpp.ts25141.ifRignal.get_bandwidth() \n
		Selects the interferer scenario. \n
			:return: bwidth: WIDE| NARRow
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:BWIDth?')
		return Conversions.str_to_scalar_enum(response, enums.FilterWidth)

	def set_bandwidth(self, bwidth: enums.FilterWidth) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:BWIDth \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.set_bandwidth(bwidth = enums.FilterWidth.NARRow) \n
		Selects the interferer scenario. \n
			:param bwidth: WIDE| NARRow
		"""
		param = Conversions.enum_scalar_to_str(bwidth, enums.FilterWidth)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:BWIDth {param}')

	def get_cn_ratio(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:CNRatio \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.ifRignal.get_cn_ratio() \n
		In test case 7.4, sets the power ratio of wanted signal to interfering signal. In test case 6.6, sets the power ratio of
		interfering signal to wanted signal. \n
			:return: cn_ratio: float Range: -145 to 20
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:CNRatio?')
		return Conversions.str_to_float(response)

	def set_cn_ratio(self, cn_ratio: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:CNRatio \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.set_cn_ratio(cn_ratio = 1.0) \n
		In test case 7.4, sets the power ratio of wanted signal to interfering signal. In test case 6.6, sets the power ratio of
		interfering signal to wanted signal. \n
			:param cn_ratio: float Range: -145 to 20
		"""
		param = Conversions.decimal_value_to_str(cn_ratio)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:CNRatio {param}')

	def get_foffset(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:FOFFset \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.ifRignal.get_foffset() \n
		Sets frequency offset of the interfering signal versus the wanted signal RF frequency. ) . \n
			:return: foffset: float Range: -40 MHz to 40 MHz
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, foffset: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:FOFFset \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.set_foffset(foffset = 1.0) \n
		Sets frequency offset of the interfering signal versus the wanted signal RF frequency. ) . \n
			:param foffset: float Range: -40 MHz to 40 MHz
		"""
		param = Conversions.decimal_value_to_str(foffset)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:FOFFset {param}')

	def get_power(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:POWer \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.ifRignal.get_power() \n
		Sets the RF level of the interfering signal. \n
			:return: power: float
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:POWer?')
		return Conversions.str_to_float(response)

	def set_power(self, power: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:POWer \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.set_power(power = 1.0) \n
		Sets the RF level of the interfering signal. \n
			:param power: float
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:POWer {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.ts25141.ifRignal.get_state() \n
		Enable/disables the modulated interfering signal. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:STATe \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.set_state(state = False) \n
		Enable/disables the modulated interfering signal. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:STATe {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.Ts25141SigMod:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:TYPE \n
		Snippet: value: enums.Ts25141SigMod = driver.source.bb.w3Gpp.ts25141.ifRignal.get_type_py() \n
		Selects the type of modulation for the interfering signal. \n
			:return: type_py: WCDMa| CW| GMSK| QPSK
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141SigMod)

	def set_type_py(self, type_py: enums.Ts25141SigMod) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:TYPE \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.set_type_py(type_py = enums.Ts25141SigMod.CW) \n
		Selects the type of modulation for the interfering signal. \n
			:param type_py: WCDMa| CW| GMSK| QPSK
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.Ts25141SigMod)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:TYPE {param}')

	def clone(self) -> 'IfRignal':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IfRignal(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
