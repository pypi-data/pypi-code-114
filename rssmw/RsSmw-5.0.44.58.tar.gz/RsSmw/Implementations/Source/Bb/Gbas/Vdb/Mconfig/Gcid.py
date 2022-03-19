from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gcid:
	"""Gcid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gcid", core, parent)

	def set(self, gcid: enums.GbasGcid, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:GCID \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.gcid.set(gcid = enums.GbasGcid.FC, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the ground station continuity/integrity designator. \n
			:param gcid: FC| FD
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.enum_scalar_to_str(gcid, enums.GbasGcid)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:GCID {param}')

	# noinspection PyTypeChecker
	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> enums.GbasGcid:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:GCID \n
		Snippet: value: enums.GbasGcid = driver.source.bb.gbas.vdb.mconfig.gcid.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the ground station continuity/integrity designator. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: gcid: FC| FD"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:GCID?')
		return Conversions.str_to_scalar_enum(response, enums.GbasGcid)
