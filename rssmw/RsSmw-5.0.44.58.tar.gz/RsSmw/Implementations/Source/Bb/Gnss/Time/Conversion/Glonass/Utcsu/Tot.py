from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tot:
	"""Tot commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tot", core, parent)

	def get_unscaled(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:TOT:UNSCaled \n
		Snippet: value: int = driver.source.bb.gnss.time.conversion.glonass.utcsu.tot.get_unscaled() \n
		Sets the UTC data reference time of week, tot. \n
			:return: tot: integer Range: 0 to 255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:TOT:UNSCaled?')
		return Conversions.str_to_int(response)

	def set_unscaled(self, tot: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:TOT:UNSCaled \n
		Snippet: driver.source.bb.gnss.time.conversion.glonass.utcsu.tot.set_unscaled(tot = 1) \n
		Sets the UTC data reference time of week, tot. \n
			:param tot: integer Range: 0 to 255
		"""
		param = Conversions.decimal_value_to_str(tot)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:TOT:UNSCaled {param}')

	def get_value(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:TOT \n
		Snippet: value: int = driver.source.bb.gnss.time.conversion.glonass.utcsu.tot.get_value() \n
		Sets the UTC data reference time of week, tot. \n
			:return: tot: integer Range: 0 to 255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:TOT?')
		return Conversions.str_to_int(response)

	def set_value(self, tot: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:TOT \n
		Snippet: driver.source.bb.gnss.time.conversion.glonass.utcsu.tot.set_value(tot = 1) \n
		Sets the UTC data reference time of week, tot. \n
			:param tot: integer Range: 0 to 255
		"""
		param = Conversions.decimal_value_to_str(tot)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:TOT {param}')
