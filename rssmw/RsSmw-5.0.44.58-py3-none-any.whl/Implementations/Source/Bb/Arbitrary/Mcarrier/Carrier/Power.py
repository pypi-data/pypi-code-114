from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: float, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CARRier<CH>:POWer \n
		Snippet: driver.source.bb.arbitrary.mcarrier.carrier.power.set(power = 1.0, carrier = repcap.Carrier.Default) \n
		Sets the gain of the selected carrier. \n
			:param power: float Range: -80 to 0, Unit: dB
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mcarrier')
		"""
		param = Conversions.decimal_value_to_str(power)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CARRier{carrier_cmd_val}:POWer {param}')

	def get(self, carrier=repcap.Carrier.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CARRier<CH>:POWer \n
		Snippet: value: float = driver.source.bb.arbitrary.mcarrier.carrier.power.get(carrier = repcap.Carrier.Default) \n
		Sets the gain of the selected carrier. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mcarrier')
			:return: power: float Range: -80 to 0, Unit: dB"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CARRier{carrier_cmd_val}:POWer?')
		return Conversions.str_to_float(response)
