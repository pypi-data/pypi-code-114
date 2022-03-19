from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Issy:
	"""Issy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("issy", core, parent)

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Dvbt2InputIssy:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:ISSY \n
		Snippet: value: enums.Dvbt2InputIssy = driver.source.bb.t2Dvb.plp.issy.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Queries the state. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: issy: OFF| SHORt| LONG OFF ISSY is not active. ISSY indicator field is 0. SHORt ISSY is active. ISSY indicator field is 1. The synchronizer uses a short . LONG ISSY is active. ISSY indicator field is 1. The synchronizer uses a long ."""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:ISSY?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2InputIssy)
