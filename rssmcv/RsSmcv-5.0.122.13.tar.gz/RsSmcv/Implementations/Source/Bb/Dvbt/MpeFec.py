from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MpeFec:
	"""MpeFec commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mpeFec", core, parent)

	def get_low(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBT:MPEFec:LOW \n
		Snippet: value: bool = driver.source.bb.dvbt.mpeFec.get_low() \n
		Enables/disables . If enabled, 1 TPS bit (s49) is used to signal that MPE FEC is used in at least one data stream. \n
			:return: mpe_fec_lp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:MPEFec:LOW?')
		return Conversions.str_to_bool(response)

	def set_low(self, mpe_fec_lp: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:MPEFec:LOW \n
		Snippet: driver.source.bb.dvbt.mpeFec.set_low(mpe_fec_lp = False) \n
		Enables/disables . If enabled, 1 TPS bit (s49) is used to signal that MPE FEC is used in at least one data stream. \n
			:param mpe_fec_lp: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(mpe_fec_lp)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:MPEFec:LOW {param}')

	def get_high(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBT:MPEFec:[HIGH] \n
		Snippet: value: bool = driver.source.bb.dvbt.mpeFec.get_high() \n
		Enables/disables . If enabled, 1 TPS bit (s49) is used to signal that MPE FEC is used in at least one data stream. \n
			:return: mpe_fec_hp: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:MPEFec:HIGH?')
		return Conversions.str_to_bool(response)

	def set_high(self, mpe_fec_hp: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:MPEFec:[HIGH] \n
		Snippet: driver.source.bb.dvbt.mpeFec.set_high(mpe_fec_hp = False) \n
		Enables/disables . If enabled, 1 TPS bit (s49) is used to signal that MPE FEC is used in at least one data stream. \n
			:param mpe_fec_hp: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(mpe_fec_hp)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:MPEFec:HIGH {param}')
