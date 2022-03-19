from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Index:
	"""Index commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("index", core, parent)

	def get_start(self) -> int:
		"""SCPI: [SOURce<HW>]:LIST:INDex:STARt \n
		Snippet: value: int = driver.source.listPy.index.get_start() \n
		Sets the start and stop index of the index range which defines a subgroup of frequency/level value pairs in the current
		list. \n
			:return: start: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:INDex:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, start: int) -> None:
		"""SCPI: [SOURce<HW>]:LIST:INDex:STARt \n
		Snippet: driver.source.listPy.index.set_start(start = 1) \n
		Sets the start and stop index of the index range which defines a subgroup of frequency/level value pairs in the current
		list. \n
			:param start: integer Index range Only values inside this range are processed in list mode Range: 0 to list length
		"""
		param = Conversions.decimal_value_to_str(start)
		self._core.io.write(f'SOURce<HwInstance>:LIST:INDex:STARt {param}')

	def get_stop(self) -> int:
		"""SCPI: [SOURce<HW>]:LIST:INDex:STOP \n
		Snippet: value: int = driver.source.listPy.index.get_stop() \n
		Sets the start and stop index of the index range which defines a subgroup of frequency/level value pairs in the current
		list. \n
			:return: stop: integer Index range Only values inside this range are processed in list mode Range: 0 to list length
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:INDex:STOP?')
		return Conversions.str_to_int(response)

	def set_stop(self, stop: int) -> None:
		"""SCPI: [SOURce<HW>]:LIST:INDex:STOP \n
		Snippet: driver.source.listPy.index.set_stop(stop = 1) \n
		Sets the start and stop index of the index range which defines a subgroup of frequency/level value pairs in the current
		list. \n
			:param stop: integer Index range Only values inside this range are processed in list mode Range: 0 to list length
		"""
		param = Conversions.decimal_value_to_str(stop)
		self._core.io.write(f'SOURce<HwInstance>:LIST:INDex:STOP {param}')

	def get_value(self) -> int:
		"""SCPI: [SOURce<HW>]:LIST:INDex \n
		Snippet: value: int = driver.source.listPy.index.get_value() \n
		Sets the list index in LIST:MODE STEP. After the trigger signal, the instrument processes the frequency and level
		settings of the selected index. \n
			:return: index: integer
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:INDex?')
		return Conversions.str_to_int(response)

	def set_value(self, index: int) -> None:
		"""SCPI: [SOURce<HW>]:LIST:INDex \n
		Snippet: driver.source.listPy.index.set_value(index = 1) \n
		Sets the list index in LIST:MODE STEP. After the trigger signal, the instrument processes the frequency and level
		settings of the selected index. \n
			:param index: integer
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'SOURce<HwInstance>:LIST:INDex {param}')
