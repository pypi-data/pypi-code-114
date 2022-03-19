from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TrSource:
	"""TrSource commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trSource", core, parent)

	def set(self, tran_source: enums.TranSource, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[SUBF<ST0>]:ENCC:PDCCh:DCRegs:TRSource \n
		Snippet: driver.source.bb.oneweb.downlink.subf.encc.pdcch.dcRegs.trSource.set(tran_source = enums.TranSource.DATA, subframeNull = repcap.SubframeNull.Default) \n
		No command help available \n
			:param tran_source: No help available
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.enum_scalar_to_str(tran_source, enums.TranSource)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:DCRegs:TRSource {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default) -> enums.TranSource:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[SUBF<ST0>]:ENCC:PDCCh:DCRegs:TRSource \n
		Snippet: value: enums.TranSource = driver.source.bb.oneweb.downlink.subf.encc.pdcch.dcRegs.trSource.get(subframeNull = repcap.SubframeNull.Default) \n
		No command help available \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: tran_source: No help available"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:DCRegs:TRSource?')
		return Conversions.str_to_scalar_enum(response, enums.TranSource)
