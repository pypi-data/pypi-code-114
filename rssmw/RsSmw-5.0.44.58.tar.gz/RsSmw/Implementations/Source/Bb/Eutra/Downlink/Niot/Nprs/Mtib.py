from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mtib:
	"""Mtib commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mtib", core, parent)

	def set(self, nprs_muting_info_b: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:NPRS:MTIB \n
		Snippet: driver.source.bb.eutra.downlink.niot.nprs.mtib.set(nprs_muting_info_b = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Sets the nprs-MutingInfoA/nprs-MutingInfoB parameter, required if muting is used for the NPRS part A (and Part B)
		configurations. \n
			:param nprs_muting_info_b: numeric '1' indicates that the NPRS is transmitted in the corresponding occasion; a '0' indicates a muted NPRS.
			:param bitcount: integer Sets the length of the periodically repeating NPRS bit sequence in number of NPRS position occurrences. Allowed are the following values: 2, 4, 8 or 16 Range: 2 to 16
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('nprs_muting_info_b', nprs_muting_info_b, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:NPRS:MTIB {param}'.rstrip())

	# noinspection PyTypeChecker
	class MtibStruct(StructBase):
		"""Response structure. Fields: \n
			- Nprs_Muting_Info_B: List[str]: numeric '1' indicates that the NPRS is transmitted in the corresponding occasion; a '0' indicates a muted NPRS.
			- Bitcount: int: integer Sets the length of the periodically repeating NPRS bit sequence in number of NPRS position occurrences. Allowed are the following values: 2, 4, 8 or 16 Range: 2 to 16"""
		__meta_args_list = [
			ArgStruct('Nprs_Muting_Info_B', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Nprs_Muting_Info_B: List[str] = None
			self.Bitcount: int = None

	def get(self) -> MtibStruct:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:NPRS:MTIB \n
		Snippet: value: MtibStruct = driver.source.bb.eutra.downlink.niot.nprs.mtib.get() \n
		Sets the nprs-MutingInfoA/nprs-MutingInfoB parameter, required if muting is used for the NPRS part A (and Part B)
		configurations. \n
			:return: structure: for return value, see the help for MtibStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:NPRS:MTIB?', self.__class__.MtibStruct())
