from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Store:
	"""Store commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("store", core, parent)

	def set(self, filename: str, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:STORe \n
		Snippet: driver.source.regenerator.object.store.set(filename = '1', objectIx = repcap.ObjectIx.Default) \n
		Stores the current settings into the selected file; the file extension (*.reg_obj) is assigned automatically. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param filename: string
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.value_to_quoted_str(filename)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:STORe {param}')
