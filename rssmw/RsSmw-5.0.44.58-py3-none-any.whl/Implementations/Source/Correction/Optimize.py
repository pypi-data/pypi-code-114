from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Optimize:
	"""Optimize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("optimize", core, parent)

	def get_evm(self) -> bool:
		"""SCPI: [SOURce<HW>]:CORRection:OPTimize:EVM \n
		Snippet: value: bool = driver.source.correction.optimize.get_evm() \n
		Activates further optimization of preexisting excellent EVM performance of I/Q modulated RF signals.
		Activate EVM optimization, if your test setup requires lowest EVM values. For example, if you need to generate 5G NR
		signals, LTE signals or IEEE 802.11 signals that require optimal EVM performance. \n
			:return: optimize_evm: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:OPTimize:EVM?')
		return Conversions.str_to_bool(response)

	def set_evm(self, optimize_evm: bool) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:OPTimize:EVM \n
		Snippet: driver.source.correction.optimize.set_evm(optimize_evm = False) \n
		Activates further optimization of preexisting excellent EVM performance of I/Q modulated RF signals.
		Activate EVM optimization, if your test setup requires lowest EVM values. For example, if you need to generate 5G NR
		signals, LTE signals or IEEE 802.11 signals that require optimal EVM performance. \n
			:param optimize_evm: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(optimize_evm)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:OPTimize:EVM {param}')
