from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Isf:
	"""Isf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("isf", core, parent)

	def set(self, dci_isf: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:NPDSch:ISF \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.alloc.npdsch.isf.set(dci_isf = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI feild resource assignment field (ISF) . \n
			:param dci_isf: integer Range: 0 to 7
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(dci_isf)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:NPDSch:ISF {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:NPDSch:ISF \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.dci.alloc.npdsch.isf.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI feild resource assignment field (ISF) . \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dci_isf: integer Range: 0 to 7"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:NPDSch:ISF?')
		return Conversions.str_to_int(response)
