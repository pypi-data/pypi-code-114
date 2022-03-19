from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	def get_all(self) -> List[int]:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID:GPS:LIST:ALL \n
		Snippet: value: List[int] = driver.source.bb.gnss.svid.gps.listPy.get_all() \n
		Queries the SV IDs of all satellites of the GNSS system. The query lists SV IDs of the satellites included in and
		excluded from the satellite constellation (Figure 'Satellites constellation: Understanding the displayed information') . \n
			:return: id_pi_db_gnss_sat_sv_id_list_all: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('SOURce<HwInstance>:BB:GNSS:SVID:GPS:LIST:ALL?')
		return response

	def get_valid(self) -> List[int]:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID:GPS:LIST:[VALid] \n
		Snippet: value: List[int] = driver.source.bb.gnss.svid.gps.listPy.get_valid() \n
		Queries the SV IDs of all valid satellites for the GNSS system. The query lists SV IDs of the satellites included in the
		satellite constellation. \n
			:return: gnss_sat_sv_id_list: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('SOURce<HwInstance>:BB:GNSS:SVID:GPS:LIST:VALid?')
		return response
