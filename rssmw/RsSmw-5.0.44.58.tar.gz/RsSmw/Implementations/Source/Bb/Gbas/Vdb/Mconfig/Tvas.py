from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tvas:
	"""Tvas commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tvas", core, parent)

	def set(self, tvas: float, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:TVAS \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.tvas.set(tvas = 1.0, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Requires 'Mode > GBAS' (LAAS) header information. Sets the value of the broadcast vertical alert limit. \n
			:param tvas: float Range: 0 to 127
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.decimal_value_to_str(tvas)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:TVAS {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:TVAS \n
		Snippet: value: float = driver.source.bb.gbas.vdb.mconfig.tvas.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Requires 'Mode > GBAS' (LAAS) header information. Sets the value of the broadcast vertical alert limit. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: tvas: float Range: 0 to 127"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:TVAS?')
		return Conversions.str_to_float(response)
