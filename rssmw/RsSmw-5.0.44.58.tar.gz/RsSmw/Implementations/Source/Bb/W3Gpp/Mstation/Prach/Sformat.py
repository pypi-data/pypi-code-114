from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sformat:
	"""Sformat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sformat", core, parent)

	def set(self, sformat: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PRACh:SFORmat \n
		Snippet: driver.source.bb.w3Gpp.mstation.prach.sformat.set(sformat = 1, mobileStation = repcap.MobileStation.Default) \n
		Defines the slot format of the PRACH. A change of slot format leads to an automatic change of symbol rate
		[:SOURce<hw>]:BB:W3GPp:MSTation<st>:PRACh:SRATe When channel coding is active, the slot format is predetermined. So in
		this case, the command has no effect. \n
			:param sformat: 0 | 1 | 2 | 3
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(sformat)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PRACh:SFORmat {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PRACh:SFORmat \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.prach.sformat.get(mobileStation = repcap.MobileStation.Default) \n
		Defines the slot format of the PRACH. A change of slot format leads to an automatic change of symbol rate
		[:SOURce<hw>]:BB:W3GPp:MSTation<st>:PRACh:SRATe When channel coding is active, the slot format is predetermined. So in
		this case, the command has no effect. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: sformat: 0 | 1 | 2 | 3"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PRACh:SFORmat?')
		return Conversions.str_to_int(response)
