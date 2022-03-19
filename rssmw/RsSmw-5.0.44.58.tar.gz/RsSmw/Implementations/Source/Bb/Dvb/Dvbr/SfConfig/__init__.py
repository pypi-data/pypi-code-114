from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SfConfig:
	"""SfConfig commands group definition. 48 total commands, 3 Subgroups, 2 group commands
	Repeated Capability: SfCfgIxNull, default value after init: SfCfgIxNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfConfig", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_sfCfgIxNull_get', 'repcap_sfCfgIxNull_set', repcap.SfCfgIxNull.Nr0)

	def repcap_sfCfgIxNull_set(self, sfCfgIxNull: repcap.SfCfgIxNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SfCfgIxNull.Default
		Default value after init: SfCfgIxNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(sfCfgIxNull)

	def repcap_sfCfgIxNull_get(self) -> repcap.SfCfgIxNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def append(self):
		"""append commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_append'):
			from .Append import Append
			self._append = Append(self._core, self._cmd_group)
		return self._append

	@property
	def frames(self):
		"""frames commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frames'):
			from .Frames import Frames
			self._frames = Frames(self._core, self._cmd_group)
		return self._frames

	@property
	def frConfig(self):
		"""frConfig commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_frConfig'):
			from .FrConfig import FrConfig
			self._frConfig = FrConfig(self._core, self._cmd_group)
		return self._frConfig

	def delete(self, sfCfgIxNull=repcap.SfCfgIxNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFConfig<CH0>:DELete \n
		Snippet: driver.source.bb.dvb.dvbr.sfConfig.delete(sfCfgIxNull = repcap.SfCfgIxNull.Default) \n
		No command help available \n
			:param sfCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SfConfig')
		"""
		sfCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(sfCfgIxNull, repcap.SfCfgIxNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBR:SFConfig{sfCfgIxNull_cmd_val}:DELete')

	def delete_with_opc(self, sfCfgIxNull=repcap.SfCfgIxNull.Default, opc_timeout_ms: int = -1) -> None:
		sfCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(sfCfgIxNull, repcap.SfCfgIxNull)
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFConfig<CH0>:DELete \n
		Snippet: driver.source.bb.dvb.dvbr.sfConfig.delete_with_opc(sfCfgIxNull = repcap.SfCfgIxNull.Default) \n
		No command help available \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param sfCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SfConfig')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:DVB:DVBR:SFConfig{sfCfgIxNull_cmd_val}:DELete', opc_timeout_ms)

	def reset(self, sfCfgIxNull=repcap.SfCfgIxNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFConfig<CH0>:RESet \n
		Snippet: driver.source.bb.dvb.dvbr.sfConfig.reset(sfCfgIxNull = repcap.SfCfgIxNull.Default) \n
		No command help available \n
			:param sfCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SfConfig')
		"""
		sfCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(sfCfgIxNull, repcap.SfCfgIxNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBR:SFConfig{sfCfgIxNull_cmd_val}:RESet')

	def reset_with_opc(self, sfCfgIxNull=repcap.SfCfgIxNull.Default, opc_timeout_ms: int = -1) -> None:
		sfCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(sfCfgIxNull, repcap.SfCfgIxNull)
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFConfig<CH0>:RESet \n
		Snippet: driver.source.bb.dvb.dvbr.sfConfig.reset_with_opc(sfCfgIxNull = repcap.SfCfgIxNull.Default) \n
		No command help available \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param sfCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SfConfig')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:DVB:DVBR:SFConfig{sfCfgIxNull_cmd_val}:RESet', opc_timeout_ms)

	def clone(self) -> 'SfConfig':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SfConfig(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
