from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	# noinspection PyTypeChecker
	def get_output(self) -> enums.Ts25141MarkerConf:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:TRIGger:OUTPut \n
		Snippet: value: enums.Ts25141MarkerConf = driver.source.bb.w3Gpp.ts25141.trigger.get_output() \n
		Defines the signal for the selected marker output. \n
			:return: output: AUTO| PRESet
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:TRIGger:OUTPut?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141MarkerConf)

	def set_output(self, output: enums.Ts25141MarkerConf) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:TRIGger:OUTPut \n
		Snippet: driver.source.bb.w3Gpp.ts25141.trigger.set_output(output = enums.Ts25141MarkerConf.AUTO) \n
		Defines the signal for the selected marker output. \n
			:param output: AUTO| PRESet
		"""
		param = Conversions.enum_scalar_to_str(output, enums.Ts25141MarkerConf)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:TRIGger:OUTPut {param}')

	def get_slength(self) -> float:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:TRIGger:SLENgth \n
		Snippet: value: float = driver.source.bb.w3Gpp.ts25141.trigger.get_slength() \n
		No command help available \n
			:return: slength: No help available
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:TRIGger:SLENgth?')
		return Conversions.str_to_float(response)

	def set_slength(self, slength: float) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:TRIGger:SLENgth \n
		Snippet: driver.source.bb.w3Gpp.ts25141.trigger.set_slength(slength = 1.0) \n
		No command help available \n
			:param slength: No help available
		"""
		param = Conversions.decimal_value_to_str(slength)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:TRIGger:SLENgth {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.Ts25141TriggerConf:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:TRIGger \n
		Snippet: value: enums.Ts25141TriggerConf = driver.source.bb.w3Gpp.ts25141.trigger.get_value() \n
		Selects the trigger mode. The trigger is used to synchronize the signal generator to the other equipment. \n
			:return: trigger: AUTO| PRESet| SINGle
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:TRIGger?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141TriggerConf)

	def set_value(self, trigger: enums.Ts25141TriggerConf) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:TRIGger \n
		Snippet: driver.source.bb.w3Gpp.ts25141.trigger.set_value(trigger = enums.Ts25141TriggerConf.AUTO) \n
		Selects the trigger mode. The trigger is used to synchronize the signal generator to the other equipment. \n
			:param trigger: AUTO| PRESet| SINGle
		"""
		param = Conversions.enum_scalar_to_str(trigger, enums.Ts25141TriggerConf)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:TRIGger {param}')
