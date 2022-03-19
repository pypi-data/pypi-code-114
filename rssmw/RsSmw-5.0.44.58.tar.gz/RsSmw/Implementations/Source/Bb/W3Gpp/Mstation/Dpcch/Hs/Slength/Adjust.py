from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Adjust:
	"""Adjust commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("adjust", core, parent)

	def set(self, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:SLENgth:ADJust \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.slength.adjust.set(mobileStation = repcap.MobileStation.Default) \n
		(Release 8 and Later) Sets the current ARB sequence length to the suggested value. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:SLENgth:ADJust')

	def set_with_opc(self, mobileStation=repcap.MobileStation.Default, opc_timeout_ms: int = -1) -> None:
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:SLENgth:ADJust \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.slength.adjust.set_with_opc(mobileStation = repcap.MobileStation.Default) \n
		(Release 8 and Later) Sets the current ARB sequence length to the suggested value. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:SLENgth:ADJust', opc_timeout_ms)
