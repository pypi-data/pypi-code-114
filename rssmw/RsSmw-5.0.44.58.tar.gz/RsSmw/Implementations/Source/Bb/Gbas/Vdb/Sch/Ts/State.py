from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, vdbTransmitter=repcap.VdbTransmitter.Default, timeSlot=repcap.TimeSlot.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:SCH:TS<ST>:STATe \n
		Snippet: driver.source.bb.gbas.vdb.sch.ts.state.set(state = False, vdbTransmitter = repcap.VdbTransmitter.Default, timeSlot = repcap.TimeSlot.Default) \n
		Enables the VDB in the corresponding time slot (TS) . \n
			:param state: 0| 1| OFF| ON
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param timeSlot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ts')
		"""
		param = Conversions.bool_to_str(state)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		timeSlot_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlot, repcap.TimeSlot)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:SCH:TS{timeSlot_cmd_val}:STATe {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default, timeSlot=repcap.TimeSlot.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:SCH:TS<ST>:STATe \n
		Snippet: value: bool = driver.source.bb.gbas.vdb.sch.ts.state.get(vdbTransmitter = repcap.VdbTransmitter.Default, timeSlot = repcap.TimeSlot.Default) \n
		Enables the VDB in the corresponding time slot (TS) . \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param timeSlot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ts')
			:return: state: 0| 1| OFF| ON"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		timeSlot_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlot, repcap.TimeSlot)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:SCH:TS{timeSlot_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
