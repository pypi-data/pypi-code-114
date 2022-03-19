from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Globale:
	"""Globale commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("globale", core, parent)

	def get_seed(self) -> int:
		"""SCPI: [SOURce<HW>]:FSIMulator:GLOBal:SEED \n
		Snippet: value: int = driver.source.fsimulator.globale.get_seed() \n
		This command enters the fading start seed. This value is global for the instrument. \n
			:return: seed: integer Range: 0 to 9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:GLOBal:SEED?')
		return Conversions.str_to_int(response)

	def set_seed(self, seed: int) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:GLOBal:SEED \n
		Snippet: driver.source.fsimulator.globale.set_seed(seed = 1) \n
		This command enters the fading start seed. This value is global for the instrument. \n
			:param seed: integer Range: 0 to 9
		"""
		param = Conversions.decimal_value_to_str(seed)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:GLOBal:SEED {param}')
