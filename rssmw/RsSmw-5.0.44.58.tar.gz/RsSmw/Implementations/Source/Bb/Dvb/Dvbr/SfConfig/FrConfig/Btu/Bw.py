from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bw:
	"""Bw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bw", core, parent)

	def set(self, bw: float, sfCfgIxNull=repcap.SfCfgIxNull.Default, frCfgIxNull=repcap.FrCfgIxNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFConfig<CH0>:FRConfig<ST0>:BTU:BW \n
		Snippet: driver.source.bb.dvb.dvbr.sfConfig.frConfig.btu.bw.set(bw = 1.0, sfCfgIxNull = repcap.SfCfgIxNull.Default, frCfgIxNull = repcap.FrCfgIxNull.Default) \n
		No command help available \n
			:param bw: No help available
			:param sfCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SfConfig')
			:param frCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'FrConfig')
		"""
		param = Conversions.decimal_value_to_str(bw)
		sfCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(sfCfgIxNull, repcap.SfCfgIxNull)
		frCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(frCfgIxNull, repcap.FrCfgIxNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBR:SFConfig{sfCfgIxNull_cmd_val}:FRConfig{frCfgIxNull_cmd_val}:BTU:BW {param}')

	def get(self, sfCfgIxNull=repcap.SfCfgIxNull.Default, frCfgIxNull=repcap.FrCfgIxNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBR:SFConfig<CH0>:FRConfig<ST0>:BTU:BW \n
		Snippet: value: float = driver.source.bb.dvb.dvbr.sfConfig.frConfig.btu.bw.get(sfCfgIxNull = repcap.SfCfgIxNull.Default, frCfgIxNull = repcap.FrCfgIxNull.Default) \n
		No command help available \n
			:param sfCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SfConfig')
			:param frCfgIxNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'FrConfig')
			:return: bw: No help available"""
		sfCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(sfCfgIxNull, repcap.SfCfgIxNull)
		frCfgIxNull_cmd_val = self._cmd_group.get_repcap_cmd_value(frCfgIxNull, repcap.FrCfgIxNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:DVBR:SFConfig{sfCfgIxNull_cmd_val}:FRConfig{frCfgIxNull_cmd_val}:BTU:BW?')
		return Conversions.str_to_float(response)
