from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eew:
	"""Eew commands group definition. 13 total commands, 9 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eew", core, parent)

	@property
	def apai(self):
		"""apai commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apai'):
			from .Apai import Apai
			self._apai = Apai(self._core, self._cmd_group)
		return self._apai

	@property
	def ape1(self):
		"""ape1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ape1'):
			from .Ape1 import Ape1
			self._ape1 = Ape1(self._core, self._cmd_group)
		return self._ape1

	@property
	def ape2(self):
		"""ape2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ape2'):
			from .Ape2 import Ape2
			self._ape2 = Ape2(self._core, self._cmd_group)
		return self._ape2

	@property
	def depth(self):
		"""depth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_depth'):
			from .Depth import Depth
			self._depth = Depth(self._core, self._cmd_group)
		return self._depth

	@property
	def infoType(self):
		"""infoType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_infoType'):
			from .InfoType import InfoType
			self._infoType = InfoType(self._core, self._cmd_group)
		return self._infoType

	@property
	def latitude(self):
		"""latitude commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_latitude'):
			from .Latitude import Latitude
			self._latitude = Latitude(self._core, self._cmd_group)
		return self._latitude

	@property
	def longitude(self):
		"""longitude commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_longitude'):
			from .Longitude import Longitude
			self._longitude = Longitude(self._core, self._cmd_group)
		return self._longitude

	@property
	def occurence(self):
		"""occurence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_occurence'):
			from .Occurence import Occurence
			self._occurence = Occurence(self._core, self._cmd_group)
		return self._occurence

	@property
	def warnId(self):
		"""warnId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_warnId'):
			from .WarnId import WarnId
			self._warnId = WarnId(self._core, self._cmd_group)
		return self._warnId

	def get_area_info(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:AREAinfo \n
		Snippet: value: List[str] = driver.source.bb.isdbt.eew.get_area_info() \n
		Sets the target area of the seismic motion warning in hexadecimal presentation. \n
			:return: area_inf: integer Range: #H00000000000000 to #HFFFFFFFFFFFFFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:EEW:AREAinfo?')
		return Conversions.str_to_str_list(response)

	def set_area_info(self, area_inf: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:AREAinfo \n
		Snippet: driver.source.bb.isdbt.eew.set_area_info(area_inf = ['raw1', 'raw2', 'raw3']) \n
		Sets the target area of the seismic motion warning in hexadecimal presentation. \n
			:param area_inf: integer Range: #H00000000000000 to #HFFFFFFFFFFFFFF
		"""
		param = Conversions.list_to_csv_str(area_inf)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:EEW:AREAinfo {param}')

	def get_eew(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:EEW \n
		Snippet: value: bool = driver.source.bb.isdbt.eew.get_eew() \n
		Enables/disables the system. \n
			:return: eew: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:EEW:EEW?')
		return Conversions.str_to_bool(response)

	def set_eew(self, eew: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:EEW \n
		Snippet: driver.source.bb.isdbt.eew.set_eew(eew = False) \n
		Enables/disables the system. \n
			:param eew: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(eew)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:EEW:EEW {param}')

	def get_num_epicenter(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:NUMepicenter \n
		Snippet: value: int = driver.source.bb.isdbt.eew.get_num_epicenter() \n
		Identifies the total number of seismic motion information being transmitted. \n
			:return: num_epicenter: integer Range: 1 to 2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:EEW:NUMepicenter?')
		return Conversions.str_to_int(response)

	def set_num_epicenter(self, num_epicenter: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:NUMepicenter \n
		Snippet: driver.source.bb.isdbt.eew.set_num_epicenter(num_epicenter = 1) \n
		Identifies the total number of seismic motion information being transmitted. \n
			:param num_epicenter: integer Range: 1 to 2
		"""
		param = Conversions.decimal_value_to_str(num_epicenter)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:EEW:NUMepicenter {param}')

	# noinspection PyTypeChecker
	def get_signal_type(self) -> enums.IsdbtEewSignalType:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:SIGNaltype \n
		Snippet: value: enums.IsdbtEewSignalType = driver.source.bb.isdbt.eew.get_signal_type() \n
		Identifies the type of seismic motion warning. \n
			:return: signal_type: WWA| WWOA| TWA| TWOA
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:EEW:SIGNaltype?')
		return Conversions.str_to_scalar_enum(response, enums.IsdbtEewSignalType)

	def set_signal_type(self, signal_type: enums.IsdbtEewSignalType) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:SIGNaltype \n
		Snippet: driver.source.bb.isdbt.eew.set_signal_type(signal_type = enums.IsdbtEewSignalType.TWA) \n
		Identifies the type of seismic motion warning. \n
			:param signal_type: WWA| WWOA| TWA| TWOA
		"""
		param = Conversions.enum_scalar_to_str(signal_type, enums.IsdbtEewSignalType)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:EEW:SIGNaltype {param}')

	def clone(self) -> 'Eew':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eew(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
