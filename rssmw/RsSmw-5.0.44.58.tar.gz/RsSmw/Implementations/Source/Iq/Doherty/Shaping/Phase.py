from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:PHASe:STATe \n
		Snippet: value: bool = driver.source.iq.doherty.shaping.phase.get_state() \n
		Enables/disables the power and phase corrections. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:SHAPing:PHASe:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:PHASe:STATe \n
		Snippet: driver.source.iq.doherty.shaping.phase.set_state(state = False) \n
		Enables/disables the power and phase corrections. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:SHAPing:PHASe:STATe {param}')
