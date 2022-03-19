from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vcc:
	"""Vcc commands group definition. 5 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vcc", core, parent)

	@property
	def value(self):
		"""value commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_value'):
			from .Value import Value
			self._value = Value(self._core, self._cmd_group)
		return self._value

	def get_max(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:VCC:MAX \n
		Snippet: value: float = driver.source.iq.output.analog.envelope.vcc.get_max() \n
		Sets the maximum value of the supply voltage Vcc. \n
			:return: vcc_max: float Range: 0.04 to 8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:VCC:MAX?')
		return Conversions.str_to_float(response)

	def set_max(self, vcc_max: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:VCC:MAX \n
		Snippet: driver.source.iq.output.analog.envelope.vcc.set_max(vcc_max = 1.0) \n
		Sets the maximum value of the supply voltage Vcc. \n
			:param vcc_max: float Range: 0.04 to 8
		"""
		param = Conversions.decimal_value_to_str(vcc_max)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:VCC:MAX {param}')

	def get_min(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:VCC:MIN \n
		Snippet: value: float = driver.source.iq.output.analog.envelope.vcc.get_min() \n
		Sets the maximum value of the supply voltage Vcc. \n
			:return: vcc_min: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:VCC:MIN?')
		return Conversions.str_to_float(response)

	def set_min(self, vcc_min: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:VCC:MIN \n
		Snippet: driver.source.iq.output.analog.envelope.vcc.set_min(vcc_min = 1.0) \n
		Sets the maximum value of the supply voltage Vcc. \n
			:param vcc_min: float Range: 0.04 to 8
		"""
		param = Conversions.decimal_value_to_str(vcc_min)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:VCC:MIN {param}')

	def get_offset(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:VCC:OFFSet \n
		Snippet: value: float = driver.source.iq.output.analog.envelope.vcc.get_offset() \n
		Applies a voltage offset on the supply voltage Vcc. \n
			:return: vcc_offset: float Range: 0 to 30, Unit: mV
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:VCC:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, vcc_offset: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:VCC:OFFSet \n
		Snippet: driver.source.iq.output.analog.envelope.vcc.set_offset(vcc_offset = 1.0) \n
		Applies a voltage offset on the supply voltage Vcc. \n
			:param vcc_offset: float Range: 0 to 30, Unit: mV
		"""
		param = Conversions.decimal_value_to_str(vcc_offset)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:VCC:OFFSet {param}')

	def clone(self) -> 'Vcc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Vcc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
