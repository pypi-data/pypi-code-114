from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coding:
	"""Coding commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coding", core, parent)

	# noinspection PyTypeChecker
	def get_rate(self) -> enums.WlanadCodRate:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:CODing:RATE \n
		Snippet: value: enums.WlanadCodRate = driver.source.bb.wlad.pconfig.coding.get_rate() \n
		Sets the coding rate. \n
			:return: rate: CR1D2| CR3D4| CR5D8| CR13D14| CR13D16| CR13D21| CR13D28| CR52D63| CR7D8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:CODing:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.WlanadCodRate)

	def set_rate(self, rate: enums.WlanadCodRate) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:CODing:RATE \n
		Snippet: driver.source.bb.wlad.pconfig.coding.set_rate(rate = enums.WlanadCodRate.CR13D14) \n
		Sets the coding rate. \n
			:param rate: CR1D2| CR3D4| CR5D8| CR13D14| CR13D16| CR13D21| CR13D28| CR52D63| CR7D8
		"""
		param = Conversions.enum_scalar_to_str(rate, enums.WlanadCodRate)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:CODing:RATE {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.WlanadChCod:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:CODing:TYPE \n
		Snippet: value: enums.WlanadChCod = driver.source.bb.wlad.pconfig.coding.get_type_py() \n
		No command help available \n
			:return: type_py: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:CODing:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.WlanadChCod)

	def set_type_py(self, type_py: enums.WlanadChCod) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:CODing:TYPE \n
		Snippet: driver.source.bb.wlad.pconfig.coding.set_type_py(type_py = enums.WlanadChCod.LDPC) \n
		No command help available \n
			:param type_py: No help available
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.WlanadChCod)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:CODing:TYPE {param}')
