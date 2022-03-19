from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ToEnd:
	"""ToEnd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("toEnd", core, parent)

	def get(self, objectIx=repcap.ObjectIx.Default) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:TIME:TOENd \n
		Snippet: value: float = driver.source.regenerator.object.time.toEnd.get(objectIx = repcap.ObjectIx.Default) \n
		Queries the time it takes that the object moves from its start to its end range position. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: time_to_end: float Range: 0 to 1E15, Unit: s"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:TIME:TOENd?')
		return Conversions.str_to_float(response)
