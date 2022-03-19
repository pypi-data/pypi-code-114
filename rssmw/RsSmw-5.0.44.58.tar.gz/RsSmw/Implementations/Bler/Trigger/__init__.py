from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	@property
	def immediate(self):
		"""immediate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_immediate'):
			from .Immediate import Immediate
			self._immediate = Immediate(self._core, self._cmd_group)
		return self._immediate

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.BlerTrigMode:
		"""SCPI: BLER:TRIGger:MODE \n
		Snippet: value: enums.BlerTrigMode = driver.bler.trigger.get_mode() \n
		Selects the type of measurement. \n
			:return: polarity: AUTO| SINGle AUTO Continuous measurement. Terminates the measurement in progress if one or both termination criteria are met. Delays the restart of a new measurement until the first measurement result has been queried. The resulting brief measurement interruption is irrelevant because the subsequent measurement is synchronized within 24 data bits. SINGle Single measurement, started with method RsSmw.Bert.Trigger.Immediate.set | method RsSmw.Bler.Trigger.Immediate.set.
		"""
		response = self._core.io.query_str('BLER:TRIGger:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.BlerTrigMode)

	def set_mode(self, polarity: enums.BlerTrigMode) -> None:
		"""SCPI: BLER:TRIGger:MODE \n
		Snippet: driver.bler.trigger.set_mode(polarity = enums.BlerTrigMode.AUTO) \n
		Selects the type of measurement. \n
			:param polarity: AUTO| SINGle AUTO Continuous measurement. Terminates the measurement in progress if one or both termination criteria are met. Delays the restart of a new measurement until the first measurement result has been queried. The resulting brief measurement interruption is irrelevant because the subsequent measurement is synchronized within 24 data bits. SINGle Single measurement, started with method RsSmw.Bert.Trigger.Immediate.set | method RsSmw.Bler.Trigger.Immediate.set.
		"""
		param = Conversions.enum_scalar_to_str(polarity, enums.BlerTrigMode)
		self._core.io.write(f'BLER:TRIGger:MODE {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TrigSourBerBler:
		"""SCPI: BLER:TRIGger:SOURce \n
		Snippet: value: enums.TrigSourBerBler = driver.bler.trigger.get_source() \n
		For method RsSmw.Bler.Trigger.modeSINGle, selects the source of the trigger signal. \n
			:return: polarity: INTernal| EGT1
		"""
		response = self._core.io.query_str('BLER:TRIGger:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TrigSourBerBler)

	def set_source(self, polarity: enums.TrigSourBerBler) -> None:
		"""SCPI: BLER:TRIGger:SOURce \n
		Snippet: driver.bler.trigger.set_source(polarity = enums.TrigSourBerBler.EGT1) \n
		For method RsSmw.Bler.Trigger.modeSINGle, selects the source of the trigger signal. \n
			:param polarity: INTernal| EGT1
		"""
		param = Conversions.enum_scalar_to_str(polarity, enums.TrigSourBerBler)
		self._core.io.write(f'BLER:TRIGger:SOURce {param}')

	def clone(self) -> 'Trigger':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trigger(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
