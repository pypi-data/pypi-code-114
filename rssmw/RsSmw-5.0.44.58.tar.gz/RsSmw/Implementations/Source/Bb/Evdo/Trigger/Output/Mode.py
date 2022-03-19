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

	def set(self, mode: enums.EvdoMarkMode, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TRIGger:OUTPut<CH>:MODE \n
		Snippet: driver.source.bb.evdo.trigger.output.mode.set(mode = enums.EvdoMarkMode.CSPeriod, output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param mode: SLOT| PNSPeriod| ESM| CSPeriod| USER| RATio SLOT Each slot (every 1.67 ms) PNSPeriod Every 26.67 ms (PN Sequence Period) ESM Every 2 s (even second mark) . CSPeriod Each arbitrary waveform sequence RATio Regular marker signal USER Every user-defined period.
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EvdoMarkMode)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TRIGger:OUTPut{output_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.EvdoMarkMode:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TRIGger:OUTPut<CH>:MODE \n
		Snippet: value: enums.EvdoMarkMode = driver.source.bb.evdo.trigger.output.mode.get(output = repcap.Output.Default) \n
		Defines the signal for the selected marker output. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: mode: SLOT| PNSPeriod| ESM| CSPeriod| USER| RATio SLOT Each slot (every 1.67 ms) PNSPeriod Every 26.67 ms (PN Sequence Period) ESM Every 2 s (even second mark) . CSPeriod Each arbitrary waveform sequence RATio Regular marker signal USER Every user-defined period."""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TRIGger:OUTPut{output_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoMarkMode)
