from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class KpGlonass:
	"""KpGlonass commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("kpGlonass", core, parent)

	def set(self, kmd_epos_glonass: float, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:KPGLonass \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.kpGlonass.set(kmd_epos_glonass = 1.0, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the ephemeris missed detection parameter (Kmd_e) , GBAS positioning service . This is a multiplier considered when
		calculating the ephemeris error position bound for the GBAS positioning. It is derived from the probability that a
		detection is missed because of an ephemeris error in a GPS/GLONASS satellite. \n
			:param kmd_epos_glonass: float Range: 0 to 12.75
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.decimal_value_to_str(kmd_epos_glonass)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:KPGLonass {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:KPGLonass \n
		Snippet: value: float = driver.source.bb.gbas.vdb.mconfig.kpGlonass.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the ephemeris missed detection parameter (Kmd_e) , GBAS positioning service . This is a multiplier considered when
		calculating the ephemeris error position bound for the GBAS positioning. It is derived from the probability that a
		detection is missed because of an ephemeris error in a GPS/GLONASS satellite. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: kmd_epos_glonass: No help available"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:KPGLonass?')
		return Conversions.str_to_float(response)
