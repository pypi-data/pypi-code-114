from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Soffset:
	"""Soffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("soffset", core, parent)

	def set(self, chan_cod_sfn_offset: float, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:CCODing:SOFFset \n
		Snippet: driver.source.bb.eutra.downlink.emtc.alloc.ccoding.soffset.set(chan_cod_sfn_offset = 1.0, allocationNull = repcap.AllocationNull.Default) \n
		Sets the start SFN value. \n
			:param chan_cod_sfn_offset: float Range: 0 to 1020
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(chan_cod_sfn_offset)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:CCODing:SOFFset {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:CCODing:SOFFset \n
		Snippet: value: float = driver.source.bb.eutra.downlink.emtc.alloc.ccoding.soffset.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the start SFN value. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: chan_cod_sfn_offset: float Range: 0 to 1020"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:CCODing:SOFFset?')
		return Conversions.str_to_float(response)
