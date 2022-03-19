from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fcontrol:
	"""Fcontrol commands group definition. 13 total commands, 0 Subgroups, 13 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fcontrol", core, parent)

	def get_cf_extension(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:CFEXtension \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.fcontrol.get_cf_extension() \n
		Set the value of the individual bits of the frame control field. \n
			:return: extension: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:CFEXtension?')
		return Conversions.str_to_str_list(response)

	def set_cf_extension(self, extension: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:CFEXtension \n
		Snippet: driver.source.bb.wlad.pconfig.mac.fcontrol.set_cf_extension(extension = ['raw1', 'raw2', 'raw3']) \n
		Set the value of the individual bits of the frame control field. \n
			:param extension: 2 bits
		"""
		param = Conversions.list_to_csv_str(extension)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:CFEXtension {param}')

	def get_fds(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:FDS \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.fcontrol.get_fds() \n
		Set the value of the individual bits of the frame control field. \n
			:return: fds: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:FDS?')
		return Conversions.str_to_str_list(response)

	def set_fds(self, fds: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:FDS \n
		Snippet: driver.source.bb.wlad.pconfig.mac.fcontrol.set_fds(fds = ['raw1', 'raw2', 'raw3']) \n
		Set the value of the individual bits of the frame control field. \n
			:param fds: 2 bits
		"""
		param = Conversions.list_to_csv_str(fds)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:FDS {param}')

	def get_mdata(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:MDATa \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.fcontrol.get_mdata() \n
		Set the value of the individual bits of the frame control field. \n
			:return: mdata: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:MDATa?')
		return Conversions.str_to_str_list(response)

	def set_mdata(self, mdata: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:MDATa \n
		Snippet: driver.source.bb.wlad.pconfig.mac.fcontrol.set_mdata(mdata = ['raw1', 'raw2', 'raw3']) \n
		Set the value of the individual bits of the frame control field. \n
			:param mdata: 2 bits
		"""
		param = Conversions.list_to_csv_str(mdata)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:MDATa {param}')

	def get_mfragments(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:MFRagments \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.fcontrol.get_mfragments() \n
		Set the value of the individual bits of the frame control field. \n
			:return: mfragments: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:MFRagments?')
		return Conversions.str_to_str_list(response)

	def set_mfragments(self, mfragments: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:MFRagments \n
		Snippet: driver.source.bb.wlad.pconfig.mac.fcontrol.set_mfragments(mfragments = ['raw1', 'raw2', 'raw3']) \n
		Set the value of the individual bits of the frame control field. \n
			:param mfragments: 2 bits
		"""
		param = Conversions.list_to_csv_str(mfragments)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:MFRagments {param}')

	def get_order(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:ORDer \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.fcontrol.get_order() \n
		Set the value of the individual bits of the frame control field. \n
			:return: order: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:ORDer?')
		return Conversions.str_to_str_list(response)

	def set_order(self, order: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:ORDer \n
		Snippet: driver.source.bb.wlad.pconfig.mac.fcontrol.set_order(order = ['raw1', 'raw2', 'raw3']) \n
		Set the value of the individual bits of the frame control field. \n
			:param order: 2 bits
		"""
		param = Conversions.list_to_csv_str(order)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:ORDer {param}')

	def get_pframe(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:PFRame \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.fcontrol.get_pframe() \n
		Set the value of the individual bits of the frame control field. \n
			:return: protd_frm: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:PFRame?')
		return Conversions.str_to_str_list(response)

	def set_pframe(self, protd_frm: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:PFRame \n
		Snippet: driver.source.bb.wlad.pconfig.mac.fcontrol.set_pframe(protd_frm = ['raw1', 'raw2', 'raw3']) \n
		Set the value of the individual bits of the frame control field. \n
			:param protd_frm: 2 bits
		"""
		param = Conversions.list_to_csv_str(protd_frm)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:PFRame {param}')

	def get_pmanagement(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:PMANagement \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.fcontrol.get_pmanagement() \n
		Set the value of the individual bits of the frame control field. \n
			:return: pmanagement: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:PMANagement?')
		return Conversions.str_to_str_list(response)

	def set_pmanagement(self, pmanagement: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:PMANagement \n
		Snippet: driver.source.bb.wlad.pconfig.mac.fcontrol.set_pmanagement(pmanagement = ['raw1', 'raw2', 'raw3']) \n
		Set the value of the individual bits of the frame control field. \n
			:param pmanagement: 2 bits
		"""
		param = Conversions.list_to_csv_str(pmanagement)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:PMANagement {param}')

	def get_pversion(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:PVERsion \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.fcontrol.get_pversion() \n
		Set the value of the individual bits of the frame control field. \n
			:return: pversion: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:PVERsion?')
		return Conversions.str_to_str_list(response)

	def set_pversion(self, pversion: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:PVERsion \n
		Snippet: driver.source.bb.wlad.pconfig.mac.fcontrol.set_pversion(pversion = ['raw1', 'raw2', 'raw3']) \n
		Set the value of the individual bits of the frame control field. \n
			:param pversion: 2 bits
		"""
		param = Conversions.list_to_csv_str(pversion)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:PVERsion {param}')

	def get_retry(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:RETRy \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.fcontrol.get_retry() \n
		Set the value of the individual bits of the frame control field. \n
			:return: retry: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:RETRy?')
		return Conversions.str_to_str_list(response)

	def set_retry(self, retry: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:RETRy \n
		Snippet: driver.source.bb.wlad.pconfig.mac.fcontrol.set_retry(retry = ['raw1', 'raw2', 'raw3']) \n
		Set the value of the individual bits of the frame control field. \n
			:param retry: 2 bits
		"""
		param = Conversions.list_to_csv_str(retry)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:RETRy {param}')

	def get_sub_type(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:SUBType \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.fcontrol.get_sub_type() \n
		Set the value of the individual bits of the frame control field. \n
			:return: sub_type: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:SUBType?')
		return Conversions.str_to_str_list(response)

	def set_sub_type(self, sub_type: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:SUBType \n
		Snippet: driver.source.bb.wlad.pconfig.mac.fcontrol.set_sub_type(sub_type = ['raw1', 'raw2', 'raw3']) \n
		Set the value of the individual bits of the frame control field. \n
			:param sub_type: 2 bits
		"""
		param = Conversions.list_to_csv_str(sub_type)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:SUBType {param}')

	def get_tds(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:TDS \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.fcontrol.get_tds() \n
		Set the value of the individual bits of the frame control field. \n
			:return: tds: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:TDS?')
		return Conversions.str_to_str_list(response)

	def set_tds(self, tds: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:TDS \n
		Snippet: driver.source.bb.wlad.pconfig.mac.fcontrol.set_tds(tds = ['raw1', 'raw2', 'raw3']) \n
		Set the value of the individual bits of the frame control field. \n
			:param tds: 2 bits
		"""
		param = Conversions.list_to_csv_str(tds)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:TDS {param}')

	def get_type_py(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:TYPE \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.fcontrol.get_type_py() \n
		Set the value of the individual bits of the frame control field. \n
			:return: type_py: 2 bits
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:TYPE?')
		return Conversions.str_to_str_list(response)

	def set_type_py(self, type_py: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol:TYPE \n
		Snippet: driver.source.bb.wlad.pconfig.mac.fcontrol.set_type_py(type_py = ['raw1', 'raw2', 'raw3']) \n
		Set the value of the individual bits of the frame control field. \n
			:param type_py: 2 bits
		"""
		param = Conversions.list_to_csv_str(type_py)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol:TYPE {param}')

	def get_value(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.fcontrol.get_value() \n
		Sets the value of the frame control field. The frame control field has a length of 2 bytes (16 bits) and is used to
		define, for example, the protocol version, the frame type, and its function. As an alternative, the individual bits can
		be set. \n
			:return: fcontrol: 16 bits
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol?')
		return Conversions.str_to_str_list(response)

	def set_value(self, fcontrol: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:FCONtrol \n
		Snippet: driver.source.bb.wlad.pconfig.mac.fcontrol.set_value(fcontrol = ['raw1', 'raw2', 'raw3']) \n
		Sets the value of the frame control field. The frame control field has a length of 2 bytes (16 bits) and is used to
		define, for example, the protocol version, the frame type, and its function. As an alternative, the individual bits can
		be set. \n
			:param fcontrol: 16 bits
		"""
		param = Conversions.list_to_csv_str(fcontrol)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:FCONtrol {param}')
