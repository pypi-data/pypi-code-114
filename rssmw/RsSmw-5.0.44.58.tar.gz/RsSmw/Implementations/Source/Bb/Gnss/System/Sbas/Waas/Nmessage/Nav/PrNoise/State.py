from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, gnssPsRandomNumberNull=repcap.GnssPsRandomNumberNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:WAAS:NMESsage:NAV:PRN<CH>:STATe \n
		Snippet: driver.source.bb.gnss.system.sbas.waas.nmessage.nav.prNoise.state.set(state = False, gnssPsRandomNumberNull = repcap.GnssPsRandomNumberNull.Default) \n
		Enables an SV ID/ SV PRN. \n
			:param state: 0| 1| OFF| ON
			:param gnssPsRandomNumberNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'PrNoise')
		"""
		param = Conversions.bool_to_str(state)
		gnssPsRandomNumberNull_cmd_val = self._cmd_group.get_repcap_cmd_value(gnssPsRandomNumberNull, repcap.GnssPsRandomNumberNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:WAAS:NMESsage:NAV:PRN{gnssPsRandomNumberNull_cmd_val}:STATe {param}')

	def get(self, gnssPsRandomNumberNull=repcap.GnssPsRandomNumberNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:WAAS:NMESsage:NAV:PRN<CH>:STATe \n
		Snippet: value: bool = driver.source.bb.gnss.system.sbas.waas.nmessage.nav.prNoise.state.get(gnssPsRandomNumberNull = repcap.GnssPsRandomNumberNull.Default) \n
		Enables an SV ID/ SV PRN. \n
			:param gnssPsRandomNumberNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'PrNoise')
			:return: state: 0| 1| OFF| ON"""
		gnssPsRandomNumberNull_cmd_val = self._cmd_group.get_repcap_cmd_value(gnssPsRandomNumberNull, repcap.GnssPsRandomNumberNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:WAAS:NMESsage:NAV:PRN{gnssPsRandomNumberNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
