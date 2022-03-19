from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aone:
	"""Aone commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aone", core, parent)

	def get_unscaled(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:GALileo:NMESsage:INAV:TIME:CONVersion:GPS:AONE:UNSCaled \n
		Snippet: value: float = driver.source.bb.gnss.sv.galileo.nmessage.inav.time.conversion.gps.aone.get_unscaled() \n
		Sets the A1 parameter. \n
			:return: a_1: integer Range: -4096 to 4095
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:GALileo:NMESsage:INAV:TIME:CONVersion:GPS:AONE:UNSCaled?')
		return Conversions.str_to_float(response)

	def set_unscaled(self, a_1: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:GALileo:NMESsage:INAV:TIME:CONVersion:GPS:AONE:UNSCaled \n
		Snippet: driver.source.bb.gnss.sv.galileo.nmessage.inav.time.conversion.gps.aone.set_unscaled(a_1 = 1.0) \n
		Sets the A1 parameter. \n
			:param a_1: integer Range: -4096 to 4095
		"""
		param = Conversions.decimal_value_to_str(a_1)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:GALileo:NMESsage:INAV:TIME:CONVersion:GPS:AONE:UNSCaled {param}')

	def get_value(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:GALileo:NMESsage:INAV:TIME:CONVersion:GPS:AONE \n
		Snippet: value: int = driver.source.bb.gnss.sv.galileo.nmessage.inav.time.conversion.gps.aone.get_value() \n
		Sets the A1 parameter. \n
			:return: a_1: integer Range: -4096 to 4095
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:GALileo:NMESsage:INAV:TIME:CONVersion:GPS:AONE?')
		return Conversions.str_to_int(response)

	def set_value(self, a_1: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:GALileo:NMESsage:INAV:TIME:CONVersion:GPS:AONE \n
		Snippet: driver.source.bb.gnss.sv.galileo.nmessage.inav.time.conversion.gps.aone.set_value(a_1 = 1) \n
		Sets the A1 parameter. \n
			:param a_1: integer Range: -4096 to 4095
		"""
		param = Conversions.decimal_value_to_str(a_1)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:GALileo:NMESsage:INAV:TIME:CONVersion:GPS:AONE {param}')
