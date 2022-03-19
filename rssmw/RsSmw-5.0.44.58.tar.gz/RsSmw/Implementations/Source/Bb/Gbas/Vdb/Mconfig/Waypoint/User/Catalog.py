from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:WAYPoint:USER:CATalog \n
		Snippet: value: List[str] = driver.source.bb.gbas.vdb.mconfig.waypoint.user.catalog.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Requires 'Mode > GBAS' (LAAS) header information. Queries the names of the existing user defined/predefined waypoint
		files. Per default, the instrument saves user-defined files in the /var/user/ directory. Use the command method RsSmw.
		MassMemory.currentDirectory to change the default directory to the currently used one. Only files with extension *.
		txt are listed. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: gbas_mc_waypoint_cat_name_user: No help available"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:WAYPoint:USER:CATalog?')
		return Conversions.str_to_str_list(response)
