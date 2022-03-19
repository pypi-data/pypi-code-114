from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Direction:
	"""Direction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("direction", core, parent)

	def set(self, direction: enums.RegObjDir, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:DIRection \n
		Snippet: driver.source.regenerator.object.direction.set(direction = enums.RegObjDir.APPRoaching, objectIx = repcap.ObjectIx.Default) \n
		Sets the object direction of a static+moving object. \n
			:param direction: APPRoaching| DEParting
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.enum_scalar_to_str(direction, enums.RegObjDir)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:DIRection {param}')

	# noinspection PyTypeChecker
	def get(self, objectIx=repcap.ObjectIx.Default) -> enums.RegObjDir:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:DIRection \n
		Snippet: value: enums.RegObjDir = driver.source.regenerator.object.direction.get(objectIx = repcap.ObjectIx.Default) \n
		Sets the object direction of a static+moving object. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: direction: APPRoaching| DEParting"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:DIRection?')
		return Conversions.str_to_scalar_enum(response, enums.RegObjDir)
