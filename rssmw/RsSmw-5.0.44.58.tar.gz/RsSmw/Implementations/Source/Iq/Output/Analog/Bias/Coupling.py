from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coupling:
	"""Coupling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupling", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:BIAS:COUPling:[STATe] \n
		Snippet: value: bool = driver.source.iq.output.analog.bias.coupling.get_state() \n
		Couples the bias setting of the I and Q signal components. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:BIAS:COUPling:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:BIAS:COUPling:[STATe] \n
		Snippet: driver.source.iq.output.analog.bias.coupling.set_state(state = False) \n
		Couples the bias setting of the I and Q signal components. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:BIAS:COUPling:STATe {param}')
