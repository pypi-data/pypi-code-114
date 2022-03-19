from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.BertTgEnTrigMode:
		"""SCPI: TEST:BB:DATA:TRIGger:[MODE] \n
		Snippet: value: enums.BertTgEnTrigMode = driver.test.bb.data.trigger.get_mode() \n
		Selects the trigger input mode for the BER test generator. \n
			:return: trigger_mode: DENable| RESTart
		"""
		response = self._core.io.query_str('TEST:BB:DATA:TRIGger:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.BertTgEnTrigMode)

	def set_mode(self, trigger_mode: enums.BertTgEnTrigMode) -> None:
		"""SCPI: TEST:BB:DATA:TRIGger:[MODE] \n
		Snippet: driver.test.bb.data.trigger.set_mode(trigger_mode = enums.BertTgEnTrigMode.DENable) \n
		Selects the trigger input mode for the BER test generator. \n
			:param trigger_mode: DENable| RESTart
		"""
		param = Conversions.enum_scalar_to_str(trigger_mode, enums.BertTgEnTrigMode)
		self._core.io.write(f'TEST:BB:DATA:TRIGger:MODE {param}')
