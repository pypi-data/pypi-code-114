from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AnPattern:
	"""AnPattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: AntennaPattern, default value after init: AntennaPattern.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("anPattern", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_antennaPattern_get', 'repcap_antennaPattern_set', repcap.AntennaPattern.Nr0)

	def repcap_antennaPattern_set(self, antennaPattern: repcap.AntennaPattern) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AntennaPattern.Default
		Default value after init: AntennaPattern.Nr0"""
		self._cmd_group.set_repcap_enum_value(antennaPattern)

	def repcap_antennaPattern_get(self) -> repcap.AntennaPattern:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, an_pattern: List[str], bitcount: int, subframeNull=repcap.SubframeNull.Default, cellNull=repcap.CellNull.Default, antennaPattern=repcap.AntennaPattern.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[SUBF<ST0>]:ENCC:PHICh:CELL<CH0>:ANPattern<GR0> \n
		Snippet: driver.source.bb.oneweb.downlink.subf.encc.phich.cell.anPattern.set(an_pattern = ['raw1', 'raw2', 'raw3'], bitcount = 1, subframeNull = repcap.SubframeNull.Default, cellNull = repcap.CellNull.Default, antennaPattern = repcap.AntennaPattern.Default) \n
		No command help available \n
			:param an_pattern: No help available
			:param bitcount: No help available
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param antennaPattern: optional repeated capability selector. Default value: Nr0 (settable in the interface 'AnPattern')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('an_pattern', an_pattern, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		antennaPattern_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPattern, repcap.AntennaPattern)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:SUBF{subframeNull_cmd_val}:ENCC:PHICh:CELL{cellNull_cmd_val}:ANPattern{antennaPattern_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class AnPatternStruct(StructBase):
		"""Response structure. Fields: \n
			- An_Pattern: List[str]: No parameter help available
			- Bitcount: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct('An_Pattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.An_Pattern: List[str] = None
			self.Bitcount: int = None

	def get(self, subframeNull=repcap.SubframeNull.Default, cellNull=repcap.CellNull.Default, antennaPattern=repcap.AntennaPattern.Default) -> AnPatternStruct:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[SUBF<ST0>]:ENCC:PHICh:CELL<CH0>:ANPattern<GR0> \n
		Snippet: value: AnPatternStruct = driver.source.bb.oneweb.downlink.subf.encc.phich.cell.anPattern.get(subframeNull = repcap.SubframeNull.Default, cellNull = repcap.CellNull.Default, antennaPattern = repcap.AntennaPattern.Default) \n
		No command help available \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param antennaPattern: optional repeated capability selector. Default value: Nr0 (settable in the interface 'AnPattern')
			:return: structure: for return value, see the help for AnPatternStruct structure arguments."""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		antennaPattern_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPattern, repcap.AntennaPattern)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:ONEWeb:DL:SUBF{subframeNull_cmd_val}:ENCC:PHICh:CELL{cellNull_cmd_val}:ANPattern{antennaPattern_cmd_val}?', self.__class__.AnPatternStruct())

	def clone(self) -> 'AnPattern':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AnPattern(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
