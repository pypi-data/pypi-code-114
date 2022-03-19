from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duplexing:
	"""Duplexing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duplexing", core, parent)

	def set(self, duplexing: enums.EutraDuplexMode, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:DUPLexing \n
		Snippet: driver.source.bb.nr5G.trigger.output.duplexing.set(duplexing = enums.EutraDuplexMode.FDD, output = repcap.Output.Default) \n
		Defines the duplexing mode for a UL/DL pattern containing a marker. \n
			:param duplexing: TDD| FDD TDD Sets TDD (time division duplex) as the duplexing mode. FDD Sets FDD (frequency division duplex) as the duplexing mode.
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(duplexing, enums.EutraDuplexMode)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:DUPLexing {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.EutraDuplexMode:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:DUPLexing \n
		Snippet: value: enums.EutraDuplexMode = driver.source.bb.nr5G.trigger.output.duplexing.get(output = repcap.Output.Default) \n
		Defines the duplexing mode for a UL/DL pattern containing a marker. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: duplexing: TDD| FDD TDD Sets TDD (time division duplex) as the duplexing mode. FDD Sets FDD (frequency division duplex) as the duplexing mode."""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:DUPLexing?')
		return Conversions.str_to_scalar_enum(response, enums.EutraDuplexMode)
