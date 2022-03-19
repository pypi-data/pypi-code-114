from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TrigSweepSourNoHopExtAuto:
		"""SCPI: [SOURce<HW>]:LIST:TRIGger:SOURce \n
		Snippet: value: enums.TrigSweepSourNoHopExtAuto = driver.source.listPy.trigger.get_source() \n
		Selects the trigger source for processing lists. The designation of the parameters correspond to those in sweep mode.
		SCPI standard uses other designations for the parameters, which are also accepted by the instrument. The SCPI designation
		should be used if compatibility is an important consideration. For an overview, see the following table:
			Table Header: Rohde & Schwarz parameter / SCPI parameter / Applies to the list mode parameters: \n
			- AUTO / IMMediate / [:SOURce<hw>]:LIST:MODE AUTO
			- SINGle / BUS / [:SOURce<hw>]:LIST:MODE AUTO or [:SOURce<hw>]:LIST:MODE STEP
			- EXTernal / EXTernal / [:SOURce<hw>]:LIST:MODE AUTO or [:SOURce<hw>]:LIST:MODE STEP \n
			:return: source: AUTO| IMMediate| SINGle| BUS| EXTernal AUTO|IMMediate The trigger is free-running, i.e. the trigger condition is fulfilled continuously. The selected list is restarted as soon as it is finished. SINGle|BUS The list is triggered by the command [:SOURcehw]:LIST:TRIGger:EXECute. The list is executed once. EXTernal The list is triggered externally and executed once.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:TRIGger:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TrigSweepSourNoHopExtAuto)

	def set_source(self, source: enums.TrigSweepSourNoHopExtAuto) -> None:
		"""SCPI: [SOURce<HW>]:LIST:TRIGger:SOURce \n
		Snippet: driver.source.listPy.trigger.set_source(source = enums.TrigSweepSourNoHopExtAuto.AUTO) \n
		Selects the trigger source for processing lists. The designation of the parameters correspond to those in sweep mode.
		SCPI standard uses other designations for the parameters, which are also accepted by the instrument. The SCPI designation
		should be used if compatibility is an important consideration. For an overview, see the following table:
			Table Header: Rohde & Schwarz parameter / SCPI parameter / Applies to the list mode parameters: \n
			- AUTO / IMMediate / [:SOURce<hw>]:LIST:MODE AUTO
			- SINGle / BUS / [:SOURce<hw>]:LIST:MODE AUTO or [:SOURce<hw>]:LIST:MODE STEP
			- EXTernal / EXTernal / [:SOURce<hw>]:LIST:MODE AUTO or [:SOURce<hw>]:LIST:MODE STEP \n
			:param source: AUTO| IMMediate| SINGle| BUS| EXTernal AUTO|IMMediate The trigger is free-running, i.e. the trigger condition is fulfilled continuously. The selected list is restarted as soon as it is finished. SINGle|BUS The list is triggered by the command [:SOURcehw]:LIST:TRIGger:EXECute. The list is executed once. EXTernal The list is triggered externally and executed once.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TrigSweepSourNoHopExtAuto)
		self._core.io.write(f'SOURce<HwInstance>:LIST:TRIGger:SOURce {param}')

	def clone(self) -> 'Trigger':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trigger(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
