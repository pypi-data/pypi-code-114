from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsChannel:
	"""TsChannel commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsChannel", core, parent)

	# noinspection PyTypeChecker
	def get_low(self) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:DVBT:INPut:TSCHannel:LOW \n
		Snippet: value: enums.NumberA = driver.source.bb.dvbt.inputPy.tsChannel.get_low() \n
		No command help available \n
			:return: ts_channel_lp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:INPut:TSCHannel:LOW?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)

	def set_low(self, ts_channel_lp: enums.NumberA) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:INPut:TSCHannel:LOW \n
		Snippet: driver.source.bb.dvbt.inputPy.tsChannel.set_low(ts_channel_lp = enums.NumberA._1) \n
		No command help available \n
			:param ts_channel_lp: No help available
		"""
		param = Conversions.enum_scalar_to_str(ts_channel_lp, enums.NumberA)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:INPut:TSCHannel:LOW {param}')

	# noinspection PyTypeChecker
	def get_high(self) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:DVBT:INPut:TSCHannel:[HIGH] \n
		Snippet: value: enums.NumberA = driver.source.bb.dvbt.inputPy.tsChannel.get_high() \n
		Selects the IP-based transport stream (TS) channel. You can select 1 out of 4 IP TS channels as input at the 'IP Data'
		interface. To configure a particular channel, see 'IP channel x settings'. \n
			:return: ts_channel: 1| 2| 3| 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:INPut:TSCHannel:HIGH?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)

	def set_high(self, ts_channel: enums.NumberA) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:INPut:TSCHannel:[HIGH] \n
		Snippet: driver.source.bb.dvbt.inputPy.tsChannel.set_high(ts_channel = enums.NumberA._1) \n
		Selects the IP-based transport stream (TS) channel. You can select 1 out of 4 IP TS channels as input at the 'IP Data'
		interface. To configure a particular channel, see 'IP channel x settings'. \n
			:param ts_channel: 1| 2| 3| 4
		"""
		param = Conversions.enum_scalar_to_str(ts_channel, enums.NumberA)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:INPut:TSCHannel:HIGH {param}')
