from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NsRatio:
	"""NsRatio commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsRatio", core, parent)

	@property
	def mtime(self):
		"""mtime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mtime'):
			from .Mtime import Mtime
			self._mtime = Mtime(self._core, self._cmd_group)
		return self._mtime

	def set(self, ns_ratio: float, channel=repcap.Channel.Default) -> None:
		"""SCPI: SENSe<CH>:[POWer]:FILTer:NSRatio \n
		Snippet: driver.sense.power.filterPy.nsRatio.set(ns_ratio = 1.0, channel = repcap.Channel.Default) \n
		Sets an upper limit for the relative noise content in fixed noise filter mode (method RsSmw.Sense.Power.FilterPy.TypePy.
		set) . This value determines the proportion of intrinsic noise in the measurement results. \n
			:param ns_ratio: float Range: 0.001 to 1
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
		"""
		param = Conversions.decimal_value_to_str(ns_ratio)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe{channel_cmd_val}:POWer:FILTer:NSRatio {param}')

	def get(self, channel=repcap.Channel.Default) -> float:
		"""SCPI: SENSe<CH>:[POWer]:FILTer:NSRatio \n
		Snippet: value: float = driver.sense.power.filterPy.nsRatio.get(channel = repcap.Channel.Default) \n
		Sets an upper limit for the relative noise content in fixed noise filter mode (method RsSmw.Sense.Power.FilterPy.TypePy.
		set) . This value determines the proportion of intrinsic noise in the measurement results. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
			:return: ns_ratio: float Range: 0.001 to 1"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe{channel_cmd_val}:POWer:FILTer:NSRatio?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'NsRatio':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NsRatio(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
