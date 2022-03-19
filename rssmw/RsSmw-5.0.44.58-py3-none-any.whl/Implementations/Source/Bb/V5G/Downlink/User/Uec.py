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

	def set(self, ue_category: enums.V5GuEcat, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:UEC \n
		Snippet: driver.source.bb.v5G.downlink.user.uec.set(ue_category = enums.V5GuEcat.C1, userIx = repcap.UserIx.Default) \n
		No command help available \n
			:param ue_category: No help available
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(ue_category, enums.V5GuEcat)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:UEC {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.V5GuEcat:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:UEC \n
		Snippet: value: enums.V5GuEcat = driver.source.bb.v5G.downlink.user.uec.get(userIx = repcap.UserIx.Default) \n
		No command help available \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: ue_category: No help available"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:UEC?')
		return Conversions.str_to_scalar_enum(response, enums.V5GuEcat)
