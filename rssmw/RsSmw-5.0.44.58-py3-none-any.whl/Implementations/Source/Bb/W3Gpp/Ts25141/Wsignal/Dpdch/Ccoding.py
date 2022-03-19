from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccoding:
	"""Ccoding commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccoding", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.ChanCodType:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPDCh:CCODing:TYPE \n
		Snippet: value: enums.ChanCodType = driver.source.bb.w3Gpp.ts25141.wsignal.dpdch.ccoding.get_type_py() \n
		Selects the channel coding scheme in accordance with the 3GPP specification. \n
			:return: type_py: M12K2| M64K| M144k| M384k| AMR M12K2 | M64K | M144K | M384K Measurement channel with an input data bit rate of respectively 12.2 ksps, 64 ksps, 144 ksps and 384 ksps AMR Channel coding for the AMR Coder (coding a voice channel)
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:DPDCh:CCODing:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.ChanCodType)

	def set_type_py(self, type_py: enums.ChanCodType) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPDCh:CCODing:TYPE \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.dpdch.ccoding.set_type_py(type_py = enums.ChanCodType.AMR) \n
		Selects the channel coding scheme in accordance with the 3GPP specification. \n
			:param type_py: M12K2| M64K| M144k| M384k| AMR M12K2 | M64K | M144K | M384K Measurement channel with an input data bit rate of respectively 12.2 ksps, 64 ksps, 144 ksps and 384 ksps AMR Channel coding for the AMR Coder (coding a voice channel)
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.ChanCodType)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:DPDCh:CCODing:TYPE {param}')
