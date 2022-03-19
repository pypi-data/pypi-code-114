from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Diagram:
	"""Diagram commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("diagram", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.RegPrevDiagrType:
		"""SCPI: [SOURce<HW>]:REGenerator:DIAGram:TYPE \n
		Snippet: value: enums.RegPrevDiagrType = driver.source.regenerator.diagram.get_type_py() \n
		Sets the diagram type. \n
			:return: type_py: VELocity| POWer
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:DIAGram:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.RegPrevDiagrType)

	def set_type_py(self, type_py: enums.RegPrevDiagrType) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:DIAGram:TYPE \n
		Snippet: driver.source.regenerator.diagram.set_type_py(type_py = enums.RegPrevDiagrType.POLar) \n
		Sets the diagram type. \n
			:param type_py: VELocity| POWer
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.RegPrevDiagrType)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:DIAGram:TYPE {param}')
