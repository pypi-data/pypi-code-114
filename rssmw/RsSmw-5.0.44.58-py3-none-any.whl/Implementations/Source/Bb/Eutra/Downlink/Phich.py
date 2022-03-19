from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phich:
	"""Phich commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phich", core, parent)

	# noinspection PyTypeChecker
	def get_duration(self) -> enums.EuTraDuration:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PHICh:DURation \n
		Snippet: value: enums.EuTraDuration = driver.source.bb.eutra.downlink.phich.get_duration() \n
		No command help available \n
			:return: duration: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PHICh:DURation?')
		return Conversions.str_to_scalar_enum(response, enums.EuTraDuration)

	def set_duration(self, duration: enums.EuTraDuration) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PHICh:DURation \n
		Snippet: driver.source.bb.eutra.downlink.phich.set_duration(duration = enums.EuTraDuration.EXTended) \n
		No command help available \n
			:param duration: No help available
		"""
		param = Conversions.enum_scalar_to_str(duration, enums.EuTraDuration)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PHICh:DURation {param}')

	# noinspection PyTypeChecker
	def get_ng_parameter(self) -> enums.PhichNg:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PHICh:NGParameter \n
		Snippet: value: enums.PhichNg = driver.source.bb.eutra.downlink.phich.get_ng_parameter() \n
		No command help available \n
			:return: ng_parameter: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:PHICh:NGParameter?')
		return Conversions.str_to_scalar_enum(response, enums.PhichNg)

	def set_ng_parameter(self, ng_parameter: enums.PhichNg) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:PHICh:NGParameter \n
		Snippet: driver.source.bb.eutra.downlink.phich.set_ng_parameter(ng_parameter = enums.PhichNg.NG1) \n
		No command help available \n
			:param ng_parameter: No help available
		"""
		param = Conversions.enum_scalar_to_str(ng_parameter, enums.PhichNg)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:PHICh:NGParameter {param}')
