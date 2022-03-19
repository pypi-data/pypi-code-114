from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dm:
	"""Dm commands group definition. 6 total commands, 5 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dm", core, parent)

	@property
	def audio(self):
		"""audio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_audio'):
			from .Audio import Audio
			self._audio = Audio(self._core, self._cmd_group)
		return self._audio

	@property
	def external(self):
		"""external commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_external'):
			from .External import External
			self._external = External(self._core, self._cmd_group)
		return self._external

	@property
	def filterPy(self):
		"""filterPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def polarity(self):
		"""polarity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_polarity'):
			from .Polarity import Polarity
			self._polarity = Polarity(self._core, self._cmd_group)
		return self._polarity

	@property
	def transmission(self):
		"""transmission commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_transmission'):
			from .Transmission import Transmission
			self._transmission = Transmission(self._core, self._cmd_group)
		return self._transmission

	# noinspection PyTypeChecker
	def get_source(self) -> enums.SfeBbType:
		"""SCPI: [SOURce]:DM:SOURce \n
		Snippet: value: enums.SfeBbType = driver.source.dm.get_source() \n
		No command help available \n
			:return: source: No help available
		"""
		response = self._core.io.query_str('SOURce:DM:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.SfeBbType)

	def set_source(self, source: enums.SfeBbType) -> None:
		"""SCPI: [SOURce]:DM:SOURce \n
		Snippet: driver.source.dm.set_source(source = enums.SfeBbType.AM) \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.enum_scalar_to_str(source, enums.SfeBbType)
		self._core.io.write(f'SOURce:DM:SOURce {param}')

	def clone(self) -> 'Dm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
