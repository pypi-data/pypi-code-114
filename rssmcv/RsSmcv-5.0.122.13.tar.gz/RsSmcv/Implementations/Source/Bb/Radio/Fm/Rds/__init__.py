from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rds:
	"""Rds commands group definition. 135 total commands, 7 Subgroups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rds", core, parent)

	@property
	def af(self):
		"""af commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_af'):
			from .Af import Af
			self._af = Af(self._core, self._cmd_group)
		return self._af

	@property
	def di(self):
		"""di commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_di'):
			from .Di import Di
			self._di = Di(self._core, self._cmd_group)
		return self._di

	@property
	def eon(self):
		"""eon commands group. 1 Sub-classes, 10 commands."""
		if not hasattr(self, '_eon'):
			from .Eon import Eon
			self._eon = Eon(self._core, self._cmd_group)
		return self._eon

	@property
	def group(self):
		"""group commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_group'):
			from .Group import Group
			self._group = Group(self._core, self._cmd_group)
		return self._group

	@property
	def opf(self):
		"""opf commands group. 24 Sub-classes, 1 commands."""
		if not hasattr(self, '_opf'):
			from .Opf import Opf
			self._opf = Opf(self._core, self._cmd_group)
		return self._opf

	@property
	def tmc(self):
		"""tmc commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_tmc'):
			from .Tmc import Tmc
			self._tmc = Tmc(self._core, self._cmd_group)
		return self._tmc

	@property
	def tp(self):
		"""tp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp'):
			from .Tp import Tp
			self._tp = Tp(self._core, self._cmd_group)
		return self._tp

	def get_ct(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:CT \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.get_ct() \n
		Enables/disables the clock time and date information. \n
			:return: ct: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:CT?')
		return Conversions.str_to_bool(response)

	def set_ct(self, ct: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:CT \n
		Snippet: driver.source.bb.radio.fm.rds.set_ct(ct = False) \n
		Enables/disables the clock time and date information. \n
			:param ct: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(ct)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:CT {param}')

	def get_ct_offset(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:CTOFfset \n
		Snippet: value: str = driver.source.bb.radio.fm.rds.get_ct_offset() \n
		Sets the clock time offset. \n
			:return: ct_offset: string Range: 00:00 to 99:59
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:CTOFfset?')
		return trim_str_response(response)

	def set_ct_offset(self, ct_offset: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:CTOFfset \n
		Snippet: driver.source.bb.radio.fm.rds.set_ct_offset(ct_offset = '1') \n
		Sets the clock time offset. \n
			:param ct_offset: string Range: 00:00 to 99:59
		"""
		param = Conversions.value_to_quoted_str(ct_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:CTOFfset {param}')

	def get_deviation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:DEViation \n
		Snippet: value: float = driver.source.bb.radio.fm.rds.get_deviation() \n
		Defines the resulting frequency deviation of the radio data system irrespective of the audio signals. \n
			:return: freq_dev_rds: float Range: 0 to 10, Unit: kHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:DEViation?')
		return Conversions.str_to_float(response)

	def set_deviation(self, freq_dev_rds: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:DEViation \n
		Snippet: driver.source.bb.radio.fm.rds.set_deviation(freq_dev_rds = 1.0) \n
		Defines the resulting frequency deviation of the radio data system irrespective of the audio signals. \n
			:param freq_dev_rds: float Range: 0 to 10, Unit: kHz
		"""
		param = Conversions.decimal_value_to_str(freq_dev_rds)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:DEViation {param}')

	# noinspection PyTypeChecker
	def get_ms(self) -> enums.TxAudioBcFmRdsMs:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:MS \n
		Snippet: value: enums.TxAudioBcFmRdsMs = driver.source.bb.radio.fm.rds.get_ms() \n
		Identifies if the transmission contains music or speech. \n
			:return: ms: MUSic| SPEech
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:MS?')
		return Conversions.str_to_scalar_enum(response, enums.TxAudioBcFmRdsMs)

	def set_ms(self, ms: enums.TxAudioBcFmRdsMs) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:MS \n
		Snippet: driver.source.bb.radio.fm.rds.set_ms(ms = enums.TxAudioBcFmRdsMs.MUSic) \n
		Identifies if the transmission contains music or speech. \n
			:param ms: MUSic| SPEech
		"""
		param = Conversions.enum_scalar_to_str(ms, enums.TxAudioBcFmRdsMs)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:MS {param}')

	def get_pi(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:PI \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.get_pi() \n
		Sets the program identification, that is a 16-bit value in hexadecimal representation. \n
			:return: pi: integer Range: #H0000 to #HFFFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:PI?')
		return Conversions.str_to_int(response)

	def set_pi(self, pi: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:PI \n
		Snippet: driver.source.bb.radio.fm.rds.set_pi(pi = 1) \n
		Sets the program identification, that is a 16-bit value in hexadecimal representation. \n
			:param pi: integer Range: #H0000 to #HFFFF
		"""
		param = Conversions.decimal_value_to_str(pi)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:PI {param}')

	def get_ps(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:PS \n
		Snippet: value: str = driver.source.bb.radio.fm.rds.get_ps() \n
		Sets the program service name. \n
			:return: ps: string Up to eight characters in ASCII format, see Figure 'Character sets for names'.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:PS?')
		return trim_str_response(response)

	def set_ps(self, ps: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:PS \n
		Snippet: driver.source.bb.radio.fm.rds.set_ps(ps = '1') \n
		Sets the program service name. \n
			:param ps: string Up to eight characters in ASCII format, see Figure 'Character sets for names'.
		"""
		param = Conversions.value_to_quoted_str(ps)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:PS {param}')

	def get_pty(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:PTY \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.get_pty() \n
		Sets the program type. \n
			:return: pty: integer Range: 0 to 31
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:PTY?')
		return Conversions.str_to_int(response)

	def set_pty(self, pty: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:PTY \n
		Snippet: driver.source.bb.radio.fm.rds.set_pty(pty = 1) \n
		Sets the program type. \n
			:param pty: integer Range: 0 to 31
		"""
		param = Conversions.decimal_value_to_str(pty)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:PTY {param}')

	def get_ptyn(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:PTYN \n
		Snippet: value: str = driver.source.bb.radio.fm.rds.get_ptyn() \n
		Sets the program type name. \n
			:return: ptyn: string Up to eight characters in ASCII format, see Figure 'Character sets for names'.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:PTYN?')
		return trim_str_response(response)

	def set_ptyn(self, ptyn: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:PTYN \n
		Snippet: driver.source.bb.radio.fm.rds.set_ptyn(ptyn = '1') \n
		Sets the program type name. \n
			:param ptyn: string Up to eight characters in ASCII format, see Figure 'Character sets for names'.
		"""
		param = Conversions.value_to_quoted_str(ptyn)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:PTYN {param}')

	def get_rt(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:RT \n
		Snippet: value: str = driver.source.bb.radio.fm.rds.get_rt() \n
		Sets the radio text. \n
			:return: rt: string Up to 64 characters in ASCII format, see Figure 'Character sets for names'.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:RT?')
		return trim_str_response(response)

	def set_rt(self, rt: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:RT \n
		Snippet: driver.source.bb.radio.fm.rds.set_rt(rt = '1') \n
		Sets the radio text. \n
			:param rt: string Up to 64 characters in ASCII format, see Figure 'Character sets for names'.
		"""
		param = Conversions.value_to_quoted_str(rt)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:RT {param}')

	def get_ta(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TA \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.get_ta() \n
		Enables/disables the traffic announcement flag. \n
			:return: ta: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:TA?')
		return Conversions.str_to_bool(response)

	def set_ta(self, ta: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TA \n
		Snippet: driver.source.bb.radio.fm.rds.set_ta(ta = False) \n
		Enables/disables the traffic announcement flag. \n
			:param ta: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(ta)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:TA {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:[STATe] \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.get_state() \n
		Enables/disables /. \n
			:return: rds_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, rds_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:[STATe] \n
		Snippet: driver.source.bb.radio.fm.rds.set_state(rds_state = False) \n
		Enables/disables /. \n
			:param rds_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(rds_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:STATe {param}')

	def clone(self) -> 'Rds':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rds(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
