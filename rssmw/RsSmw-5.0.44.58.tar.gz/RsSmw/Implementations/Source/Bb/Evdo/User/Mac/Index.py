from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Index:
	"""Index commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("index", core, parent)

	def set(self, index: int, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:MAC:INDex \n
		Snippet: driver.source.bb.evdo.user.mac.index.set(index = 1, userIx = repcap.UserIx.Default) \n
		Sets the MAC Index used for the selected user. MAC Index has to be different for the different users. However, in case
		that two users are using the same value for MAC Index, the lower priority user is disabled, or be unable to enable. The
		values for the MAC Indexes for the other users (see [:SOURce<hw>]:BB:EVDO:ANETwork:OUCount) are assigned from a pool of
		valid MAC Indexes. \n
			:param index: integer Range: 5 to 63 for physical layer subtype 0&1, 6 to 127 for physical layer subtype 2, 4 to 383 for physical layer subtype 3
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(index)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:MAC:INDex {param}')

	def get(self, userIx=repcap.UserIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:MAC:INDex \n
		Snippet: value: int = driver.source.bb.evdo.user.mac.index.get(userIx = repcap.UserIx.Default) \n
		Sets the MAC Index used for the selected user. MAC Index has to be different for the different users. However, in case
		that two users are using the same value for MAC Index, the lower priority user is disabled, or be unable to enable. The
		values for the MAC Indexes for the other users (see [:SOURce<hw>]:BB:EVDO:ANETwork:OUCount) are assigned from a pool of
		valid MAC Indexes. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: index: integer Range: 5 to 63 for physical layer subtype 0&1, 6 to 127 for physical layer subtype 2, 4 to 383 for physical layer subtype 3"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:MAC:INDex?')
		return Conversions.str_to_int(response)
