from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:VCC:VALue:LEVel \n
		Snippet: value: float = driver.source.iq.output.analog.envelope.vcc.value.get_level() \n
		Queries the Vcc value of the current RMS power level (operating point) . \n
			:return: vcc_for_rf_level: float Range: 0 to 38
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:VCC:VALue:LEVel?')
		return Conversions.str_to_float(response)

	def get_pep(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:VCC:VALue:PEP \n
		Snippet: value: float = driver.source.iq.output.analog.envelope.vcc.value.get_pep() \n
		Queries the Vcc value of the current PEP of the generated RF signal. \n
			:return: vcc_for_crt_pep: float Range: 0 to 38
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:VCC:VALue:PEP?')
		return Conversions.str_to_float(response)
