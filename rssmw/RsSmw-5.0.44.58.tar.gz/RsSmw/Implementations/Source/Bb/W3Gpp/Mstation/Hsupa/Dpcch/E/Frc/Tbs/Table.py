from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Table:
	"""Table commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("table", core, parent)

	def set(self, table: enums.HsUpaFrcTable, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:TBS:TABLe \n
		Snippet: driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.tbs.table.set(table = enums.HsUpaFrcTable.TAB0TTI10, mobileStation = repcap.MobileStation.Default) \n
		Selects the Transport Block Size Table from 3GPP TS 25.321, Annex B according to that the transport block size is
		configured. The transport block size is determined also by the Transport Block Size Index
		([:SOURce<hw>]:BB:W3GPp:MSTation<st>[:HSUPa]:DPCCh:E:FRC:TBS:INDex) . The allowed values for this command depend on the
		selected E-DCH TTI ([:SOURce<hw>]:BB:W3GPp:MSTation<st>[:HSUPa]:DPCCh:E:FRC:TTIEdch) and modulation scheme
		([:SOURce<hw>]:BB:W3GPp:MSTation<st>[:HSUPa]:DPCCh:E:FRC:MODulation) .
			Table Header: E-DCH TTI / Modulation / Transport Block Size Table / SCPI Paramater / Transport Block Size Index (E-TFCI) \n
			- 2ms / BPSK / Table 0 / TAB0TTI2 / 0 .. 127
			- Table 1 / TAB1TTI2 / 0 .. 125
			- 4PAM / Table 2 / TAB2TTI2 / 0 .. 127
			- Table 3 / TAB3TTI2 / 0 .. 124
			- 10ms / Table 0 / TAB0TTI10 / 0 .. 127
			- Table 1 / TAB1TTI10 / 0 .. 120 \n
			:param table: TAB0TTI2| TAB1TTI2| TAB2TTI2| TAB3TTI2| TAB0TTI10| TAB1TTI10
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(table, enums.HsUpaFrcTable)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:TBS:TABLe {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.HsUpaFrcTable:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:TBS:TABLe \n
		Snippet: value: enums.HsUpaFrcTable = driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.tbs.table.get(mobileStation = repcap.MobileStation.Default) \n
		Selects the Transport Block Size Table from 3GPP TS 25.321, Annex B according to that the transport block size is
		configured. The transport block size is determined also by the Transport Block Size Index
		([:SOURce<hw>]:BB:W3GPp:MSTation<st>[:HSUPa]:DPCCh:E:FRC:TBS:INDex) . The allowed values for this command depend on the
		selected E-DCH TTI ([:SOURce<hw>]:BB:W3GPp:MSTation<st>[:HSUPa]:DPCCh:E:FRC:TTIEdch) and modulation scheme
		([:SOURce<hw>]:BB:W3GPp:MSTation<st>[:HSUPa]:DPCCh:E:FRC:MODulation) .
			Table Header: E-DCH TTI / Modulation / Transport Block Size Table / SCPI Paramater / Transport Block Size Index (E-TFCI) \n
			- 2ms / BPSK / Table 0 / TAB0TTI2 / 0 .. 127
			- Table 1 / TAB1TTI2 / 0 .. 125
			- 4PAM / Table 2 / TAB2TTI2 / 0 .. 127
			- Table 3 / TAB3TTI2 / 0 .. 124
			- 10ms / Table 0 / TAB0TTI10 / 0 .. 127
			- Table 1 / TAB1TTI10 / 0 .. 120 \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: table: TAB0TTI2| TAB1TTI2| TAB2TTI2| TAB3TTI2| TAB0TTI10| TAB1TTI10"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:TBS:TABLe?')
		return Conversions.str_to_scalar_enum(response, enums.HsUpaFrcTable)
