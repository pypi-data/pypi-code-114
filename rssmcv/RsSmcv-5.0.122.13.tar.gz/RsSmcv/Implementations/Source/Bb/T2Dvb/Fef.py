from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fef:
	"""Fef commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fef", core, parent)

	def get_interval(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:FEF:INTerval \n
		Snippet: value: int = driver.source.bb.t2Dvb.fef.get_interval() \n
		Queries the number of T2 frames between two FEF parts. The T2 frame shall always be the first frame in a T2 super frame
		which contains both FEF parts and T2 frames. \n
			:return: fef_interval: integer Range: 0 to 255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:FEF:INTerval?')
		return Conversions.str_to_int(response)

	def set_interval(self, fef_interval: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:FEF:INTerval \n
		Snippet: driver.source.bb.t2Dvb.fef.set_interval(fef_interval = 1) \n
		Queries the number of T2 frames between two FEF parts. The T2 frame shall always be the first frame in a T2 super frame
		which contains both FEF parts and T2 frames. \n
			:param fef_interval: integer Range: 0 to 255
		"""
		param = Conversions.decimal_value_to_str(fef_interval)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:FEF:INTerval {param}')

	def get_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:FEF:LENGth \n
		Snippet: value: int = driver.source.bb.t2Dvb.fef.get_length() \n
		Queries the length of the associated FEF part as the number of elementary periods T, from the start of the P1 symbol of
		the FEF part to the start of the P1 symbol of the next T2 frame. The FEF length is '0' for 'T2-MI Interface > Off'. \n
			:return: fef_length: integer Range: 0 to 16777215
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:FEF:LENGth?')
		return Conversions.str_to_int(response)

	def set_length(self, fef_length: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:FEF:LENGth \n
		Snippet: driver.source.bb.t2Dvb.fef.set_length(fef_length = 1) \n
		Queries the length of the associated FEF part as the number of elementary periods T, from the start of the P1 symbol of
		the FEF part to the start of the P1 symbol of the next T2 frame. The FEF length is '0' for 'T2-MI Interface > Off'. \n
			:param fef_length: integer Range: 0 to 16777215
		"""
		param = Conversions.decimal_value_to_str(fef_length)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:FEF:LENGth {param}')

	# noinspection PyTypeChecker
	def get_payload(self) -> enums.Dvbt2T2SystemFefPayload:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:FEF:PAYLoad \n
		Snippet: value: enums.Dvbt2T2SystemFefPayload = driver.source.bb.t2Dvb.fef.get_payload() \n
		Sets the FEF payload. \n
			:return: fef_payload: NULL| NOISe NULL I/Q values of the FEF payload are zeroes. NOISe I/Q values of the FEF payload are modulated in the frequency domain using a PRBS and transformed into the time domain by . The technique allows generating payload with a power level equal to the T2 frame.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:FEF:PAYLoad?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2T2SystemFefPayload)

	def set_payload(self, fef_payload: enums.Dvbt2T2SystemFefPayload) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:FEF:PAYLoad \n
		Snippet: driver.source.bb.t2Dvb.fef.set_payload(fef_payload = enums.Dvbt2T2SystemFefPayload.NOISe) \n
		Sets the FEF payload. \n
			:param fef_payload: NULL| NOISe NULL I/Q values of the FEF payload are zeroes. NOISe I/Q values of the FEF payload are modulated in the frequency domain using a PRBS and transformed into the time domain by . The technique allows generating payload with a power level equal to the T2 frame.
		"""
		param = Conversions.enum_scalar_to_str(fef_payload, enums.Dvbt2T2SystemFefPayload)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:FEF:PAYLoad {param}')

	def get_type_py(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:FEF:TYPE \n
		Snippet: value: int = driver.source.bb.t2Dvb.fef.get_type_py() \n
		Queries the type of the associated FEF part. \n
			:return: fef_type: integer Range: 0 to 15
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:FEF:TYPE?')
		return Conversions.str_to_int(response)

	def set_type_py(self, fef_type: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:FEF:TYPE \n
		Snippet: driver.source.bb.t2Dvb.fef.set_type_py(fef_type = 1) \n
		Queries the type of the associated FEF part. \n
			:param fef_type: integer Range: 0 to 15
		"""
		param = Conversions.decimal_value_to_str(fef_type)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:FEF:TYPE {param}')

	def get_value(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:FEF \n
		Snippet: value: bool = driver.source.bb.t2Dvb.fef.get_value() \n
		Enables/disables . \n
			:return: fef: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:FEF?')
		return Conversions.str_to_bool(response)

	def set_value(self, fef: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:FEF \n
		Snippet: driver.source.bb.t2Dvb.fef.set_value(fef = False) \n
		Enables/disables . \n
			:param fef: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(fef)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:FEF {param}')
