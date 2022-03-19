from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 19 total commands, 5 Subgroups, 5 group commands"""

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
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	@property
	def external(self):
		"""external commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_external'):
			from .External import External
			self._external = External(self._core, self._cmd_group)
		return self._external

	@property
	def obaseband(self):
		"""obaseband commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_obaseband'):
			from .Obaseband import Obaseband
			self._obaseband = Obaseband(self._core, self._cmd_group)
		return self._obaseband

	@property
	def output(self):
		"""output commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	# noinspection PyTypeChecker
	def get_rmode(self) -> enums.TrigRunMode:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:RMODe \n
		Snippet: value: enums.TrigRunMode = driver.source.bb.nfc.trigger.get_rmode() \n
		Queries the status of signal generation. \n
			:return: rmode: STOP| RUN
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:TRIGger:RMODe?')
		return Conversions.str_to_scalar_enum(response, enums.TrigRunMode)

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:SLENgth \n
		Snippet: value: int = driver.source.bb.nfc.trigger.get_slength() \n
		Defines the length of the signal sequence to be output in the SINGle trigger mode. \n
			:return: slength: integer Range: 1 to 4294967295.0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:TRIGger:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, slength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:SLENgth \n
		Snippet: driver.source.bb.nfc.trigger.set_slength(slength = 1) \n
		Defines the length of the signal sequence to be output in the SINGle trigger mode. \n
			:param slength: integer Range: 1 to 4294967295.0
		"""
		param = Conversions.decimal_value_to_str(slength)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:TRIGger:SLENgth {param}')

	# noinspection PyTypeChecker
	def get_sl_unit(self) -> enums.UnitSlB:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:SLUNit \n
		Snippet: value: enums.UnitSlB = driver.source.bb.nfc.trigger.get_sl_unit() \n
		Defines the unit for the entry of the signal sequence length. \n
			:return: sl_unit: SEQuence| SAMPle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:TRIGger:SLUNit?')
		return Conversions.str_to_scalar_enum(response, enums.UnitSlB)

	def set_sl_unit(self, sl_unit: enums.UnitSlB) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:SLUNit \n
		Snippet: driver.source.bb.nfc.trigger.set_sl_unit(sl_unit = enums.UnitSlB.SAMPle) \n
		Defines the unit for the entry of the signal sequence length. \n
			:param sl_unit: SEQuence| SAMPle
		"""
		param = Conversions.enum_scalar_to_str(sl_unit, enums.UnitSlB)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:TRIGger:SLUNit {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TriggerSourceC:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:SOURce \n
		Snippet: value: enums.TriggerSourceC = driver.source.bb.nfc.trigger.get_source() \n
			INTRO_CMD_HELP: Selects the trigger signal source and determines the way the triggering is executed. Provided are: \n
			- Internal triggering by a command (INTernal)
			- External trigger signal via one of the local or global connectors
			Table Header:  \n
			- EGT1|EGT2: External global trigger
			- EGC1|EGC2: External global clock
			- ELTRigger: External local trigger
			- ELCLock: External local clock
			- Internal triggering by a signal from the other basebands (INTA|INTB)
			- OBASeband|BEXTernal|EXTernal: Setting only Provided only for backward
		compatibility with other Rohde & Schwarz signal generators. The R&S SMW accepts these values and maps them automatically
		as follows: EXTernal = EGT1, BEXTernal = EGT2, OBASeband = INTA or INTB (depending on the current baseband) \n
			:return: source: INTB| INTernal| OBASeband| EGT1| EGT2| EGC1| EGC2| ELTRigger| INTA| ELCLock| BEXTernal| EXTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:TRIGger:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSourceC)

	def set_source(self, source: enums.TriggerSourceC) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:SOURce \n
		Snippet: driver.source.bb.nfc.trigger.set_source(source = enums.TriggerSourceC.BBSY) \n
			INTRO_CMD_HELP: Selects the trigger signal source and determines the way the triggering is executed. Provided are: \n
			- Internal triggering by a command (INTernal)
			- External trigger signal via one of the local or global connectors
			Table Header:  \n
			- EGT1|EGT2: External global trigger
			- EGC1|EGC2: External global clock
			- ELTRigger: External local trigger
			- ELCLock: External local clock
			- Internal triggering by a signal from the other basebands (INTA|INTB)
			- OBASeband|BEXTernal|EXTernal: Setting only Provided only for backward
		compatibility with other Rohde & Schwarz signal generators. The R&S SMW accepts these values and maps them automatically
		as follows: EXTernal = EGT1, BEXTernal = EGT2, OBASeband = INTA or INTB (depending on the current baseband) \n
			:param source: INTB| INTernal| OBASeband| EGT1| EGT2| EGC1| EGC2| ELTRigger| INTA| ELCLock| BEXTernal| EXTernal
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TriggerSourceC)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:TRIGger:SOURce {param}')

	# noinspection PyTypeChecker
	def get_sequence(self) -> enums.DmTrigMode:
		"""SCPI: [SOURce<HW>]:BB:NFC:[TRIGger]:SEQuence \n
		Snippet: value: enums.DmTrigMode = driver.source.bb.nfc.trigger.get_sequence() \n
		Selects a reqular trigger mode. \n
			:return: sequence: AUTO| RETRigger| AAUTo| ARETrigger| SINGle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:TRIGger:SEQuence?')
		return Conversions.str_to_scalar_enum(response, enums.DmTrigMode)

	def set_sequence(self, sequence: enums.DmTrigMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:[TRIGger]:SEQuence \n
		Snippet: driver.source.bb.nfc.trigger.set_sequence(sequence = enums.DmTrigMode.AAUTo) \n
		Selects a reqular trigger mode. \n
			:param sequence: AUTO| RETRigger| AAUTo| ARETrigger| SINGle
		"""
		param = Conversions.enum_scalar_to_str(sequence, enums.DmTrigMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:TRIGger:SEQuence {param}')

	def clone(self) -> 'Trigger':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trigger(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
