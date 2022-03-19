from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, pattern: List[str], bitcount: int, macPdu=repcap.MacPdu.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MPDU<ST>:DATA:PATTern \n
		Snippet: driver.source.bb.wlad.pconfig.mpdu.data.pattern.set(pattern = ['raw1', 'raw2', 'raw3'], bitcount = 1, macPdu = repcap.MacPdu.Default) \n
		Determines the bit pattern for the PATTern selection. \n
			:param pattern: numeric
			:param bitcount: integer Range: 1 to 64
			:param macPdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mpdu')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('pattern', pattern, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		macPdu_cmd_val = self._cmd_group.get_repcap_cmd_value(macPdu, repcap.MacPdu)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MPDU{macPdu_cmd_val}:DATA:PATTern {param}'.rstrip())

	# noinspection PyTypeChecker
	class PatternStruct(StructBase):
		"""Response structure. Fields: \n
			- Pattern: List[str]: numeric
			- Bitcount: int: integer Range: 1 to 64"""
		__meta_args_list = [
			ArgStruct('Pattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pattern: List[str] = None
			self.Bitcount: int = None

	def get(self, macPdu=repcap.MacPdu.Default) -> PatternStruct:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MPDU<ST>:DATA:PATTern \n
		Snippet: value: PatternStruct = driver.source.bb.wlad.pconfig.mpdu.data.pattern.get(macPdu = repcap.MacPdu.Default) \n
		Determines the bit pattern for the PATTern selection. \n
			:param macPdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mpdu')
			:return: structure: for return value, see the help for PatternStruct structure arguments."""
		macPdu_cmd_val = self._cmd_group.get_repcap_cmd_value(macPdu, repcap.MacPdu)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MPDU{macPdu_cmd_val}:DATA:PATTern?', self.__class__.PatternStruct())
