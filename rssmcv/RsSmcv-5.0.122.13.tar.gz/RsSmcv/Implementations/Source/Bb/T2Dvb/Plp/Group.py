from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Group:
	"""Group commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("group", core, parent)

	def set(self, group: int, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:GROup \n
		Snippet: driver.source.bb.t2Dvb.plp.group.set(group = 1, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the PLP group ID for multi-PLP, i.e. the number of PLPs is greater than 1. See [:SOURce<hw>]:BB:T2DVb:INPut:NPLP?. \n
			:param group: integer Range: 0 to 255
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.decimal_value_to_str(group)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:GROup {param}')

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:GROup \n
		Snippet: value: int = driver.source.bb.t2Dvb.plp.group.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the PLP group ID for multi-PLP, i.e. the number of PLPs is greater than 1. See [:SOURce<hw>]:BB:T2DVb:INPut:NPLP?. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: group: integer Range: 0 to 255"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:GROup?')
		return Conversions.str_to_int(response)
