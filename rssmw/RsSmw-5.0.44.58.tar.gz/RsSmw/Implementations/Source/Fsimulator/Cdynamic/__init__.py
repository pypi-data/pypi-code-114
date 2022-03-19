from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cdynamic:
	"""Cdynamic commands group definition. 7 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdynamic", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	@property
	def path(self):
		"""path commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_path'):
			from .Path import Path
			self._path = Path(self._core, self._cmd_group)
		return self._path

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:CDYNamic:DELete \n
		Snippet: driver.source.fsimulator.cdynamic.delete(filename = '1') \n
		Deletes the specified file. Deleted are user-defined files with file extension *.fad_udyn. \n
			:param filename: 'filename' Complete file path and file name; file extension can be omitted.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:CDYNamic:DELete {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:CDYNamic:STATe \n
		Snippet: value: bool = driver.source.fsimulator.cdynamic.get_state() \n
		Activates the customized dynamic fading configuration. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:CDYNamic:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:CDYNamic:STATe \n
		Snippet: driver.source.fsimulator.cdynamic.set_state(state = False) \n
		Activates the customized dynamic fading configuration. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:CDYNamic:STATe {param}')

	def clone(self) -> 'Cdynamic':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cdynamic(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
