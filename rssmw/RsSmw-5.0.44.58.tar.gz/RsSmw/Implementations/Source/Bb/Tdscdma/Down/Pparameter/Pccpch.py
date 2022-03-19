from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pccpch:
	"""Pccpch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pccpch", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:PPARameter:PCCPch:STATe \n
		Snippet: value: bool = driver.source.bb.tdscdma.down.pparameter.pccpch.get_state() \n
		Defines, if P-CCPCH is used in the scenario or not. If P-CCPCH is used, both P-CCPCHs are activated in slot 0 with
		spreading code 0+1. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:TDSCdma:DOWN:PPARameter:PCCPch:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:PPARameter:PCCPch:STATe \n
		Snippet: driver.source.bb.tdscdma.down.pparameter.pccpch.set_state(state = False) \n
		Defines, if P-CCPCH is used in the scenario or not. If P-CCPCH is used, both P-CCPCHs are activated in slot 0 with
		spreading code 0+1. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:PPARameter:PCCPch:STATe {param}')
