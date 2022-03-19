from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Name:
	"""Name commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("name", core, parent)

	def set(self, name: str, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:NAME \n
		Snippet: driver.source.regenerator.object.name.set(name = '1', objectIx = repcap.ObjectIx.Default) \n
		Enter a symbolic name. \n
			:param name: string
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.value_to_quoted_str(name)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:NAME {param}')

	def get(self, objectIx=repcap.ObjectIx.Default) -> str:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:NAME \n
		Snippet: value: str = driver.source.regenerator.object.name.get(objectIx = repcap.ObjectIx.Default) \n
		Enter a symbolic name. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: name: string"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:NAME?')
		return trim_str_response(response)
