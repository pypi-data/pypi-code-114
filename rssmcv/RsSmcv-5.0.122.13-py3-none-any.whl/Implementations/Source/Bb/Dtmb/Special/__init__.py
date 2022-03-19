from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Special:
	"""Special commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("special", core, parent)

	@property
	def settings(self):
		"""settings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import Settings
			self._settings = Settings(self._core, self._cmd_group)
		return self._settings

	def get_sip_normal(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DTMB:[SPECial]:SIPNormal \n
		Snippet: value: bool = driver.source.bb.dtmb.special.get_sip_normal() \n
		Enables or disables the system information (SI) power normalization. \n
			:return: dtmb_sip_normal: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:SPECial:SIPNormal?')
		return Conversions.str_to_bool(response)

	def set_sip_normal(self, dtmb_sip_normal: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:[SPECial]:SIPNormal \n
		Snippet: driver.source.bb.dtmb.special.set_sip_normal(dtmb_sip_normal = False) \n
		Enables or disables the system information (SI) power normalization. \n
			:param dtmb_sip_normal: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(dtmb_sip_normal)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:SPECial:SIPNormal {param}')

	def clone(self) -> 'Special':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Special(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
