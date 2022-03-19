from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rx:
	"""Rx commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rx", core, parent)

	@property
	def dedication(self):
		"""dedication commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dedication'):
			from .Dedication import Dedication
			self._dedication = Dedication(self._core, self._cmd_group)
		return self._dedication

	@property
	def end(self):
		"""end commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_end'):
			from .End import End
			self._end = End(self._core, self._cmd_group)
		return self._end

	@property
	def start(self):
		"""start commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_start'):
			from .Start import Start
			self._start = Start(self._core, self._cmd_group)
		return self._start

	def set(self, radar_power_rx: float, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:POWer:RX \n
		Snippet: driver.source.regenerator.object.power.rx.set(radar_power_rx = 1.0, objectIx = repcap.ObjectIx.Default) \n
		In [:SOURce<hw>]:REGenerator:RADar:POWer:MODE MANual mode, sets the Rx power of each object. \n
			:param radar_power_rx: float Range: -145 to 30
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.decimal_value_to_str(radar_power_rx)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:POWer:RX {param}')

	def get(self, objectIx=repcap.ObjectIx.Default) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:POWer:RX \n
		Snippet: value: float = driver.source.regenerator.object.power.rx.get(objectIx = repcap.ObjectIx.Default) \n
		In [:SOURce<hw>]:REGenerator:RADar:POWer:MODE MANual mode, sets the Rx power of each object. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: radar_power_rx: float Range: -145 to 30"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:POWer:RX?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Rx':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rx(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
