from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PacketLength:
	"""PacketLength commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("packetLength", core, parent)

	# noinspection PyTypeChecker
	def get_low(self) -> enums.InputSignalPacketLength:
		"""SCPI: [SOURce<HW>]:BB:DVBT:PACKetlength:LOW \n
		Snippet: value: enums.InputSignalPacketLength = driver.source.bb.dvbt.packetLength.get_low() \n
		Queries the packet length of the external transport stream in bytes. \n
			:return: packet_length_lp: P188| P204| INValid P188|P204 188/204 byte packets specified for serial input and parallel input. INValid Packet length does not match the specified length.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:PACKetlength:LOW?')
		return Conversions.str_to_scalar_enum(response, enums.InputSignalPacketLength)

	# noinspection PyTypeChecker
	def get_high(self) -> enums.InputSignalPacketLength:
		"""SCPI: [SOURce<HW>]:BB:DVBT:PACKetlength:[HIGH] \n
		Snippet: value: enums.InputSignalPacketLength = driver.source.bb.dvbt.packetLength.get_high() \n
		Queries the packet length of the external transport stream in bytes. \n
			:return: packet_length_hp: P188| P204| INValid P188|P204 188/204 byte packets specified for serial input and parallel input. INValid Packet length does not match the specified length.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:PACKetlength:HIGH?')
		return Conversions.str_to_scalar_enum(response, enums.InputSignalPacketLength)
