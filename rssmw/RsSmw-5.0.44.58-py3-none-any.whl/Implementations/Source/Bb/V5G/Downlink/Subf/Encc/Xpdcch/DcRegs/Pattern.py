from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, pattern: List[str], subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:DCRegs:PATTern \n
		Snippet: driver.source.bb.v5G.downlink.subf.encc.xpdcch.dcRegs.pattern.set(pattern = ['raw1', 'raw2', 'raw3'], subframeNull = repcap.SubframeNull.Default) \n
		Sets the bit pattern. The setting is relevant for [:SOURce<hw>]:BB:V5G:DL[:SUBF<st0>]:ENCC:XPDCch:DCRegs:DATAPATTern \n
			:param pattern: 64 bit
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.list_to_csv_str(pattern)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:DCRegs:PATTern {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:DCRegs:PATTern \n
		Snippet: value: List[str] = driver.source.bb.v5G.downlink.subf.encc.xpdcch.dcRegs.pattern.get(subframeNull = repcap.SubframeNull.Default) \n
		Sets the bit pattern. The setting is relevant for [:SOURce<hw>]:BB:V5G:DL[:SUBF<st0>]:ENCC:XPDCch:DCRegs:DATAPATTern \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: pattern: 64 bit"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:DCRegs:PATTern?')
		return Conversions.str_to_str_list(response)
