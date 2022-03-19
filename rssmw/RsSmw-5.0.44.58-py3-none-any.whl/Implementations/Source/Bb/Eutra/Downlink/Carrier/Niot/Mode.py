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

	def set(self, mode: enums.IdEutraNbiotMode, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:MODE \n
		Snippet: driver.source.bb.eutra.downlink.carrier.niot.mode.set(mode = enums.IdEutraNbiotMode.ALON, carrier = repcap.Carrier.Default) \n
		Sets the operating mode. \n
			:param mode: INBD| ALON| GBD
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.IdEutraNbiotMode)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, carrier=repcap.Carrier.Default) -> enums.IdEutraNbiotMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:MODE \n
		Snippet: value: enums.IdEutraNbiotMode = driver.source.bb.eutra.downlink.carrier.niot.mode.get(carrier = repcap.Carrier.Default) \n
		Sets the operating mode. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: mode: INBD| ALON| GBD"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.IdEutraNbiotMode)
