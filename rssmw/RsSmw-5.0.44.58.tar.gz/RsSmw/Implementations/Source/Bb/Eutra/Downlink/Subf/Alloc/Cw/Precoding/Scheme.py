from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scheme:
	"""Scheme commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scheme", core, parent)

	def set(self, scheme: enums.DlpRecMultAntScheme, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default, codeword=repcap.Codeword.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ALLoc<CH0>:[CW<USER>]:PRECoding:SCHeme \n
		Snippet: driver.source.bb.eutra.downlink.subf.alloc.cw.precoding.scheme.set(scheme = enums.DlpRecMultAntScheme.BF, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default, codeword = repcap.Codeword.Default) \n
		(available for the first codeword only) Selects the precoding scheme. The available selections depend on the selected
		content type. \n
			:param scheme: NONE| SPM| TXD| BF NONE Disables precoding. SPM Spatial multiplexing TXD Transmit diversity BF Sets the PDSCH to transmission mode selected with the command [:SOURcehw]:BB:EUTRa:DL[:SUBFst0]:ALLocch0[:CWuser]:PRECoding:TRSCheme.
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param codeword: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cw')
		"""
		param = Conversions.enum_scalar_to_str(scheme, enums.DlpRecMultAntScheme)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		codeword_cmd_val = self._cmd_group.get_repcap_cmd_value(codeword, repcap.Codeword)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:CW{codeword_cmd_val}:PRECoding:SCHeme {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default, codeword=repcap.Codeword.Default) -> enums.DlpRecMultAntScheme:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ALLoc<CH0>:[CW<USER>]:PRECoding:SCHeme \n
		Snippet: value: enums.DlpRecMultAntScheme = driver.source.bb.eutra.downlink.subf.alloc.cw.precoding.scheme.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default, codeword = repcap.Codeword.Default) \n
		(available for the first codeword only) Selects the precoding scheme. The available selections depend on the selected
		content type. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param codeword: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cw')
			:return: scheme: NONE| SPM| TXD| BF NONE Disables precoding. SPM Spatial multiplexing TXD Transmit diversity BF Sets the PDSCH to transmission mode selected with the command [:SOURcehw]:BB:EUTRa:DL[:SUBFst0]:ALLocch0[:CWuser]:PRECoding:TRSCheme."""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		codeword_cmd_val = self._cmd_group.get_repcap_cmd_value(codeword, repcap.Codeword)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:CW{codeword_cmd_val}:PRECoding:SCHeme?')
		return Conversions.str_to_scalar_enum(response, enums.DlpRecMultAntScheme)
