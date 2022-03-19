from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IcPhase:
	"""IcPhase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("icPhase", core, parent)

	def set(self, init_code_phase: float, satelliteSvid=repcap.SatelliteSvid.Default, vehicle=repcap.Vehicle.Default, antenna=repcap.Antenna.Default, echo=repcap.Echo.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:MPATh:[V<US>]:[A<GR>]:ECHO<S2US0>:ICPHase \n
		Snippet: driver.source.bb.gnss.svid.galileo.mpath.v.a.echo.icPhase.set(init_code_phase = 1.0, satelliteSvid = repcap.SatelliteSvid.Default, vehicle = repcap.Vehicle.Default, antenna = repcap.Antenna.Default, echo = repcap.Echo.Default) \n
		Sets an initial code phase for the selected echo. \n
			:param init_code_phase: float Range: 0 to 3000, Unit: m
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'A')
			:param echo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Echo')
		"""
		param = Conversions.decimal_value_to_str(init_code_phase)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		echo_cmd_val = self._cmd_group.get_repcap_cmd_value(echo, repcap.Echo)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:MPATh:V{vehicle_cmd_val}:A{antenna_cmd_val}:ECHO{echo_cmd_val}:ICPHase {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default, vehicle=repcap.Vehicle.Default, antenna=repcap.Antenna.Default, echo=repcap.Echo.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:MPATh:[V<US>]:[A<GR>]:ECHO<S2US0>:ICPHase \n
		Snippet: value: float = driver.source.bb.gnss.svid.galileo.mpath.v.a.echo.icPhase.get(satelliteSvid = repcap.SatelliteSvid.Default, vehicle = repcap.Vehicle.Default, antenna = repcap.Antenna.Default, echo = repcap.Echo.Default) \n
		Sets an initial code phase for the selected echo. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param vehicle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'V')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'A')
			:param echo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Echo')
			:return: init_code_phase: float Range: 0 to 3000, Unit: m"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		vehicle_cmd_val = self._cmd_group.get_repcap_cmd_value(vehicle, repcap.Vehicle)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		echo_cmd_val = self._cmd_group.get_repcap_cmd_value(echo, repcap.Echo)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:MPATh:V{vehicle_cmd_val}:A{antenna_cmd_val}:ECHO{echo_cmd_val}:ICPHase?')
		return Conversions.str_to_float(response)
