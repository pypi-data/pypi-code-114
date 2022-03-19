from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dheading:
	"""Dheading commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dheading", core, parent)

	def set(self, delta_heading: float, baseSt=repcap.BaseSt.Default, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RTK:BASE<ST>:A<CH>:DHEading \n
		Snippet: driver.source.bb.gnss.rtk.base.a.dheading.set(delta_heading = 1.0, baseSt = repcap.BaseSt.Default, antenna = repcap.Antenna.Default) \n
		No command help available \n
			:param delta_heading: No help available
			:param baseSt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Base')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'A')
		"""
		param = Conversions.decimal_value_to_str(delta_heading)
		baseSt_cmd_val = self._cmd_group.get_repcap_cmd_value(baseSt, repcap.BaseSt)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RTK:BASE{baseSt_cmd_val}:A{antenna_cmd_val}:DHEading {param}')

	def get(self, baseSt=repcap.BaseSt.Default, antenna=repcap.Antenna.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RTK:BASE<ST>:A<CH>:DHEading \n
		Snippet: value: float = driver.source.bb.gnss.rtk.base.a.dheading.get(baseSt = repcap.BaseSt.Default, antenna = repcap.Antenna.Default) \n
		No command help available \n
			:param baseSt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Base')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'A')
			:return: delta_heading: No help available"""
		baseSt_cmd_val = self._cmd_group.get_repcap_cmd_value(baseSt, repcap.BaseSt)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RTK:BASE{baseSt_cmd_val}:A{antenna_cmd_val}:DHEading?')
		return Conversions.str_to_float(response)
