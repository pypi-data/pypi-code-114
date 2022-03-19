from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ovelocity:
	"""Ovelocity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ovelocity", core, parent)

	def set(self, object_velocity: float, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:OVELocity \n
		Snippet: driver.source.regenerator.object.ovelocity.set(object_velocity = 1.0, objectIx = repcap.ObjectIx.Default) \n
		Sets the speed of a moving object. \n
			:param object_velocity: float Range: 0.001 to 2E11, Unit: m/s
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.decimal_value_to_str(object_velocity)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:OVELocity {param}')

	def get(self, objectIx=repcap.ObjectIx.Default) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:OVELocity \n
		Snippet: value: float = driver.source.regenerator.object.ovelocity.get(objectIx = repcap.ObjectIx.Default) \n
		Sets the speed of a moving object. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: object_velocity: float Range: 0.001 to 2E11, Unit: m/s"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:OVELocity?')
		return Conversions.str_to_float(response)
