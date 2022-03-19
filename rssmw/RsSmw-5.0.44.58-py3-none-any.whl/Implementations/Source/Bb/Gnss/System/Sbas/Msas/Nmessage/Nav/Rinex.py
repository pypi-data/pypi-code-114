from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rinex:
	"""Rinex commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rinex", core, parent)

	def get_period(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:MSAS:NMESsage:NAV:RINex:PERiod \n
		Snippet: value: int = driver.source.bb.gnss.system.sbas.msas.nmessage.nav.rinex.get_period() \n
		Sets the periodicity of the SBAS message. \n
			:return: interval: integer Range: 0 to 999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:MSAS:NMESsage:NAV:RINex:PERiod?')
		return Conversions.str_to_int(response)

	def set_period(self, interval: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:MSAS:NMESsage:NAV:RINex:PERiod \n
		Snippet: driver.source.bb.gnss.system.sbas.msas.nmessage.nav.rinex.set_period(interval = 1) \n
		Sets the periodicity of the SBAS message. \n
			:param interval: integer Range: 0 to 999
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:MSAS:NMESsage:NAV:RINex:PERiod {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:MSAS:NMESsage:NAV:RINex:STATe \n
		Snippet: value: bool = driver.source.bb.gnss.system.sbas.msas.nmessage.nav.rinex.get_state() \n
		Enables generation of the particular SBAS correction data. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:MSAS:NMESsage:NAV:RINex:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:MSAS:NMESsage:NAV:RINex:STATe \n
		Snippet: driver.source.bb.gnss.system.sbas.msas.nmessage.nav.rinex.set_state(state = False) \n
		Enables generation of the particular SBAS correction data. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:MSAS:NMESsage:NAV:RINex:STATe {param}')
