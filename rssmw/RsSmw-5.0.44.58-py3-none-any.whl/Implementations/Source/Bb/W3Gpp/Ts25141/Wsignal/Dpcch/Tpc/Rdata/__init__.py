from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Utilities import trim_str_response
from .......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rdata:
	"""Rdata commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rdata", core, parent)

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	def get_dselect(self) -> str:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:RDATa:DSELect \n
		Snippet: value: str = driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.rdata.get_dselect() \n
		Selects the data list when the DLISt data source is selected for the TPC repeat pattern of the DPCCH. The files are
		stored with the fixed file extensions *.dm_iqd in a directory of the user's choice. The directory applicable to the
		commands is defined with the command method RsSmw.MassMemory.currentDirectory. To access the files in this directory,
		only the file name has to be given, without the path and the file extension. \n
			:return: dselect: data_list_name
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:RDATa:DSELect?')
		return trim_str_response(response)

	def set_dselect(self, dselect: str) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:RDATa:DSELect \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.rdata.set_dselect(dselect = '1') \n
		Selects the data list when the DLISt data source is selected for the TPC repeat pattern of the DPCCH. The files are
		stored with the fixed file extensions *.dm_iqd in a directory of the user's choice. The directory applicable to the
		commands is defined with the command method RsSmw.MassMemory.currentDirectory. To access the files in this directory,
		only the file name has to be given, without the path and the file extension. \n
			:param dselect: data_list_name
		"""
		param = Conversions.value_to_quoted_str(dselect)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:RDATa:DSELect {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.Ts25141TpcRepeatPattSour:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:RDATa \n
		Snippet: value: enums.Ts25141TpcRepeatPattSour = driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.rdata.get_value() \n
		Sets the TPC repeat pattern for verification of the base stations power control steps. \n
			:return: rdata: SINGle| AGGRegated| ONE| ZERO| PATTern| DLISt
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:RDATa?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141TpcRepeatPattSour)

	def set_value(self, rdata: enums.Ts25141TpcRepeatPattSour) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:RDATa \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.rdata.set_value(rdata = enums.Ts25141TpcRepeatPattSour.AGGRegated) \n
		Sets the TPC repeat pattern for verification of the base stations power control steps. \n
			:param rdata: SINGle| AGGRegated| ONE| ZERO| PATTern| DLISt
		"""
		param = Conversions.enum_scalar_to_str(rdata, enums.Ts25141TpcRepeatPattSour)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:RDATa {param}')

	def clone(self) -> 'Rdata':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rdata(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
