from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pratio:
	"""Pratio commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pratio", core, parent)

	def get_horizontal(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:POLarization:PRATio:HORizontal \n
		Snippet: value: float = driver.source.fsimulator.scm.polarization.pratio.get_horizontal() \n
		Sets the cross polarization power ratio (XPR) in dB. \n
			:return: ratio_horizontal: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:POLarization:PRATio:HORizontal?')
		return Conversions.str_to_float(response)

	def set_horizontal(self, ratio_horizontal: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:POLarization:PRATio:HORizontal \n
		Snippet: driver.source.fsimulator.scm.polarization.pratio.set_horizontal(ratio_horizontal = 1.0) \n
		Sets the cross polarization power ratio (XPR) in dB. \n
			:param ratio_horizontal: float Range: 0 to 20
		"""
		param = Conversions.decimal_value_to_str(ratio_horizontal)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:POLarization:PRATio:HORizontal {param}')

	def get_vertical(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:POLarization:PRATio:VERTical \n
		Snippet: value: float = driver.source.fsimulator.scm.polarization.pratio.get_vertical() \n
		Sets the cross polarization power ratio (XPR) in dB. \n
			:return: ratio_vertical: float Range: 0 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:POLarization:PRATio:VERTical?')
		return Conversions.str_to_float(response)

	def set_vertical(self, ratio_vertical: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:POLarization:PRATio:VERTical \n
		Snippet: driver.source.fsimulator.scm.polarization.pratio.set_vertical(ratio_vertical = 1.0) \n
		Sets the cross polarization power ratio (XPR) in dB. \n
			:param ratio_vertical: float Range: 0 to 20
		"""
		param = Conversions.decimal_value_to_str(ratio_vertical)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:POLarization:PRATio:VERTical {param}')
