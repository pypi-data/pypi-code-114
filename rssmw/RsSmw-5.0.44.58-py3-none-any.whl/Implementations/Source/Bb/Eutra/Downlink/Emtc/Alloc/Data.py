from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, data_source: enums.IdEutraDataSourceDlEmtc, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:DATA \n
		Snippet: driver.source.bb.eutra.downlink.emtc.alloc.data.set(data_source = enums.IdEutraDataSourceDlEmtc.DLISt, allocationNull = repcap.AllocationNull.Default) \n
			INTRO_CMD_HELP: Queries the data source or sets the data source for the following allocations: \n
			- PBCH if MIB is disabled
			- PDSCH SIB1-BR allocation
			- PDSCH allocations configured for P-RNTI or RA-RNTI. \n
			:param data_source: USER1| USER2| USER3| USER4| PN9| PN11| PN15| PN16| PN20| PN21| PN23| PATTern| DLISt| ZERO| ONE| MIB| PRNTi| RARNti| SIBBr
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(data_source, enums.IdEutraDataSourceDlEmtc)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:DATA {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.IdEutraDataSourceDlEmtc:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:DATA \n
		Snippet: value: enums.IdEutraDataSourceDlEmtc = driver.source.bb.eutra.downlink.emtc.alloc.data.get(allocationNull = repcap.AllocationNull.Default) \n
			INTRO_CMD_HELP: Queries the data source or sets the data source for the following allocations: \n
			- PBCH if MIB is disabled
			- PDSCH SIB1-BR allocation
			- PDSCH allocations configured for P-RNTI or RA-RNTI. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: data_source: USER1| USER2| USER3| USER4| PN9| PN11| PN15| PN16| PN20| PN21| PN23| PATTern| DLISt| ZERO| ONE| MIB| PRNTi| RARNti| SIBBr"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.IdEutraDataSourceDlEmtc)
