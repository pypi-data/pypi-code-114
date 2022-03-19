from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rpif:
	"""Rpif commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rpif", core, parent)

	def set(self, rpif: str, vdbTransmitter=repcap.VdbTransmitter.Default, fdbTransmitter=repcap.FdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:FDB<ST>:RPIF \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.fdb.rpif.set(rpif = '1', vdbTransmitter = repcap.VdbTransmitter.Default, fdbTransmitter = repcap.FdbTransmitter.Default) \n
		Sets the reference path identifier for FAS. \n
			:param rpif: string Three or four alphanumeric characters
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param fdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fdb')
		"""
		param = Conversions.value_to_quoted_str(rpif)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		fdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(fdbTransmitter, repcap.FdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:FDB{fdbTransmitter_cmd_val}:RPIF {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default, fdbTransmitter=repcap.FdbTransmitter.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:FDB<ST>:RPIF \n
		Snippet: value: str = driver.source.bb.gbas.vdb.mconfig.fdb.rpif.get(vdbTransmitter = repcap.VdbTransmitter.Default, fdbTransmitter = repcap.FdbTransmitter.Default) \n
		Sets the reference path identifier for FAS. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param fdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fdb')
			:return: rpif: string Three or four alphanumeric characters"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		fdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(fdbTransmitter, repcap.FdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:FDB{fdbTransmitter_cmd_val}:RPIF?')
		return trim_str_response(response)
