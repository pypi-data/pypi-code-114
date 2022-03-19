from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ignore:
	"""Ignore commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ignore", core, parent)

	def get_rf_changes(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:IGNore:RFCHanges \n
		Snippet: value: bool = driver.source.fsimulator.ignore.get_rf_changes() \n
		This is a password-protected function. Unlock the protection level 1 to access it. See method RsSmw.System.Protect.State.
		set. Sets if frequency changes < 5% are ignored. This enables faster frequency hopping. \n
			:return: rf_changes: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:IGNore:RFCHanges?')
		return Conversions.str_to_bool(response)

	def set_rf_changes(self, rf_changes: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:IGNore:RFCHanges \n
		Snippet: driver.source.fsimulator.ignore.set_rf_changes(rf_changes = False) \n
		This is a password-protected function. Unlock the protection level 1 to access it. See method RsSmw.System.Protect.State.
		set. Sets if frequency changes < 5% are ignored. This enables faster frequency hopping. \n
			:param rf_changes: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(rf_changes)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:IGNore:RFCHanges {param}')
