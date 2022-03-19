from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slength:
	"""Slength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slength", core, parent)

	def set(self, slot_length: enums.QuickSetSlotLenAll, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:SLENgth \n
		Snippet: driver.source.bb.nr5G.trigger.output.slength.set(slot_length = enums.QuickSetSlotLenAll.S10, output = repcap.Output.Default) \n
		Sets the duration of a UL/DL pattern containing a marker. \n
			:param slot_length: S5| S10 S5 Sets the duration of the UL/DL pattern to 5 slots. S10 Sets the duration of the UL/DL pattern to 10 slots.
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(slot_length, enums.QuickSetSlotLenAll)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:SLENgth {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.QuickSetSlotLenAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:SLENgth \n
		Snippet: value: enums.QuickSetSlotLenAll = driver.source.bb.nr5G.trigger.output.slength.get(output = repcap.Output.Default) \n
		Sets the duration of a UL/DL pattern containing a marker. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: slot_length: S5| S10 S5 Sets the duration of the UL/DL pattern to 5 slots. S10 Sets the duration of the UL/DL pattern to 10 slots."""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:SLENgth?')
		return Conversions.str_to_scalar_enum(response, enums.QuickSetSlotLenAll)
