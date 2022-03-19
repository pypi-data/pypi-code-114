from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mmode:
	"""Mmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mmode", core, parent)

	def set(self, config_mode: enums.Nr5GmarkConfigMode, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:MMODe \n
		Snippet: driver.source.bb.nr5G.trigger.output.mmode.set(config_mode = enums.Nr5GmarkConfigMode.AUTO, output = repcap.Output.Default) \n
		No command help available \n
			:param config_mode: No help available
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(config_mode, enums.Nr5GmarkConfigMode)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:MMODe {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.Nr5GmarkConfigMode:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:MMODe \n
		Snippet: value: enums.Nr5GmarkConfigMode = driver.source.bb.nr5G.trigger.output.mmode.get(output = repcap.Output.Default) \n
		No command help available \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: config_mode: No help available"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:MMODe?')
		return Conversions.str_to_scalar_enum(response, enums.Nr5GmarkConfigMode)
