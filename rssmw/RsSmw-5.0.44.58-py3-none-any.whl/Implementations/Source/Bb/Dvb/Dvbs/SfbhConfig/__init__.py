from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SfbhConfig:
	"""SfbhConfig commands group definition. 10 total commands, 2 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfbhConfig", core, parent)

	@property
	def dt(self):
		"""dt commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dt'):
			from .Dt import Dt
			self._dt = Dt(self._core, self._cmd_group)
		return self._dt

	@property
	def fodt(self):
		"""fodt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fodt'):
			from .Fodt import Fodt
			self._fodt = Fodt(self._core, self._cmd_group)
		return self._fodt

	def get_ao_dwell(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:AODWell \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.sfbhConfig.get_ao_dwell() \n
		No command help available \n
			:return: attenuate_oth_dw: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:AODWell?')
		return Conversions.str_to_bool(response)

	def set_ao_dwell(self, attenuate_oth_dw: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:AODWell \n
		Snippet: driver.source.bb.dvb.dvbs.sfbhConfig.set_ao_dwell(attenuate_oth_dw = False) \n
		No command help available \n
			:param attenuate_oth_dw: No help available
		"""
		param = Conversions.bool_to_str(attenuate_oth_dw)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:AODWell {param}')

	def get_bh_cycle(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:BHCycle \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfbhConfig.get_bh_cycle() \n
		No command help available \n
			:return: bh_cycle: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:BHCycle?')
		return Conversions.str_to_int(response)

	def get_bs_time(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:BSTime \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfbhConfig.get_bs_time() \n
		No command help available \n
			:return: beam_switch_time: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:BSTime?')
		return Conversions.str_to_int(response)

	def set_bs_time(self, beam_switch_time: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:BSTime \n
		Snippet: driver.source.bb.dvb.dvbs.sfbhConfig.set_bs_time(beam_switch_time = 1) \n
		No command help available \n
			:param beam_switch_time: No help available
		"""
		param = Conversions.decimal_value_to_str(beam_switch_time)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:BSTime {param}')

	def get_lsf_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:LSFLength \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfbhConfig.get_lsf_length() \n
		No command help available \n
			:return: last_sf_length: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:LSFLength?')
		return Conversions.str_to_int(response)

	def get_no_dwells(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:NODWells \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfbhConfig.get_no_dwells() \n
		No command help available \n
			:return: number_of_dwells: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:NODWells?')
		return Conversions.str_to_int(response)

	def set_no_dwells(self, number_of_dwells: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:NODWells \n
		Snippet: driver.source.bb.dvb.dvbs.sfbhConfig.set_no_dwells(number_of_dwells = 1) \n
		No command help available \n
			:param number_of_dwells: No help available
		"""
		param = Conversions.decimal_value_to_str(number_of_dwells)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:NODWells {param}')

	def get_nosf(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:NOSF \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfbhConfig.get_nosf() \n
		No command help available \n
			:return: number_of_sf: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:NOSF?')
		return Conversions.str_to_int(response)

	def set_nosf(self, number_of_sf: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:NOSF \n
		Snippet: driver.source.bb.dvb.dvbs.sfbhConfig.set_nosf(number_of_sf = 1) \n
		No command help available \n
			:param number_of_sf: No help available
		"""
		param = Conversions.decimal_value_to_str(number_of_sf)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:NOSF {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:STATe \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.sfbhConfig.get_state() \n
		No command help available \n
			:return: beam_hopping_stat: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, beam_hopping_stat: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:STATe \n
		Snippet: driver.source.bb.dvb.dvbs.sfbhConfig.set_state(beam_hopping_stat = False) \n
		No command help available \n
			:param beam_hopping_stat: No help available
		"""
		param = Conversions.bool_to_str(beam_hopping_stat)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:STATe {param}')

	def get_zbs_signal(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:ZBSSignal \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.sfbhConfig.get_zbs_signal() \n
		No command help available \n
			:return: zero_beam_switch: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:ZBSSignal?')
		return Conversions.str_to_bool(response)

	def set_zbs_signal(self, zero_beam_switch: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:ZBSSignal \n
		Snippet: driver.source.bb.dvb.dvbs.sfbhConfig.set_zbs_signal(zero_beam_switch = False) \n
		No command help available \n
			:param zero_beam_switch: No help available
		"""
		param = Conversions.bool_to_str(zero_beam_switch)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:ZBSSignal {param}')

	def clone(self) -> 'SfbhConfig':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SfbhConfig(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
