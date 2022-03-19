from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tx:
	"""Tx commands group definition. 9 total commands, 6 Subgroups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tx", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_index_get', 'repcap_index_set', repcap.Index.Nr1)

	def repcap_index_set(self, index: repcap.Index) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Index.Default
		Default value after init: Index.Nr1"""
		self._cmd_group.set_repcap_enum_value(index)

	def repcap_index_get(self) -> repcap.Index:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

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
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:TX:PATTern \n
		Snippet: value: enums.AntMod3DaNtPattern = driver.source.fsimulator.mimo.antenna.tx.get_pattern() \n
		Sets the antenna pattern mode. \n
			:return: ant_tx_patt_descr: ISOtropic| USER| SEC3| SEC6| DIPole| DPISotripic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:TX:PATTern?')
		return Conversions.str_to_scalar_enum(response, enums.AntMod3DaNtPattern)

	def set_pattern(self, ant_tx_patt_descr: enums.AntMod3DaNtPattern) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:TX:PATTern \n
		Snippet: driver.source.fsimulator.mimo.antenna.tx.set_pattern(ant_tx_patt_descr = enums.AntMod3DaNtPattern.DIPole) \n
		Sets the antenna pattern mode. \n
			:param ant_tx_patt_descr: ISOtropic| USER| SEC3| SEC6| DIPole| DPISotripic
		"""
		param = Conversions.enum_scalar_to_str(ant_tx_patt_descr, enums.AntMod3DaNtPattern)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:TX:PATTern {param}')

	def clone(self) -> 'Tx':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tx(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
