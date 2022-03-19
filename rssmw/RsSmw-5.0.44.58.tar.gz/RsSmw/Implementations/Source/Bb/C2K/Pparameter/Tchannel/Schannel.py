from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Schannel:
	"""Schannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("schannel", core, parent)

	def get_count(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:C2K:PPARameter:TCHannel:SCHannel:COUNt \n
		Snippet: value: int = driver.source.bb.c2K.pparameter.tchannel.schannel.get_count() \n
		Sets the number of supplemental channels. The maximum number of supplemental channels depends on the selected radio
		configuration. The setting takes effect only after execution of command [:SOURce<hw>]:BB:C2K:PPARameter:EXECute. It is
		specific for the selected radio configuration. \n
			:return: count: integer Range: 0 to 7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:PPARameter:TCHannel:SCHannel:COUNt?')
		return Conversions.str_to_int(response)

	def set_count(self, count: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:PPARameter:TCHannel:SCHannel:COUNt \n
		Snippet: driver.source.bb.c2K.pparameter.tchannel.schannel.set_count(count = 1) \n
		Sets the number of supplemental channels. The maximum number of supplemental channels depends on the selected radio
		configuration. The setting takes effect only after execution of command [:SOURce<hw>]:BB:C2K:PPARameter:EXECute. It is
		specific for the selected radio configuration. \n
			:param count: integer Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:PPARameter:TCHannel:SCHannel:COUNt {param}')
