from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	# noinspection PyTypeChecker
	def get(self, modulation: enums.ModulationC) -> enums.ModulationC:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:AI:MCCH:MODulation \n
		Snippet: value: enums.ModulationC = driver.source.bb.eutra.downlink.mbsfn.ai.mcch.modulation.get(modulation = enums.ModulationC.QAM16) \n
		Queries the values as set with the command [:SOURce<hw>]:BB:EUTRa:DL:MBSFn:AI:MCCH:MCS. \n
			:param modulation: QPSK| QAM16| QAM64
			:return: modulation: QPSK| QAM16| QAM64"""
		param = Conversions.enum_scalar_to_str(modulation, enums.ModulationC)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:AI:MCCH:MODulation? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModulationC)
