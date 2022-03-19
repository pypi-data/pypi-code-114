from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dvbr:
	"""Dvbr commands group definition. 50 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dvbr", core, parent)

	@property
	def sfConfig(self):
		"""sfConfig commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_sfConfig'):
			from .SfConfig import SfConfig
			self._sfConfig = SfConfig(self._core, self._cmd_group)
		return self._sfConfig

	def get_sf_index(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFINdex \n
		Snippet: value: int = driver.source.bb.dvb.dvbr.get_sf_index() \n
		No command help available \n
			:return: sf_index: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBR:SFINdex?')
		return Conversions.str_to_int(response)

	def set_sf_index(self, sf_index: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFINdex \n
		Snippet: driver.source.bb.dvb.dvbr.set_sf_index(sf_index = 1) \n
		No command help available \n
			:param sf_index: No help available
		"""
		param = Conversions.decimal_value_to_str(sf_index)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBR:SFINdex {param}')

	def get_sframes(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFRames \n
		Snippet: value: int = driver.source.bb.dvb.dvbr.get_sframes() \n
		No command help available \n
			:return: sframes: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBR:SFRames?')
		return Conversions.str_to_int(response)

	def set_sframes(self, sframes: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFRames \n
		Snippet: driver.source.bb.dvb.dvbr.set_sframes(sframes = 1) \n
		No command help available \n
			:param sframes: No help available
		"""
		param = Conversions.decimal_value_to_str(sframes)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBR:SFRames {param}')

	def clone(self) -> 'Dvbr':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dvbr(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
