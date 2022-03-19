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

	def set(self, ue_category: enums.UeCat, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:UEC \n
		Snippet: driver.source.bb.oneweb.downlink.user.uec.set(ue_category = enums.UeCat.C1, userIx = repcap.UserIx.Default) \n
		Sets the UE Category. \n
			:param ue_category: C1| C2| C3| C5| C4
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(ue_category, enums.UeCat)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:UEC {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.UeCat:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:UEC \n
		Snippet: value: enums.UeCat = driver.source.bb.oneweb.downlink.user.uec.get(userIx = repcap.UserIx.Default) \n
		Sets the UE Category. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: ue_category: C1| C2| C3| C5| C4"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:UEC?')
		return Conversions.str_to_scalar_enum(response, enums.UeCat)
