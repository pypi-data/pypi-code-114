from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Umotion:
	"""Umotion commands group definition. 24 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("umotion", core, parent)

	@property
	def csv(self):
		"""csv commands group. 6 Sub-classes, 8 commands."""
		if not hasattr(self, '_csv'):
			from .Csv import Csv
			self._csv = Csv(self._core, self._cmd_group)
		return self._csv

	# noinspection PyTypeChecker
	def get_format_py(self) -> enums.LogFmtSat:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:FORMat \n
		Snippet: value: enums.LogFmtSat = driver.source.bb.gnss.logging.category.umotion.get_format_py() \n
		Sets the file format in that the logged data is saved. \n
			:return: format_py: CSV
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.LogFmtSat)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:STATe \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.get_state() \n
		Enables the logging of the selected category. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:STATe \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.set_state(state = False) \n
		Enables the logging of the selected category. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:STATe {param}')

	# noinspection PyTypeChecker
	def get_step(self) -> enums.LogRes:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:STEP \n
		Snippet: value: enums.LogRes = driver.source.bb.gnss.logging.category.umotion.get_step() \n
		Sets the logging step. \n
			:return: resolution: R1S| R2S| R5S| R10S| R02S| R04S| R08S
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:STEP?')
		return Conversions.str_to_scalar_enum(response, enums.LogRes)

	def set_step(self, resolution: enums.LogRes) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:STEP \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.set_step(resolution = enums.LogRes.R02S) \n
		Sets the logging step. \n
			:param resolution: R1S| R2S| R5S| R10S| R02S| R04S| R08S
		"""
		param = Conversions.enum_scalar_to_str(resolution, enums.LogRes)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:STEP {param}')

	def clone(self) -> 'Umotion':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Umotion(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
