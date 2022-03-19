from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cs:
	"""Cs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cs", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:ES:CS:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.qckset.general.es.cs.get_state() \n
		Activate to schedule a CORESET. \n
			:return: qck_set_cs_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:ES:CS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, qck_set_cs_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:ES:CS:STATe \n
		Snippet: driver.source.bb.nr5G.qckset.general.es.cs.set_state(qck_set_cs_state = False) \n
		Activate to schedule a CORESET. \n
			:param qck_set_cs_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(qck_set_cs_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:ES:CS:STATe {param}')
