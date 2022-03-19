from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uec:
	"""Uec commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uec", core, parent)

	def set(self, ue_category: enums.EutraUeCat, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:UEC \n
		Snippet: driver.source.bb.eutra.downlink.user.uec.set(ue_category = enums.EutraUeCat.C1, userIx = repcap.UserIx.Default) \n
		Sets the UE Category. \n
			:param ue_category: USER | C1| C2| C3| C4| C5| C6| C7| C8| C9| C10| C11| C12| C13| C14| C15| C16| C17| C18| C19| C20 | M1| NB1 | M2| NB2
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(ue_category, enums.EutraUeCat)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:UEC {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.EutraUeCat:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:UEC \n
		Snippet: value: enums.EutraUeCat = driver.source.bb.eutra.downlink.user.uec.get(userIx = repcap.UserIx.Default) \n
		Sets the UE Category. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: ue_category: USER | C1| C2| C3| C4| C5| C6| C7| C8| C9| C10| C11| C12| C13| C14| C15| C16| C17| C18| C19| C20 | M1| NB1 | M2| NB2"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:UEC?')
		return Conversions.str_to_scalar_enum(response, enums.EutraUeCat)
