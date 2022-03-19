from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdd:
	"""Tdd commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdd", core, parent)

	def get_sps_conf(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TDD:SPSConf \n
		Snippet: value: int = driver.source.bb.oneweb.tdd.get_sps_conf() \n
		No command help available \n
			:return: spec_subfr_conf: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:TDD:SPSConf?')
		return Conversions.str_to_int(response)

	def set_sps_conf(self, spec_subfr_conf: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TDD:SPSConf \n
		Snippet: driver.source.bb.oneweb.tdd.set_sps_conf(spec_subfr_conf = 1) \n
		No command help available \n
			:param spec_subfr_conf: No help available
		"""
		param = Conversions.decimal_value_to_str(spec_subfr_conf)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:TDD:SPSConf {param}')

	def get_ud_conf(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TDD:UDConf \n
		Snippet: value: int = driver.source.bb.oneweb.tdd.get_ud_conf() \n
		No command help available \n
			:return: ul_dl_conf: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ONEWeb:TDD:UDConf?')
		return Conversions.str_to_int(response)

	def set_ud_conf(self, ul_dl_conf: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:TDD:UDConf \n
		Snippet: driver.source.bb.oneweb.tdd.set_ud_conf(ul_dl_conf = 1) \n
		No command help available \n
			:param ul_dl_conf: No help available
		"""
		param = Conversions.decimal_value_to_str(ul_dl_conf)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:TDD:UDConf {param}')
