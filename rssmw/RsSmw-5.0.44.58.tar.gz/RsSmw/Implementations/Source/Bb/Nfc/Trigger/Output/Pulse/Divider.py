from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Divider:
	"""Divider commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("divider", core, parent)

	def set(self, divider: int, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:OUTPut<CH>:PULSe:DIVider \n
		Snippet: driver.source.bb.nfc.trigger.output.pulse.divider.set(divider = 1, output = repcap.Output.Default) \n
		Sets the divider for the pulsed marker signal. \n
			:param divider: integer Range: 2 to 1024
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(divider)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:TRIGger:OUTPut{output_cmd_val}:PULSe:DIVider {param}')

	def get(self, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:OUTPut<CH>:PULSe:DIVider \n
		Snippet: value: int = driver.source.bb.nfc.trigger.output.pulse.divider.get(output = repcap.Output.Default) \n
		Sets the divider for the pulsed marker signal. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: divider: integer Range: 2 to 1024"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:TRIGger:OUTPut{output_cmd_val}:PULSe:DIVider?')
		return Conversions.str_to_int(response)
