from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Atwo:
	"""Atwo commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("atwo", core, parent)

	def get_unscaled(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:UTC:ATWO:UNSCaled \n
		Snippet: value: float = driver.source.bb.gnss.sv.gps.nmessage.cnav.time.conversion.utc.atwo.get_unscaled() \n
		Sets the A2 parameter. \n
			:return: a_2: integer Range: -64 to 63
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:UTC:ATWO:UNSCaled?')
		return Conversions.str_to_float(response)

	def set_unscaled(self, a_2: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:UTC:ATWO:UNSCaled \n
		Snippet: driver.source.bb.gnss.sv.gps.nmessage.cnav.time.conversion.utc.atwo.set_unscaled(a_2 = 1.0) \n
		Sets the A2 parameter. \n
			:param a_2: integer Range: -64 to 63
		"""
		param = Conversions.decimal_value_to_str(a_2)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:UTC:ATWO:UNSCaled {param}')

	def get_value(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:UTC:ATWO \n
		Snippet: value: int = driver.source.bb.gnss.sv.gps.nmessage.cnav.time.conversion.utc.atwo.get_value() \n
		Sets the A2 parameter. \n
			:return: a_2: integer Range: -64 to 63
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:UTC:ATWO?')
		return Conversions.str_to_int(response)

	def set_value(self, a_2: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:UTC:ATWO \n
		Snippet: driver.source.bb.gnss.sv.gps.nmessage.cnav.time.conversion.utc.atwo.set_value(a_2 = 1) \n
		Sets the A2 parameter. \n
			:param a_2: integer Range: -64 to 63
		"""
		param = Conversions.decimal_value_to_str(a_2)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:GPS:NMESsage:CNAV:TIME:CONVersion:UTC:ATWO {param}')
