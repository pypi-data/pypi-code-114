from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.Dvbt2ModeStreamAdapterPlpType, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:TYPE \n
		Snippet: driver.source.bb.t2Dvb.plp.typePy.set(type_py = enums.Dvbt2ModeStreamAdapterPlpType.COMMon, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the PLP type. The type depends on the number of PLPs in the setup. \n
			:param type_py: DT1| DT2| COMMon COMMon Common PLP of the PLP Group. Requires a multi-PLP setup, see [:SOURcehw]:BB:T2DVb:INPut:NPLP?. DT1 Data type 1. Fixed for a single-PLP setup. Configurable for a multi-PLP setup. DT2 Data type 2. Requires a multi-PLP setup.
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.Dvbt2ModeStreamAdapterPlpType)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Dvbt2ModeStreamAdapterPlpType:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:TYPE \n
		Snippet: value: enums.Dvbt2ModeStreamAdapterPlpType = driver.source.bb.t2Dvb.plp.typePy.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the PLP type. The type depends on the number of PLPs in the setup. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: type_py: DT1| DT2| COMMon COMMon Common PLP of the PLP Group. Requires a multi-PLP setup, see [:SOURcehw]:BB:T2DVb:INPut:NPLP?. DT1 Data type 1. Fixed for a single-PLP setup. Configurable for a multi-PLP setup. DT2 Data type 2. Requires a multi-PLP setup."""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2ModeStreamAdapterPlpType)
