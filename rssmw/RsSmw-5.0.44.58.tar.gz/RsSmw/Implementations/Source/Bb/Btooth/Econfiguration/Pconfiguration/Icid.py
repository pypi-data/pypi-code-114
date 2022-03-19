from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Icid:
	"""Icid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("icid", core, parent)

	def set(self, icid: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ICID \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.icid.set(icid = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Sets the advertiser´s device address. For advertising channel packets, the format of the device address differs,
		depending on the selected address type.
			INTRO_CMD_HELP: Selects the clock source: \n
			- 'Public Address Types' The public address is given from the registration authority IEEE and is composed of:
			Table Header:  \n
			- LSB: 24 bits = company_assigned
			- MSB: 24 bits = company_id
			- 'Random Address Type' is a 48-bits random static device address.
			- 'Private Address Type' A private address is optional and composed of:
			Table Header:  \n
			- LSB: 24 bits = hash
			- MSB: 24 bits = random \n
			:param icid: numeric
			:param bitcount: integer Range: 24 to 24
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('icid', icid, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ICID {param}'.rstrip())

	# noinspection PyTypeChecker
	class IcidStruct(StructBase):
		"""Response structure. Fields: \n
			- Icid: List[str]: numeric
			- Bitcount: int: integer Range: 24 to 24"""
		__meta_args_list = [
			ArgStruct('Icid', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Icid: List[str] = None
			self.Bitcount: int = None

	def get(self) -> IcidStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:ICID \n
		Snippet: value: IcidStruct = driver.source.bb.btooth.econfiguration.pconfiguration.icid.get() \n
		Sets the advertiser´s device address. For advertising channel packets, the format of the device address differs,
		depending on the selected address type.
			INTRO_CMD_HELP: Selects the clock source: \n
			- 'Public Address Types' The public address is given from the registration authority IEEE and is composed of:
			Table Header:  \n
			- LSB: 24 bits = company_assigned
			- MSB: 24 bits = company_id
			- 'Random Address Type' is a 48-bits random static device address.
			- 'Private Address Type' A private address is optional and composed of:
			Table Header:  \n
			- LSB: 24 bits = hash
			- MSB: 24 bits = random \n
			:return: structure: for return value, see the help for IcidStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:ICID?', self.__class__.IcidStruct())
