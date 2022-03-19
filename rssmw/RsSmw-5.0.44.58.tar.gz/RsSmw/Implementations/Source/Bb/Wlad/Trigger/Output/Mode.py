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

	def set(self, mode: enums.WlanadMarkMode, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:TRIGger:OUTPut<CH>:MODE \n
		Snippet: driver.source.bb.wlad.trigger.output.mode.set(mode = enums.WlanadMarkMode.FAPart, output = repcap.Output.Default) \n
		Sets the marker mode. \n
			:param mode: RESTart| FBLock| FRAMe| FAPart| PULSe| PATTern| RATio| FIPart RESTart A marker signal is generated at the start of each signal sequence (period = all frame blocks) . FRAMe Number of Frame Blocks = 1, that is, a marker signal is generated at the start of each frame in the single frame block. Otherwise, the frame block and frame index are entered and the specific frame is masked. FBLock Number of Frame Blocks =1, that is, a marker signal is generated at the start of each frame block. Otherwise, a specific frame block index is given and the whole frame block is marked. FAPart Number of Frame Blocks = 1, that is, a marker signal is generated to mark every active part of each frame. The active data transfer part (PPDU) of a frame period is marked with high, the inactive part (idle time) with low. This marker can be used to decrease the carrier leakage during inactive signal parts by feeding it into the pulse modulator. Otherwise, the frame block and frame index are entered and the active part of the specific frame is masked. PATTern A marker signal is generated according to the user-defined pattern (command SOURce:BB:WLAD:TRIGger:OUTPut:PATTern) . PULSe A pulsed marker signal is generated. The pulse frequency (= symbol rate/divider) is defined with the SOUR:BB:WLAD:TRIG:OUTP:PULSe:DIVider command and can be queried with the SOUR:BB:WLAD:TRIG:OUTP:PULSe:FREQuency? command. RATio A marker signal corresponding to the Time Off / Time On specifications in the commands SOURce:BB:WLAD:TRIGger:OUTPut:OFFT and SOURce:BB:WLAD:TRIGger:OUTPut:ONT is generated.
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.WlanadMarkMode)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:TRIGger:OUTPut{output_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.WlanadMarkMode:
		"""SCPI: [SOURce<HW>]:BB:WLAD:TRIGger:OUTPut<CH>:MODE \n
		Snippet: value: enums.WlanadMarkMode = driver.source.bb.wlad.trigger.output.mode.get(output = repcap.Output.Default) \n
		Sets the marker mode. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mode: RESTart| FBLock| FRAMe| FAPart| PULSe| PATTern| RATio| FIPart RESTart A marker signal is generated at the start of each signal sequence (period = all frame blocks) . FRAMe Number of Frame Blocks = 1, that is, a marker signal is generated at the start of each frame in the single frame block. Otherwise, the frame block and frame index are entered and the specific frame is masked. FBLock Number of Frame Blocks =1, that is, a marker signal is generated at the start of each frame block. Otherwise, a specific frame block index is given and the whole frame block is marked. FAPart Number of Frame Blocks = 1, that is, a marker signal is generated to mark every active part of each frame. The active data transfer part (PPDU) of a frame period is marked with high, the inactive part (idle time) with low. This marker can be used to decrease the carrier leakage during inactive signal parts by feeding it into the pulse modulator. Otherwise, the frame block and frame index are entered and the active part of the specific frame is masked. PATTern A marker signal is generated according to the user-defined pattern (command SOURce:BB:WLAD:TRIGger:OUTPut:PATTern) . PULSe A pulsed marker signal is generated. The pulse frequency (= symbol rate/divider) is defined with the SOUR:BB:WLAD:TRIG:OUTP:PULSe:DIVider command and can be queried with the SOUR:BB:WLAD:TRIG:OUTP:PULSe:FREQuency? command. RATio A marker signal corresponding to the Time Off / Time On specifications in the commands SOURce:BB:WLAD:TRIGger:OUTPut:OFFT and SOURce:BB:WLAD:TRIGger:OUTPut:ONT is generated."""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLAD:TRIGger:OUTPut{output_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.WlanadMarkMode)
