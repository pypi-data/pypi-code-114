from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scheme:
	"""Scheme commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scheme", core, parent)

	def set(self, scheme: enums.DlecpRecScheme, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:PRECoding:SCHeme \n
		Snippet: driver.source.bb.v5G.downlink.subf.encc.precoding.scheme.set(scheme = enums.DlecpRecScheme.NONE, subframeNull = repcap.SubframeNull.Default) \n
		No command help available \n
			:param scheme: No help available
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.enum_scalar_to_str(scheme, enums.DlecpRecScheme)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:PRECoding:SCHeme {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default) -> enums.DlecpRecScheme:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:[SUBF<ST0>]:ENCC:PRECoding:SCHeme \n
		Snippet: value: enums.DlecpRecScheme = driver.source.bb.v5G.downlink.subf.encc.precoding.scheme.get(subframeNull = repcap.SubframeNull.Default) \n
		No command help available \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: scheme: No help available"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:SUBF{subframeNull_cmd_val}:ENCC:PRECoding:SCHeme?')
		return Conversions.str_to_scalar_enum(response, enums.DlecpRecScheme)
