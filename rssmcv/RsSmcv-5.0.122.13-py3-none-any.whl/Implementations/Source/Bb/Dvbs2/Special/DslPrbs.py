from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DslPrbs:
	"""DslPrbs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dslPrbs", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[SPECial]:DSLPrbs:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvbs2.special.dslPrbs.get_state() \n
		Enable for test purposes. PRBS can be inserted into the data slices. The PRBS transmitted in the data slices is
		continuous, so that a BER measurement on decoded data slices can be performed. \n
			:return: data_slice_prbs: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:SPECial:DSLPrbs:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, data_slice_prbs: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[SPECial]:DSLPrbs:[STATe] \n
		Snippet: driver.source.bb.dvbs2.special.dslPrbs.set_state(data_slice_prbs = False) \n
		Enable for test purposes. PRBS can be inserted into the data slices. The PRBS transmitted in the data slices is
		continuous, so that a BER measurement on decoded data slices can be performed. \n
			:param data_slice_prbs: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(data_slice_prbs)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:SPECial:DSLPrbs:STATe {param}')
