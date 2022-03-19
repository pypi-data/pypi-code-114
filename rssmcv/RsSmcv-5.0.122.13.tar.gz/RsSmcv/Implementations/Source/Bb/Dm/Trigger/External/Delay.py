from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delay", core, parent)

	def set(self, delay: float, external=repcap.External.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:TRIGger:[EXTernal<CH>]:DELay \n
		Snippet: driver.source.bb.dm.trigger.external.delay.set(delay = 1.0, external = repcap.External.Default) \n
		Specifies the trigger delay in symbols. Maximum trigger delay and trigger inhibit values depend on the installed options.
		See 'Specifying delay and inhibit values'. \n
			:param delay: float Range: 0 to depends on the symbol rate, Unit: symbol
			:param external: optional repeated capability selector. Default value: Nr1 (settable in the interface 'External')
		"""
		param = Conversions.decimal_value_to_str(delay)
		external_cmd_val = self._cmd_group.get_repcap_cmd_value(external, repcap.External)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:TRIGger:EXTernal{external_cmd_val}:DELay {param}')

	def get(self, external=repcap.External.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:TRIGger:[EXTernal<CH>]:DELay \n
		Snippet: value: float = driver.source.bb.dm.trigger.external.delay.get(external = repcap.External.Default) \n
		Specifies the trigger delay in symbols. Maximum trigger delay and trigger inhibit values depend on the installed options.
		See 'Specifying delay and inhibit values'. \n
			:param external: optional repeated capability selector. Default value: Nr1 (settable in the interface 'External')
			:return: delay: float Range: 0 to depends on the symbol rate, Unit: symbol"""
		external_cmd_val = self._cmd_group.get_repcap_cmd_value(external, repcap.External)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DM:TRIGger:EXTernal{external_cmd_val}:DELay?')
		return Conversions.str_to_float(response)
