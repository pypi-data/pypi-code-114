from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, format_py: enums.PdccFmt2, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:FORMat \n
		Snippet: driver.source.bb.eutra.downlink.subf.encc.pdcch.formatPy.set(format_py = enums.PdccFmt2._0, subframeNull = repcap.SubframeNull.Default) \n
		Sets the PDCCH format. \n
			:param format_py: VAR| -1| 0| 1| 2| 3 VAR Enables full flexibility by the configuration of the downlink control information (DCI) format and content. -1 Proprietary format for legacy support. 0 | 1 | 2 | 3 One PDCCH is transmitted on one, two, four or eight CCEs
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.PdccFmt2)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default) -> enums.PdccFmt2:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PDCCh:FORMat \n
		Snippet: value: enums.PdccFmt2 = driver.source.bb.eutra.downlink.subf.encc.pdcch.formatPy.get(subframeNull = repcap.SubframeNull.Default) \n
		Sets the PDCCH format. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: format_py: VAR| -1| 0| 1| 2| 3 VAR Enables full flexibility by the configuration of the downlink control information (DCI) format and content. -1 Proprietary format for legacy support. 0 | 1 | 2 | 3 One PDCCH is transmitted on one, two, four or eight CCEs"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.PdccFmt2)
