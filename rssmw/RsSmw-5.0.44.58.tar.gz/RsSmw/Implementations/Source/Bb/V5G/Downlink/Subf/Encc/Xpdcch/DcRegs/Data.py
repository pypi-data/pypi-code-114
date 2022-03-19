from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, data: enums.DataSourceA, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:DCRegs:DATA \n
		Snippet: driver.source.bb.v5G.downlink.subf.encc.xpdcch.dcRegs.data.set(data = enums.DataSourceA.DLISt, subframeNull = repcap.SubframeNull.Default) \n
		Selects the data source for xPDCCH. \n
			:param data: PN9| PN11| PN15| PN16| PN20| PN21| PN23| PATTern| DLISt| ZERO| ONE PNxx Pseudo-random bit sequences (PRBS) of a length of xx bits. The length in bit can be 9, 11, 15, 16, 20, 21, or 23. PATTern User-defined pattern. The pattern can be specified via: [:SOURcehw]:BB:V5G:DL[:SUBFst0]:ENCC:XPDCch:DCRegs:PATTern DLISt Internal data list is used. The data list can be specified via: [:SOURcehw]:BB:V5G:DL[:SUBFst0]:ENCC:XPDCch:DCRegs:DSELect ZERO | ONE Internal 0 or 1 data is used.
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DataSourceA)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:DCRegs:DATA {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default) -> enums.DataSourceA:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:XPDCch:DCRegs:DATA \n
		Snippet: value: enums.DataSourceA = driver.source.bb.v5G.downlink.subf.encc.xpdcch.dcRegs.data.get(subframeNull = repcap.SubframeNull.Default) \n
		Selects the data source for xPDCCH. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: data: PN9| PN11| PN15| PN16| PN20| PN21| PN23| PATTern| DLISt| ZERO| ONE PNxx Pseudo-random bit sequences (PRBS) of a length of xx bits. The length in bit can be 9, 11, 15, 16, 20, 21, or 23. PATTern User-defined pattern. The pattern can be specified via: [:SOURcehw]:BB:V5G:DL[:SUBFst0]:ENCC:XPDCch:DCRegs:PATTern DLISt Internal data list is used. The data list can be specified via: [:SOURcehw]:BB:V5G:DL[:SUBFst0]:ENCC:XPDCch:DCRegs:DSELect ZERO | ONE Internal 0 or 1 data is used."""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:XPDCch:DCRegs:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceA)
