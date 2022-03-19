from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.TriggerMarkModeB, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:OUTPut<CH>:MODE \n
		Snippet: driver.source.bb.nfc.trigger.output.mode.set(mode = enums.TriggerMarkModeB.PATTern, output = repcap.Output.Default) \n
		No command help available \n
			:param mode: PULSe| RESTart| PATTern| RATio PULSe A regular marker signal is generated. The frequency is derived by dividing the sample rate by the divider, which is input with the command [:SOURcehw]:BB:NFC:TRIGger:OUTPutch:PULSe:DIVider. RESTart A marker signal is generated on every repetition of the complete frame sequence. PATTern A marker signal that is defined by a bit pattern is generated. The pattern has a maximum length of 64 bits and is defined with the command[:SOURcehw]:BB:NFC:TRIGger:OUTPutch:PATTern RATio A marker signal corresponding to the Time Off / Time On specifications in the commands [:SOURcehw]:BB:NFC:TRIGger:OUTPutch:ONTime and [:SOURcehw]:BB:NFC:TRIGger:OUTPutch:OFFTime
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TriggerMarkModeB)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:TRIGger:OUTPut{output_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.TriggerMarkModeB:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:OUTPut<CH>:MODE \n
		Snippet: value: enums.TriggerMarkModeB = driver.source.bb.nfc.trigger.output.mode.get(output = repcap.Output.Default) \n
		No command help available \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mode: PULSe| RESTart| PATTern| RATio PULSe A regular marker signal is generated. The frequency is derived by dividing the sample rate by the divider, which is input with the command [:SOURcehw]:BB:NFC:TRIGger:OUTPutch:PULSe:DIVider. RESTart A marker signal is generated on every repetition of the complete frame sequence. PATTern A marker signal that is defined by a bit pattern is generated. The pattern has a maximum length of 64 bits and is defined with the command[:SOURcehw]:BB:NFC:TRIGger:OUTPutch:PATTern RATio A marker signal corresponding to the Time Off / Time On specifications in the commands [:SOURcehw]:BB:NFC:TRIGger:OUTPutch:ONTime and [:SOURcehw]:BB:NFC:TRIGger:OUTPutch:OFFTime"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:TRIGger:OUTPut{output_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerMarkModeB)
