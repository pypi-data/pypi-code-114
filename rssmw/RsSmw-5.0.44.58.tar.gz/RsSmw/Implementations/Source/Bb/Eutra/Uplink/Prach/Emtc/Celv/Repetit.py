from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Repetit:
	"""Repetit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("repetit", core, parent)

	def set(self, repetitions: enums.EutraRepetitionsNbiot, ceLevel=repcap.CeLevel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:EMTC:CELV<CH0>:REPetit \n
		Snippet: driver.source.bb.eutra.uplink.prach.emtc.celv.repetit.set(repetitions = enums.EutraRepetitionsNbiot.R1, ceLevel = repcap.CeLevel.Default) \n
		Sets the PRACH number of repetitions. \n
			:param repetitions: R1| R2| R4| R8| R16| R32| R64| R128
			:param ceLevel: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Celv')
		"""
		param = Conversions.enum_scalar_to_str(repetitions, enums.EutraRepetitionsNbiot)
		ceLevel_cmd_val = self._cmd_group.get_repcap_cmd_value(ceLevel, repcap.CeLevel)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:EMTC:CELV{ceLevel_cmd_val}:REPetit {param}')

	# noinspection PyTypeChecker
	def get(self, ceLevel=repcap.CeLevel.Default) -> enums.EutraRepetitionsNbiot:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:EMTC:CELV<CH0>:REPetit \n
		Snippet: value: enums.EutraRepetitionsNbiot = driver.source.bb.eutra.uplink.prach.emtc.celv.repetit.get(ceLevel = repcap.CeLevel.Default) \n
		Sets the PRACH number of repetitions. \n
			:param ceLevel: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Celv')
			:return: repetitions: R1| R2| R4| R8| R16| R32| R64| R128"""
		ceLevel_cmd_val = self._cmd_group.get_repcap_cmd_value(ceLevel, repcap.CeLevel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:EMTC:CELV{ceLevel_cmd_val}:REPetit?')
		return Conversions.str_to_scalar_enum(response, enums.EutraRepetitionsNbiot)
