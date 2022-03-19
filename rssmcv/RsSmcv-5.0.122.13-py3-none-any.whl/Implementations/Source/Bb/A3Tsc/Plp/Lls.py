from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lls:
	"""Lls commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lls", core, parent)

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Atsc30LowLevelSignaling:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:PLP<CH>:LLS \n
		Snippet: value: enums.Atsc30LowLevelSignaling = driver.source.bb.a3Tsc.plp.lls.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Displays, if low-level signaling is present in the . \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: low_level_signaling: ABSent| PRESent"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:PLP{physicalLayerPipe_cmd_val}:LLS?')
		return Conversions.str_to_scalar_enum(response, enums.Atsc30LowLevelSignaling)
