from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Crotation:
	"""Crotation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crotation", core, parent)

	def set(self, crotation: bool, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:CROTation \n
		Snippet: driver.source.bb.t2Dvb.plp.crotation.set(crotation = False, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the constellation rotation state. \n
			:param crotation: 1| ON| 0| OFF ON Transmits the constellation rotated, i.e. the Q path is delayed vs. the I path. For each constellation, there is a different (but fixed) angle of rotation. OFF Transmits non-rotated constellation.
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.bool_to_str(crotation)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:CROTation {param}')

	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:CROTation \n
		Snippet: value: bool = driver.source.bb.t2Dvb.plp.crotation.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Sets the constellation rotation state. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: crotation: 1| ON| 0| OFF ON Transmits the constellation rotated, i.e. the Q path is delayed vs. the I path. For each constellation, there is a different (but fixed) angle of rotation. OFF Transmits non-rotated constellation."""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:CROTation?')
		return Conversions.str_to_bool(response)
