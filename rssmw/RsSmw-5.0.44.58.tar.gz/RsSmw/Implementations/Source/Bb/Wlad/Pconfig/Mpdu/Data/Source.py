from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.DataSourceA, macPdu=repcap.MacPdu.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MPDU<ST>:DATA:SOURce \n
		Snippet: driver.source.bb.wlad.pconfig.mpdu.data.source.set(source = enums.DataSourceA.DLISt, macPdu = repcap.MacPdu.Default) \n
		Selects the data source. \n
			:param source: ZERO| ONE| PATTern| PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt PNxx The pseudo-random sequence generator is used as the data source. Different random sequence lengths can be selected. DLISt A data list is used. The data list is selected with the command BB:WLAD:FBLch:MPDUst:DATA:DSEL ZERO | ONE Internal 0 or 1 data is used. PATTern Internal data is used. The bit pattern for the data is defined by the command BB:WLAD:FBLch:MPDUst:DATA:PATT.
			:param macPdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mpdu')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.DataSourceA)
		macPdu_cmd_val = self._cmd_group.get_repcap_cmd_value(macPdu, repcap.MacPdu)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MPDU{macPdu_cmd_val}:DATA:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, macPdu=repcap.MacPdu.Default) -> enums.DataSourceA:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MPDU<ST>:DATA:SOURce \n
		Snippet: value: enums.DataSourceA = driver.source.bb.wlad.pconfig.mpdu.data.source.get(macPdu = repcap.MacPdu.Default) \n
		Selects the data source. \n
			:param macPdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mpdu')
			:return: source: ZERO| ONE| PATTern| PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt PNxx The pseudo-random sequence generator is used as the data source. Different random sequence lengths can be selected. DLISt A data list is used. The data list is selected with the command BB:WLAD:FBLch:MPDUst:DATA:DSEL ZERO | ONE Internal 0 or 1 data is used. PATTern Internal data is used. The bit pattern for the data is defined by the command BB:WLAD:FBLch:MPDUst:DATA:PATT."""
		macPdu_cmd_val = self._cmd_group.get_repcap_cmd_value(macPdu, repcap.MacPdu)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MPDU{macPdu_cmd_val}:DATA:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceA)
