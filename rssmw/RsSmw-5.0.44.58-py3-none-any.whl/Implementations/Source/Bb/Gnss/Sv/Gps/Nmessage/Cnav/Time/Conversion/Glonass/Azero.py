from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Azero:
	"""Azero commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("azero", core, parent)

	def get_unscaled(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:GLONass:AZERo:UNSCaled \n
		Snippet: value: float = driver.source.bb.gnss.sv.gps.nmessage.cnav.time.conversion.glonass.azero.get_unscaled() \n
		No command help available \n
			:return: a_0: integer Range: -32768 to 32767
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:GLONass:AZERo:UNSCaled?')
		return Conversions.str_to_float(response)

	def set_unscaled(self, a_0: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:GLONass:AZERo:UNSCaled \n
		Snippet: driver.source.bb.gnss.sv.gps.nmessage.cnav.time.conversion.glonass.azero.set_unscaled(a_0 = 1.0) \n
		No command help available \n
			:param a_0: integer Range: -32768 to 32767
		"""
		param = Conversions.decimal_value_to_str(a_0)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:GLONass:AZERo:UNSCaled {param}')

	def get_value(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:GLONass:AZERo \n
		Snippet: value: int = driver.source.bb.gnss.sv.gps.nmessage.cnav.time.conversion.glonass.azero.get_value() \n
		No command help available \n
			:return: a_0: integer Range: -32768 to 32767
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:GLONass:AZERo?')
		return Conversions.str_to_int(response)

	def set_value(self, a_0: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:GLONass:AZERo \n
		Snippet: driver.source.bb.gnss.sv.gps.nmessage.cnav.time.conversion.glonass.azero.set_value(a_0 = 1) \n
		No command help available \n
			:param a_0: integer Range: -32768 to 32767
		"""
		param = Conversions.decimal_value_to_str(a_0)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:GLONass:AZERo {param}')
