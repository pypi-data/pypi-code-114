from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tmodel:
	"""Tmodel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tmodel", core, parent)

	# noinspection PyTypeChecker
	def get_bstation(self) -> enums.Ts25141IfScen:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:SETTing:TMODel:BSTation \n
		Snippet: value: enums.Ts25141IfScen = driver.source.bb.w3Gpp.ts25141.ifRignal.setting.tmodel.get_bstation() \n
		Selects the interfering signal from a list of test models in accordance with TS 25.141. All test models refer to the
		predefined downlink configurations. \n
			:return: bstation: TM164| TM116| TM132| TM2| TM316| TM332| TM4| TM538| TM528| TM58
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:IFSignal:SETTing:TMODel:BSTation?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141IfScen)

	def set_bstation(self, bstation: enums.Ts25141IfScen) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:IFSignal:SETTing:TMODel:BSTation \n
		Snippet: driver.source.bb.w3Gpp.ts25141.ifRignal.setting.tmodel.set_bstation(bstation = enums.Ts25141IfScen.TM116) \n
		Selects the interfering signal from a list of test models in accordance with TS 25.141. All test models refer to the
		predefined downlink configurations. \n
			:param bstation: TM164| TM116| TM132| TM2| TM316| TM332| TM4| TM538| TM528| TM58
		"""
		param = Conversions.enum_scalar_to_str(bstation, enums.Ts25141IfScen)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:IFSignal:SETTing:TMODel:BSTation {param}')
