from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:IQ:DOHerty:MEASurement:[STATe] \n
		Snippet: value: bool = driver.source.iq.doherty.measurement.get_state() \n
		Query the calculation status of the PEP and Level values. \n
			:return: measure_validity: 1| ON| 0| OFF 1|ON PEP and Level output values are valid 0|OFF PEP and Level output values are in calculation In the user interface, you recognize this state if '---.--' is indicated.
		"""
		response = self._core.io.query_str('SOURce:IQ:DOHerty:MEASurement:STATe?')
		return Conversions.str_to_bool(response)
