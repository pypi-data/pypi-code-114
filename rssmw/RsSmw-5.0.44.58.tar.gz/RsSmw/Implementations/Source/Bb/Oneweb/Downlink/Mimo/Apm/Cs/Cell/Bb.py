from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bb:
	"""Bb commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: BasebandNull, default value after init: BasebandNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bb", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_basebandNull_get', 'repcap_basebandNull_set', repcap.BasebandNull.Nr0)

	def repcap_basebandNull_set(self, basebandNull: repcap.BasebandNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BasebandNull.Default
		Default value after init: BasebandNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(basebandNull)

	def repcap_basebandNull_get(self) -> repcap.BasebandNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, ant_port_cc_index: enums.OneWebCcIndex, basebandNull=repcap.BasebandNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:MIMO:APM:CS:CELL:BB<ST0> \n
		Snippet: driver.source.bb.oneweb.downlink.mimo.apm.cs.cell.bb.set(ant_port_cc_index = enums.OneWebCcIndex.PC, basebandNull = repcap.BasebandNull.Default) \n
		Maps a component carrier to a baseband. \n
			:param ant_port_cc_index: PC| SC1
			:param basebandNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bb')
		"""
		param = Conversions.enum_scalar_to_str(ant_port_cc_index, enums.OneWebCcIndex)
		basebandNull_cmd_val = self._cmd_group.get_repcap_cmd_value(basebandNull, repcap.BasebandNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:MIMO:APM:CS:CELL:BB{basebandNull_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, basebandNull=repcap.BasebandNull.Default) -> enums.OneWebCcIndex:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:MIMO:APM:CS:CELL:BB<ST0> \n
		Snippet: value: enums.OneWebCcIndex = driver.source.bb.oneweb.downlink.mimo.apm.cs.cell.bb.get(basebandNull = repcap.BasebandNull.Default) \n
		Maps a component carrier to a baseband. \n
			:param basebandNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bb')
			:return: ant_port_cc_index: PC| SC1"""
		basebandNull_cmd_val = self._cmd_group.get_repcap_cmd_value(basebandNull, repcap.BasebandNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:MIMO:APM:CS:CELL:BB{basebandNull_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.OneWebCcIndex)

	def clone(self) -> 'Bb':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bb(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
