from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qzss:
	"""Qzss commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qzss", core, parent)

	def get_active(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:SELection:QZSS:ACTive \n
		Snippet: value: int = driver.source.bb.gnss.sv.selection.qzss.get_active() \n
		Queries the number of active satellites per GNSS system that are currently part of the satellite's constellation. \n
			:return: active_svs: integer Range: 0 to 24
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:SELection:QZSS:ACTive?')
		return Conversions.str_to_int(response)

	def get_available(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:SELection:QZSS:AVAilable \n
		Snippet: value: int = driver.source.bb.gnss.sv.selection.qzss.get_available() \n
		Queries the number of available satellites per GNSS system. \n
			:return: available_svs: integer Range: 0 to 40
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:SELection:QZSS:AVAilable?')
		return Conversions.str_to_int(response)

	def get_max(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:SELection:QZSS:MAX \n
		Snippet: value: int = driver.source.bb.gnss.sv.selection.qzss.get_max() \n
		Sets the minimum and maximum number of satellites per GNSS system that can be included in the satellite constellation. \n
			:return: maximum_svs: integer Range: 0 to 24
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:SELection:QZSS:MAX?')
		return Conversions.str_to_int(response)

	def set_max(self, maximum_svs: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:SELection:QZSS:MAX \n
		Snippet: driver.source.bb.gnss.sv.selection.qzss.set_max(maximum_svs = 1) \n
		Sets the minimum and maximum number of satellites per GNSS system that can be included in the satellite constellation. \n
			:param maximum_svs: integer Range: 0 to 24
		"""
		param = Conversions.decimal_value_to_str(maximum_svs)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:SELection:QZSS:MAX {param}')

	def get_min(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:SELection:QZSS:MIN \n
		Snippet: value: int = driver.source.bb.gnss.sv.selection.qzss.get_min() \n
		Sets the minimum and maximum number of satellites per GNSS system that can be included in the satellite constellation. \n
			:return: minimum_svs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SV:SELection:QZSS:MIN?')
		return Conversions.str_to_int(response)

	def set_min(self, minimum_svs: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SV:SELection:QZSS:MIN \n
		Snippet: driver.source.bb.gnss.sv.selection.qzss.set_min(minimum_svs = 1) \n
		Sets the minimum and maximum number of satellites per GNSS system that can be included in the satellite constellation. \n
			:param minimum_svs: integer Range: 0 to 24
		"""
		param = Conversions.decimal_value_to_str(minimum_svs)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SV:SELection:QZSS:MIN {param}')
