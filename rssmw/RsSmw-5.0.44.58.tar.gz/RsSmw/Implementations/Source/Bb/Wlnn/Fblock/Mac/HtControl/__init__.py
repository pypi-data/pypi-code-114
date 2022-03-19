from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HtControl:
	"""HtControl commands group definition. 13 total commands, 11 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("htControl", core, parent)

	@property
	def acConstraint(self):
		"""acConstraint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acConstraint'):
			from .AcConstraint import AcConstraint
			self._acConstraint = AcConstraint(self._core, self._cmd_group)
		return self._acConstraint

	@property
	def calibration(self):
		"""calibration commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_calibration'):
			from .Calibration import Calibration
			self._calibration = Calibration(self._core, self._cmd_group)
		return self._calibration

	@property
	def csiSteering(self):
		"""csiSteering commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csiSteering'):
			from .CsiSteering import CsiSteering
			self._csiSteering = CsiSteering(self._core, self._cmd_group)
		return self._csiSteering

	@property
	def frequest(self):
		"""frequest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequest'):
			from .Frequest import Frequest
			self._frequest = Frequest(self._core, self._cmd_group)
		return self._frequest

	@property
	def hvIndicator(self):
		"""hvIndicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hvIndicator'):
			from .HvIndicator import HvIndicator
			self._hvIndicator = HvIndicator(self._core, self._cmd_group)
		return self._hvIndicator

	@property
	def laControl(self):
		"""laControl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_laControl'):
			from .LaControl import LaControl
			self._laControl = LaControl(self._core, self._cmd_group)
		return self._laControl

	@property
	def ndp(self):
		"""ndp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndp'):
			from .Ndp import Ndp
			self._ndp = Ndp(self._core, self._cmd_group)
		return self._ndp

	@property
	def rdgMore(self):
		"""rdgMore commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rdgMore'):
			from .RdgMore import RdgMore
			self._rdgMore = RdgMore(self._core, self._cmd_group)
		return self._rdgMore

	@property
	def reserved(self):
		"""reserved commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reserved'):
			from .Reserved import Reserved
			self._reserved = Reserved(self._core, self._cmd_group)
		return self._reserved

	@property
	def sreserved(self):
		"""sreserved commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sreserved'):
			from .Sreserved import Sreserved
			self._sreserved = Sreserved(self._core, self._cmd_group)
		return self._sreserved

	@property
	def zlf(self):
		"""zlf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zlf'):
			from .Zlf import Zlf
			self._zlf = Zlf(self._core, self._cmd_group)
		return self._zlf

	def set(self, ht_control: List[str], frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:HTControl \n
		Snippet: driver.source.bb.wlnn.fblock.mac.htControl.set(ht_control = ['raw1', 'raw2', 'raw3'], frameBlock = repcap.FrameBlock.Default) \n
		Sets the value for the HT control field. \n
			:param ht_control: integer Range: #H00000000,32 to #HFFFFFFFF,32
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		param = Conversions.list_to_csv_str(ht_control)
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:HTControl {param}')

	def get(self, frameBlock=repcap.FrameBlock.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:MAC:HTControl \n
		Snippet: value: List[str] = driver.source.bb.wlnn.fblock.mac.htControl.get(frameBlock = repcap.FrameBlock.Default) \n
		Sets the value for the HT control field. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:return: ht_control: integer Range: #H00000000,32 to #HFFFFFFFF,32"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:MAC:HTControl?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'HtControl':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HtControl(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
