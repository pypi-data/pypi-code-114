from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 5 total commands, 2 Subgroups, 3 group commands
	Repeated Capability: External, default value after init: External.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("external", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_external_get', 'repcap_external_set', repcap.External.Nr1)

	def repcap_external_set(self, external: repcap.External) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to External.Default
		Default value after init: External.Nr1"""
		self._cmd_group.set_repcap_enum_value(external)

	def repcap_external_get(self) -> repcap.External:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def synchronize(self):
		"""synchronize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_synchronize'):
			from .Synchronize import Synchronize
			self._synchronize = Synchronize(self._core, self._cmd_group)
		return self._synchronize

	@property
	def delay(self):
		"""delay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import Delay
			self._delay = Delay(self._core, self._cmd_group)
		return self._delay

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DM:TRIGger:[EXTernal]:INHibit \n
		Snippet: value: int = driver.source.bb.dm.trigger.external.get_inhibit() \n
		Specifies the number of symbols, by which a restart is inhibited. Maximum trigger delay and trigger inhibit values depend
		on the installed options. See 'Specifying delay and inhibit values'. \n
			:return: inhibit: integer Range: 0 to 21.47 * (symbol rate) , Unit: symbol
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:TRIGger:EXTernal:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:TRIGger:[EXTernal]:INHibit \n
		Snippet: driver.source.bb.dm.trigger.external.set_inhibit(inhibit = 1) \n
		Specifies the number of symbols, by which a restart is inhibited. Maximum trigger delay and trigger inhibit values depend
		on the installed options. See 'Specifying delay and inhibit values'. \n
			:param inhibit: integer Range: 0 to 21.47 * (symbol rate) , Unit: symbol
		"""
		param = Conversions.decimal_value_to_str(inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:TRIGger:EXTernal:INHibit {param}')

	def get_rdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:TRIGger:[EXTernal]:RDELay \n
		Snippet: value: float = driver.source.bb.dm.trigger.external.get_rdelay() \n
		Queries the time (in seconds) an external trigger event is delayed for. \n
			:return: res_time_delay_sec: float Range: 0 to 688
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:TRIGger:EXTernal:RDELay?')
		return Conversions.str_to_float(response)

	def get_tdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:TRIGger:[EXTernal]:TDELay \n
		Snippet: value: float = driver.source.bb.dm.trigger.external.get_tdelay() \n
		Specifies the trigger delay for external triggering. The value affects all external trigger signals. Maximum trigger
		delay and trigger inhibit values depend on the installed options. See 'Specifying delay and inhibit values'. \n
			:return: ext_time_delay: float Range: 0 to 7929.170398682, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:TRIGger:EXTernal:TDELay?')
		return Conversions.str_to_float(response)

	def set_tdelay(self, ext_time_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:TRIGger:[EXTernal]:TDELay \n
		Snippet: driver.source.bb.dm.trigger.external.set_tdelay(ext_time_delay = 1.0) \n
		Specifies the trigger delay for external triggering. The value affects all external trigger signals. Maximum trigger
		delay and trigger inhibit values depend on the installed options. See 'Specifying delay and inhibit values'. \n
			:param ext_time_delay: float Range: 0 to 7929.170398682, Unit: s
		"""
		param = Conversions.decimal_value_to_str(ext_time_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:TRIGger:EXTernal:TDELay {param}')

	def clone(self) -> 'External':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = External(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
