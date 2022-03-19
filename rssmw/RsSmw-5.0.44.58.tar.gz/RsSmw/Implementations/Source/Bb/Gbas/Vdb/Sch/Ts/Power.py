from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: float, vdbTransmitter=repcap.VdbTransmitter.Default, timeSlot=repcap.TimeSlot.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:SCH:TS<ST>:POWer \n
		Snippet: driver.source.bb.gbas.vdb.sch.ts.power.set(power = 1.0, vdbTransmitter = repcap.VdbTransmitter.Default, timeSlot = repcap.TimeSlot.Default) \n
		Sets the relative power of a VDB per time slot (TS) . \n
			:param power: float Range: -21 to 0
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param timeSlot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ts')
		"""
		param = Conversions.decimal_value_to_str(power)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		timeSlot_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlot, repcap.TimeSlot)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:SCH:TS{timeSlot_cmd_val}:POWer {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default, timeSlot=repcap.TimeSlot.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:SCH:TS<ST>:POWer \n
		Snippet: value: float = driver.source.bb.gbas.vdb.sch.ts.power.get(vdbTransmitter = repcap.VdbTransmitter.Default, timeSlot = repcap.TimeSlot.Default) \n
		Sets the relative power of a VDB per time slot (TS) . \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param timeSlot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ts')
			:return: power: float Range: -21 to 0"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		timeSlot_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlot, repcap.TimeSlot)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:SCH:TS{timeSlot_cmd_val}:POWer?')
		return Conversions.str_to_float(response)
