from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AnfMode:
	"""AnfMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("anfMode", core, parent)

	def set(self, ack_nack_fb_mode: enums.AckNackAll, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:ANFMode \n
		Snippet: driver.source.bb.nr5G.ubwp.user.dsch.anfMode.set(ack_nack_fb_mode = enums.AckNackAll.JOIN, userNull = repcap.UserNull.Default) \n
		Selects the state of the parameter ackNackFeedbackMode. \n
			:param ack_nack_fb_mode: NCON| JOIN| SEP
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(ack_nack_fb_mode, enums.AckNackAll)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:ANFMode {param}')

	# noinspection PyTypeChecker
	def get(self, userNull=repcap.UserNull.Default) -> enums.AckNackAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:ANFMode \n
		Snippet: value: enums.AckNackAll = driver.source.bb.nr5G.ubwp.user.dsch.anfMode.get(userNull = repcap.UserNull.Default) \n
		Selects the state of the parameter ackNackFeedbackMode. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: ack_nack_fb_mode: No help available"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:ANFMode?')
		return Conversions.str_to_scalar_enum(response, enums.AckNackAll)
