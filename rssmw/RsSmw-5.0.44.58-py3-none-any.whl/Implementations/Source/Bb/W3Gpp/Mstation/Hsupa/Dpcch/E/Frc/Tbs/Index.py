from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Index:
	"""Index commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("index", core, parent)

	def set(self, index: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:TBS:INDex \n
		Snippet: driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.tbs.index.set(index = 1, mobileStation = repcap.MobileStation.Default) \n
		Selects the Transport Block Size Index (E-TFCI) for the corresponding table, as described in in 3GPP TS 25.321, Annex B.
		The value range of this parameter depends on the selected Transport Block Size Table
		([:SOURce<hw>]:BB:W3GPp:MSTation<st>[:HSUPa]:DPCCh:E:FRC:TBS:TABLe) . \n
			:param index: integer Range: 0 to max
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(index)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:TBS:INDex {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:TBS:INDex \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.tbs.index.get(mobileStation = repcap.MobileStation.Default) \n
		Selects the Transport Block Size Index (E-TFCI) for the corresponding table, as described in in 3GPP TS 25.321, Annex B.
		The value range of this parameter depends on the selected Transport Block Size Table
		([:SOURce<hw>]:BB:W3GPp:MSTation<st>[:HSUPa]:DPCCh:E:FRC:TBS:TABLe) . \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: index: integer Range: 0 to max"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:TBS:INDex?')
		return Conversions.str_to_int(response)
