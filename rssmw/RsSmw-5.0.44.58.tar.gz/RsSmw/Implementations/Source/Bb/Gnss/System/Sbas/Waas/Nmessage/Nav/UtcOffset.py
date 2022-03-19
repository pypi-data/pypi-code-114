from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UtcOffset:
	"""UtcOffset commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("utcOffset", core, parent)

	def get_period(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:WAAS:NMESsage:NAV:UTCoffset:PERiod \n
		Snippet: value: int = driver.source.bb.gnss.system.sbas.waas.nmessage.nav.utcOffset.get_period() \n
		Sets the periodicity of the SBAS message. \n
			:return: utc_offset_period: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:WAAS:NMESsage:NAV:UTCoffset:PERiod?')
		return Conversions.str_to_int(response)

	def set_period(self, utc_offset_period: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:WAAS:NMESsage:NAV:UTCoffset:PERiod \n
		Snippet: driver.source.bb.gnss.system.sbas.waas.nmessage.nav.utcOffset.set_period(utc_offset_period = 1) \n
		Sets the periodicity of the SBAS message. \n
			:param utc_offset_period: integer Range: 0 to 999
		"""
		param = Conversions.decimal_value_to_str(utc_offset_period)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:WAAS:NMESsage:NAV:UTCoffset:PERiod {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:WAAS:NMESsage:NAV:UTCoffset:STATe \n
		Snippet: value: bool = driver.source.bb.gnss.system.sbas.waas.nmessage.nav.utcOffset.get_state() \n
		Enables generation of the particular SBAS correction data. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:WAAS:NMESsage:NAV:UTCoffset:STATe?')
		return Conversions.str_to_bool(response)
