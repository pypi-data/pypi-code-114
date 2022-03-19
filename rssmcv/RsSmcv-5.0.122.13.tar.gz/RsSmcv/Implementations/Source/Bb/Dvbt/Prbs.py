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
	def get_sequence(self) -> enums.SettingsPrbs:
		"""SCPI: [SOURce<HW>]:BB:DVBT:PRBS:[SEQuence] \n
		Snippet: value: enums.SettingsPrbs = driver.source.bb.dvbt.prbs.get_sequence() \n
		Sets the length of the PRBS sequence. You can select a PRBS 15 or a PRBS 23 sequence as specified by . \n
			:return: prbs: P15_1| P23_1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:PRBS:SEQuence?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsPrbs)

	def set_sequence(self, prbs: enums.SettingsPrbs) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:PRBS:[SEQuence] \n
		Snippet: driver.source.bb.dvbt.prbs.set_sequence(prbs = enums.SettingsPrbs.P15_1) \n
		Sets the length of the PRBS sequence. You can select a PRBS 15 or a PRBS 23 sequence as specified by . \n
			:param prbs: P15_1| P23_1
		"""
		param = Conversions.enum_scalar_to_str(prbs, enums.SettingsPrbs)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:PRBS:SEQuence {param}')
