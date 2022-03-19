from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eon:
	"""Eon commands group definition. 16 total commands, 1 Subgroups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eon", core, parent)

	@property
	def af(self):
		"""af commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_af'):
			from .Af import Af
			self._af = Af(self._core, self._cmd_group)
		return self._af

	def get_eg(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:EG \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.eon.get_eg() \n
		Enables the enhanced other network extended generic indicator. \n
			:return: eon_eg: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:EG?')
		return Conversions.str_to_bool(response)

	def set_eg(self, eon_eg: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:EG \n
		Snippet: driver.source.bb.radio.fm.rds.eon.set_eg(eon_eg = False) \n
		Enables the enhanced other network extended generic indicator. \n
			:param eon_eg: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(eon_eg)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:EG {param}')

	def get_ils(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:ILS \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.eon.get_ils() \n
		Enables the enhanced other network international linkage set indicator. \n
			:return: eon_ils: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:ILS?')
		return Conversions.str_to_bool(response)

	def set_ils(self, eon_ils: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:ILS \n
		Snippet: driver.source.bb.radio.fm.rds.eon.set_ils(eon_ils = False) \n
		Enables the enhanced other network international linkage set indicator. \n
			:param eon_ils: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(eon_ils)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:ILS {param}')

	def get_la(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:LA \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.eon.get_la() \n
		Enables the enhanced other network linkage actuator. \n
			:return: eon_la: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:LA?')
		return Conversions.str_to_bool(response)

	def set_la(self, eon_la: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:LA \n
		Snippet: driver.source.bb.radio.fm.rds.eon.set_la(eon_la = False) \n
		Enables the enhanced other network linkage actuator. \n
			:param eon_la: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(eon_la)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:LA {param}')

	def get_lsn(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:LSN \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.eon.get_lsn() \n
		Sets the enhanced other network linkage set number. The LSN comprises a 12-bit value in decimal representation. \n
			:return: eon_lsn: integer Range: 0 to 4095
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:LSN?')
		return Conversions.str_to_int(response)

	def set_lsn(self, eon_lsn: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:LSN \n
		Snippet: driver.source.bb.radio.fm.rds.eon.set_lsn(eon_lsn = 1) \n
		Sets the enhanced other network linkage set number. The LSN comprises a 12-bit value in decimal representation. \n
			:param eon_lsn: integer Range: 0 to 4095
		"""
		param = Conversions.decimal_value_to_str(eon_lsn)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:LSN {param}')

	def get_pi(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:PI \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.eon.get_pi() \n
		Sets the enhanced other network program identification. \n
			:return: eon_pi: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:PI?')
		return Conversions.str_to_int(response)

	def set_pi(self, eon_pi: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:PI \n
		Snippet: driver.source.bb.radio.fm.rds.eon.set_pi(eon_pi = 1) \n
		Sets the enhanced other network program identification. \n
			:param eon_pi: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(eon_pi)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:PI {param}')

	def get_pin(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:PIN \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.eon.get_pin() \n
		Sets the enhanced other network program item number. \n
			:return: eon_pin: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:PIN?')
		return Conversions.str_to_int(response)

	def set_pin(self, eon_pin: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:PIN \n
		Snippet: driver.source.bb.radio.fm.rds.eon.set_pin(eon_pin = 1) \n
		Sets the enhanced other network program item number. \n
			:param eon_pin: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(eon_pin)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:PIN {param}')

	def get_ps(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:PS \n
		Snippet: value: str = driver.source.bb.radio.fm.rds.eon.get_ps() \n
		Sets the enhanced other network program service name. \n
			:return: eon_ps: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:PS?')
		return trim_str_response(response)

	def set_ps(self, eon_ps: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:PS \n
		Snippet: driver.source.bb.radio.fm.rds.eon.set_ps(eon_ps = '1') \n
		Sets the enhanced other network program service name. \n
			:param eon_ps: string
		"""
		param = Conversions.value_to_quoted_str(eon_ps)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:PS {param}')

	def get_pty(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:PTY \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.eon.get_pty() \n
		Sets the enhanced other network program type. \n
			:return: eon_pty: integer Range: 0 to 31
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:PTY?')
		return Conversions.str_to_int(response)

	def set_pty(self, eon_pty: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:PTY \n
		Snippet: driver.source.bb.radio.fm.rds.eon.set_pty(eon_pty = 1) \n
		Sets the enhanced other network program type. \n
			:param eon_pty: integer Range: 0 to 31
		"""
		param = Conversions.decimal_value_to_str(eon_pty)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:PTY {param}')

	def get_tp(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:TP \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.eon.get_tp() \n
		Enables the enhanced other network traffic program. \n
			:return: eon_tp: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:TP?')
		return Conversions.str_to_bool(response)

	def set_tp(self, eon_tp: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:TP \n
		Snippet: driver.source.bb.radio.fm.rds.eon.set_tp(eon_tp = False) \n
		Enables the enhanced other network traffic program. \n
			:param eon_tp: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(eon_tp)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:TP {param}')

	def get_ta(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:Ta \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.eon.get_ta() \n
		Enables the enhanced other network traffic announcement. \n
			:return: eon_ta: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:EON:Ta?')
		return Conversions.str_to_bool(response)

	def set_ta(self, eon_ta: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:EON:Ta \n
		Snippet: driver.source.bb.radio.fm.rds.eon.set_ta(eon_ta = False) \n
		Enables the enhanced other network traffic announcement. \n
			:param eon_ta: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(eon_ta)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:EON:Ta {param}')

	def clone(self) -> 'Eon':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eon(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
