from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BhConfig:
	"""BhConfig commands group definition. 8 total commands, 4 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bhConfig", core, parent)

	@property
	def adfl(self):
		"""adfl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_adfl'):
			from .Adfl import Adfl
			self._adfl = Adfl(self._core, self._cmd_group)
		return self._adfl

	@property
	def iactive(self):
		"""iactive commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iactive'):
			from .Iactive import Iactive
			self._iactive = Iactive(self._core, self._cmd_group)
		return self._iactive

	@property
	def nactive(self):
		"""nactive commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nactive'):
			from .Nactive import Nactive
			self._nactive = Nactive(self._core, self._cmd_group)
		return self._nactive

	@property
	def sbyte(self):
		"""sbyte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sbyte'):
			from .Sbyte import Sbyte
			self._sbyte = Sbyte(self._core, self._cmd_group)
		return self._sbyte

	# noinspection PyTypeChecker
	def get_cacm(self) -> enums.DvbS2XccmAcm:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:BHConfig:CACM \n
		Snippet: value: enums.DvbS2XccmAcm = driver.source.bb.dvb.dvbs.bhConfig.get_cacm() \n
		Selects whether constant coding and modulation (CCM) or adaptive coding and modulation (ACM) communication is used. \n
			:return: cacm: CCM| ACM
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:BHConfig:CACM?')
		return Conversions.str_to_scalar_enum(response, enums.DvbS2XccmAcm)

	def set_cacm(self, cacm: enums.DvbS2XccmAcm) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:BHConfig:CACM \n
		Snippet: driver.source.bb.dvb.dvbs.bhConfig.set_cacm(cacm = enums.DvbS2XccmAcm.ACM) \n
		Selects whether constant coding and modulation (CCM) or adaptive coding and modulation (ACM) communication is used. \n
			:param cacm: CCM| ACM
		"""
		param = Conversions.enum_scalar_to_str(cacm, enums.DvbS2XccmAcm)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:BHConfig:CACM {param}')

	def get_dfl(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:BHConfig:DFL \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.bhConfig.get_dfl() \n
		Sets the data field length (DFL) . \n
			:return: df_length: integer Range: 1 to 7264
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:BHConfig:DFL?')
		return Conversions.str_to_int(response)

	def set_dfl(self, df_length: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:BHConfig:DFL \n
		Snippet: driver.source.bb.dvb.dvbs.bhConfig.set_dfl(df_length = 1) \n
		Sets the data field length (DFL) . \n
			:param df_length: integer Range: 1 to 7264
		"""
		param = Conversions.decimal_value_to_str(df_length)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:BHConfig:DFL {param}')

	def get_upl(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:BHConfig:UPL \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.bhConfig.get_upl() \n
		Sets the user packet length (UPL) . \n
			:return: up_length: integer Range: 1 to 8192
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:BHConfig:UPL?')
		return Conversions.str_to_int(response)

	def set_upl(self, up_length: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:BHConfig:UPL \n
		Snippet: driver.source.bb.dvb.dvbs.bhConfig.set_upl(up_length = 1) \n
		Sets the user packet length (UPL) . \n
			:param up_length: integer Range: 1 to 8192
		"""
		param = Conversions.decimal_value_to_str(up_length)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:BHConfig:UPL {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:BHConfig:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.bhConfig.get_state() \n
		Inserts baseband header information in the stream. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:BHConfig:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:BHConfig:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbs.bhConfig.set_state(state = False) \n
		Inserts baseband header information in the stream. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:BHConfig:STATe {param}')

	def clone(self) -> 'BhConfig':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BhConfig(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
