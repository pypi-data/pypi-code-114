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

	def set(self, pattern: List[str], bitcount: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:FBI:PATTern \n
		Snippet: driver.source.bb.w3Gpp.mstation.pcpch.fbi.pattern.set(pattern = ['raw1', 'raw2', 'raw3'], bitcount = 1, mobileStation = repcap.MobileStation.Default) \n
		The command determines the bit pattern for the FBI field when the PATTern data source is selected. The maximum length of
		the pattern is 32 bits. The first parameter determines the bit pattern (choice of hexadecimal, octal or binary notation) ,
		the second specifies the number of bits to use. \n
			:param pattern: numeric
			:param bitcount: integer Range: 1 to 32
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('pattern', pattern, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:FBI:PATTern {param}'.rstrip())

	# noinspection PyTypeChecker
	class PatternStruct(StructBase):
		"""Response structure. Fields: \n
			- Pattern: List[str]: numeric
			- Bitcount: int: integer Range: 1 to 32"""
		__meta_args_list = [
			ArgStruct('Pattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pattern: List[str] = None
			self.Bitcount: int = None

	def get(self, mobileStation=repcap.MobileStation.Default) -> PatternStruct:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:PCPCh:FBI:PATTern \n
		Snippet: value: PatternStruct = driver.source.bb.w3Gpp.mstation.pcpch.fbi.pattern.get(mobileStation = repcap.MobileStation.Default) \n
		The command determines the bit pattern for the FBI field when the PATTern data source is selected. The maximum length of
		the pattern is 32 bits. The first parameter determines the bit pattern (choice of hexadecimal, octal or binary notation) ,
		the second specifies the number of bits to use. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: structure: for return value, see the help for PatternStruct structure arguments."""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:PCPCh:FBI:PATTern?', self.__class__.PatternStruct())
