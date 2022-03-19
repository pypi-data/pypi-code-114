from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Predefined:
	"""Predefined commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("predefined", core, parent)

	# noinspection PyTypeChecker
	def get_category(self) -> enums.FadDssUsrVehCat:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:RX:VEHicle:PREDefined:CATegory \n
		Snippet: value: enums.FadDssUsrVehCat = driver.source.fsimulator.dsSimulation.user.rx.vehicle.predefined.get_category() \n
		No command help available \n
			:return: veh_pred_cat: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:RX:VEHicle:PREDefined:CATegory?')
		return Conversions.str_to_scalar_enum(response, enums.FadDssUsrVehCat)

	def set_category(self, veh_pred_cat: enums.FadDssUsrVehCat) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:RX:VEHicle:PREDefined:CATegory \n
		Snippet: driver.source.fsimulator.dsSimulation.user.rx.vehicle.predefined.set_category(veh_pred_cat = enums.FadDssUsrVehCat.AIR) \n
		No command help available \n
			:param veh_pred_cat: No help available
		"""
		param = Conversions.enum_scalar_to_str(veh_pred_cat, enums.FadDssUsrVehCat)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:USER:RX:VEHicle:PREDefined:CATegory {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.FadDssVehTypeAll:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:RX:VEHicle:PREDefined:TYPE \n
		Snippet: value: enums.FadDssVehTypeAll = driver.source.fsimulator.dsSimulation.user.rx.vehicle.predefined.get_type_py() \n
		No command help available \n
			:return: veh_pred_type: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:RX:VEHicle:PREDefined:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FadDssVehTypeAll)

	def set_type_py(self, veh_pred_type: enums.FadDssVehTypeAll) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:RX:VEHicle:PREDefined:TYPE \n
		Snippet: driver.source.fsimulator.dsSimulation.user.rx.vehicle.predefined.set_type_py(veh_pred_type = enums.FadDssVehTypeAll.AHELicopter) \n
		No command help available \n
			:param veh_pred_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(veh_pred_type, enums.FadDssVehTypeAll)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:USER:RX:VEHicle:PREDefined:TYPE {param}')
