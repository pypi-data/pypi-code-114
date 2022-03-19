from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CpsFormat:
	"""CpsFormat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cpsFormat", core, parent)

	def set(self, cps_format: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:CPSFormat \n
		Snippet: driver.source.bb.w3Gpp.mstation.pcpch.cpsFormat.set(cps_format = 1, mobileStation = repcap.MobileStation.Default) \n
		The command defines the slot format of the control component of the PCPCH.
			INTRO_CMD_HELP: The slot format sets the associated FBI mode automatically: \n
			- Slot format 0 = FBI OFF
			- Slot format 1 = FBI 1 bit
			- Slot format 2 = FBI 2 bits \n
			:param cps_format: integer Range: 0 to 2
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(cps_format)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:CPSFormat {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:CPSFormat \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.pcpch.cpsFormat.get(mobileStation = repcap.MobileStation.Default) \n
		The command defines the slot format of the control component of the PCPCH.
			INTRO_CMD_HELP: The slot format sets the associated FBI mode automatically: \n
			- Slot format 0 = FBI OFF
			- Slot format 1 = FBI 1 bit
			- Slot format 2 = FBI 2 bits \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: cps_format: integer Range: 0 to 2"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:CPSFormat?')
		return Conversions.str_to_int(response)
