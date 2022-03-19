from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, user_list_state: bool, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:ULISt:STATe \n
		Snippet: driver.source.regenerator.object.ulist.state.set(user_list_state = False, objectIx = repcap.ObjectIx.Default) \n
		Enables the selected list.
			INTRO_CMD_HELP: The following applies POWer = RF output level + OFFSet, where: \n
			- Query the existing list with [:SOURce<hw>]:REGenerator:OBJect:ULISt:CATalog?
			- Load the list with [:SOURce<hw>]:REGenerator:OBJect<ch>:ULISt:SELect \n
			:param user_list_state: OFF| ON| 1| 0
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.bool_to_str(user_list_state)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:ULISt:STATe {param}')

	def get(self, objectIx=repcap.ObjectIx.Default) -> bool:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:ULISt:STATe \n
		Snippet: value: bool = driver.source.regenerator.object.ulist.state.get(objectIx = repcap.ObjectIx.Default) \n
		Enables the selected list.
			INTRO_CMD_HELP: The following applies POWer = RF output level + OFFSet, where: \n
			- Query the existing list with [:SOURce<hw>]:REGenerator:OBJect:ULISt:CATalog?
			- Load the list with [:SOURce<hw>]:REGenerator:OBJect<ch>:ULISt:SELect \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: user_list_state: OFF| ON| 1| 0"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:ULISt:STATe?')
		return Conversions.str_to_bool(response)
