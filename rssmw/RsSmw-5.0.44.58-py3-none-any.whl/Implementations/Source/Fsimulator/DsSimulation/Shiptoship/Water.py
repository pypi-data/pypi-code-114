from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Water:
	"""Water commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("water", core, parent)

	# noinspection PyTypeChecker
	def get_surface(self) -> enums.FadDssS2SwatSurfType:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:WATer:SURFace \n
		Snippet: value: enums.FadDssS2SwatSurfType = driver.source.fsimulator.dsSimulation.shiptoship.water.get_surface() \n
		No command help available \n
			:return: water_surface: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:WATer:SURFace?')
		return Conversions.str_to_scalar_enum(response, enums.FadDssS2SwatSurfType)

	def set_surface(self, water_surface: enums.FadDssS2SwatSurfType) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:WATer:SURFace \n
		Snippet: driver.source.fsimulator.dsSimulation.shiptoship.water.set_surface(water_surface = enums.FadDssS2SwatSurfType.ROUGh) \n
		No command help available \n
			:param water_surface: No help available
		"""
		param = Conversions.enum_scalar_to_str(water_surface, enums.FadDssS2SwatSurfType)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:WATer:SURFace {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.FadDssS2SwatType:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:WATer:TYPE \n
		Snippet: value: enums.FadDssS2SwatType = driver.source.fsimulator.dsSimulation.shiptoship.water.get_type_py() \n
		No command help available \n
			:return: water_type: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:WATer:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FadDssS2SwatType)

	def set_type_py(self, water_type: enums.FadDssS2SwatType) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:WATer:TYPE \n
		Snippet: driver.source.fsimulator.dsSimulation.shiptoship.water.set_type_py(water_type = enums.FadDssS2SwatType.FRESh) \n
		No command help available \n
			:param water_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(water_type, enums.FadDssS2SwatType)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:WATer:TYPE {param}')
