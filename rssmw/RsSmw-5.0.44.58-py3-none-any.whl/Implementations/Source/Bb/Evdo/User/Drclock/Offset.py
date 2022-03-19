from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, offset: int, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:DRCLock:OFFSet \n
		Snippet: driver.source.bb.evdo.user.drclock.offset.set(offset = 1, userIx = repcap.UserIx.Default) \n
		Sets the reverse link frame offset for the reverse link. The frame offset is used to position the DRC Lock bit within the
		MAC channel. \n
			:param offset: integer Range: 0 to 15
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(offset)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:DRCLock:OFFSet {param}')

	def get(self, userIx=repcap.UserIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:DRCLock:OFFSet \n
		Snippet: value: int = driver.source.bb.evdo.user.drclock.offset.get(userIx = repcap.UserIx.Default) \n
		Sets the reverse link frame offset for the reverse link. The frame offset is used to position the DRC Lock bit within the
		MAC channel. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: offset: integer Range: 0 to 15"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:DRCLock:OFFSet?')
		return Conversions.str_to_int(response)
