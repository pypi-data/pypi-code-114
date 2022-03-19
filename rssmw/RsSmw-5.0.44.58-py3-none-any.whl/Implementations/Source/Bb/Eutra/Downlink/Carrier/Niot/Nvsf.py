from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nvsf:
	"""Nvsf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nvsf", core, parent)

	def set(self, no_valid_subframe: enums.EutraNbiotInbandBitmapSfAll, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:NVSF \n
		Snippet: driver.source.bb.eutra.downlink.carrier.niot.nvsf.set(no_valid_subframe = enums.EutraNbiotInbandBitmapSfAll.N10, carrier = repcap.Carrier.Default) \n
		Sets the subframes bitmap. \n
			:param no_valid_subframe: N10| N40
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		param = Conversions.enum_scalar_to_str(no_valid_subframe, enums.EutraNbiotInbandBitmapSfAll)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:NVSF {param}')

	# noinspection PyTypeChecker
	def get(self, carrier=repcap.Carrier.Default) -> enums.EutraNbiotInbandBitmapSfAll:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:NVSF \n
		Snippet: value: enums.EutraNbiotInbandBitmapSfAll = driver.source.bb.eutra.downlink.carrier.niot.nvsf.get(carrier = repcap.Carrier.Default) \n
		Sets the subframes bitmap. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: no_valid_subframe: N10| N40"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:NVSF?')
		return Conversions.str_to_scalar_enum(response, enums.EutraNbiotInbandBitmapSfAll)
