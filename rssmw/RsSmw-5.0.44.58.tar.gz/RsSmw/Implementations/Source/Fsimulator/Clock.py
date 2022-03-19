from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clock:
	"""Clock commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clock", core, parent)

	# noinspection PyTypeChecker
	def get_rate(self) -> enums.BbClock:
		"""SCPI: [SOURce<HW>]:FSIMulator:CLOCk:RATE \n
		Snippet: value: enums.BbClock = driver.source.fsimulator.clock.get_rate() \n
		Queries the clock rate the fading simulator is using for the signal processing. \n
			:return: cloc_rate: CR200| CR100| CR050| CR025 | CR250| CR125| CR062| CR500| CR1G CR200 = 200 MHz, CR100 = 100 MHz, CR050 = 50 MHz, CR025 = 25 MHz CR250 = 250 MHz, CR125 = 125 MHz, CR062 = 62.5 MHz, CR500 = 500 MHz, CR1G = 1GHz The value depends on the selected 'System Configuration' and influences the bandwidth of the generated signal. *) CR200M (R&S SMW-B10) /CR250M (R&S SMW-B9)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:CLOCk:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.BbClock)
