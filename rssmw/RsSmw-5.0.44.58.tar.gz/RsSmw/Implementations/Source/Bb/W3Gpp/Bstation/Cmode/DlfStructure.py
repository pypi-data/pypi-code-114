from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DlfStructure:
	"""DlfStructure commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dlfStructure", core, parent)

	def set(self, dlf_structure: enums.MappingType, baseStation=repcap.BaseStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CMODe:DLFStructure \n
		Snippet: driver.source.bb.w3Gpp.bstation.cmode.dlfStructure.set(dlf_structure = enums.MappingType.A, baseStation = repcap.BaseStation.Default) \n
		The command selects the frame structure. The frame structure determines the transmission of TPC and pilot field in the
		transmission gaps. \n
			:param dlf_structure: A| B A Type A, the pilot field is sent in the last slot of each transmission gap. B Type B, the pilot field is sent in the last slot of each transmission gap. The first TPC field of the transmission gap is sent in addition.
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
		"""
		param = Conversions.enum_scalar_to_str(dlf_structure, enums.MappingType)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CMODe:DLFStructure {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default) -> enums.MappingType:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CMODe:DLFStructure \n
		Snippet: value: enums.MappingType = driver.source.bb.w3Gpp.bstation.cmode.dlfStructure.get(baseStation = repcap.BaseStation.Default) \n
		The command selects the frame structure. The frame structure determines the transmission of TPC and pilot field in the
		transmission gaps. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: dlf_structure: A| B A Type A, the pilot field is sent in the last slot of each transmission gap. B Type B, the pilot field is sent in the last slot of each transmission gap. The first TPC field of the transmission gap is sent in addition."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CMODe:DLFStructure?')
		return Conversions.str_to_scalar_enum(response, enums.MappingType)
