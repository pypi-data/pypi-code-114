from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Store:
	"""Store commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("store", core, parent)

	def get_fast(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DAB:SETTing:STORe:FAST \n
		Snippet: value: bool = driver.source.bb.dab.setting.store.get_fast() \n
		No command help available \n
			:return: fast: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DAB:SETTing:STORe:FAST?')
		return Conversions.str_to_bool(response)

	def set_fast(self, fast: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DAB:SETTing:STORe:FAST \n
		Snippet: driver.source.bb.dab.setting.store.set_fast(fast = False) \n
		No command help available \n
			:param fast: No help available
		"""
		param = Conversions.bool_to_str(fast)
		self._core.io.write(f'SOURce<HwInstance>:BB:DAB:SETTing:STORe:FAST {param}')

	def set_value(self, store: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DAB:SETTing:STORe \n
		Snippet: driver.source.bb.dab.setting.store.set_value(store = '1') \n
		No command help available \n
			:param store: No help available
		"""
		param = Conversions.value_to_quoted_str(store)
		self._core.io.write(f'SOURce<HwInstance>:BB:DAB:SETTing:STORe {param}')
