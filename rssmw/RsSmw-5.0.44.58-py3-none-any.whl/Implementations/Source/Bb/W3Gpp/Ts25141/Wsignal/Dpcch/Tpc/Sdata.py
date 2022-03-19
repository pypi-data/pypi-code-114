from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sdata:
	"""Sdata commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sdata", core, parent)

	def get_dselect(self) -> str:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa:DSELect \n
		Snippet: value: str = driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.sdata.get_dselect() \n
		Selects the data list when the DLISt data source is selected for the TPC start pattern of the DPCCH. The files are stored
		with the fixed file extensions *.dm_iqd in a directory of the user's choice. The directory applicable to the commands is
		defined with the command method RsSmw.MassMemory.currentDirectory. To access the files in this directory, only the file
		name has to be given, without the path and the file extension. \n
			:return: dselect: data_list_name
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa:DSELect?')
		return trim_str_response(response)

	def set_dselect(self, dselect: str) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa:DSELect \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.sdata.set_dselect(dselect = '1') \n
		Selects the data list when the DLISt data source is selected for the TPC start pattern of the DPCCH. The files are stored
		with the fixed file extensions *.dm_iqd in a directory of the user's choice. The directory applicable to the commands is
		defined with the command method RsSmw.MassMemory.currentDirectory. To access the files in this directory, only the file
		name has to be given, without the path and the file extension. \n
			:param dselect: data_list_name
		"""
		param = Conversions.value_to_quoted_str(dselect)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa:DSELect {param}')

	def get_pd_steps(self) -> int:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa:PDSTeps \n
		Snippet: value: int = driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.sdata.get_pd_steps() \n
		Sets the amount of power down bits in the TPC start pattern. \n
			:return: pd_steps: integer Range: 0 to 1000
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa:PDSTeps?')
		return Conversions.str_to_int(response)

	def set_pd_steps(self, pd_steps: int) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa:PDSTeps \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.sdata.set_pd_steps(pd_steps = 1) \n
		Sets the amount of power down bits in the TPC start pattern. \n
			:param pd_steps: integer Range: 0 to 1000
		"""
		param = Conversions.decimal_value_to_str(pd_steps)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa:PDSTeps {param}')

	def get_pu_steps(self) -> int:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa:PUSTeps \n
		Snippet: value: int = driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.sdata.get_pu_steps() \n
		Sets the amount of power up bits in the TPC start pattern. \n
			:return: pu_steps: integer Range: 0 to 1000
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa:PUSTeps?')
		return Conversions.str_to_int(response)

	def set_pu_steps(self, pu_steps: int) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa:PUSTeps \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.sdata.set_pu_steps(pu_steps = 1) \n
		Sets the amount of power up bits in the TPC start pattern. \n
			:param pu_steps: integer Range: 0 to 1000
		"""
		param = Conversions.decimal_value_to_str(pu_steps)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa:PUSTeps {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.Ts25141TpcStartPattSour:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa \n
		Snippet: value: enums.Ts25141TpcStartPattSour = driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.sdata.get_value() \n
		Sets the TPC pattern for initialization of the base stations power level. \n
			:return: sdata: PMAX| DLISt PMAX Maximum Power Less n Steps DLISt The TPC start pattern is taken from a data list.
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141TpcStartPattSour)

	def set_value(self, sdata: enums.Ts25141TpcStartPattSour) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.tpc.sdata.set_value(sdata = enums.Ts25141TpcStartPattSour.DLISt) \n
		Sets the TPC pattern for initialization of the base stations power level. \n
			:param sdata: PMAX| DLISt PMAX Maximum Power Less n Steps DLISt The TPC start pattern is taken from a data list.
		"""
		param = Conversions.enum_scalar_to_str(sdata, enums.Ts25141TpcStartPattSour)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:TPC:SDATa {param}')
