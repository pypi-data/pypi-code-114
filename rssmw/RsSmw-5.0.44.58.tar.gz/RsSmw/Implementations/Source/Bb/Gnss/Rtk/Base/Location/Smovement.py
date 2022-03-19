from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Smovement:
	"""Smovement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smovement", core, parent)

	def set(self, smooth_movement: bool, baseSt=repcap.BaseSt.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RTK:BASE<ST>:LOCation:SMOVement \n
		Snippet: driver.source.bb.gnss.rtk.base.location.smovement.set(smooth_movement = False, baseSt = repcap.BaseSt.Default) \n
		No command help available \n
			:param smooth_movement: No help available
			:param baseSt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Base')
		"""
		param = Conversions.bool_to_str(smooth_movement)
		baseSt_cmd_val = self._cmd_group.get_repcap_cmd_value(baseSt, repcap.BaseSt)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:RTK:BASE{baseSt_cmd_val}:LOCation:SMOVement {param}')

	def get(self, baseSt=repcap.BaseSt.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RTK:BASE<ST>:LOCation:SMOVement \n
		Snippet: value: bool = driver.source.bb.gnss.rtk.base.location.smovement.get(baseSt = repcap.BaseSt.Default) \n
		No command help available \n
			:param baseSt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Base')
			:return: smooth_movement: No help available"""
		baseSt_cmd_val = self._cmd_group.get_repcap_cmd_value(baseSt, repcap.BaseSt)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RTK:BASE{baseSt_cmd_val}:LOCation:SMOVement?')
		return Conversions.str_to_bool(response)
