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

	def set(self, mode: enums.PowerRampMarkMode, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:TRIGger:OUTPut<CH>:MODE \n
		Snippet: driver.source.bb.pramp.trigger.output.mode.set(mode = enums.PowerRampMarkMode.PRESweep, output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param mode: UNCHanged| RFBLanking| PRESweep| STARt| STOP UNCHanged Provides the standard marker signal. RFBLanking Returns the marker signal when the RF blanking is active. PRESweep Returns the marker signal when the power sweep reaches the pre-sweep level. STARt Returns the marker signal when the power sweep reaches the stop level.
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PowerRampMarkMode)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:TRIGger:OUTPut{output_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.PowerRampMarkMode:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:TRIGger:OUTPut<CH>:MODE \n
		Snippet: value: enums.PowerRampMarkMode = driver.source.bb.pramp.trigger.output.mode.get(output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mode: UNCHanged| RFBLanking| PRESweep| STARt| STOP UNCHanged Provides the standard marker signal. RFBLanking Returns the marker signal when the RF blanking is active. PRESweep Returns the marker signal when the power sweep reaches the pre-sweep level. STARt Returns the marker signal when the power sweep reaches the stop level."""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:PRAMp:TRIGger:OUTPut{output_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PowerRampMarkMode)
