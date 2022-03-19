from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmiConfirm:
	"""PmiConfirm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmiConfirm", core, parent)

	def set(self, dci_pmi_confirm: bool, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:PMIConfirm \n
		Snippet: driver.source.bb.eutra.downlink.emtc.dci.alloc.pmiConfirm.set(dci_pmi_confirm = False, allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field PMI confirmation for precoding. \n
			:param dci_pmi_confirm: 1| ON| 0| OFF
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.bool_to_str(dci_pmi_confirm)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:PMIConfirm {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:PMIConfirm \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.emtc.dci.alloc.pmiConfirm.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field PMI confirmation for precoding. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dci_pmi_confirm: 1| ON| 0| OFF"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:PMIConfirm?')
		return Conversions.str_to_bool(response)
