from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def get_icomponent(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:OFFSet:I \n
		Snippet: value: float = driver.source.iq.output.analog.offset.get_icomponent() \n
		Sets an offset Voffset between the inverting and non-inverting input of the differential analog I/Q output signal.
		The value range is adjusted so that the maximum overall output voltage does not exceed 4V, see 'Maximum overall output
		voltage'. \n
			:return: ipart: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:OFFSet:I?')
		return Conversions.str_to_float(response)

	def set_icomponent(self, ipart: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:OFFSet:I \n
		Snippet: driver.source.iq.output.analog.offset.set_icomponent(ipart = 1.0) \n
		Sets an offset Voffset between the inverting and non-inverting input of the differential analog I/Q output signal.
		The value range is adjusted so that the maximum overall output voltage does not exceed 4V, see 'Maximum overall output
		voltage'. \n
			:param ipart: float Range: (-4+Vp/2+Vbias/2) ,V to (4-Vp/2-Vbias/2) ,V (R&S SMW-B10) / (-2+Vp) ,V to (2-Vp) ,V (R&S SMW-B9) , Unit: V
		"""
		param = Conversions.decimal_value_to_str(ipart)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:OFFSet:I {param}')

	def get_qcomponent(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:OFFSet:Q \n
		Snippet: value: float = driver.source.iq.output.analog.offset.get_qcomponent() \n
		Sets an offset Voffset between the inverting and non-inverting input of the differential analog I/Q output signal.
		The value range is adjusted so that the maximum overall output voltage does not exceed 4V, see 'Maximum overall output
		voltage'. \n
			:return: qpart: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:OFFSet:Q?')
		return Conversions.str_to_float(response)

	def set_qcomponent(self, qpart: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:OFFSet:Q \n
		Snippet: driver.source.iq.output.analog.offset.set_qcomponent(qpart = 1.0) \n
		Sets an offset Voffset between the inverting and non-inverting input of the differential analog I/Q output signal.
		The value range is adjusted so that the maximum overall output voltage does not exceed 4V, see 'Maximum overall output
		voltage'. \n
			:param qpart: float Range: (-4+Vp/2+Vbias/2) ,V to (4-Vp/2-Vbias/2) ,V (R&S SMW-B10) / (-2+Vp) ,V to (2-Vp) ,V (R&S SMW-B9) , Unit: V
		"""
		param = Conversions.decimal_value_to_str(qpart)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:OFFSet:Q {param}')
