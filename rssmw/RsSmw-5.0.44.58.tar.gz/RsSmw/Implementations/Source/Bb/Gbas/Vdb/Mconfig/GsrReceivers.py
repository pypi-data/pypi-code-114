from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GsrReceivers:
	"""GsrReceivers commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gsrReceivers", core, parent)

	def set(self, gsrr: enums.GbasGrdStRefRec, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:GSRReceivers \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.gsrReceivers.set(gsrr = enums.GbasGrdStRefRec.GW2R, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the number of ground station reference receivers. \n
			:param gsrr: GW3R| GW4R| GW2R
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.enum_scalar_to_str(gsrr, enums.GbasGrdStRefRec)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:GSRReceivers {param}')

	# noinspection PyTypeChecker
	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> enums.GbasGrdStRefRec:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:GSRReceivers \n
		Snippet: value: enums.GbasGrdStRefRec = driver.source.bb.gbas.vdb.mconfig.gsrReceivers.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the number of ground station reference receivers. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: gsrr: GW3R| GW4R| GW2R"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:GSRReceivers?')
		return Conversions.str_to_scalar_enum(response, enums.GbasGrdStRefRec)
