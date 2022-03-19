from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GhConfig:
	"""GhConfig commands group definition. 11 total commands, 7 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ghConfig", core, parent)

	@property
	def fid(self):
		"""fid commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fid'):
			from .Fid import Fid
			self._fid = Fid(self._core, self._cmd_group)
		return self._fid

	@property
	def fiUse(self):
		"""fiUse commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fiUse'):
			from .FiUse import FiUse
			self._fiUse = FiUse(self._core, self._cmd_group)
		return self._fiUse

	@property
	def label(self):
		"""label commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_label'):
			from .Label import Label
			self._label = Label(self._core, self._cmd_group)
		return self._label

	@property
	def luse(self):
		"""luse commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_luse'):
			from .Luse import Luse
			self._luse = Luse(self._core, self._cmd_group)
		return self._luse

	@property
	def ptUse(self):
		"""ptUse commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ptUse'):
			from .PtUse import PtUse
			self._ptUse = PtUse(self._core, self._cmd_group)
		return self._ptUse

	@property
	def ptype(self):
		"""ptype commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ptype'):
			from .Ptype import Ptype
			self._ptype = Ptype(self._core, self._cmd_group)
		return self._ptype

	@property
	def tluse(self):
		"""tluse commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tluse'):
			from .Tluse import Tluse
			self._tluse = Tluse(self._core, self._cmd_group)
		return self._tluse

	def get_glength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:GLENgth \n
		Snippet: value: int = driver.source.bb.dvb.dvbx.ghConfig.get_glength() \n
		Sets the number of bytes following in the GSE packet. \n
			:return: glength: integer Range: 1 to 4096
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:GLENgth?')
		return Conversions.str_to_int(response)

	def set_glength(self, glength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:GLENgth \n
		Snippet: driver.source.bb.dvb.dvbx.ghConfig.set_glength(glength = 1) \n
		Sets the number of bytes following in the GSE packet. \n
			:param glength: integer Range: 1 to 4096
		"""
		param = Conversions.decimal_value_to_str(glength)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:GLENgth {param}')

	def get_ltype(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:LTYPe \n
		Snippet: value: int = driver.source.bb.dvb.dvbx.ghConfig.get_ltype() \n
		Set the type of the used label field. \n
			:return: ltype: integer Range: 0 to 3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:LTYPe?')
		return Conversions.str_to_int(response)

	def set_ltype(self, ltype: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:LTYPe \n
		Snippet: driver.source.bb.dvb.dvbx.ghConfig.set_ltype(ltype = 1) \n
		Set the type of the used label field. \n
			:param ltype: integer Range: 0 to 3
		"""
		param = Conversions.decimal_value_to_str(ltype)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:LTYPe {param}')

	def get_tlength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:TLENgth \n
		Snippet: value: int = driver.source.bb.dvb.dvbx.ghConfig.get_tlength() \n
		Queries the total length. \n
			:return: tlength: integer Range: 1 to 65536, Unit: bytes
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:TLENgth?')
		return Conversions.str_to_int(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbx.ghConfig.get_state() \n
		Inserts header information in the transport stream. \n
			:return: gh_active: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, gh_active: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbx.ghConfig.set_state(gh_active = False) \n
		Inserts header information in the transport stream. \n
			:param gh_active: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(gh_active)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:STATe {param}')

	def clone(self) -> 'GhConfig':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GhConfig(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
