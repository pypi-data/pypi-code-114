from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rba:
	"""Rba commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rba", core, parent)

	def set(self, dci_rba: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:RBA \n
		Snippet: driver.source.bb.eutra.downlink.emtc.dci.alloc.rba.set(dci_rba = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI filed resource block assignment. \n
			:param dci_rba: integer Range: 0 to depends on the installed options* max = 2047 (R&S SMW-K115) max = 4095 (R&S SMW-K143)
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(dci_rba)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:RBA {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:RBA \n
		Snippet: value: int = driver.source.bb.eutra.downlink.emtc.dci.alloc.rba.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI filed resource block assignment. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dci_rba: integer Range: 0 to depends on the installed options* max = 2047 (R&S SMW-K115) max = 4095 (R&S SMW-K143)"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:RBA?')
		return Conversions.str_to_int(response)
