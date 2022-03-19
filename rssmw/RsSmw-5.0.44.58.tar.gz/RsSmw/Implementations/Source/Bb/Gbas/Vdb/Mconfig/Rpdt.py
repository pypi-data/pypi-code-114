from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rpdt:
	"""Rpdt commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rpdt", core, parent)

	def set(self, rpdt: int, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:RPDT \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.rpdt.set(rpdt = 1, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Requires 'Mode > GBAS' (LAAS) header information. Sets the reference path data selector. \n
			:param rpdt: integer Range: 0 to 254
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.decimal_value_to_str(rpdt)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:RPDT {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:RPDT \n
		Snippet: value: int = driver.source.bb.gbas.vdb.mconfig.rpdt.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Requires 'Mode > GBAS' (LAAS) header information. Sets the reference path data selector. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: rpdt: integer Range: 0 to 254"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:RPDT?')
		return Conversions.str_to_int(response)
