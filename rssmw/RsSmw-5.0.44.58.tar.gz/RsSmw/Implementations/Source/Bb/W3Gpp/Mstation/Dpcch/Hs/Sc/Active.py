from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Active:
	"""Active commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("active", core, parent)

	def set(self, sec_cell_active: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:SC:ACTive \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.sc.active.set(sec_cell_active = 1, mobileStation = repcap.MobileStation.Default) \n
		(Release 8 and Later) Sets the number of active secondary cells for the selected UE. \n
			:param sec_cell_active: integer Range: 0 to 7
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(sec_cell_active)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:SC:ACTive {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:SC:ACTive \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.dpcch.hs.sc.active.get(mobileStation = repcap.MobileStation.Default) \n
		(Release 8 and Later) Sets the number of active secondary cells for the selected UE. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: sec_cell_active: integer Range: 0 to 7"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:SC:ACTive?')
		return Conversions.str_to_int(response)
