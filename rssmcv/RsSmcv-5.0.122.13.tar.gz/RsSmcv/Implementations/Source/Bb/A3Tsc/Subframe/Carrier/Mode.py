from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, red_carrier_mode: int, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:CARRier:MODE \n
		Snippet: driver.source.bb.a3Tsc.subframe.carrier.mode.set(red_carrier_mode = 1, subframe = repcap.Subframe.Default) \n
		Sets a coefficient for reducing the maximum number of carriers. \n
			:param red_carrier_mode: integer Range: 0 to 4
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
		"""
		param = Conversions.decimal_value_to_str(red_carrier_mode)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:CARRier:MODE {param}')

	def get(self, subframe=repcap.Subframe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:CARRier:MODE \n
		Snippet: value: int = driver.source.bb.a3Tsc.subframe.carrier.mode.get(subframe = repcap.Subframe.Default) \n
		Sets a coefficient for reducing the maximum number of carriers. \n
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
			:return: red_carrier_mode: integer Range: 0 to 4"""
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:CARRier:MODE?')
		return Conversions.str_to_int(response)
