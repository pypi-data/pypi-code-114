from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsPackets:
	"""TsPackets commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsPackets", core, parent)

	# noinspection PyTypeChecker
	def get_a(self) -> enums.SettingsTestTsPacket:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TSPackets:A \n
		Snippet: value: enums.SettingsTestTsPacket = driver.source.bb.isdbt.tsPackets.get_a() \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:return: test_ts_packet: S187| H184
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:TSPackets:A?')
		return Conversions.str_to_scalar_enum(response, enums.SettingsTestTsPacket)

	def set_a(self, test_ts_packet: enums.SettingsTestTsPacket) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:TSPackets:A \n
		Snippet: driver.source.bb.isdbt.tsPackets.set_a(test_ts_packet = enums.SettingsTestTsPacket.H184) \n
		Specifies the structure of the test transport stream packet that is fed to the modulator. \n
			:param test_ts_packet: S187| H184
		"""
		param = Conversions.enum_scalar_to_str(test_ts_packet, enums.SettingsTestTsPacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:TSPackets:A {param}')
