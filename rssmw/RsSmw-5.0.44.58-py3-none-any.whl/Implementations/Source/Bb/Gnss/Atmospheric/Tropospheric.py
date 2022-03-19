from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tropospheric:
	"""Tropospheric commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tropospheric", core, parent)

	# noinspection PyTypeChecker
	def get_model(self) -> enums.TropModel:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:TROPospheric:MODel \n
		Snippet: value: enums.TropModel = driver.source.bb.gnss.atmospheric.tropospheric.get_model() \n
		Determines the tropospheric model. \n
			:return: model: NONE| STANag| MOPS
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ATMospheric:TROPospheric:MODel?')
		return Conversions.str_to_scalar_enum(response, enums.TropModel)

	def set_model(self, model: enums.TropModel) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:TROPospheric:MODel \n
		Snippet: driver.source.bb.gnss.atmospheric.tropospheric.set_model(model = enums.TropModel.MOPS) \n
		Determines the tropospheric model. \n
			:param model: NONE| STANag| MOPS
		"""
		param = Conversions.enum_scalar_to_str(model, enums.TropModel)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:TROPospheric:MODel {param}')
