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

	def set(self, mode: enums.TdscdmaMarkMode, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:TRIGger:OUTPut<CH>:MODE \n
		Snippet: driver.source.bb.tdscdma.trigger.output.mode.set(mode = enums.TdscdmaMarkMode.CSPeriod, output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param mode: RFRame| SFNR| CSPeriod| RATio| USER| FACTive RFRame = Radio Frame SFNR = System Frame Number (SFN) Restart CSPeriod = Chip Sequence Period (ARB) RATio = On/Off Ratio USER = User Period
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TdscdmaMarkMode)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:TRIGger:OUTPut{output_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.TdscdmaMarkMode:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:TRIGger:OUTPut<CH>:MODE \n
		Snippet: value: enums.TdscdmaMarkMode = driver.source.bb.tdscdma.trigger.output.mode.get(output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mode: RFRame| SFNR| CSPeriod| RATio| USER| FACTive RFRame = Radio Frame SFNR = System Frame Number (SFN) Restart CSPeriod = Chip Sequence Period (ARB) RATio = On/Off Ratio USER = User Period"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:TRIGger:OUTPut{output_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TdscdmaMarkMode)
