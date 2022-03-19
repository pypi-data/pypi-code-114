from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Width:
	"""Width commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("width", core, parent)

	def set(self, width: float, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TRIGger:OUTPut<CH>:PULSe:WIDTh \n
		Snippet: driver.source.bb.gnss.trigger.output.pulse.width.set(width = 1.0, output = repcap.Output.Default) \n
		Sets the pulse width for 1PPS, 1PP2S and PPS10 marker mode. The maximum pulse width depends on the marker mode.
			Table Header:  \n
			- Marker mode / 1PPS / 1PP2S / PPS10
			- Max. pulse width / 1 s / 2 s / 0.1 s \n
			:param width: float Range: 1E-9 to depends on the marker mode
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(width)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:TRIGger:OUTPut{output_cmd_val}:PULSe:WIDTh {param}')

	def get(self, output=repcap.Output.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TRIGger:OUTPut<CH>:PULSe:WIDTh \n
		Snippet: value: float = driver.source.bb.gnss.trigger.output.pulse.width.get(output = repcap.Output.Default) \n
		Sets the pulse width for 1PPS, 1PP2S and PPS10 marker mode. The maximum pulse width depends on the marker mode.
			Table Header:  \n
			- Marker mode / 1PPS / 1PP2S / PPS10
			- Max. pulse width / 1 s / 2 s / 0.1 s \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: width: float Range: 1E-9 to depends on the marker mode"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:TRIGger:OUTPut{output_cmd_val}:PULSe:WIDTh?')
		return Conversions.str_to_float(response)
