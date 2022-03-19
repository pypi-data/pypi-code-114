from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Conflict:
	"""Conflict commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("conflict", core, parent)

	def get(self, mimoTap=repcap.MimoTap.Default) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:MATRix:CONFlict \n
		Snippet: value: bool = driver.source.fsimulator.mimo.tap.matrix.conflict.get(mimoTap = repcap.MimoTap.Default) \n
		Queries whether there is a matrix conflict or not. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:return: conflict: 1| ON| 0| OFF"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:MATRix:CONFlict?')
		return Conversions.str_to_bool(response)
