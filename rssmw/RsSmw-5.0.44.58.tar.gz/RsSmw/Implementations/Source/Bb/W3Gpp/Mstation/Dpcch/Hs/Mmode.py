from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mmode:
	"""Mmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mmode", core, parent)

	def set(self, mmode: bool, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MMODe \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.mmode.set(mmode = False, mobileStation = repcap.MobileStation.Default) \n
		(Release 8 and Later, Release 8 and Later (RT) Enables/disables working in MIMO mode for the selected UE. \n
			:param mmode: 1| ON| 0| OFF
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.bool_to_str(mmode)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MMODe {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:MMODe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.mstation.dpcch.hs.mmode.get(mobileStation = repcap.MobileStation.Default) \n
		(Release 8 and Later, Release 8 and Later (RT) Enables/disables working in MIMO mode for the selected UE. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: mmode: 1| ON| 0| OFF"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:MMODe?')
		return Conversions.str_to_bool(response)
