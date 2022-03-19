from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulated:
	"""Modulated commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulated", core, parent)

	def get_foffset(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:MODulated:FOFFset \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.ifRignal.modulated.get_foffset() \n
		Sets frequency offset of the modulated interfering signal versus the wanted signal RF frequency. \n
			:return: foffset: float Range: -40 MHz to 40 MHz
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:MODulated:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, foffset: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:MODulated:FOFFset \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.modulated.set_foffset(foffset = 1.0) \n
		Sets frequency offset of the modulated interfering signal versus the wanted signal RF frequency. \n
			:param foffset: float Range: -40 MHz to 40 MHz
		"""
		param = Conversions.decimal_value_to_str(foffset)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:MODulated:FOFFset {param}')

	def get_power(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:MODulated:POWer \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.ifRignal.modulated.get_power() \n
		Sets the RF level of the modulated interfering signal. \n
			:return: power: float Range: -145 to 20
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:MODulated:POWer?')
		return Conversions.str_to_float(response)

	def set_power(self, power: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:MODulated:POWer \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.modulated.set_power(power = 1.0) \n
		Sets the RF level of the modulated interfering signal. \n
			:param power: float Range: -145 to 20
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:MODulated:POWer {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:MODulated:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.ts25141.ifRignal.modulated.get_state() \n
		Enable/disables the modulated interfering signal. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:MODulated:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:MODulated:STATe \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.modulated.set_state(state = False) \n
		Enable/disables the modulated interfering signal. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:MODulated:STATe {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.Ts25141SigMod:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:MODulated:TYPE \n
		Snippet: value: enums.Ts25141SigMod = driver.source.bb.w3Gpp.ts25141.ifRignal.modulated.get_type_py() \n
		Selects the type of modulation for the interfering uplink signal in the second path. \n
			:return: type_py: WCDMa| CW| GMSK| QPSK
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:MODulated:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141SigMod)

	def set_type_py(self, type_py: enums.Ts25141SigMod) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:MODulated:TYPE \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.modulated.set_type_py(type_py = enums.Ts25141SigMod.CW) \n
		Selects the type of modulation for the interfering uplink signal in the second path. \n
			:param type_py: WCDMa| CW| GMSK| QPSK
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.Ts25141SigMod)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:MODulated:TYPE {param}')
