from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccd:
	"""Ccd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccd", core, parent)

	def set(self, cyc_del_div: enums.DlpRecCycDelDiv, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:PRECoding:CCD \n
		Snippet: driver.source.bb.eutra.downlink.emtc.alloc.precoding.ccd.set(cyc_del_div = enums.DlpRecCycDelDiv.LADelay, allocationNull = repcap.AllocationNull.Default) \n
		Sets the cyclic delay diversity for the selected allocation. \n
			:param cyc_del_div: NOCDd| LADelay
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(cyc_del_div, enums.DlpRecCycDelDiv)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:PRECoding:CCD {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.DlpRecCycDelDiv:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:PRECoding:CCD \n
		Snippet: value: enums.DlpRecCycDelDiv = driver.source.bb.eutra.downlink.emtc.alloc.precoding.ccd.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the cyclic delay diversity for the selected allocation. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: cyc_del_div: NOCDd| LADelay"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:PRECoding:CCD?')
		return Conversions.str_to_scalar_enum(response, enums.DlpRecCycDelDiv)
