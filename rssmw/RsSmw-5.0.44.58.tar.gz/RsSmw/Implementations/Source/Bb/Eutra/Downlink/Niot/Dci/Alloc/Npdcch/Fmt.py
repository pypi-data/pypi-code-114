from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fmt:
	"""Fmt commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fmt", core, parent)

	def set(self, npdcch_fmt: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:NPDCch:FMT \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.alloc.npdcch.fmt.set(npdcch_fmt = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets the NPDCCH format. \n
			:param npdcch_fmt: integer Range: 0 to 1
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(npdcch_fmt)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:NPDCch:FMT {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:NPDCch:FMT \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.dci.alloc.npdcch.fmt.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the NPDCCH format. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: npdcch_fmt: integer Range: 0 to 1"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:NPDCch:FMT?')
		return Conversions.str_to_int(response)
