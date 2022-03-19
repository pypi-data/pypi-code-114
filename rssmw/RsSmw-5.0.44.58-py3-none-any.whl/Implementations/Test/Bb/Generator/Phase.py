from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def get_qcomponent(self) -> float:
		"""SCPI: TEST:BB:GENerator:PHASe:Q \n
		Snippet: value: float = driver.test.bb.generator.phase.get_qcomponent() \n
		No command help available \n
			:return: test_gen_phase_q: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:PHASe:Q?')
		return Conversions.str_to_float(response)

	def set_qcomponent(self, test_gen_phase_q: float) -> None:
		"""SCPI: TEST:BB:GENerator:PHASe:Q \n
		Snippet: driver.test.bb.generator.phase.set_qcomponent(test_gen_phase_q = 1.0) \n
		No command help available \n
			:param test_gen_phase_q: No help available
		"""
		param = Conversions.decimal_value_to_str(test_gen_phase_q)
		self._core.io.write(f'TEST:BB:GENerator:PHASe:Q {param}')
