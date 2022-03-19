from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 17 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	@property
	def parameter(self):
		"""parameter commands group. 2 Sub-classes, 8 commands."""
		if not hasattr(self, '_parameter'):
			from .Parameter import Parameter
			self._parameter = Parameter(self._core, self._cmd_group)
		return self._parameter

	def get_auto(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:FILTer:AUTO \n
		Snippet: value: bool = driver.source.bb.v5G.filterPy.get_auto() \n
		No command help available \n
			:return: auto: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:FILTer:AUTO?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FiltOptMode:
		"""SCPI: [SOURce<HW>]:BB:V5G:FILTer:MODE \n
		Snippet: value: enums.FiltOptMode = driver.source.bb.v5G.filterPy.get_mode() \n
		No command help available \n
			:return: opt_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:FILTer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FiltOptMode)

	def set_mode(self, opt_mode: enums.FiltOptMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:FILTer:MODE \n
		Snippet: driver.source.bb.v5G.filterPy.set_mode(opt_mode = enums.FiltOptMode.OFFLine) \n
		No command help available \n
			:param opt_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(opt_mode, enums.FiltOptMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:FILTer:MODE {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.DmFilterEutra:
		"""SCPI: [SOURce<HW>]:BB:V5G:FILTer:TYPE \n
		Snippet: value: enums.DmFilterEutra = driver.source.bb.v5G.filterPy.get_type_py() \n
		No command help available \n
			:return: type_py: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:FILTer:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.DmFilterEutra)

	def set_type_py(self, type_py: enums.DmFilterEutra) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:FILTer:TYPE \n
		Snippet: driver.source.bb.v5G.filterPy.set_type_py(type_py = enums.DmFilterEutra.APCO25) \n
		No command help available \n
			:param type_py: No help available
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.DmFilterEutra)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:FILTer:TYPE {param}')

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
