from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 39 total commands, 8 Subgroups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def alc(self):
		"""alc commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_alc'):
			from .Alc import Alc
			self._alc = Alc(self._core, self._cmd_group)
		return self._alc

	@property
	def attenuation(self):
		"""attenuation commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_attenuation'):
			from .Attenuation import Attenuation
			self._attenuation = Attenuation(self._core, self._cmd_group)
		return self._attenuation

	@property
	def emf(self):
		"""emf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_emf'):
			from .Emf import Emf
			self._emf = Emf(self._core, self._cmd_group)
		return self._emf

	@property
	def level(self):
		"""level commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def limit(self):
		"""limit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import Limit
			self._limit = Limit(self._core, self._cmd_group)
		return self._limit

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_range'):
			from .Range import Range
			self._range = Range(self._core, self._cmd_group)
		return self._range

	@property
	def spc(self):
		"""spc commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_spc'):
			from .Spc import Spc
			self._spc = Spc(self._core, self._cmd_group)
		return self._spc

	@property
	def step(self):
		"""step commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_step'):
			from .Step import Step
			self._step = Step(self._core, self._cmd_group)
		return self._step

	def get_iq_pep(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:IQPep \n
		Snippet: value: float = driver.source.power.get_iq_pep() \n
		No command help available \n
			:return: ipart_qpep: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:IQPep?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_lbehaviour(self) -> enums.PowLevBehaviour:
		"""SCPI: [SOURce<HW>]:POWer:LBEHaviour \n
		Snippet: value: enums.PowLevBehaviour = driver.source.power.get_lbehaviour() \n
		Selects the level behavior at the RF output over time. \n
			:return: behaviour: AUTO| UNINterrupted| MONotone| CVSWr| CPHase UNINterrupted|MONotone Do not use the uninterrupted level settings and strictly monotone modes in combination with the high-quality optimization mode (see [:SOURcehw]:BB:IMPairment:OPTimization:MODE) CVSWr Constant VSWR CPHase Continuous phase CONStant Constant phase
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:LBEHaviour?')
		return Conversions.str_to_scalar_enum(response, enums.PowLevBehaviour)

	def set_lbehaviour(self, behaviour: enums.PowLevBehaviour) -> None:
		"""SCPI: [SOURce<HW>]:POWer:LBEHaviour \n
		Snippet: driver.source.power.set_lbehaviour(behaviour = enums.PowLevBehaviour.AUTO) \n
		Selects the level behavior at the RF output over time. \n
			:param behaviour: AUTO| UNINterrupted| MONotone| CVSWr| CPHase UNINterrupted|MONotone Do not use the uninterrupted level settings and strictly monotone modes in combination with the high-quality optimization mode (see [:SOURcehw]:BB:IMPairment:OPTimization:MODE) CVSWr Constant VSWR CPHase Continuous phase CONStant Constant phase
		"""
		param = Conversions.enum_scalar_to_str(behaviour, enums.PowLevBehaviour)
		self._core.io.write(f'SOURce<HwInstance>:POWer:LBEHaviour {param}')

	# noinspection PyTypeChecker
	def get_lmode(self) -> enums.PowLevMode:
		"""SCPI: [SOURce<HW>]:POWer:LMODe \n
		Snippet: value: enums.PowLevMode = driver.source.power.get_lmode() \n
		Sets the RF level mode. \n
			:return: lev_mode: NORMal| LOWNoise| LOWDistortion NORMal Supplies the RF signal with the standard power level of the instrument. LOWNoise Supplies a very low noise sinewave signal. LOWDistortion Supplies a very pure sinewave signal.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:LMODe?')
		return Conversions.str_to_scalar_enum(response, enums.PowLevMode)

	def set_lmode(self, lev_mode: enums.PowLevMode) -> None:
		"""SCPI: [SOURce<HW>]:POWer:LMODe \n
		Snippet: driver.source.power.set_lmode(lev_mode = enums.PowLevMode.LOWDistortion) \n
		Sets the RF level mode. \n
			:param lev_mode: NORMal| LOWNoise| LOWDistortion NORMal Supplies the RF signal with the standard power level of the instrument. LOWNoise Supplies a very low noise sinewave signal. LOWDistortion Supplies a very pure sinewave signal.
		"""
		param = Conversions.enum_scalar_to_str(lev_mode, enums.PowLevMode)
		self._core.io.write(f'SOURce<HwInstance>:POWer:LMODe {param}')

	def get_manual(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:MANual \n
		Snippet: value: float = driver.source.power.get_manual() \n
		Sets the level for the subsequent sweep step if [:SOURce<hw>]:SWEep:POWer:MODE. Use a separate command for each sweep
		step. \n
			:return: manual: float You can select any level within the setting range, where: STARt is set with [:SOURcehw]:POWer:STARt STOP is set with [:SOURcehw]:POWer:STOP OFFSet is set with [:SOURcehw]:POWer[:LEVel][:IMMediate]:OFFSet Range: (STARt + OFFSet) to (STOP + OFFSet) , Unit: dBm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:MANual?')
		return Conversions.str_to_float(response)

	def set_manual(self, manual: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:MANual \n
		Snippet: driver.source.power.set_manual(manual = 1.0) \n
		Sets the level for the subsequent sweep step if [:SOURce<hw>]:SWEep:POWer:MODE. Use a separate command for each sweep
		step. \n
			:param manual: float You can select any level within the setting range, where: STARt is set with [:SOURcehw]:POWer:STARt STOP is set with [:SOURcehw]:POWer:STOP OFFSet is set with [:SOURcehw]:POWer[:LEVel][:IMMediate]:OFFSet Range: (STARt + OFFSet) to (STOP + OFFSet) , Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(manual)
		self._core.io.write(f'SOURce<HwInstance>:POWer:MANual {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.LfFreqMode:
		"""SCPI: [SOURce<HW>]:POWer:MODE \n
		Snippet: value: enums.LfFreqMode = driver.source.power.get_mode() \n
		Selects the operating mode of the instrument to set the output level. \n
			:return: mode: CW| FIXed| SWEep CW|FIXed Operates at a constant level. CW and FIXed are synonyms. To set the output level value, use the command [:SOURcehw]:POWer[:LEVel][:IMMediate][:AMPLitude]. SWEep Sets sweep mode. Set the range and current level with the commands: [:SOURcehw]:POWer:STARt and [:SOURcehw]:POWer:STOP, [:SOURcehw]:POWer:MANual.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.LfFreqMode)

	def set_mode(self, mode: enums.LfFreqMode) -> None:
		"""SCPI: [SOURce<HW>]:POWer:MODE \n
		Snippet: driver.source.power.set_mode(mode = enums.LfFreqMode.CW) \n
		Selects the operating mode of the instrument to set the output level. \n
			:param mode: CW| FIXed| SWEep CW|FIXed Operates at a constant level. CW and FIXed are synonyms. To set the output level value, use the command [:SOURcehw]:POWer[:LEVel][:IMMediate][:AMPLitude]. SWEep Sets sweep mode. Set the range and current level with the commands: [:SOURcehw]:POWer:STARt and [:SOURcehw]:POWer:STOP, [:SOURcehw]:POWer:MANual.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.LfFreqMode)
		self._core.io.write(f'SOURce<HwInstance>:POWer:MODE {param}')

	def get_pep(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:PEP \n
		Snippet: value: float = driver.source.power.get_pep() \n
		Queries the PEP 'Peak Envelope Power) of digital modulation or digital standards at the RF output. This value corresponds
		to the level specification, displayed in the status bar (header) . \n
			:return: pep: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:PEP?')
		return Conversions.str_to_float(response)

	def get_power(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:POWer \n
		Snippet: value: float = driver.source.power.get_power() \n
		Sets the level at the RF output connector. This value does not consider a specified offset.
		The command [:SOURce<hw>]:POWer[:LEVel][:IMMediate][:AMPLitude] sets the level of the 'Level' display, that means the
		level containing offset. See 'Displayed RF frequency and level values with downstream instruments'. \n
			:return: power: float Level at the RF output, without level offset Range: See data sheet , Unit: dBm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:POWer?')
		return Conversions.str_to_float(response)

	def set_power(self, power: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:POWer \n
		Snippet: driver.source.power.set_power(power = 1.0) \n
		Sets the level at the RF output connector. This value does not consider a specified offset.
		The command [:SOURce<hw>]:POWer[:LEVel][:IMMediate][:AMPLitude] sets the level of the 'Level' display, that means the
		level containing offset. See 'Displayed RF frequency and level values with downstream instruments'. \n
			:param power: float Level at the RF output, without level offset Range: See data sheet , Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'SOURce<HwInstance>:POWer:POWer {param}')

	def get_start(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:STARt \n
		Snippet: value: float = driver.source.power.get_start() \n
		Sets the RF start/stop level in sweep mode. \n
			:return: start: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:STARt?')
		return Conversions.str_to_float(response)

	def set_start(self, start: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:STARt \n
		Snippet: driver.source.power.set_start(start = 1.0) \n
		Sets the RF start/stop level in sweep mode. \n
			:param start: float Sets the setting range calculated as follows: (Level_min + OFFSet) to (Level_max + OFFSet) Where the values are set with the commands: [:SOURcehw]:POWer[:LEVel][:IMMediate]:OFFSet [:SOURcehw]:POWer:STARt [:SOURcehw]:POWer:STOP Range: Minimum level to maximum level , Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(start)
		self._core.io.write(f'SOURce<HwInstance>:POWer:STARt {param}')

	def get_stop(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:STOP \n
		Snippet: value: float = driver.source.power.get_stop() \n
		Sets the RF start/stop level in sweep mode. \n
			:return: stop: float Sets the setting range calculated as follows: (Level_min + OFFSet) to (Level_max + OFFSet) Where the values are set with the commands: [:SOURcehw]:POWer[:LEVel][:IMMediate]:OFFSet [:SOURcehw]:POWer:STARt [:SOURcehw]:POWer:STOP Range: Minimum level to maximum level , Unit: dBm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:STOP?')
		return Conversions.str_to_float(response)

	def set_stop(self, stop: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:STOP \n
		Snippet: driver.source.power.set_stop(stop = 1.0) \n
		Sets the RF start/stop level in sweep mode. \n
			:param stop: float Sets the setting range calculated as follows: (Level_min + OFFSet) to (Level_max + OFFSet) Where the values are set with the commands: [:SOURcehw]:POWer[:LEVel][:IMMediate]:OFFSet [:SOURcehw]:POWer:STARt [:SOURcehw]:POWer:STOP Range: Minimum level to maximum level , Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(stop)
		self._core.io.write(f'SOURce<HwInstance>:POWer:STOP {param}')

	def get_wignore(self) -> bool:
		"""SCPI: [SOURce]:POWer:WIGNore \n
		Snippet: value: bool = driver.source.power.get_wignore() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce:POWer:WIGNore?')
		return Conversions.str_to_bool(response)

	def set_wignore(self, state: bool) -> None:
		"""SCPI: [SOURce]:POWer:WIGNore \n
		Snippet: driver.source.power.set_wignore(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce:POWer:WIGNore {param}')

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
