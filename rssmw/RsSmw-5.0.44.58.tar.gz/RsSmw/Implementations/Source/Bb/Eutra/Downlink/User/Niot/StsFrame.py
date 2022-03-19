from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StsFrame:
	"""StsFrame commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stsFrame", core, parent)

	def set(self, search_sp_start_sf: enums.EutraNbiotSearchSpaceStSubFrame, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:NIOT:STSFrame \n
		Snippet: driver.source.bb.eutra.downlink.user.niot.stsFrame.set(search_sp_start_sf = enums.EutraNbiotSearchSpaceStSubFrame.S1_5, userIx = repcap.UserIx.Default) \n
		Sets the serach space start subframe (G) . \n
			:param search_sp_start_sf: S1_5| S2| S4| S8| S16| S32| S48| S64
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(search_sp_start_sf, enums.EutraNbiotSearchSpaceStSubFrame)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:NIOT:STSFrame {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.EutraNbiotSearchSpaceStSubFrame:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:NIOT:STSFrame \n
		Snippet: value: enums.EutraNbiotSearchSpaceStSubFrame = driver.source.bb.eutra.downlink.user.niot.stsFrame.get(userIx = repcap.UserIx.Default) \n
		Sets the serach space start subframe (G) . \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: search_sp_start_sf: S1_5| S2| S4| S8| S16| S32| S48| S64"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:NIOT:STSFrame?')
		return Conversions.str_to_scalar_enum(response, enums.EutraNbiotSearchSpaceStSubFrame)
