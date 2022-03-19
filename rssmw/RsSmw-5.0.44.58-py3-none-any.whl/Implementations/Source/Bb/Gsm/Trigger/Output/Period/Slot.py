from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slot:
	"""Slot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slot", core, parent)

	def set(self, slot: int, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:TRIGger:OUTPut<CH>:PERiod:SLOT \n
		Snippet: driver.source.bb.gsm.trigger.output.period.slot.set(slot = 1, output = repcap.Output.Default) \n
		Sets the repetition rate for the slot clock at the marker outputs. \n
			:param slot: integer Range: 1 to 8
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(slot)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:TRIGger:OUTPut{output_cmd_val}:PERiod:SLOT {param}')

	def get(self, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GSM:TRIGger:OUTPut<CH>:PERiod:SLOT \n
		Snippet: value: int = driver.source.bb.gsm.trigger.output.period.slot.get(output = repcap.Output.Default) \n
		Sets the repetition rate for the slot clock at the marker outputs. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: slot: integer Range: 1 to 8"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GSM:TRIGger:OUTPut{output_cmd_val}:PERiod:SLOT?')
		return Conversions.str_to_int(response)
