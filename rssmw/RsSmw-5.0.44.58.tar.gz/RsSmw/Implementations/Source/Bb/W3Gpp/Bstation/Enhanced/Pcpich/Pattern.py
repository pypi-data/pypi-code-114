from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, pattern: enums.TxDiv, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:ENHanced:PCPich:PATTern \n
		Snippet: driver.source.bb.w3Gpp.bstation.enhanced.pcpich.pattern.set(pattern = enums.TxDiv.ANT1, baseStation = repcap.BaseStation.Default) \n
		Sets the P-CPICh pattern (channel 0) . \n
			:param pattern: ANT1| ANT2
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.TxDiv)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:ENHanced:PCPich:PATTern {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default) -> enums.TxDiv:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:ENHanced:PCPich:PATTern \n
		Snippet: value: enums.TxDiv = driver.source.bb.w3Gpp.bstation.enhanced.pcpich.pattern.get(baseStation = repcap.BaseStation.Default) \n
		Sets the P-CPICh pattern (channel 0) . \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: pattern: ANT1| ANT2"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:ENHanced:PCPich:PATTern?')
		return Conversions.str_to_scalar_enum(response, enums.TxDiv)
