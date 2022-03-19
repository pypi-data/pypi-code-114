from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LmVariation:
	"""LmVariation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lmVariation", core, parent)

	def set(self, lmv: float, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:LMVariation \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.lmVariation.set(lmv = 1.0, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the local magnetic variation. \n
			:param lmv: float A positive value represents an east variation (clockwise from true north) Range: -180 to 180, Unit: deg
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.decimal_value_to_str(lmv)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:LMVariation {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:LMVariation \n
		Snippet: value: float = driver.source.bb.gbas.vdb.mconfig.lmVariation.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the local magnetic variation. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: lmv: float A positive value represents an east variation (clockwise from true north) Range: -180 to 180, Unit: deg"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:LMVariation?')
		return Conversions.str_to_float(response)
