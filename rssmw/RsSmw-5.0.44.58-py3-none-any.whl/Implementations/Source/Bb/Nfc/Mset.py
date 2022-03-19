from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mset:
	"""Mset commands group definition. 13 total commands, 0 Subgroups, 13 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mset", core, parent)

	def get_boutput(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:BOUTput \n
		Snippet: value: bool = driver.source.bb.nfc.mset.get_boutput() \n
		When activated the signal at the baseband output changes between 0% and 100% voltage to be able to control the Reference
		Listeners. \n
			:return: boutput: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:MSET:BOUTput?')
		return Conversions.str_to_bool(response)

	def set_boutput(self, boutput: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:BOUTput \n
		Snippet: driver.source.bb.nfc.mset.set_boutput(boutput = False) \n
		When activated the signal at the baseband output changes between 0% and 100% voltage to be able to control the Reference
		Listeners. \n
			:param boutput: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(boutput)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:MSET:BOUTput {param}')

	def get_brate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:BRATe \n
		Snippet: value: float = driver.source.bb.nfc.mset.get_brate() \n
		Returns the resulting bitrate for the current settings. \n
			:return: brate: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:MSET:BRATe?')
		return Conversions.str_to_float(response)

	def get_imodulation(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:IMODulation \n
		Snippet: value: bool = driver.source.bb.nfc.mset.get_imodulation() \n
		When selected, inverse modulation will be used. \n
			:return: imodulation: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:MSET:IMODulation?')
		return Conversions.str_to_bool(response)

	def set_imodulation(self, imodulation: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:IMODulation \n
		Snippet: driver.source.bb.nfc.mset.set_imodulation(imodulation = False) \n
		When selected, inverse modulation will be used. \n
			:param imodulation: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(imodulation)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:MSET:IMODulation {param}')

	def get_mdepth(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:MDEPth \n
		Snippet: value: float = driver.source.bb.nfc.mset.get_mdepth() \n
		Sets the modulation depth in %. \n
			:return: mdepth: float Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:MSET:MDEPth?')
		return Conversions.str_to_float(response)

	def set_mdepth(self, mdepth: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:MDEPth \n
		Snippet: driver.source.bb.nfc.mset.set_mdepth(mdepth = 1.0) \n
		Sets the modulation depth in %. \n
			:param mdepth: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(mdepth)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:MSET:MDEPth {param}')

	def get_mindex(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:MINDex \n
		Snippet: value: float = driver.source.bb.nfc.mset.get_mindex() \n
		Defines the signal's modulation index in %. \n
			:return: mindex: float Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:MSET:MINDex?')
		return Conversions.str_to_float(response)

	def set_mindex(self, mindex: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:MINDex \n
		Snippet: driver.source.bb.nfc.mset.set_mindex(mindex = 1.0) \n
		Defines the signal's modulation index in %. \n
			:param mindex: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(mindex)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:MSET:MINDex {param}')

	def get_osrise(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:OSRise \n
		Snippet: value: float = driver.source.bb.nfc.mset.get_osrise() \n
		Determines the size of the overshoot after the rising slope. \n
			:return: orise: float Range: 0 to 42
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:MSET:OSRise?')
		return Conversions.str_to_float(response)

	def set_osrise(self, orise: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:OSRise \n
		Snippet: driver.source.bb.nfc.mset.set_osrise(orise = 1.0) \n
		Determines the size of the overshoot after the rising slope. \n
			:param orise: float Range: 0 to 42
		"""
		param = Conversions.decimal_value_to_str(orise)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:MSET:OSRise {param}')

	def get_rcurve(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:RCURve \n
		Snippet: value: bool = driver.source.bb.nfc.mset.get_rcurve() \n
		When activated an 'RLC curve' is applied to the signal, otherwise a linear ramp is used. \n
			:return: rcurve: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:MSET:RCURve?')
		return Conversions.str_to_bool(response)

	def set_rcurve(self, rcurve: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:RCURve \n
		Snippet: driver.source.bb.nfc.mset.set_rcurve(rcurve = False) \n
		When activated an 'RLC curve' is applied to the signal, otherwise a linear ramp is used. \n
			:param rcurve: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(rcurve)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:MSET:RCURve {param}')

	def get_slope(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:SLOPe \n
		Snippet: value: bool = driver.source.bb.nfc.mset.get_slope() \n
		Determines the transition between the modulated and unmodulated parts (Edge/Slope) . \n
			:return: eslope: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:MSET:SLOPe?')
		return Conversions.str_to_bool(response)

	def set_slope(self, eslope: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:SLOPe \n
		Snippet: driver.source.bb.nfc.mset.set_slope(eslope = False) \n
		Determines the transition between the modulated and unmodulated parts (Edge/Slope) . \n
			:param eslope: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(eslope)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:MSET:SLOPe {param}')

	def get_symbol_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:SRATe \n
		Snippet: value: float = driver.source.bb.nfc.mset.get_symbol_rate() \n
		Enters the sample rate, i.e. the time resolution of the generated signal. \n
			:return: srate: float Range: depends on protocol mode to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:MSET:SRATe?')
		return Conversions.str_to_float(response)

	def set_symbol_rate(self, srate: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:SRATe \n
		Snippet: driver.source.bb.nfc.mset.set_symbol_rate(srate = 1.0) \n
		Enters the sample rate, i.e. the time resolution of the generated signal. \n
			:param srate: float Range: depends on protocol mode to dynamic
		"""
		param = Conversions.decimal_value_to_str(srate)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:MSET:SRATe {param}')

	def get_tfall(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:TFALl \n
		Snippet: value: float = driver.source.bb.nfc.mset.get_tfall() \n
		Defines the fall time (90 to 5 %) in μs. \n
			:return: tfall: float Range: 0 to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:MSET:TFALl?')
		return Conversions.str_to_float(response)

	def set_tfall(self, tfall: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:TFALl \n
		Snippet: driver.source.bb.nfc.mset.set_tfall(tfall = 1.0) \n
		Defines the fall time (90 to 5 %) in μs. \n
			:param tfall: float Range: 0 to dynamic
		"""
		param = Conversions.decimal_value_to_str(tfall)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:MSET:TFALl {param}')

	def get_tlow(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:TLOW \n
		Snippet: value: float = driver.source.bb.nfc.mset.get_tlow() \n
		Defines the signals low time (below 5%) in µs. \n
			:return: tlow: float Range: 0.4 to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:MSET:TLOW?')
		return Conversions.str_to_float(response)

	def set_tlow(self, tlow: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:TLOW \n
		Snippet: driver.source.bb.nfc.mset.set_tlow(tlow = 1.0) \n
		Defines the signals low time (below 5%) in µs. \n
			:param tlow: float Range: 0.4 to dynamic
		"""
		param = Conversions.decimal_value_to_str(tlow)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:MSET:TLOW {param}')

	def get_trise(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:TRISe \n
		Snippet: value: float = driver.source.bb.nfc.mset.get_trise() \n
		Defines the signals rise time (5 to 90 %) in μs. \n
			:return: trise: float Range: dynamic to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:MSET:TRISe?')
		return Conversions.str_to_float(response)

	def set_trise(self, trise: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:TRISe \n
		Snippet: driver.source.bb.nfc.mset.set_trise(trise = 1.0) \n
		Defines the signals rise time (5 to 90 %) in μs. \n
			:param trise: float Range: dynamic to dynamic
		"""
		param = Conversions.decimal_value_to_str(trise)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:MSET:TRISe {param}')

	def get_usfall(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:USFall \n
		Snippet: value: float = driver.source.bb.nfc.mset.get_usfall() \n
		Determines the size of the undershoot (ringing) after the falling slope. \n
			:return: ofall: float Range: 0 to 42
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:MSET:USFall?')
		return Conversions.str_to_float(response)

	def set_usfall(self, ofall: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:MSET:USFall \n
		Snippet: driver.source.bb.nfc.mset.set_usfall(ofall = 1.0) \n
		Determines the size of the undershoot (ringing) after the falling slope. \n
			:param ofall: float Range: 0 to 42
		"""
		param = Conversions.decimal_value_to_str(ofall)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:MSET:USFall {param}')
