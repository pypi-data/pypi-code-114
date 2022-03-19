from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 25 total commands, 6 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	@property
	def arm(self):
		"""arm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_arm'):
			from .Arm import Arm
			self._arm = Arm(self._core, self._cmd_group)
		return self._arm

	@property
	def delay(self):
		"""delay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import Delay
			self._delay = Delay(self._core, self._cmd_group)
		return self._delay

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	@property
	def external(self):
		"""external commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_external'):
			from .External import External
			self._external = External(self._core, self._cmd_group)
		return self._external

	@property
	def obaseband(self):
		"""obaseband commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_obaseband'):
			from .Obaseband import Obaseband
			self._obaseband = Obaseband(self._core, self._cmd_group)
		return self._obaseband

	@property
	def output(self):
		"""output commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	# noinspection PyTypeChecker
	def get_rmode(self) -> enums.TrigRunMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:RMODe \n
		Snippet: value: enums.TrigRunMode = driver.source.bb.eutra.trigger.get_rmode() \n
		Queries the signal generation status. \n
			:return: run_mode: STOP| RUN
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TRIGger:RMODe?')
		return Conversions.str_to_scalar_enum(response, enums.TrigRunMode)

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:SLENgth \n
		Snippet: value: int = driver.source.bb.eutra.trigger.get_slength() \n
		Defines the length of the signal sequence that is output in the SINGle trigger mode. \n
			:return: sequence_length: integer Range: 1 to 4294967295
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TRIGger:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, sequence_length: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:SLENgth \n
		Snippet: driver.source.bb.eutra.trigger.set_slength(sequence_length = 1) \n
		Defines the length of the signal sequence that is output in the SINGle trigger mode. \n
			:param sequence_length: integer Range: 1 to 4294967295
		"""
		param = Conversions.decimal_value_to_str(sequence_length)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TRIGger:SLENgth {param}')

	# noinspection PyTypeChecker
	def get_sl_unit(self) -> enums.Unit:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:SLUNit \n
		Snippet: value: enums.Unit = driver.source.bb.eutra.trigger.get_sl_unit() \n
		Defines the unit for the entry of the signal sequence length. \n
			:return: seq_len_unit: SEQuence| FRAMe| SUBFrame| SLOT| SAMPle FRAMe A single frame is generated after a trigger event. SEQuence A single sequence is generated after a trigger event. SUBFrame A single subframe is generated after a trigger event. SLOT A single slot is generated after a trigger event. SAMPle Number of samples are generated after a trigger event.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TRIGger:SLUNit?')
		return Conversions.str_to_scalar_enum(response, enums.Unit)

	def set_sl_unit(self, seq_len_unit: enums.Unit) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:SLUNit \n
		Snippet: driver.source.bb.eutra.trigger.set_sl_unit(seq_len_unit = enums.Unit.FRAMe) \n
		Defines the unit for the entry of the signal sequence length. \n
			:param seq_len_unit: SEQuence| FRAMe| SUBFrame| SLOT| SAMPle FRAMe A single frame is generated after a trigger event. SEQuence A single sequence is generated after a trigger event. SUBFrame A single subframe is generated after a trigger event. SLOT A single slot is generated after a trigger event. SAMPle Number of samples are generated after a trigger event.
		"""
		param = Conversions.enum_scalar_to_str(seq_len_unit, enums.Unit)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TRIGger:SLUNit {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TriggerSourceC:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:SOURce \n
		Snippet: value: enums.TriggerSourceC = driver.source.bb.eutra.trigger.get_source() \n
			INTRO_CMD_HELP: Selects the trigger signal source and determines the way the triggering is executed. Provided are: \n
			- Internal triggering by a command (INTernal)
			- External trigger signal via one of the local or global connectors
			Table Header:  \n
			- EGT1|EGT2: External global trigger
			- EGC1|EGC2: External global clock
			- ELTRigger: External local trigger
			- ELCLock: External local clock
			- Internal triggering by a signal from the other basebands (INTA|INTB)
			- In primary-secondary instrument mode, the external baseband synchronization
		signal (BBSY)
			- OBASeband|BEXTernal|EXTernal: Setting only Provided only for backward
		compatibility with other Rohde & Schwarz signal generators. The R&S SMW accepts these values and maps them automatically
		as follows: EXTernal = EGT1, BEXTernal = EGT2, OBASeband = INTA or INTB (depending on the current baseband) \n
			:return: source: INTB| INTernal| OBASeband| EGT1| EGT2| EGC1| EGC2| ELTRigger| INTA| ELCLock| BEXTernal| EXTernal | BBSY
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TRIGger:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSourceC)

	def set_source(self, source: enums.TriggerSourceC) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:SOURce \n
		Snippet: driver.source.bb.eutra.trigger.set_source(source = enums.TriggerSourceC.BBSY) \n
			INTRO_CMD_HELP: Selects the trigger signal source and determines the way the triggering is executed. Provided are: \n
			- Internal triggering by a command (INTernal)
			- External trigger signal via one of the local or global connectors
			Table Header:  \n
			- EGT1|EGT2: External global trigger
			- EGC1|EGC2: External global clock
			- ELTRigger: External local trigger
			- ELCLock: External local clock
			- Internal triggering by a signal from the other basebands (INTA|INTB)
			- In primary-secondary instrument mode, the external baseband synchronization
		signal (BBSY)
			- OBASeband|BEXTernal|EXTernal: Setting only Provided only for backward
		compatibility with other Rohde & Schwarz signal generators. The R&S SMW accepts these values and maps them automatically
		as follows: EXTernal = EGT1, BEXTernal = EGT2, OBASeband = INTA or INTB (depending on the current baseband) \n
			:param source: INTB| INTernal| OBASeband| EGT1| EGT2| EGC1| EGC2| ELTRigger| INTA| ELCLock| BEXTernal| EXTernal | BBSY
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TriggerSourceC)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TRIGger:SOURce {param}')

	# noinspection PyTypeChecker
	def get_sequence(self) -> enums.DmTrigMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:[TRIGger]:SEQuence \n
		Snippet: value: enums.DmTrigMode = driver.source.bb.eutra.trigger.get_sequence() \n
			INTRO_CMD_HELP: Selects the trigger mode: \n
			- AUTO = auto
			- RETRigger = retrigger
			- AAUTo = armed auto
			- ARETrigger = armed retrigger
			- SINGle = single \n
			:return: trigger_mode: AUTO| RETRigger| AAUTo| ARETrigger| SINGle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:TRIGger:SEQuence?')
		return Conversions.str_to_scalar_enum(response, enums.DmTrigMode)

	def set_sequence(self, trigger_mode: enums.DmTrigMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:[TRIGger]:SEQuence \n
		Snippet: driver.source.bb.eutra.trigger.set_sequence(trigger_mode = enums.DmTrigMode.AAUTo) \n
			INTRO_CMD_HELP: Selects the trigger mode: \n
			- AUTO = auto
			- RETRigger = retrigger
			- AAUTo = armed auto
			- ARETrigger = armed retrigger
			- SINGle = single \n
			:param trigger_mode: AUTO| RETRigger| AAUTo| ARETrigger| SINGle
		"""
		param = Conversions.enum_scalar_to_str(trigger_mode, enums.DmTrigMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TRIGger:SEQuence {param}')

	def clone(self) -> 'Trigger':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trigger(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
