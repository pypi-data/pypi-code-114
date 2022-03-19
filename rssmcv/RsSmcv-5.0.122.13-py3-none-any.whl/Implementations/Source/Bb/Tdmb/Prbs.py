from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prbs:
	"""Prbs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prbs", core, parent)

	# noinspection PyTypeChecker
	def get_sequence(self) -> enums.TdmbSettingsPrbs:
		"""SCPI: [SOURce<HW>]:BB:TDMB:PRBS:[SEQuence] \n
		Snippet: value: enums.TdmbSettingsPrbs = driver.source.bb.tdmb.prbs.get_sequence() \n
		Sets the test signal sequence, that is transmitted in the subchannel. You can select a PRBS 15, PRBS 20 and PRBS 23
		sequence as specified by . Also you can define a sequence of zeroes (0x00) . This setting takes effect, if special
		settings are active: SOURce1:BB:TDMB:SPECial:SETTings:STATe 1 \n
			:return: prbs: P15_1| P20_1| ZERO| P23_1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDMB:PRBS:SEQuence?')
		return Conversions.str_to_scalar_enum(response, enums.TdmbSettingsPrbs)

	def set_sequence(self, prbs: enums.TdmbSettingsPrbs) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDMB:PRBS:[SEQuence] \n
		Snippet: driver.source.bb.tdmb.prbs.set_sequence(prbs = enums.TdmbSettingsPrbs.P15_1) \n
		Sets the test signal sequence, that is transmitted in the subchannel. You can select a PRBS 15, PRBS 20 and PRBS 23
		sequence as specified by . Also you can define a sequence of zeroes (0x00) . This setting takes effect, if special
		settings are active: SOURce1:BB:TDMB:SPECial:SETTings:STATe 1 \n
			:param prbs: P15_1| P20_1| ZERO| P23_1
		"""
		param = Conversions.enum_scalar_to_str(prbs, enums.TdmbSettingsPrbs)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDMB:PRBS:SEQuence {param}')
