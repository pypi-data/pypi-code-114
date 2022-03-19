from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pa:
	"""Pa commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pa", core, parent)

	def set(self, power: enums.PdscPowA, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:PA \n
		Snippet: driver.source.bb.oneweb.downlink.user.pa.set(power = enums.PdscPowA._0, userIx = repcap.UserIx.Default) \n
		Sets PDSCH power factor. \n
			:param power: -6.02| -4.77| -3.01| -1.77| 0.97| 2.04| 3.01| 0
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(power, enums.PdscPowA)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:PA {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.PdscPowA:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:PA \n
		Snippet: value: enums.PdscPowA = driver.source.bb.oneweb.downlink.user.pa.get(userIx = repcap.UserIx.Default) \n
		Sets PDSCH power factor. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: power: -6.02| -4.77| -3.01| -1.77| 0.97| 2.04| 3.01| 0"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:PA?')
		return Conversions.str_to_scalar_enum(response, enums.PdscPowA)
