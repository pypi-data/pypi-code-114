from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ssp:
	"""Ssp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssp", core, parent)

	def set(self, dci_search_space: enums.EutraSearchSpaceEmtc, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:SSP \n
		Snippet: driver.source.bb.eutra.downlink.emtc.dci.alloc.ssp.set(dci_search_space = enums.EutraSearchSpaceEmtc.T0CM, allocationNull = repcap.AllocationNull.Default) \n
		Sets the search space for the selected DCI. \n
			:param dci_search_space: UE| T1CM| T2CM| T0CM
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(dci_search_space, enums.EutraSearchSpaceEmtc)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:SSP {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.EutraSearchSpaceEmtc:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:SSP \n
		Snippet: value: enums.EutraSearchSpaceEmtc = driver.source.bb.eutra.downlink.emtc.dci.alloc.ssp.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the search space for the selected DCI. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dci_search_space: UE| T1CM| T2CM| T0CM"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:SSP?')
		return Conversions.str_to_scalar_enum(response, enums.EutraSearchSpaceEmtc)
