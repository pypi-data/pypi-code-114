from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PreLen:
	"""PreLen commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preLen", core, parent)

	def set(self, pre_len: int, sfCfgIxNull=repcap.SfCfgIxNull.Default, frCfgIxNull=repcap.FrCfgIxNull.Default, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFConfig<CH0>:FRConfig<ST0>:SEC<DI0>:PRELen \n
		Snippet: driver.source.bb.dvb.dvbr.sfConfig.frConfig.sec.preLen.set(pre_len = 1, sfCfgIxNull = repcap.SfCfgIxNull.Default, frCfgIxNull = repcap.FrCfgIxNull.Default, indexNull = repcap.IndexNull.Default) \n
		No command help available \n
			:param pre_len: No help available
			:param sfCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SfConfig')
			:param frCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'FrConfig')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sec')
		"""
		param = Conversions.decimal_value_to_str(pre_len)
		sfCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(sfCfgIxNull, repcap.SfCfgIxNull)
		frCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(frCfgIxNull, repcap.FrCfgIxNull)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBR:SFConfig{sfCfgIxNull_cmd_val}:FRConfig{frCfgIxNull_cmd_val}:SEC{indexNull_cmd_val}:PRELen {param}')

	def get(self, sfCfgIxNull=repcap.SfCfgIxNull.Default, frCfgIxNull=repcap.FrCfgIxNull.Default, indexNull=repcap.IndexNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFConfig<CH0>:FRConfig<ST0>:SEC<DI0>:PRELen \n
		Snippet: value: int = driver.source.bb.dvb.dvbr.sfConfig.frConfig.sec.preLen.get(sfCfgIxNull = repcap.SfCfgIxNull.Default, frCfgIxNull = repcap.FrCfgIxNull.Default, indexNull = repcap.IndexNull.Default) \n
		No command help available \n
			:param sfCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SfConfig')
			:param frCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'FrConfig')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sec')
			:return: pre_len: No help available"""
		sfCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(sfCfgIxNull, repcap.SfCfgIxNull)
		frCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(frCfgIxNull, repcap.FrCfgIxNull)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:DVBR:SFConfig{sfCfgIxNull_cmd_val}:FRConfig{frCfgIxNull_cmd_val}:SEC{indexNull_cmd_val}:PRELen?')
		return Conversions.str_to_int(response)
