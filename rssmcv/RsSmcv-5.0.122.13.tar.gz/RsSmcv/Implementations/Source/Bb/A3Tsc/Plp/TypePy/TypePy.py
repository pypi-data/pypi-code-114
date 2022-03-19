from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.Atsc30Type, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TYPE:TYPE \n
		Snippet: driver.source.bb.a3Tsc.plp.typePy.typePy.set(type_py = enums.Atsc30Type.DISPersed, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the type if the PLP is not an enhanced layer. \n
			:param type_py: DISPersed| NONDispersed
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.Atsc30Type)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TYPE:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Atsc30Type:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:TYPE:TYPE \n
		Snippet: value: enums.Atsc30Type = driver.source.bb.a3Tsc.plp.typePy.typePy.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the type if the PLP is not an enhanced layer. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: type_py: DISPersed| NONDispersed"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:TYPE:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30Type)
