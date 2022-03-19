from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signature:
	"""Signature commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signature", core, parent)

	def set(self, signature: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:SIGNature \n
		Snippet: driver.source.bb.w3Gpp.mstation.pcpch.signature.set(signature = 1, mobileStation = repcap.MobileStation.Default) \n
		The command selects the signature of the PCPCH (see Table 3 in 3GPP TS 25.213 Version 3.4.0 Release 1999) . \n
			:param signature: integer Range: 0 to 15
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(signature)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:SIGNature {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:SIGNature \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.pcpch.signature.get(mobileStation = repcap.MobileStation.Default) \n
		The command selects the signature of the PCPCH (see Table 3 in 3GPP TS 25.213 Version 3.4.0 Release 1999) . \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: signature: integer Range: 0 to 15"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:SIGNature?')
		return Conversions.str_to_int(response)
