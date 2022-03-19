from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 17 total commands, 1 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	@property
	def t2Mi(self):
		"""t2Mi commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_t2Mi'):
			from .T2Mi import T2Mi
			self._t2Mi = T2Mi(self._core, self._cmd_group)
		return self._t2Mi

	# noinspection PyTypeChecker
	def get_format_py(self) -> enums.CodingInputFormat:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:FORMat \n
		Snippet: value: enums.CodingInputFormat = driver.source.bb.t2Dvb.inputPy.get_format_py() \n
		Sets the input format of the input signal. \n
			:return: dvbt_2_inp_format: ASI| SMPTE
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputFormat)

	def set_format_py(self, dvbt_2_inp_format: enums.CodingInputFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:FORMat \n
		Snippet: driver.source.bb.t2Dvb.inputPy.set_format_py(dvbt_2_inp_format = enums.CodingInputFormat.ASI) \n
		Sets the input format of the input signal. \n
			:param dvbt_2_inp_format: ASI| SMPTE
		"""
		param = Conversions.enum_scalar_to_str(dvbt_2_inp_format, enums.CodingInputFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:INPut:FORMat {param}')

	def get_nplp(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:NPLP \n
		Snippet: value: int = driver.source.bb.t2Dvb.inputPy.get_nplp() \n
		Queries the number of physical layer pipes (PLP) . \n
			:return: nplp: integer Range: 1 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:NPLP?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_ts_channel(self) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:TSCHannel \n
		Snippet: value: enums.NumberA = driver.source.bb.t2Dvb.inputPy.get_ts_channel() \n
		Selects the IP-based transport stream (TS) channel. You can select 1 out of 4 IP TS channels as input at the 'IP Data'
		interface. To configure a particular channel, see 'IP channel x settings'. \n
			:return: dvbt_2_ts_channel: 1| 2| 3| 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:TSCHannel?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)

	def set_ts_channel(self, dvbt_2_ts_channel: enums.NumberA) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:TSCHannel \n
		Snippet: driver.source.bb.t2Dvb.inputPy.set_ts_channel(dvbt_2_ts_channel = enums.NumberA._1) \n
		Selects the IP-based transport stream (TS) channel. You can select 1 out of 4 IP TS channels as input at the 'IP Data'
		interface. To configure a particular channel, see 'IP channel x settings'. \n
			:param dvbt_2_ts_channel: 1| 2| 3| 4
		"""
		param = Conversions.enum_scalar_to_str(dvbt_2_ts_channel, enums.NumberA)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:INPut:TSCHannel {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.CodingInputSignalInputA:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut \n
		Snippet: value: enums.CodingInputSignalInputA = driver.source.bb.t2Dvb.inputPy.get_value() \n
		Sets the external input interface. \n
			:return: dvbt_2_input: TS| IP
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputSignalInputA)

	def set_value(self, dvbt_2_input: enums.CodingInputSignalInputA) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut \n
		Snippet: driver.source.bb.t2Dvb.inputPy.set_value(dvbt_2_input = enums.CodingInputSignalInputA.ASI1) \n
		Sets the external input interface. \n
			:param dvbt_2_input: TS| IP
		"""
		param = Conversions.enum_scalar_to_str(dvbt_2_input, enums.CodingInputSignalInputA)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:INPut {param}')

	def clone(self) -> 'InputPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
