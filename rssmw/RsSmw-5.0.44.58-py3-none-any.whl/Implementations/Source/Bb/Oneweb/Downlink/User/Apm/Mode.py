from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, ant_port_map: enums.BfapMapMode, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:APM:MODE \n
		Snippet: driver.source.bb.oneweb.downlink.user.apm.mode.set(ant_port_map = enums.BfapMapMode.CB, userIx = repcap.UserIx.Default) \n
		No command help available \n
			:param ant_port_map: No help available
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(ant_port_map, enums.BfapMapMode)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:APM:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.BfapMapMode:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:APM:MODE \n
		Snippet: value: enums.BfapMapMode = driver.source.bb.oneweb.downlink.user.apm.mode.get(userIx = repcap.UserIx.Default) \n
		No command help available \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: ant_port_map: No help available"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:APM:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.BfapMapMode)
