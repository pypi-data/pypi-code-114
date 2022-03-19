from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ibs:
	"""Ibs commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ibs", core, parent)

	@property
	def a(self):
		"""a commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_a'):
			from .A import A
			self._a = A(self._core, self._cmd_group)
		return self._a

	@property
	def b(self):
		"""b commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_b'):
			from .B import B
			self._b = B(self._core, self._cmd_group)
		return self._b

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:IBS \n
		Snippet: value: bool = driver.source.bb.t2Dvb.plp.ibs.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Queries the in-band signaling state. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: ibs: 1| ON| 0| OFF"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:IBS?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Ibs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ibs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
