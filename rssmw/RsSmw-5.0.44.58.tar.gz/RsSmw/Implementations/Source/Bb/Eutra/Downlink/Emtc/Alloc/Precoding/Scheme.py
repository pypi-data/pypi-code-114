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

	def set(self, prec_mult_ant_sche: enums.DlpRecMultAntScheme, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:PRECoding:SCHeme \n
		Snippet: driver.source.bb.eutra.downlink.emtc.alloc.precoding.scheme.set(prec_mult_ant_sche = enums.DlpRecMultAntScheme.BF, allocationNull = repcap.AllocationNull.Default) \n
		Selects the precoding scheme. \n
			:param prec_mult_ant_sche: NONE| SPM| TXD| BF
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(prec_mult_ant_sche, enums.DlpRecMultAntScheme)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:PRECoding:SCHeme {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.DlpRecMultAntScheme:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:PRECoding:SCHeme \n
		Snippet: value: enums.DlpRecMultAntScheme = driver.source.bb.eutra.downlink.emtc.alloc.precoding.scheme.get(allocationNull = repcap.AllocationNull.Default) \n
		Selects the precoding scheme. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: prec_mult_ant_sche: NONE| SPM| TXD| BF"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:PRECoding:SCHeme?')
		return Conversions.str_to_scalar_enum(response, enums.DlpRecMultAntScheme)
