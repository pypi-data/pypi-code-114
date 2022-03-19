from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffTime:
	"""OffTime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offTime", core, parent)

	def set(self, off_time: int, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:TRIGger:OUTPut<CH>:OFFTime \n
		Snippet: driver.source.bb.mccw.trigger.output.offTime.set(off_time = 1, output = repcap.Output.Default) \n
		Sets the number of samples in the off period of the corresponding marker signal. *) If R&S SMW-B9 is installed, the
		minimum marker duration depends on the sample/symbol rate. See chapter 'Basics on ...' in the R&S SMW user manual. \n
			:param off_time: integer Range: 1 (R&S SMW-B10) / 1* (R&S SMW-B9) to 16777215
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(off_time)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:TRIGger:OUTPut{output_cmd_val}:OFFTime {param}')

	def get(self, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:MCCW:TRIGger:OUTPut<CH>:OFFTime \n
		Snippet: value: int = driver.source.bb.mccw.trigger.output.offTime.get(output = repcap.Output.Default) \n
		Sets the number of samples in the off period of the corresponding marker signal. *) If R&S SMW-B9 is installed, the
		minimum marker duration depends on the sample/symbol rate. See chapter 'Basics on ...' in the R&S SMW user manual. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: off_time: integer Range: 1 (R&S SMW-B10) / 1* (R&S SMW-B9) to 16777215"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:MCCW:TRIGger:OUTPut{output_cmd_val}:OFFTime?')
		return Conversions.str_to_int(response)
