from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iab:
	"""Iab commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iab", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:FRMFormat:IAB:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.qckset.frmFormat.iab.get_state() \n
		Turns usage of the IAB frame format on and off. \n
			:return: qck_set_iab_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:FRMFormat:IAB:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, qck_set_iab_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:FRMFormat:IAB:STATe \n
		Snippet: driver.source.bb.nr5G.qckset.frmFormat.iab.set_state(qck_set_iab_state = False) \n
		Turns usage of the IAB frame format on and off. \n
			:param qck_set_iab_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(qck_set_iab_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:FRMFormat:IAB:STATe {param}')
