from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Inhibit:
	"""Inhibit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inhibit", core, parent)

	def set(self, inhibit: int, external=repcap.External.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:TRIGger:[EXTernal<CH>]:INHibit \n
		Snippet: driver.source.bb.lora.trigger.external.inhibit.set(inhibit = 1, external = repcap.External.Default) \n
		No command help available \n
			:param inhibit: No help available
			:param external: optional repeated capability selector. Default value: Nr1 (settable in the interface 'External')
		"""
		param = Conversions.decimal_value_to_str(inhibit)
		external_cmd_val = self._cmd_group.get_repcap_cmd_value(external, repcap.External)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:TRIGger:EXTernal{external_cmd_val}:INHibit {param}')

	def get(self, external=repcap.External.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:LORA:TRIGger:[EXTernal<CH>]:INHibit \n
		Snippet: value: int = driver.source.bb.lora.trigger.external.inhibit.get(external = repcap.External.Default) \n
		No command help available \n
			:param external: optional repeated capability selector. Default value: Nr1 (settable in the interface 'External')
			:return: inhibit: No help available"""
		external_cmd_val = self._cmd_group.get_repcap_cmd_value(external, repcap.External)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:LORA:TRIGger:EXTernal{external_cmd_val}:INHibit?')
		return Conversions.str_to_int(response)
