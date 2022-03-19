from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Constel:
	"""Constel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("constel", core, parent)

	def set(self, constellation: enums.Dvbt2BicmConstel, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:CONStel \n
		Snippet: driver.source.bb.t2Dvb.plp.constel.set(constellation = enums.Dvbt2BicmConstel.T16, physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the constellation. \n
			:param constellation: T4| T16| T64| T256 T4 QPSK T16|T64|T256 16/64/256QAM
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
		"""
		param = Conversions.enum_scalar_to_str(constellation, enums.Dvbt2BicmConstel)
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:CONStel {param}')

	# noinspection PyTypeChecker
	def get(self, physicalLayerPipe=repcap.PhysicalLayerPipe.Default) -> enums.Dvbt2BicmConstel:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:PLP<CH>:CONStel \n
		Snippet: value: enums.Dvbt2BicmConstel = driver.source.bb.t2Dvb.plp.constel.get(physicalLayerPipe = repcap.PhysicalLayerPipe.Default) \n
		Defines the constellation. \n
			:param physicalLayerPipe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Plp')
			:return: constellation: T4| T16| T64| T256 T4 QPSK T16|T64|T256 16/64/256QAM"""
		physicalLayerPipe_cmd_val = self._cmd_group.get_repcap_cmd_value(physicalLayerPipe, repcap.PhysicalLayerPipe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:T2DVb:PLP{physicalLayerPipe_cmd_val}:CONStel?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2BicmConstel)
