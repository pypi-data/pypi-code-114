from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SimMode:
	"""SimMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("simMode", core, parent)

	def set(self, mode: enums.RegObjSimMode, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:SIMMode \n
		Snippet: driver.source.regenerator.object.simMode.set(mode = enums.RegObjSimMode.CYCLic, objectIx = repcap.ObjectIx.Default) \n
		Describes how the object moves. \n
			:param mode: ROUNdtrip| ONEWay| CYCLic
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.RegObjSimMode)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:SIMMode {param}')

	# noinspection PyTypeChecker
	def get(self, objectIx=repcap.ObjectIx.Default) -> enums.RegObjSimMode:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:SIMMode \n
		Snippet: value: enums.RegObjSimMode = driver.source.regenerator.object.simMode.get(objectIx = repcap.ObjectIx.Default) \n
		Describes how the object moves. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: mode: ROUNdtrip| ONEWay| CYCLic"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:SIMMode?')
		return Conversions.str_to_scalar_enum(response, enums.RegObjSimMode)
