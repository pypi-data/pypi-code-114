from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrPeriod:
	"""SrPeriod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srPeriod", core, parent)

	def set(self, sfn_rest_period: enums.PbchSfnRestPeriod, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:CCODing:SRPeriod \n
		Snippet: driver.source.bb.eutra.downlink.emtc.alloc.ccoding.srPeriod.set(sfn_rest_period = enums.PbchSfnRestPeriod.PER3gpp, allocationNull = repcap.AllocationNull.Default) \n
		Determines the time span after which the SFN (System Frame Number) restarts. \n
			:param sfn_rest_period: PERSlength | PER3gpp PER3gpp = '3GPP (1024 Frames) ' PERSlength = SFN restart period to the ARB sequence length
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(sfn_rest_period, enums.PbchSfnRestPeriod)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:CCODing:SRPeriod {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.PbchSfnRestPeriod:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:CCODing:SRPeriod \n
		Snippet: value: enums.PbchSfnRestPeriod = driver.source.bb.eutra.downlink.emtc.alloc.ccoding.srPeriod.get(allocationNull = repcap.AllocationNull.Default) \n
		Determines the time span after which the SFN (System Frame Number) restarts. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: sfn_rest_period: PERSlength | PER3gpp PER3gpp = '3GPP (1024 Frames) ' PERSlength = SFN restart period to the ARB sequence length"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:CCODing:SRPeriod?')
		return Conversions.str_to_scalar_enum(response, enums.PbchSfnRestPeriod)
