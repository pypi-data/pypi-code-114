from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dwell:
	"""Dwell commands group definition. 4 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dwell", core, parent)

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ParameterSetMode:
		"""SCPI: [SOURce<HW>]:LIST:DWELl:MODE \n
		Snippet: value: enums.ParameterSetMode = driver.source.listPy.dwell.get_mode() \n
		Selects the dwell time mode. \n
			:return: dwell_mode: LIST| GLOBal LIST Uses the dwell time, specified in the data table for each value pair individually. GLOBal Uses a constant dwell time, set with command [:SOURcehw]:LIST:DWELl.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:DWELl:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ParameterSetMode)

	def set_mode(self, dwell_mode: enums.ParameterSetMode) -> None:
		"""SCPI: [SOURce<HW>]:LIST:DWELl:MODE \n
		Snippet: driver.source.listPy.dwell.set_mode(dwell_mode = enums.ParameterSetMode.GLOBal) \n
		Selects the dwell time mode. \n
			:param dwell_mode: LIST| GLOBal LIST Uses the dwell time, specified in the data table for each value pair individually. GLOBal Uses a constant dwell time, set with command [:SOURcehw]:LIST:DWELl.
		"""
		param = Conversions.enum_scalar_to_str(dwell_mode, enums.ParameterSetMode)
		self._core.io.write(f'SOURce<HwInstance>:LIST:DWELl:MODE {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:LIST:DWELl \n
		Snippet: value: float = driver.source.listPy.dwell.get_value() \n
		Sets the global dwell time. The instrument generates the signal with the frequency / power value pairs of ​​each list
		entry for that particular period. See also 'Significant parameters and functions'. \n
			:return: dwell: float Range: 0.5E-3 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:DWELl?')
		return Conversions.str_to_float(response)

	def set_value(self, dwell: float) -> None:
		"""SCPI: [SOURce<HW>]:LIST:DWELl \n
		Snippet: driver.source.listPy.dwell.set_value(dwell = 1.0) \n
		Sets the global dwell time. The instrument generates the signal with the frequency / power value pairs of ​​each list
		entry for that particular period. See also 'Significant parameters and functions'. \n
			:param dwell: float Range: 0.5E-3 to 100
		"""
		param = Conversions.decimal_value_to_str(dwell)
		self._core.io.write(f'SOURce<HwInstance>:LIST:DWELl {param}')

	def clone(self) -> 'Dwell':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dwell(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
