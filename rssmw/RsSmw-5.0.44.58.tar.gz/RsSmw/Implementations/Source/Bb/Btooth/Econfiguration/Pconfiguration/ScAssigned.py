from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScAssigned:
	"""ScAssigned commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scAssigned", core, parent)

	def set(self, sc_assigned: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SCASsigned \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.scAssigned.set(sc_assigned = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		Sets the advertiser´s device address. For advertising channel packets, the format of the device address differs,
		depending on the selected address type.
			INTRO_CMD_HELP: You can enable one or more PHYs: \n
			- 'Public Address Types' The public address is given from the registration authority IEEE and is composed of:
			Table Header:  \n
			- LSB: 24 bits = company_assigned
			- MSB: 24 bits = company_id
			- 'Random Address Type' is a 48-bits random static device address.
			- 'Private Address Type' A private address is optional and composed of:
			Table Header:  \n
			- LSB: 24 bits = hash
			- MSB: 24 bits = random \n
			:param sc_assigned: numeric
			:param bitcount: integer Range: 24 to 24
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('sc_assigned', sc_assigned, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SCASsigned {param}'.rstrip())

	# noinspection PyTypeChecker
	class ScAssignedStruct(StructBase):
		"""Response structure. Fields: \n
			- Sc_Assigned: List[str]: No parameter help available
			- Bitcount: int: integer Range: 24 to 24"""
		__meta_args_list = [
			ArgStruct('Sc_Assigned', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sc_Assigned: List[str] = None
			self.Bitcount: int = None

	def get(self) -> ScAssignedStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:SCASsigned \n
		Snippet: value: ScAssignedStruct = driver.source.bb.btooth.econfiguration.pconfiguration.scAssigned.get() \n
		Sets the advertiser´s device address. For advertising channel packets, the format of the device address differs,
		depending on the selected address type.
			INTRO_CMD_HELP: You can enable one or more PHYs: \n
			- 'Public Address Types' The public address is given from the registration authority IEEE and is composed of:
			Table Header:  \n
			- LSB: 24 bits = company_assigned
			- MSB: 24 bits = company_id
			- 'Random Address Type' is a 48-bits random static device address.
			- 'Private Address Type' A private address is optional and composed of:
			Table Header:  \n
			- LSB: 24 bits = hash
			- MSB: 24 bits = random \n
			:return: structure: for return value, see the help for ScAssignedStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:SCASsigned?', self.__class__.ScAssignedStruct())
