from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 18 total commands, 3 Subgroups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def prbs(self):
		"""prbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prbs'):
			from .Prbs import Prbs
			self._prbs = Prbs(self._core, self._cmd_group)
		return self._prbs

	@property
	def seamless(self):
		"""seamless commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_seamless'):
			from .Seamless import Seamless
			self._seamless = Seamless(self._core, self._cmd_group)
		return self._seamless

	@property
	def seek(self):
		"""seek commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_seek'):
			from .Seek import Seek
			self._seek = Seek(self._core, self._cmd_group)
		return self._seek

	# noinspection PyTypeChecker
	def get_command(self) -> enums.TspLayerStatus:
		"""SCPI: TSGen:CONFigure:COMMand \n
		Snippet: value: enums.TspLayerStatus = driver.tsGen.configure.get_command() \n
		Triggers playing, pausing and stopping of the TS player file selected with method RsSmcv.TsGen.Configure.playFile. \n
			:return: player_status: STOP| PAUSe| PLAY| RESet
		"""
		response = self._core.io.query_str('TSGen:CONFigure:COMMand?')
		return Conversions.str_to_scalar_enum(response, enums.TspLayerStatus)

	def set_command(self, player_status: enums.TspLayerStatus) -> None:
		"""SCPI: TSGen:CONFigure:COMMand \n
		Snippet: driver.tsGen.configure.set_command(player_status = enums.TspLayerStatus.PAUSe) \n
		Triggers playing, pausing and stopping of the TS player file selected with method RsSmcv.TsGen.Configure.playFile. \n
			:param player_status: STOP| PAUSe| PLAY| RESet
		"""
		param = Conversions.enum_scalar_to_str(player_status, enums.TspLayerStatus)
		self._core.io.write(f'TSGen:CONFigure:COMMand {param}')

	# noinspection PyTypeChecker
	def get_payload(self) -> enums.PayloadTestStuff:
		"""SCPI: TSGen:CONFigure:PAYLoad \n
		Snippet: value: enums.PayloadTestStuff = driver.tsGen.configure.get_payload() \n
		Determines the payload of the test packet. Also influences the payload of the generated stuffing packets while the TS
		player is running. \n
			:return: payload: HFF| H00| PRBS
		"""
		response = self._core.io.query_str('TSGen:CONFigure:PAYLoad?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadTestStuff)

	def set_payload(self, payload: enums.PayloadTestStuff) -> None:
		"""SCPI: TSGen:CONFigure:PAYLoad \n
		Snippet: driver.tsGen.configure.set_payload(payload = enums.PayloadTestStuff.H00) \n
		Determines the payload of the test packet. Also influences the payload of the generated stuffing packets while the TS
		player is running. \n
			:param payload: HFF| H00| PRBS
		"""
		param = Conversions.enum_scalar_to_str(payload, enums.PayloadTestStuff)
		self._core.io.write(f'TSGen:CONFigure:PAYLoad {param}')

	def get_pid(self) -> int:
		"""SCPI: TSGen:CONFigure:PID \n
		Snippet: value: int = driver.tsGen.configure.get_pid() \n
		The available values depend on the settings of method RsSmcv.TsGen.Configure.pidTestPack. If method RsSmcv.TsGen.
		Configure.pidTestPack is set to NULL, then method RsSmcv.TsGen.Configure.pid is 1FFF(hex) . Otherwise the values are
		variable. \n
			:return: pid: integer Range: 0 to 8191
		"""
		response = self._core.io.query_str('TSGen:CONFigure:PID?')
		return Conversions.str_to_int(response)

	def set_pid(self, pid: int) -> None:
		"""SCPI: TSGen:CONFigure:PID \n
		Snippet: driver.tsGen.configure.set_pid(pid = 1) \n
		The available values depend on the settings of method RsSmcv.TsGen.Configure.pidTestPack. If method RsSmcv.TsGen.
		Configure.pidTestPack is set to NULL, then method RsSmcv.TsGen.Configure.pid is 1FFF(hex) . Otherwise the values are
		variable. \n
			:param pid: integer Range: 0 to 8191
		"""
		param = Conversions.decimal_value_to_str(pid)
		self._core.io.write(f'TSGen:CONFigure:PID {param}')

	# noinspection PyTypeChecker
	def get_pid_test_pack(self) -> enums.PidTestPacket:
		"""SCPI: TSGen:CONFigure:PIDTestpack \n
		Snippet: value: enums.PidTestPacket = driver.tsGen.configure.get_pid_test_pack() \n
		Sets the PID, if method RsSmcv.TsGen.Configure.tsPacket is H184|H200|H204. \n
			:return: pid_test_pack: VARiable| NULL
		"""
		response = self._core.io.query_str('TSGen:CONFigure:PIDTestpack?')
		return Conversions.str_to_scalar_enum(response, enums.PidTestPacket)

	def set_pid_test_pack(self, pid_test_pack: enums.PidTestPacket) -> None:
		"""SCPI: TSGen:CONFigure:PIDTestpack \n
		Snippet: driver.tsGen.configure.set_pid_test_pack(pid_test_pack = enums.PidTestPacket.NULL) \n
		Sets the PID, if method RsSmcv.TsGen.Configure.tsPacket is H184|H200|H204. \n
			:param pid_test_pack: VARiable| NULL
		"""
		param = Conversions.enum_scalar_to_str(pid_test_pack, enums.PidTestPacket)
		self._core.io.write(f'TSGen:CONFigure:PIDTestpack {param}')

	def get_play_file(self) -> str:
		"""SCPI: TSGen:CONFigure:PLAYfile \n
		Snippet: value: str = driver.tsGen.configure.get_play_file() \n
		Specifies the file path and filename of the TS player file. \n
			:return: play_file: string
		"""
		response = self._core.io.query_str('TSGen:CONFigure:PLAYfile?')
		return trim_str_response(response)

	def set_play_file(self, play_file: str) -> None:
		"""SCPI: TSGen:CONFigure:PLAYfile \n
		Snippet: driver.tsGen.configure.set_play_file(play_file = '1') \n
		Specifies the file path and filename of the TS player file. \n
			:param play_file: string
		"""
		param = Conversions.value_to_quoted_str(play_file)
		self._core.io.write(f'TSGen:CONFigure:PLAYfile {param}')

	# noinspection PyTypeChecker
	def get_plength(self) -> enums.CodingPacketLength:
		"""SCPI: TSGen:CONFigure:PLENgth \n
		Snippet: value: enums.CodingPacketLength = driver.tsGen.configure.get_plength() \n
		Queries the packet length of the loaded file. \n
			:return: plength: P188| P204| P208| INV
		"""
		response = self._core.io.query_str('TSGen:CONFigure:PLENgth?')
		return Conversions.str_to_scalar_enum(response, enums.CodingPacketLength)

	def set_plength(self, plength: enums.CodingPacketLength) -> None:
		"""SCPI: TSGen:CONFigure:PLENgth \n
		Snippet: driver.tsGen.configure.set_plength(plength = enums.CodingPacketLength.INV) \n
		Queries the packet length of the loaded file. \n
			:param plength: P188| P204| P208| INV
		"""
		param = Conversions.enum_scalar_to_str(plength, enums.CodingPacketLength)
		self._core.io.write(f'TSGen:CONFigure:PLENgth {param}')

	# noinspection PyTypeChecker
	def get_stop_data(self) -> enums.All:
		"""SCPI: TSGen:CONFigure:STOPdata \n
		Snippet: value: enums.All = driver.tsGen.configure.get_stop_data() \n
		Ensures that a standardized TS data stream is always output at the TS output at the rear of the R&S SMCV100B. \n
			:return: stop_data: TTSP| NONE
		"""
		response = self._core.io.query_str('TSGen:CONFigure:STOPdata?')
		return Conversions.str_to_scalar_enum(response, enums.All)

	def set_stop_data(self, stop_data: enums.All) -> None:
		"""SCPI: TSGen:CONFigure:STOPdata \n
		Snippet: driver.tsGen.configure.set_stop_data(stop_data = enums.All.NONE) \n
		Ensures that a standardized TS data stream is always output at the TS output at the rear of the R&S SMCV100B. \n
			:param stop_data: TTSP| NONE
		"""
		param = Conversions.enum_scalar_to_str(stop_data, enums.All)
		self._core.io.write(f'TSGen:CONFigure:STOPdata {param}')

	def get_stuffing(self) -> bool:
		"""SCPI: TSGen:CONFigure:STUFfing \n
		Snippet: value: bool = driver.tsGen.configure.get_stuffing() \n
		Activates nullpacket stuffing. \n
			:return: stuffing: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('TSGen:CONFigure:STUFfing?')
		return Conversions.str_to_bool(response)

	def set_stuffing(self, stuffing: bool) -> None:
		"""SCPI: TSGen:CONFigure:STUFfing \n
		Snippet: driver.tsGen.configure.set_stuffing(stuffing = False) \n
		Activates nullpacket stuffing. \n
			:param stuffing: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(stuffing)
		self._core.io.write(f'TSGen:CONFigure:STUFfing {param}')

	# noinspection PyTypeChecker
	def get_ts_packet(self) -> enums.TspLayerSettingsTestTsPacket:
		"""SCPI: TSGen:CONFigure:TSPacket \n
		Snippet: value: enums.TspLayerSettingsTestTsPacket = driver.tsGen.configure.get_ts_packet() \n
		Sets the structure of the generated test packets in pause or stop status. \n
			:return: ts_paket: H184| H200| H204| S187| S203| S207 S187|S203|S207 A sync byte (0x47) followed by 187/203/207 payload bytes. H184|H200|H204 A sync byte (0x47) followed by three header bytes and 184/200/204 payload bytes.
		"""
		response = self._core.io.query_str('TSGen:CONFigure:TSPacket?')
		return Conversions.str_to_scalar_enum(response, enums.TspLayerSettingsTestTsPacket)

	def set_ts_packet(self, ts_paket: enums.TspLayerSettingsTestTsPacket) -> None:
		"""SCPI: TSGen:CONFigure:TSPacket \n
		Snippet: driver.tsGen.configure.set_ts_packet(ts_paket = enums.TspLayerSettingsTestTsPacket.H184) \n
		Sets the structure of the generated test packets in pause or stop status. \n
			:param ts_paket: H184| H200| H204| S187| S203| S207 S187|S203|S207 A sync byte (0x47) followed by 187/203/207 payload bytes. H184|H200|H204 A sync byte (0x47) followed by three header bytes and 184/200/204 payload bytes.
		"""
		param = Conversions.enum_scalar_to_str(ts_paket, enums.TspLayerSettingsTestTsPacket)
		self._core.io.write(f'TSGen:CONFigure:TSPacket {param}')

	def get_ts_rate(self) -> int:
		"""SCPI: TSGen:CONFigure:TSRate \n
		Snippet: value: int = driver.tsGen.configure.get_ts_rate() \n
		Sets the output data rate of the player. \n
			:return: ts_rate: integer Range: 1 to 35E7
		"""
		response = self._core.io.query_str('TSGen:CONFigure:TSRate?')
		return Conversions.str_to_int(response)

	def set_ts_rate(self, ts_rate: int) -> None:
		"""SCPI: TSGen:CONFigure:TSRate \n
		Snippet: driver.tsGen.configure.set_ts_rate(ts_rate = 1) \n
		Sets the output data rate of the player. \n
			:param ts_rate: integer Range: 1 to 35E7
		"""
		param = Conversions.decimal_value_to_str(ts_rate)
		self._core.io.write(f'TSGen:CONFigure:TSRate {param}')

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
