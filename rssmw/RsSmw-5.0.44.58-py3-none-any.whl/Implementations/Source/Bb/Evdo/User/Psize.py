from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Psize:
	"""Psize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psize", core, parent)

	def set(self, psize: enums.EvdoPacketSize, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:PSIZe \n
		Snippet: driver.source.bb.evdo.user.psize.set(psize = enums.EvdoPacketSize.PS1024, userIx = repcap.UserIx.Default) \n
		Sets the packet size for the packets sent to the selected user. Note: Selected rate becomes effective at the beginning of
		the next packet transmitted to the selected user. \n
			:param psize: PS128| PS256| PS512| PS768| PS1024| PS1536| PS2048| PS3072| PS4096| PS5120| PS6144| PS8192| PS12288| PS7168
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(psize, enums.EvdoPacketSize)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:PSIZe {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.EvdoPacketSize:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:PSIZe \n
		Snippet: value: enums.EvdoPacketSize = driver.source.bb.evdo.user.psize.get(userIx = repcap.UserIx.Default) \n
		Sets the packet size for the packets sent to the selected user. Note: Selected rate becomes effective at the beginning of
		the next packet transmitted to the selected user. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: psize: PS128| PS256| PS512| PS768| PS1024| PS1536| PS2048| PS3072| PS4096| PS5120| PS6144| PS8192| PS12288| PS7168"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:PSIZe?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoPacketSize)
