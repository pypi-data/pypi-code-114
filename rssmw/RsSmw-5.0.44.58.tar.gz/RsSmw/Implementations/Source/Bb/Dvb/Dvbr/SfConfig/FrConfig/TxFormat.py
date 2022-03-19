from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxFormat:
	"""TxFormat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("txFormat", core, parent)

	def set(self, tx_format: enums.DvbRcs2TxFormatClassRange, sfCfgIxNull=repcap.SfCfgIxNull.Default, frCfgIxNull=repcap.FrCfgIxNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFConfig<CH0>:FRConfig<ST0>:TXFormat \n
		Snippet: driver.source.bb.dvb.dvbr.sfConfig.frConfig.txFormat.set(tx_format = enums.DvbRcs2TxFormatClassRange.LM, sfCfgIxNull = repcap.SfCfgIxNull.Default, frCfgIxNull = repcap.FrCfgIxNull.Default) \n
		No command help available \n
			:param tx_format: No help available
			:param sfCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SfConfig')
			:param frCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'FrConfig')
		"""
		param = Conversions.enum_scalar_to_str(tx_format, enums.DvbRcs2TxFormatClassRange)
		sfCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(sfCfgIxNull, repcap.SfCfgIxNull)
		frCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(frCfgIxNull, repcap.FrCfgIxNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBR:SFConfig{sfCfgIxNull_cmd_val}:FRConfig{frCfgIxNull_cmd_val}:TXFormat {param}')

	# noinspection PyTypeChecker
	def get(self, sfCfgIxNull=repcap.SfCfgIxNull.Default, frCfgIxNull=repcap.FrCfgIxNull.Default) -> enums.DvbRcs2TxFormatClassRange:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFConfig<CH0>:FRConfig<ST0>:TXFormat \n
		Snippet: value: enums.DvbRcs2TxFormatClassRange = driver.source.bb.dvb.dvbr.sfConfig.frConfig.txFormat.get(sfCfgIxNull = repcap.SfCfgIxNull.Default, frCfgIxNull = repcap.FrCfgIxNull.Default) \n
		No command help available \n
			:param sfCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SfConfig')
			:param frCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'FrConfig')
			:return: tx_format: No help available"""
		sfCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(sfCfgIxNull, repcap.SfCfgIxNull)
		frCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(frCfgIxNull, repcap.FrCfgIxNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:DVBR:SFConfig{sfCfgIxNull_cmd_val}:FRConfig{frCfgIxNull_cmd_val}:TXFormat?')
		return Conversions.str_to_scalar_enum(response, enums.DvbRcs2TxFormatClassRange)
