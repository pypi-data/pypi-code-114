from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Crate:
	"""Crate commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crate", core, parent)

	def get_variation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:CRATe:VARiation \n
		Snippet: value: float = driver.source.bb.w3Gpp.crate.get_variation() \n
		Sets the output chip rate. The chip rate entry changes the output clock and the modulation bandwidth, as well as the
		synchronization signals that are output. It does not affect the calculated chip sequence. \n
			:return: variation: float Range: 400 to 5E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:CRATe:VARiation?')
		return Conversions.str_to_float(response)

	def set_variation(self, variation: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:CRATe:VARiation \n
		Snippet: driver.source.bb.w3Gpp.crate.set_variation(variation = 1.0) \n
		Sets the output chip rate. The chip rate entry changes the output clock and the modulation bandwidth, as well as the
		synchronization signals that are output. It does not affect the calculated chip sequence. \n
			:param variation: float Range: 400 to 5E6
		"""
		param = Conversions.decimal_value_to_str(variation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:CRATe:VARiation {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.ChipRate:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:CRATe \n
		Snippet: value: enums.ChipRate = driver.source.bb.w3Gpp.crate.get_value() \n
		The command queries the set system chip rate. The output chip rate can be set with the command SOUR:BB:W3GP:CRAT:VAR. \n
			:return: crate: R3M8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:CRATe?')
		return Conversions.str_to_scalar_enum(response, enums.ChipRate)
