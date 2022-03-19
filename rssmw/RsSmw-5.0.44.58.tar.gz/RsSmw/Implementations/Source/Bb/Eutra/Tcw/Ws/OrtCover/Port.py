from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Port:
	"""Port commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: PortNull, default value after init: PortNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("port", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_portNull_get', 'repcap_portNull_set', repcap.PortNull.Nr0)

	def repcap_portNull_set(self, portNull: repcap.PortNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to PortNull.Default
		Default value after init: PortNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(portNull)

	def repcap_portNull_get(self) -> repcap.PortNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def get(self, portNull=repcap.PortNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TCW:WS:ORTCover:[PORT<CH0>] \n
		Snippet: value: int = driver.source.bb.eutra.tcw.ws.ortCover.port.get(portNull = repcap.PortNull.Default) \n
		Queries the used resource index n_PUCCH. \n
			:param portNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Port')
			:return: ortho_cover: integer Range: 2 to 2"""
		portNull_cmd_val = self._cmd_group.get_repcap_cmd_value(portNull, repcap.PortNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:TCW:WS:ORTCover:PORT{portNull_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Port':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Port(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
