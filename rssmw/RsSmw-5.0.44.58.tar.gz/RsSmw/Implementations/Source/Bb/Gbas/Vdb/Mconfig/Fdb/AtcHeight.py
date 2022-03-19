from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AtcHeight:
	"""AtcHeight commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("atcHeight", core, parent)

	def set(self, tch: float, vdbTransmitter=repcap.VdbTransmitter.Default, fdbTransmitter=repcap.FdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:FDB<ST>:ATCHeight \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.fdb.atcHeight.set(tch = 1.0, vdbTransmitter = repcap.VdbTransmitter.Default, fdbTransmitter = repcap.FdbTransmitter.Default) \n
		Requires 'Mode > GBAS' (LAAS) header information. Sets the approach threshold crossing height. \n
			:param tch: float Range: 0 to 1638.35
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param fdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fdb')
		"""
		param = Conversions.decimal_value_to_str(tch)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		fdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(fdbTransmitter, repcap.FdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:FDB{fdbTransmitter_cmd_val}:ATCHeight {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default, fdbTransmitter=repcap.FdbTransmitter.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:FDB<ST>:ATCHeight \n
		Snippet: value: float = driver.source.bb.gbas.vdb.mconfig.fdb.atcHeight.get(vdbTransmitter = repcap.VdbTransmitter.Default, fdbTransmitter = repcap.FdbTransmitter.Default) \n
		Requires 'Mode > GBAS' (LAAS) header information. Sets the approach threshold crossing height. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param fdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fdb')
			:return: tch: float Range: 0 to 1638.35"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		fdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(fdbTransmitter, repcap.FdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:FDB{fdbTransmitter_cmd_val}:ATCHeight?')
		return Conversions.str_to_float(response)
