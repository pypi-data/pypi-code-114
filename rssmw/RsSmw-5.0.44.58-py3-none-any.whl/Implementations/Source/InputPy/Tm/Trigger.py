from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	# noinspection PyTypeChecker
	def get_impedance(self) -> enums.InputImpRf:
		"""SCPI: [SOURce<HW>]:INPut:TM:TRIGger:IMPedance \n
		Snippet: value: enums.InputImpRf = driver.source.inputPy.tm.trigger.get_impedance() \n
		Selects the input impedance for the external trigger/clock inputs. \n
			:return: impedance: G1K| G50| G10K G10K Provided only for backward compatibility with other R&S signal generators. The R&S SMW accepts this value and maps it automatically to G1K.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:INPut:TM:TRIGger:IMPedance?')
		return Conversions.str_to_scalar_enum(response, enums.InputImpRf)

	def set_impedance(self, impedance: enums.InputImpRf) -> None:
		"""SCPI: [SOURce<HW>]:INPut:TM:TRIGger:IMPedance \n
		Snippet: driver.source.inputPy.tm.trigger.set_impedance(impedance = enums.InputImpRf.G10K) \n
		Selects the input impedance for the external trigger/clock inputs. \n
			:param impedance: G1K| G50| G10K G10K Provided only for backward compatibility with other R&S signal generators. The R&S SMW accepts this value and maps it automatically to G1K.
		"""
		param = Conversions.enum_scalar_to_str(impedance, enums.InputImpRf)
		self._core.io.write(f'SOURce<HwInstance>:INPut:TM:TRIGger:IMPedance {param}')

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:INPut:TM:TRIGger:LEVel \n
		Snippet: value: float = driver.source.inputPy.tm.trigger.get_level() \n
		Sets the high/low threshold in volts for the trigger and clock signal inputs of the baseband section. \n
			:return: level: float Range: 0.3 to 2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:INPut:TM:TRIGger:LEVel?')
		return Conversions.str_to_float(response)

	def set_level(self, level: float) -> None:
		"""SCPI: [SOURce<HW>]:INPut:TM:TRIGger:LEVel \n
		Snippet: driver.source.inputPy.tm.trigger.set_level(level = 1.0) \n
		Sets the high/low threshold in volts for the trigger and clock signal inputs of the baseband section. \n
			:param level: float Range: 0.3 to 2
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SOURce<HwInstance>:INPut:TM:TRIGger:LEVel {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SlopeType:
		"""SCPI: [SOURce<HW>]:INPut:TM:TRIGger:SLOPe \n
		Snippet: value: enums.SlopeType = driver.source.inputPy.tm.trigger.get_slope() \n
		Sets the polarity of the active slope of an externally applied trigger signal. \n
			:return: slope: NEGative| POSitive
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:INPut:TM:TRIGger:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SlopeType)

	def set_slope(self, slope: enums.SlopeType) -> None:
		"""SCPI: [SOURce<HW>]:INPut:TM:TRIGger:SLOPe \n
		Snippet: driver.source.inputPy.tm.trigger.set_slope(slope = enums.SlopeType.NEGative) \n
		Sets the polarity of the active slope of an externally applied trigger signal. \n
			:param slope: NEGative| POSitive
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SlopeType)
		self._core.io.write(f'SOURce<HwInstance>:INPut:TM:TRIGger:SLOPe {param}')
