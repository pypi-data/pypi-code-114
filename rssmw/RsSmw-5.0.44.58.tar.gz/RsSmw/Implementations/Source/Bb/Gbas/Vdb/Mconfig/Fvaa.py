from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fvaa:
	"""Fvaa commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fvaa", core, parent)

	def set(self, fvaa: float, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:FVAA \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.fvaa.set(fvaa = 1.0, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Requires 'Mode > GBAS' (LAAS) header information. Sets the value of the broadcast vertical alert limit. \n
			:param fvaa: float Range: 0 to 25.4
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.decimal_value_to_str(fvaa)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:FVAA {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:FVAA \n
		Snippet: value: float = driver.source.bb.gbas.vdb.mconfig.fvaa.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Requires 'Mode > GBAS' (LAAS) header information. Sets the value of the broadcast vertical alert limit. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: fvaa: float Range: 0 to 25.4"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:FVAA?')
		return Conversions.str_to_float(response)
