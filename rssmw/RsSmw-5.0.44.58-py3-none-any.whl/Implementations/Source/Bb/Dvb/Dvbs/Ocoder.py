from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ocoder:
	"""Ocoder commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ocoder", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:OCODer:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.ocoder.get_state() \n
		Enables the BCH outer coder. \n
			:return: ocoder: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:OCODer:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, ocoder: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:OCODer:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbs.ocoder.set_state(ocoder = False) \n
		Enables the BCH outer coder. \n
			:param ocoder: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(ocoder)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:OCODer:STATe {param}')
