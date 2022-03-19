from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 11 total commands, 4 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("carrier", core, parent)

	@property
	def delay(self):
		"""delay commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import Delay
			self._delay = Delay(self._core, self._cmd_group)
		return self._delay

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	def get_file(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:FILE \n
		Snippet: value: str = driver.source.bb.arbitrary.mcarrier.edit.carrier.get_file() \n
		Selects the input file. The data of the file are modulated onto the carriers in the defined carrier range. \n
			:return: file: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:FILE?')
		return trim_str_response(response)

	def set_file(self, file: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:FILE \n
		Snippet: driver.source.bb.arbitrary.mcarrier.edit.carrier.set_file(file = '1') \n
		Selects the input file. The data of the file are modulated onto the carriers in the defined carrier range. \n
			:param file: string
		"""
		param = Conversions.value_to_quoted_str(file)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:FILE {param}')

	def get_start(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:STARt \n
		Snippet: value: int = driver.source.bb.arbitrary.mcarrier.edit.carrier.get_start() \n
		Selects the last carrier in the carrier range to which the settings shall apply. \n
			:return: start: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, start: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:STARt \n
		Snippet: driver.source.bb.arbitrary.mcarrier.edit.carrier.set_start(start = 1) \n
		Selects the last carrier in the carrier range to which the settings shall apply. \n
			:param start: integer Range: 0 to 511
		"""
		param = Conversions.decimal_value_to_str(start)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:STARt {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:STATe \n
		Snippet: value: bool = driver.source.bb.arbitrary.mcarrier.edit.carrier.get_state() \n
		Switches all the carriers in the selected carrier range on or off. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:STATe \n
		Snippet: driver.source.bb.arbitrary.mcarrier.edit.carrier.set_state(state = False) \n
		Switches all the carriers in the selected carrier range on or off. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:STATe {param}')

	def get_stop(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:STOP \n
		Snippet: value: int = driver.source.bb.arbitrary.mcarrier.edit.carrier.get_stop() \n
		Selects the last carrier in the carrier range to which the settings shall apply. \n
			:return: stop: integer Range: 0 to 511
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:STOP?')
		return Conversions.str_to_int(response)

	def set_stop(self, stop: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:EDIT:CARRier:STOP \n
		Snippet: driver.source.bb.arbitrary.mcarrier.edit.carrier.set_stop(stop = 1) \n
		Selects the last carrier in the carrier range to which the settings shall apply. \n
			:param stop: integer Range: 0 to 511
		"""
		param = Conversions.decimal_value_to_str(stop)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:EDIT:CARRier:STOP {param}')

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
