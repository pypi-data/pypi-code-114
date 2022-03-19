from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Irep:
	"""Irep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("irep", core, parent)

	def set(self, dci_in_pusch: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:NPUSch:IREP \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.alloc.npusch.irep.set(dci_in_pusch = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field number of NPUSCH repetition fields (IRep) . \n
			:param dci_in_pusch: integer Range: 0 to 7
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(dci_in_pusch)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:NPUSch:IREP {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:NPUSch:IREP \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.dci.alloc.npusch.irep.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field number of NPUSCH repetition fields (IRep) . \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dci_in_pusch: integer Range: 0 to 7"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:NPUSch:IREP?')
		return Conversions.str_to_int(response)
