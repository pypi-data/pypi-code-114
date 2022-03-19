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

	def set(self, mode: enums.MarkModeB, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:TRIGger:OUTPut<CH>:MODE \n
		Snippet: driver.source.bb.w3Gpp.trigger.output.mode.set(mode = enums.MarkModeB.CSPeriod, output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param mode: SLOT| RFRame| CSPeriod| SFNR| RATio| USER SLOT = Slot RFRame = Radio Frame CSPeriod = Chip Sequence Period (ARB) SFNR = System Frame Number (SFN) Restart RATio = ON/OFF Ratio USER = User
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.MarkModeB)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:TRIGger:OUTPut{output_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.MarkModeB:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:TRIGger:OUTPut<CH>:MODE \n
		Snippet: value: enums.MarkModeB = driver.source.bb.w3Gpp.trigger.output.mode.get(output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mode: SLOT| RFRame| CSPeriod| SFNR| RATio| USER SLOT = Slot RFRame = Radio Frame CSPeriod = Chip Sequence Period (ARB) SFNR = System Frame Number (SFN) Restart RATio = ON/OFF Ratio USER = User"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:TRIGger:OUTPut{output_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.MarkModeB)
