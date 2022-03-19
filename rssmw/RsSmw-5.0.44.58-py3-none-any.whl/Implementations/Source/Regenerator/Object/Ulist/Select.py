from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, user_list_select: str, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:ULISt:SELect \n
		Snippet: driver.source.regenerator.object.ulist.select.set(user_list_select = '1', objectIx = repcap.ObjectIx.Default) \n
		Loads the selected list from the default or the specified directory. Loaded are files with extension *.reg_list. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory.
			INTRO_CMD_HELP: The following applies POWer = RF output level + OFFSet, where: \n
			- Query the existing list with [:SOURce<hw>]:REGenerator:OBJect:ULISt:CATalog?
			- Apply the list with [:SOURce<hw>]:REGenerator:OBJect<ch>:ULISt:STATe \n
			:param user_list_select: 'filename' Filename or complete file path; file extension can be omitted
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.value_to_quoted_str(user_list_select)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:ULISt:SELect {param}')

	def get(self, objectIx=repcap.ObjectIx.Default) -> str:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:ULISt:SELect \n
		Snippet: value: str = driver.source.regenerator.object.ulist.select.get(objectIx = repcap.ObjectIx.Default) \n
		Loads the selected list from the default or the specified directory. Loaded are files with extension *.reg_list. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory.
			INTRO_CMD_HELP: The following applies POWer = RF output level + OFFSet, where: \n
			- Query the existing list with [:SOURce<hw>]:REGenerator:OBJect:ULISt:CATalog?
			- Apply the list with [:SOURce<hw>]:REGenerator:OBJect<ch>:ULISt:STATe \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: user_list_select: 'filename' Filename or complete file path; file extension can be omitted"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:ULISt:SELect?')
		return trim_str_response(response)
