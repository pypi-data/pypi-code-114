from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Utilities import trim_str_response
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dselect:
	"""Dselect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dselect", core, parent)

	def set(self, filename: str, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:DCRegs:DSELect \n
		Snippet: driver.source.bb.v5G.downlink.subf.encc.xpdcch.dcRegs.dselect.set(filename = '1', subframeNull = repcap.SubframeNull.Default) \n
		Specifies data list file. The setting is relevant for [:SOURce<hw>]:BB:V5G:DL[:SUBF<st0>]:ENCC:XPDCch:DCRegs:DATADLISt \n
			:param filename: string
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.value_to_quoted_str(filename)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:DCRegs:DSELect {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:DCRegs:DSELect \n
		Snippet: value: str = driver.source.bb.v5G.downlink.subf.encc.xpdcch.dcRegs.dselect.get(subframeNull = repcap.SubframeNull.Default) \n
		Specifies data list file. The setting is relevant for [:SOURce<hw>]:BB:V5G:DL[:SUBF<st0>]:ENCC:XPDCch:DCRegs:DATADLISt \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: filename: string"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:DCRegs:DSELect?')
		return trim_str_response(response)
