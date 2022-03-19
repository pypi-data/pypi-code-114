from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Icoder:
	"""Icoder commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("icoder", core, parent)

	# noinspection PyTypeChecker
	def get_rate(self) -> enums.DvbS2XcodRate:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:ICODer:RATE \n
		Snippet: value: enums.DvbS2XcodRate = driver.source.bb.dvb.dvbx.icoder.get_rate() \n
		Selects the code rate of the inner coder. \n
			:return: rate: CR1D4| CR1D3| CR2D5| CR1D2| CR3D5| CR2D3| CR3D4| CR4D5| CR5D6| CR8D9| CR9D10| CR2D9| CR13D45| CR9D20| CR90D180| CR96D180| CR11D20| CR100D180| CR104D180| CR26D45| CR18D30| CR28D45| CR23D36| CR116D180| CR20D30| CR124D180| CR25D36| CR128D180| CR13D18| CR132D180| CR22D30| CR135D180| CR140D180| CR7D9| CR154D180| CR1D5| CR11D45| CR4D15| CR14D45| CR7D15| CR8D15| CR32D45
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:ICODer:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.DvbS2XcodRate)

	def set_rate(self, rate: enums.DvbS2XcodRate) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:ICODer:RATE \n
		Snippet: driver.source.bb.dvb.dvbx.icoder.set_rate(rate = enums.DvbS2XcodRate.CR100D180) \n
		Selects the code rate of the inner coder. \n
			:param rate: CR1D4| CR1D3| CR2D5| CR1D2| CR3D5| CR2D3| CR3D4| CR4D5| CR5D6| CR8D9| CR9D10| CR2D9| CR13D45| CR9D20| CR90D180| CR96D180| CR11D20| CR100D180| CR104D180| CR26D45| CR18D30| CR28D45| CR23D36| CR116D180| CR20D30| CR124D180| CR25D36| CR128D180| CR13D18| CR132D180| CR22D30| CR135D180| CR140D180| CR7D9| CR154D180| CR1D5| CR11D45| CR4D15| CR14D45| CR7D15| CR8D15| CR32D45
		"""
		param = Conversions.enum_scalar_to_str(rate, enums.DvbS2XcodRate)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:ICODer:RATE {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:ICODer:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbx.icoder.get_state() \n
		Activates the inner coder. \n
			:return: icoder: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:ICODer:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, icoder: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:ICODer:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbx.icoder.set_state(icoder = False) \n
		Activates the inner coder. \n
			:param icoder: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(icoder)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:ICODer:STATe {param}')
