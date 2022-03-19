from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Opf:
	"""Opf commands group definition. 71 total commands, 24 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("opf", core, parent)

	@property
	def apply(self):
		"""apply commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import Apply
			self._apply = Apply(self._core, self._cmd_group)
		return self._apply

	@property
	def g10B(self):
		"""g10B commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g10B'):
			from .G10B import G10B
			self._g10B = G10B(self._core, self._cmd_group)
		return self._g10B

	@property
	def g11A(self):
		"""g11A commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g11A'):
			from .G11A import G11A
			self._g11A = G11A(self._core, self._cmd_group)
		return self._g11A

	@property
	def g11B(self):
		"""g11B commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g11B'):
			from .G11B import G11B
			self._g11B = G11B(self._core, self._cmd_group)
		return self._g11B

	@property
	def g12A(self):
		"""g12A commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g12A'):
			from .G12A import G12A
			self._g12A = G12A(self._core, self._cmd_group)
		return self._g12A

	@property
	def g12B(self):
		"""g12B commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g12B'):
			from .G12B import G12B
			self._g12B = G12B(self._core, self._cmd_group)
		return self._g12B

	@property
	def g13A(self):
		"""g13A commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g13A'):
			from .G13A import G13A
			self._g13A = G13A(self._core, self._cmd_group)
		return self._g13A

	@property
	def g13B(self):
		"""g13B commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g13B'):
			from .G13B import G13B
			self._g13B = G13B(self._core, self._cmd_group)
		return self._g13B

	@property
	def g15A(self):
		"""g15A commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g15A'):
			from .G15A import G15A
			self._g15A = G15A(self._core, self._cmd_group)
		return self._g15A

	@property
	def g1A(self):
		"""g1A commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g1A'):
			from .G1A import G1A
			self._g1A = G1A(self._core, self._cmd_group)
		return self._g1A

	@property
	def g1B(self):
		"""g1B commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g1B'):
			from .G1B import G1B
			self._g1B = G1B(self._core, self._cmd_group)
		return self._g1B

	@property
	def g3A(self):
		"""g3A commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g3A'):
			from .G3A import G3A
			self._g3A = G3A(self._core, self._cmd_group)
		return self._g3A

	@property
	def g3B(self):
		"""g3B commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g3B'):
			from .G3B import G3B
			self._g3B = G3B(self._core, self._cmd_group)
		return self._g3B

	@property
	def g4B(self):
		"""g4B commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g4B'):
			from .G4B import G4B
			self._g4B = G4B(self._core, self._cmd_group)
		return self._g4B

	@property
	def g5A(self):
		"""g5A commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g5A'):
			from .G5A import G5A
			self._g5A = G5A(self._core, self._cmd_group)
		return self._g5A

	@property
	def g5B(self):
		"""g5B commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g5B'):
			from .G5B import G5B
			self._g5B = G5B(self._core, self._cmd_group)
		return self._g5B

	@property
	def g6A(self):
		"""g6A commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g6A'):
			from .G6A import G6A
			self._g6A = G6A(self._core, self._cmd_group)
		return self._g6A

	@property
	def g6B(self):
		"""g6B commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g6B'):
			from .G6B import G6B
			self._g6B = G6B(self._core, self._cmd_group)
		return self._g6B

	@property
	def g7A(self):
		"""g7A commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g7A'):
			from .G7A import G7A
			self._g7A = G7A(self._core, self._cmd_group)
		return self._g7A

	@property
	def g7B(self):
		"""g7B commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g7B'):
			from .G7B import G7B
			self._g7B = G7B(self._core, self._cmd_group)
		return self._g7B

	@property
	def g8A(self):
		"""g8A commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g8A'):
			from .G8A import G8A
			self._g8A = G8A(self._core, self._cmd_group)
		return self._g8A

	@property
	def g8B(self):
		"""g8B commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g8B'):
			from .G8B import G8B
			self._g8B = G8B(self._core, self._cmd_group)
		return self._g8B

	@property
	def g9A(self):
		"""g9A commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g9A'):
			from .G9A import G9A
			self._g9A = G9A(self._core, self._cmd_group)
		return self._g9A

	@property
	def g9B(self):
		"""g9B commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_g9B'):
			from .G9B import G9B
			self._g9B = G9B(self._core, self._cmd_group)
		return self._g9B

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:OPF:[STATe] \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.opf.get_state() \n
		Enables the open format. \n
			:return: open_format_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:OPF:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, open_format_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:OPF:[STATe] \n
		Snippet: driver.source.bb.radio.fm.rds.opf.set_state(open_format_state = False) \n
		Enables the open format. \n
			:param open_format_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(open_format_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:OPF:STATe {param}')

	def clone(self) -> 'Opf':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Opf(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
