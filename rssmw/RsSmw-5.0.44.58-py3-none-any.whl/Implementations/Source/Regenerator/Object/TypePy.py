from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.RegObjType, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:TYPE \n
		Snippet: driver.source.regenerator.object.typePy.set(type_py = enums.RegObjType.MOVing, objectIx = repcap.ObjectIx.Default) \n
		Sets the object type or disables it. \n
			:param type_py: OFF| STATic| MOVing| SMOVing
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.RegObjType)
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, objectIx=repcap.ObjectIx.Default) -> enums.RegObjType:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:TYPE \n
		Snippet: value: enums.RegObjType = driver.source.regenerator.object.typePy.get(objectIx = repcap.ObjectIx.Default) \n
		Sets the object type or disables it. \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: type_py: OFF| STATic| MOVing| SMOVing"""
		objectIx_cmd_val = self._cmd_group.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.RegObjType)
