from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CoDevice:
	"""CoDevice commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coDevice", core, parent)

	def set(self, co_device: List[str], bitcount: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:CODevice \n
		Snippet: driver.source.bb.btooth.pconfiguration.coDevice.set(co_device = ['raw1', 'raw2', 'raw3'], bitcount = 1) \n
		A parameter received during the device discovery procedure, indicates the type of device and which types of service that
		are supported. \n
			:param co_device: numeric Range: #H000000 to #HFFFFFF
			:param bitcount: integer Range: 24 to 24
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('co_device', co_device, DataType.RawStringList, None), ArgSingle('bitcount', bitcount, DataType.Integer))
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:CODevice {param}'.rstrip())

	# noinspection PyTypeChecker
	class CoDeviceStruct(StructBase):
		"""Response structure. Fields: \n
			- Co_Device: List[str]: numeric Range: #H000000 to #HFFFFFF
			- Bitcount: int: integer Range: 24 to 24"""
		__meta_args_list = [
			ArgStruct('Co_Device', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Co_Device: List[str] = None
			self.Bitcount: int = None

	def get(self) -> CoDeviceStruct:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:PCONfiguration:CODevice \n
		Snippet: value: CoDeviceStruct = driver.source.bb.btooth.pconfiguration.coDevice.get() \n
		A parameter received during the device discovery procedure, indicates the type of device and which types of service that
		are supported. \n
			:return: structure: for return value, see the help for CoDeviceStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce<HwInstance>:BB:BTOoth:PCONfiguration:CODevice?', self.__class__.CoDeviceStruct())
