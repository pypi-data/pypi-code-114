from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)

	def set(self, scma_layer_user: enums.C5GscmaUser, allocationNull=repcap.AllocationNull.Default, layerNull=repcap.LayerNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:SCMA:LAYer<ST0>:USER \n
		Snippet: driver.source.bb.ofdm.alloc.scma.layer.user.set(scma_layer_user = enums.C5GscmaUser.USER0, allocationNull = repcap.AllocationNull.Default, layerNull = repcap.LayerNull.Default) \n
		Maps the users to the layers. \n
			:param scma_layer_user: USER0| USER1| USER2| USER3| USER4| USER5
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param layerNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Layer')
		"""
		param = Conversions.enum_scalar_to_str(scma_layer_user, enums.C5GscmaUser)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		layerNull_cmd_val = self._cmd_group.get_repcap_cmd_value(layerNull, repcap.LayerNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:SCMA:LAYer{layerNull_cmd_val}:USER {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default, layerNull=repcap.LayerNull.Default) -> enums.C5GscmaUser:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:SCMA:LAYer<ST0>:USER \n
		Snippet: value: enums.C5GscmaUser = driver.source.bb.ofdm.alloc.scma.layer.user.get(allocationNull = repcap.AllocationNull.Default, layerNull = repcap.LayerNull.Default) \n
		Maps the users to the layers. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param layerNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Layer')
			:return: scma_layer_user: USER0| USER1| USER2| USER3| USER4| USER5"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		layerNull_cmd_val = self._cmd_group.get_repcap_cmd_value(layerNull, repcap.LayerNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:SCMA:LAYer{layerNull_cmd_val}:USER?')
		return Conversions.str_to_scalar_enum(response, enums.C5GscmaUser)
