from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class KcGps:
	"""KcGps commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("kcGps", core, parent)

	def set(self, kmd_ec_gps: float, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:KCGPs \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.kcGps.set(kmd_ec_gps = 1.0, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the ephemeris missed detection parameter (Kmd_e) , category I precision approach and approach with vertical guidance
		(APV) . This is a multiplier considered when calculating the ephemeris error position bound for the category I precision
		approach and APV. It is derived from the probability that a detection is missed because of an ephemeris error in a
		GPS/GLONASS satellite. \n
			:param kmd_ec_gps: float Range: 0 to 12.75
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.decimal_value_to_str(kmd_ec_gps)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:KCGPs {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:KCGPs \n
		Snippet: value: float = driver.source.bb.gbas.vdb.mconfig.kcGps.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the ephemeris missed detection parameter (Kmd_e) , category I precision approach and approach with vertical guidance
		(APV) . This is a multiplier considered when calculating the ephemeris error position bound for the category I precision
		approach and APV. It is derived from the probability that a detection is missed because of an ephemeris error in a
		GPS/GLONASS satellite. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: kmd_ec_gps: float Range: 0 to 12.75"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:KCGPs?')
		return Conversions.str_to_float(response)
