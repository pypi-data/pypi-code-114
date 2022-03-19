from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsdSelector:
	"""RsdSelector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsdSelector", core, parent)

	def set(self, rsds: int, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:RSDSelector \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.rsdSelector.set(rsds = 1, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the numerical identifier for selecting the ground subsystem. \n
			:param rsds: integer Range: 0 to 48
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.decimal_value_to_str(rsds)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:RSDSelector {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:RSDSelector \n
		Snippet: value: int = driver.source.bb.gbas.vdb.mconfig.rsdSelector.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the numerical identifier for selecting the ground subsystem. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: rsds: integer Range: 0 to 48"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:RSDSelector?')
		return Conversions.str_to_int(response)
