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
	def get_type_py(self) -> enums.ChanCodTypeEnhPcpc:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:PRACh:CCODing:TYPE \n
		Snippet: value: enums.ChanCodTypeEnhPcpc = driver.source.bb.w3Gpp.ts25141.wsignal.prach.ccoding.get_type_py() \n
		Selects the Transport Block Size to 168 bits or to 360 bits. \n
			:return: type_py: TB168| TB360
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:PRACh:CCODing:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.ChanCodTypeEnhPcpc)

	def set_type_py(self, type_py: enums.ChanCodTypeEnhPcpc) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:PRACh:CCODing:TYPE \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.prach.ccoding.set_type_py(type_py = enums.ChanCodTypeEnhPcpc.TB168) \n
		Selects the Transport Block Size to 168 bits or to 360 bits. \n
			:param type_py: TB168| TB360
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.ChanCodTypeEnhPcpc)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:PRACh:CCODing:TYPE {param}')
