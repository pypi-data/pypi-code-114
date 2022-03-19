from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cw:
	"""Cw commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cw", core, parent)

	def get_foffset(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:CW:FOFFset \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.ifRignal.cw.get_foffset() \n
		Sets frequency offset of the CW interfering signal versus the wanted signal RF frequency. \n
			:return: foffset: float
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:CW:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, foffset: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:CW:FOFFset \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.cw.set_foffset(foffset = 1.0) \n
		Sets frequency offset of the CW interfering signal versus the wanted signal RF frequency. \n
			:param foffset: float
		"""
		param = Conversions.decimal_value_to_str(foffset)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:CW:FOFFset {param}')

	def get_power(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:CW:POWer \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.ifRignal.cw.get_power() \n
		Sets the RF level of the CW interfering signal. \n
			:return: power: float
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:CW:POWer?')
		return Conversions.str_to_float(response)

	def set_power(self, power: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:CW:POWer \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.cw.set_power(power = 1.0) \n
		Sets the RF level of the CW interfering signal. \n
			:param power: float
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:CW:POWer {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:CW:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.ts25141.ifRignal.cw.get_state() \n
		This command enable/disables the CW interfering signal. In mode 'According to Standard' (SOURce:BB:W3GPp:TS25141:EMODe
		STANdard) , the value is fixed to ON. Sets commands SOURce2:AWGN:CNRatio and SOURce2:AWGN:POWer:NOISe after execution of
		SOURce:BB:W3GP:TS25141:TCAS:EXEC \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:CW:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:CW:STATe \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.cw.set_state(state = False) \n
		This command enable/disables the CW interfering signal. In mode 'According to Standard' (SOURce:BB:W3GPp:TS25141:EMODe
		STANdard) , the value is fixed to ON. Sets commands SOURce2:AWGN:CNRatio and SOURce2:AWGN:POWer:NOISe after execution of
		SOURce:BB:W3GP:TS25141:TCAS:EXEC \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:CW:STATe {param}')
