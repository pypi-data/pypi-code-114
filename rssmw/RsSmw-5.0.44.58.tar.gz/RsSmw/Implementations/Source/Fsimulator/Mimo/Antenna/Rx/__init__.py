from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rx:
	"""Rx commands group definition. 9 total commands, 6 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rx", core, parent)

	@property
	def antenna(self):
		"""antenna commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import Antenna
			self._antenna = Antenna(self._core, self._cmd_group)
		return self._antenna

	@property
	def calc(self):
		"""calc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_calc'):
			from .Calc import Calc
			self._calc = Calc(self._core, self._cmd_group)
		return self._calc

	@property
	def column(self):
		"""column commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_column'):
			from .Column import Column
			self._column = Column(self._core, self._cmd_group)
		return self._column

	@property
	def espacing(self):
		"""espacing commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_espacing'):
			from .Espacing import Espacing
			self._espacing = Espacing(self._core, self._cmd_group)
		return self._espacing

	@property
	def polarization(self):
		"""polarization commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_polarization'):
			from .Polarization import Polarization
			self._polarization = Polarization(self._core, self._cmd_group)
		return self._polarization

	@property
	def rows(self):
		"""rows commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rows'):
			from .Rows import Rows
			self._rows = Rows(self._core, self._cmd_group)
		return self._rows

	# noinspection PyTypeChecker
	def get_pattern(self) -> enums.AntMod3DaNtPattern:
		"""SCPI: [SOURce]:FSIMulator:MIMO:ANTenna:RX:PATTern \n
		Snippet: value: enums.AntMod3DaNtPattern = driver.source.fsimulator.mimo.antenna.rx.get_pattern() \n
		Sets the antenna pattern mode. \n
			:return: ant_rx_patt_descr: No help available
		"""
		response = self._core.io.query_str('SOURce:FSIMulator:MIMO:ANTenna:RX:PATTern?')
		return Conversions.str_to_scalar_enum(response, enums.AntMod3DaNtPattern)

	def set_pattern(self, ant_rx_patt_descr: enums.AntMod3DaNtPattern) -> None:
		"""SCPI: [SOURce]:FSIMulator:MIMO:ANTenna:RX:PATTern \n
		Snippet: driver.source.fsimulator.mimo.antenna.rx.set_pattern(ant_rx_patt_descr = enums.AntMod3DaNtPattern.DIPole) \n
		Sets the antenna pattern mode. \n
			:param ant_rx_patt_descr: ISOtropic| USER| SEC3| SEC6| DIPole| DPISotripic
		"""
		param = Conversions.enum_scalar_to_str(ant_rx_patt_descr, enums.AntMod3DaNtPattern)
		self._core.io.write(f'SOURce:FSIMulator:MIMO:ANTenna:RX:PATTern {param}')

	def clone(self) -> 'Rx':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rx(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
