from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generator:
	"""Generator commands group definition. 12 total commands, 5 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	@property
	def const(self):
		"""const commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_const'):
			from .Const import Const
			self._const = Const(self._core, self._cmd_group)
		return self._const

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def gain(self):
		"""gain commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	def get_arbitrary(self) -> str:
		"""SCPI: TEST:BB:GENerator:ARBitrary \n
		Snippet: value: str = driver.test.bb.generator.get_arbitrary() \n
		No command help available \n
			:return: filename: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:ARBitrary?')
		return trim_str_response(response)

	def set_arbitrary(self, filename: str) -> None:
		"""SCPI: TEST:BB:GENerator:ARBitrary \n
		Snippet: driver.test.bb.generator.set_arbitrary(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'TEST:BB:GENerator:ARBitrary {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TestBbGenIqSour:
		"""SCPI: TEST:BB:GENerator:SOURce \n
		Snippet: value: enums.TestBbGenIqSour = driver.test.bb.generator.get_source() \n
		No command help available \n
			:return: iq_source: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TestBbGenIqSour)

	def set_source(self, iq_source: enums.TestBbGenIqSour) -> None:
		"""SCPI: TEST:BB:GENerator:SOURce \n
		Snippet: driver.test.bb.generator.set_source(iq_source = enums.TestBbGenIqSour.ARB) \n
		No command help available \n
			:param iq_source: No help available
		"""
		param = Conversions.enum_scalar_to_str(iq_source, enums.TestBbGenIqSour)
		self._core.io.write(f'TEST:BB:GENerator:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: TEST:BB:GENerator:STATe \n
		Snippet: value: bool = driver.test.bb.generator.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: TEST:BB:GENerator:STATe \n
		Snippet: driver.test.bb.generator.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TEST:BB:GENerator:STATe {param}')

	def clone(self) -> 'Generator':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Generator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
