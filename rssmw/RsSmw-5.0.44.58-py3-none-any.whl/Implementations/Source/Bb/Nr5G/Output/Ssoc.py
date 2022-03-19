from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ssoc:
	"""Ssoc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssoc", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:SSOC:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.output.ssoc.get_state() \n
		If enabled, the subcarriers that use the same frequency as the center frequency of the baseband output are not
		transmitted. \n
			:return: sup_scon_opc_tr: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:OUTPut:SSOC:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, sup_scon_opc_tr: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:SSOC:STATe \n
		Snippet: driver.source.bb.nr5G.output.ssoc.set_state(sup_scon_opc_tr = False) \n
		If enabled, the subcarriers that use the same frequency as the center frequency of the baseband output are not
		transmitted. \n
			:param sup_scon_opc_tr: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(sup_scon_opc_tr)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:OUTPut:SSOC:STATe {param}')
