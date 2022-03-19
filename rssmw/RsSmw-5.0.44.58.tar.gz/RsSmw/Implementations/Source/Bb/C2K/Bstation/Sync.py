from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sync:
	"""Sync commands group definition. 7 total commands, 0 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sync", core, parent)

	def get_cnumber(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:CNUMber \n
		Snippet: value: int = driver.source.bb.c2K.bstation.sync.get_cnumber() \n
		Sets the CDMA Channel Number which corresponds to the RF. \n
			:return: cnumber: integer Range: 0 to 2047
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:BSTation:SYNC:CNUMber?')
		return Conversions.str_to_int(response)

	def set_cnumber(self, cnumber: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:CNUMber \n
		Snippet: driver.source.bb.c2K.bstation.sync.set_cnumber(cnumber = 1) \n
		Sets the CDMA Channel Number which corresponds to the RF. \n
			:param cnumber: integer Range: 0 to 2047
		"""
		param = Conversions.decimal_value_to_str(cnumber)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation:SYNC:CNUMber {param}')

	def get_lc_state(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:LCSTate \n
		Snippet: value: List[str] = driver.source.bb.c2K.bstation.sync.get_lc_state() \n
		Defines the long code state in hexadecimal format. \n
			:return: lc_state: 42 bit Range: 0 to 3FFFFFFFFFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:BSTation:SYNC:LCSTate?')
		return Conversions.str_to_str_list(response)

	def set_lc_state(self, lc_state: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:LCSTate \n
		Snippet: driver.source.bb.c2K.bstation.sync.set_lc_state(lc_state = ['raw1', 'raw2', 'raw3']) \n
		Defines the long code state in hexadecimal format. \n
			:param lc_state: 42 bit Range: 0 to 3FFFFFFFFFF
		"""
		param = Conversions.list_to_csv_str(lc_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation:SYNC:LCSTate {param}')

	# noinspection PyTypeChecker
	def get_mp_rev(self) -> enums.MinPrEv:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:MPRev \n
		Snippet: value: enums.MinPrEv = driver.source.bb.c2K.bstation.sync.get_mp_rev() \n
		Sets the Minimum Protocol Revision Level. The base station sets this field to prevent mobile stations which cannot be
		supported by the base station from accessing the CDMA system. \n
			:return: mp_rev: 2| 8 Range: 2 to 8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:BSTation:SYNC:MPRev?')
		return Conversions.str_to_scalar_enum(response, enums.MinPrEv)

	def set_mp_rev(self, mp_rev: enums.MinPrEv) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:MPRev \n
		Snippet: driver.source.bb.c2K.bstation.sync.set_mp_rev(mp_rev = enums.MinPrEv._2) \n
		Sets the Minimum Protocol Revision Level. The base station sets this field to prevent mobile stations which cannot be
		supported by the base station from accessing the CDMA system. \n
			:param mp_rev: 2| 8 Range: 2 to 8
		"""
		param = Conversions.enum_scalar_to_str(mp_rev, enums.MinPrEv)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation:SYNC:MPRev {param}')

	def get_nid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:NID \n
		Snippet: value: int = driver.source.bb.c2K.bstation.sync.get_nid() \n
		Sets the Network Identification. The NID serves as a sub-identifier of a CDMA system as defined by the owner of the SID. \n
			:return: nid: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:BSTation:SYNC:NID?')
		return Conversions.str_to_int(response)

	def set_nid(self, nid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:NID \n
		Snippet: driver.source.bb.c2K.bstation.sync.set_nid(nid = 1) \n
		Sets the Network Identification. The NID serves as a sub-identifier of a CDMA system as defined by the owner of the SID. \n
			:param nid: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(nid)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation:SYNC:NID {param}')

	def get_prev(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:PREV \n
		Snippet: value: int = driver.source.bb.c2K.bstation.sync.get_prev() \n
		Sets the Protocol Revision Level, i.e. specifies the CDMA2000 system release number. The table below gives the
		cross-reference between the P_REV values and the CDMA2000 Releases.
			Table Header: P_REV / CDMA2000 Release \n
			- 1 / Korean PCS(Band Class4) , USPCS(Band Class1)
			- 2 / IS-95
			- 3 / TBS74
			- 4 / IS-95A
			- 5 / IS-95B
			- 6 / IS2000 Release 0
			- 7 / IS2000 Release A
			- 8 / IS2000 Release B \n
			:return: prev: integer Range: 1 to 8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:BSTation:SYNC:PREV?')
		return Conversions.str_to_int(response)

	def set_prev(self, prev: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:PREV \n
		Snippet: driver.source.bb.c2K.bstation.sync.set_prev(prev = 1) \n
		Sets the Protocol Revision Level, i.e. specifies the CDMA2000 system release number. The table below gives the
		cross-reference between the P_REV values and the CDMA2000 Releases.
			Table Header: P_REV / CDMA2000 Release \n
			- 1 / Korean PCS(Band Class4) , USPCS(Band Class1)
			- 2 / IS-95
			- 3 / TBS74
			- 4 / IS-95A
			- 5 / IS-95B
			- 6 / IS2000 Release 0
			- 7 / IS2000 Release A
			- 8 / IS2000 Release B \n
			:param prev: integer Range: 1 to 8
		"""
		param = Conversions.decimal_value_to_str(prev)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation:SYNC:PREV {param}')

	def get_sid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:SID \n
		Snippet: value: int = driver.source.bb.c2K.bstation.sync.get_sid() \n
		Displays the System Identification. The base station sets the system identification number. \n
			:return: sid: integer Range: 0 to 32767
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:BSTation:SYNC:SID?')
		return Conversions.str_to_int(response)

	def set_sid(self, sid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:SID \n
		Snippet: driver.source.bb.c2K.bstation.sync.set_sid(sid = 1) \n
		Displays the System Identification. The base station sets the system identification number. \n
			:param sid: integer Range: 0 to 32767
		"""
		param = Conversions.decimal_value_to_str(sid)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation:SYNC:SID {param}')

	def get_stime(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:STIMe \n
		Snippet: value: int = driver.source.bb.c2K.bstation.sync.get_stime() \n
		Displays the system time. \n
			:return: syst_time: integer Range: 0 to 68719476735
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:BSTation:SYNC:STIMe?')
		return Conversions.str_to_int(response)

	def set_stime(self, syst_time: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation:SYNC:STIMe \n
		Snippet: driver.source.bb.c2K.bstation.sync.set_stime(syst_time = 1) \n
		Displays the system time. \n
			:param syst_time: integer Range: 0 to 68719476735
		"""
		param = Conversions.decimal_value_to_str(syst_time)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation:SYNC:STIMe {param}')
