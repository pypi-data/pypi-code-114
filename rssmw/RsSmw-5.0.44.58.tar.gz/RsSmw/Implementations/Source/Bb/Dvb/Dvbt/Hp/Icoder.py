from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Icoder:
	"""Icoder commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("icoder", core, parent)

	# noinspection PyTypeChecker
	def get_rate(self) -> enums.DvbCoderate:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBT:[HP]:ICODer:RATE \n
		Snippet: value: enums.DvbCoderate = driver.source.bb.dvb.dvbt.hp.icoder.get_rate() \n
		Selects the code rate of the inner coder. \n
			:return: rate: CR1D2| CR2D3| CR3D4| CR5D6| CR7D8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBT:HP:ICODer:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.DvbCoderate)

	def set_rate(self, rate: enums.DvbCoderate) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBT:[HP]:ICODer:RATE \n
		Snippet: driver.source.bb.dvb.dvbt.hp.icoder.set_rate(rate = enums.DvbCoderate.CR1D2) \n
		Selects the code rate of the inner coder. \n
			:param rate: CR1D2| CR2D3| CR3D4| CR5D6| CR7D8
		"""
		param = Conversions.enum_scalar_to_str(rate, enums.DvbCoderate)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBT:HP:ICODer:RATE {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBT:[HP]:ICODer:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbt.hp.icoder.get_state() \n
		Activates/deactivates the inner coder. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBT:HP:ICODer:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBT:[HP]:ICODer:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbt.hp.icoder.set_state(state = False) \n
		Activates/deactivates the inner coder. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBT:HP:ICODer:STATe {param}')
