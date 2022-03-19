from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Conflicts:
	"""Conflicts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("conflicts", core, parent)

	def get(self, subframeNull=repcap.SubframeNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:EXTC:CONFlicts \n
		Snippet: value: int = driver.source.bb.eutra.downlink.subf.encc.pdcch.extc.conflicts.get(subframeNull = repcap.SubframeNull.Default) \n
		Queries the number of conflicts between the DCI formats. To query whether there is a conflict in one particular PDCCH
		item, use the command [:SOURce<hw>]:BB:EUTRa:DL[:SUBF<st0>]:ENCC:PDCCh:EXTC:ITEM<ch0>:CONFlict?. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: no_of_conf: integer Range: 0 to 20"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:EXTC:CONFlicts?')
		return Conversions.str_to_int(response)
