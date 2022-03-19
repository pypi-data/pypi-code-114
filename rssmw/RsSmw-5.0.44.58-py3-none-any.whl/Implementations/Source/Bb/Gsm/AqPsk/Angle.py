from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Angle:
	"""Angle commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: ChannelNull, default value after init: ChannelNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("angle", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_channelNull_get', 'repcap_channelNull_set', repcap.ChannelNull.Nr0)

	def repcap_channelNull_set(self, channelNull: repcap.ChannelNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ChannelNull.Default
		Default value after init: ChannelNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(channelNull)

	def repcap_channelNull_get(self) -> repcap.ChannelNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, angle: float, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:AQPSk:ANGLe<CH0> \n
		Snippet: driver.source.bb.gsm.aqPsk.angle.set(angle = 1.0, channelNull = repcap.ChannelNull.Default) \n
		Sets the angle alpha. \n
			:param angle: float Range: 0.0001 to 89.9999
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Angle')
		"""
		param = Conversions.decimal_value_to_str(angle)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:AQPSk:ANGLe{channelNull_cmd_val} {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GSM:AQPSk:ANGLe<CH0> \n
		Snippet: value: float = driver.source.bb.gsm.aqPsk.angle.get(channelNull = repcap.ChannelNull.Default) \n
		Sets the angle alpha. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Angle')
			:return: angle: float Range: 0.0001 to 89.9999"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GSM:AQPSk:ANGLe{channelNull_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Angle':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Angle(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
