from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Niot:
	"""Niot commands group definition. 96 total commands, 9 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("niot", core, parent)

	@property
	def alloc(self):
		"""alloc commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_alloc'):
			from .Alloc import Alloc
			self._alloc = Alloc(self._core, self._cmd_group)
		return self._alloc

	@property
	def ccoding(self):
		"""ccoding commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_ccoding'):
			from .Ccoding import Ccoding
			self._ccoding = Ccoding(self._core, self._cmd_group)
		return self._ccoding

	@property
	def dci(self):
		"""dci commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_dci'):
			from .Dci import Dci
			self._dci = Dci(self._core, self._cmd_group)
		return self._dci

	@property
	def gap(self):
		"""gap commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_gap'):
			from .Gap import Gap
			self._gap = Gap(self._core, self._cmd_group)
		return self._gap

	@property
	def lteCell(self):
		"""lteCell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lteCell'):
			from .LteCell import LteCell
			self._lteCell = LteCell(self._core, self._cmd_group)
		return self._lteCell

	@property
	def nprs(self):
		"""nprs commands group. 3 Sub-classes, 8 commands."""
		if not hasattr(self, '_nprs'):
			from .Nprs import Nprs
			self._nprs = Nprs(self._core, self._cmd_group)
		return self._nprs

	@property
	def pag(self):
		"""pag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pag'):
			from .Pag import Pag
			self._pag = Pag(self._core, self._cmd_group)
		return self._pag

	@property
	def rand(self):
		"""rand commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_rand'):
			from .Rand import Rand
			self._rand = Rand(self._core, self._cmd_group)
		return self._rand

	@property
	def wus(self):
		"""wus commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_wus'):
			from .Wus import Wus
			self._wus = Wus(self._core, self._cmd_group)
		return self._wus

	def get_id(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:ID \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.get_id() \n
		Queries the physical layer identity. \n
			:return: identity: integer Range: 0 to 111
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:ID?')
		return Conversions.str_to_int(response)

	def get_nalloc(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:NALLoc \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.get_nalloc() \n
		Queries the number of NB-IoT allocations. \n
			:return: nb_iot_nalloc: integer Range: 0 to 42
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:NALLoc?')
		return Conversions.str_to_int(response)

	def get_puncture(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:PUNCture \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.niot.get_puncture() \n
		Punctures the LTE signal at the NB-IoT in-band or guard band carriers. \n
			:return: puncture_inband: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:PUNCture?')
		return Conversions.str_to_bool(response)

	def set_puncture(self, puncture_inband: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:PUNCture \n
		Snippet: driver.source.bb.eutra.downlink.niot.set_puncture(puncture_inband = False) \n
		Punctures the LTE signal at the NB-IoT in-band or guard band carriers. \n
			:param puncture_inband: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(puncture_inband)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:PUNCture {param}')

	def clone(self) -> 'Niot':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Niot(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
