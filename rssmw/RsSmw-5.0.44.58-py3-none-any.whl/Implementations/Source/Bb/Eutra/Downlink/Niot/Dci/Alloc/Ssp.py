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

	def set(self, search_space: enums.EutraSearchSpaceNbiot, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:SSP \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.alloc.ssp.set(search_space = enums.EutraSearchSpaceNbiot.T1CM, allocationNull = repcap.AllocationNull.Default) \n
		Sets the search space for the selected DCI. \n
			:param search_space: UE| T1CM| T2CM
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(search_space, enums.EutraSearchSpaceNbiot)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:SSP {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.EutraSearchSpaceNbiot:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:SSP \n
		Snippet: value: enums.EutraSearchSpaceNbiot = driver.source.bb.eutra.downlink.niot.dci.alloc.ssp.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the search space for the selected DCI. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: search_space: UE| T1CM| T2CM"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:SSP?')
		return Conversions.str_to_scalar_enum(response, enums.EutraSearchSpaceNbiot)
