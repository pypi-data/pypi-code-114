from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dfactor:
	"""Dfactor commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dfactor", core, parent)

	def get_period(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:GAGAN:NMESsage:NAV:DFACtor:PERiod \n
		Snippet: value: int = driver.source.bb.gnss.system.sbas.gagan.nmessage.nav.dfactor.get_period() \n
		Sets the periodicity of the SBAS message. \n
			:return: interval: integer Range: 0 to 999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:GAGAN:NMESsage:NAV:DFACtor:PERiod?')
		return Conversions.str_to_int(response)

	def set_period(self, interval: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:GAGAN:NMESsage:NAV:DFACtor:PERiod \n
		Snippet: driver.source.bb.gnss.system.sbas.gagan.nmessage.nav.dfactor.set_period(interval = 1) \n
		Sets the periodicity of the SBAS message. \n
			:param interval: integer Range: 0 to 999
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:GAGAN:NMESsage:NAV:DFACtor:PERiod {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:GAGAN:NMESsage:NAV:DFACtor:STATe \n
		Snippet: value: bool = driver.source.bb.gnss.system.sbas.gagan.nmessage.nav.dfactor.get_state() \n
		Enables generation of the particular SBAS correction data. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:GAGAN:NMESsage:NAV:DFACtor:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:GAGAN:NMESsage:NAV:DFACtor:STATe \n
		Snippet: driver.source.bb.gnss.system.sbas.gagan.nmessage.nav.dfactor.set_state(state = False) \n
		Enables generation of the particular SBAS correction data. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:GAGAN:NMESsage:NAV:DFACtor:STATe {param}')
