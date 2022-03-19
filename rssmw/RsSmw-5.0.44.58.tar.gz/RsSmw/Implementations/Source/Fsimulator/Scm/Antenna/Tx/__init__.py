from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tx:
	"""Tx commands group definition. 8 total commands, 5 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tx", core, parent)

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
	def columns(self):
		"""columns commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_columns'):
			from .Columns import Columns
			self._columns = Columns(self._core, self._cmd_group)
		return self._columns

	@property
	def espacing(self):
		"""espacing commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_espacing'):
			from .Espacing import Espacing
			self._espacing = Espacing(self._core, self._cmd_group)
		return self._espacing

	@property
	def rows(self):
		"""rows commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rows'):
			from .Rows import Rows
			self._rows = Rows(self._core, self._cmd_group)
		return self._rows

	# noinspection PyTypeChecker
	def get_pattern(self) -> enums.AntMod3DaNtPattern:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:ANTenna:TX:PATTern \n
		Snippet: value: enums.AntMod3DaNtPattern = driver.source.fsimulator.scm.antenna.tx.get_pattern() \n
		Sets the antenna pattern mode. \n
			:return: pattern: ISOtropic| USER| SEC3| SEC6| DIPole| DPISotripic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:ANTenna:TX:PATTern?')
		return Conversions.str_to_scalar_enum(response, enums.AntMod3DaNtPattern)

	def set_pattern(self, pattern: enums.AntMod3DaNtPattern) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:ANTenna:TX:PATTern \n
		Snippet: driver.source.fsimulator.scm.antenna.tx.set_pattern(pattern = enums.AntMod3DaNtPattern.DIPole) \n
		Sets the antenna pattern mode. \n
			:param pattern: ISOtropic| USER| SEC3| SEC6| DIPole| DPISotripic
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.AntMod3DaNtPattern)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:ANTenna:TX:PATTern {param}')

	# noinspection PyTypeChecker
	def get_structure(self) -> enums.AntModStructure:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:ANTenna:TX:STRucture \n
		Snippet: value: enums.AntModStructure = driver.source.fsimulator.scm.antenna.tx.get_structure() \n
		Sets the antenna array structure. \n
			:return: antenna_struct: LIN| CROSS
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:ANTenna:TX:STRucture?')
		return Conversions.str_to_scalar_enum(response, enums.AntModStructure)

	def set_structure(self, antenna_struct: enums.AntModStructure) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:ANTenna:TX:STRucture \n
		Snippet: driver.source.fsimulator.scm.antenna.tx.set_structure(antenna_struct = enums.AntModStructure.CROSS) \n
		Sets the antenna array structure. \n
			:param antenna_struct: LIN| CROSS
		"""
		param = Conversions.enum_scalar_to_str(antenna_struct, enums.AntModStructure)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:ANTenna:TX:STRucture {param}')

	def clone(self) -> 'Tx':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tx(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
