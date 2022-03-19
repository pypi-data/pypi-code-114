from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Append:
	"""Append commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("append", core, parent)

	def set(self, sfCfgIxNull=repcap.SfCfgIxNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFConfig<CH0>:APPend \n
		Snippet: driver.source.bb.dvb.dvbr.sfConfig.append.set(sfCfgIxNull = repcap.SfCfgIxNull.Default) \n
		No command help available \n
			:param sfCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SfConfig')
		"""
		sfCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(sfCfgIxNull, repcap.SfCfgIxNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBR:SFConfig{sfCfgIxNull_cmd_val}:APPend')

	def set_with_opc(self, sfCfgIxNull=repcap.SfCfgIxNull.Default, opc_timeout_ms: int = -1) -> None:
		sfCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(sfCfgIxNull, repcap.SfCfgIxNull)
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFConfig<CH0>:APPend \n
		Snippet: driver.source.bb.dvb.dvbr.sfConfig.append.set_with_opc(sfCfgIxNull = repcap.SfCfgIxNull.Default) \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param sfCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SfConfig')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:DVB:DVBR:SFConfig{sfCfgIxNull_cmd_val}:APPend', opc_timeout_ms)
