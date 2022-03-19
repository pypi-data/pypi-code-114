from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbIdx:
	"""RbIdx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbIdx", core, parent)

	def set(self, rb_index: enums.EutraDlNbiotRbIndex, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:RBIDx \n
		Snippet: driver.source.bb.eutra.downlink.carrier.niot.rbIdx.set(rb_index = enums.EutraDlNbiotRbIndex._12, carrier = repcap.Carrier.Default) \n
		Sets the resource block number in that the NB-IoT transmissions are allocated. \n
			:param rb_index: 2| 4| 7| 9| 12| 14| 17| 19| 22| 27| 24| 29| 30| 32| 34| 35| 39| 42| 44| 40| 45| 47| 52| 55| 57| 60| 62| 65| 67| 70| 72| 75| 80| 85| 90| 95| USER
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		param = Conversions.enum_scalar_to_str(rb_index, enums.EutraDlNbiotRbIndex)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:RBIDx {param}')

	# noinspection PyTypeChecker
	def get(self, carrier=repcap.Carrier.Default) -> enums.EutraDlNbiotRbIndex:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CARRier<CH>:NIOT:RBIDx \n
		Snippet: value: enums.EutraDlNbiotRbIndex = driver.source.bb.eutra.downlink.carrier.niot.rbIdx.get(carrier = repcap.Carrier.Default) \n
		Sets the resource block number in that the NB-IoT transmissions are allocated. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: rb_index: 2| 4| 7| 9| 12| 14| 17| 19| 22| 27| 24| 29| 30| 32| 34| 35| 39| 42| 44| 40| 45| 47| 52| 55| 57| 60| 62| 65| 67| 70| 72| 75| 80| 85| 90| 95| USER"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CARRier{carrier_cmd_val}:NIOT:RBIDx?')
		return Conversions.str_to_scalar_enum(response, enums.EutraDlNbiotRbIndex)
