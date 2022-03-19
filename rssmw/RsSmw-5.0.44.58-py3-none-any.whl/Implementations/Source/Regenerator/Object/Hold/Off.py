from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Off:
	"""Off commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("off", core, parent)

	def set(self, holdoff: float, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:HOLD:OFF \n
		Snippet: driver.source.regenerator.object.hold.off.set(holdoff = 1.0, objectIx = repcap.ObjectIx.Default) \n
		Enters a time delay form the simulation start time to the moment at that an object appears for the first time. \n
			:param holdoff: float Range: 0 to 35999.999, Unit: s
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.decimal_value_to_str(holdoff)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:HOLD:OFF {param}')

	def get(self, objectIx=repcap.ObjectIx.Default) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:HOLD:OFF \n
		Snippet: value: float = driver.source.regenerator.object.hold.off.get(objectIx = repcap.ObjectIx.Default) \n
		Enters a time delay form the simulation start time to the moment at that an object appears for the first time. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: holdoff: float Range: 0 to 35999.999, Unit: s"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:HOLD:OFF?')
		return Conversions.str_to_float(response)
