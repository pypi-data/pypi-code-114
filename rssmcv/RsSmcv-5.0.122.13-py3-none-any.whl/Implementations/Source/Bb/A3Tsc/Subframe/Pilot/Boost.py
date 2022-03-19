from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Boost:
	"""Boost commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("boost", core, parent)

	def set(self, pilot_boost_mode: int, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:PILot:BOOSt \n
		Snippet: driver.source.bb.a3Tsc.subframe.pilot.boost.set(pilot_boost_mode = 1, subframe = repcap.Subframe.Default) \n
		Sets the power boost mode for the scattered pilots. \n
			:param pilot_boost_mode: integer Range: 0 to 4
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
		"""
		param = Conversions.decimal_value_to_str(pilot_boost_mode)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:PILot:BOOSt {param}')

	def get(self, subframe=repcap.Subframe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:PILot:BOOSt \n
		Snippet: value: int = driver.source.bb.a3Tsc.subframe.pilot.boost.get(subframe = repcap.Subframe.Default) \n
		Sets the power boost mode for the scattered pilots. \n
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
			:return: pilot_boost_mode: integer Range: 0 to 4"""
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:PILot:BOOSt?')
		return Conversions.str_to_int(response)
