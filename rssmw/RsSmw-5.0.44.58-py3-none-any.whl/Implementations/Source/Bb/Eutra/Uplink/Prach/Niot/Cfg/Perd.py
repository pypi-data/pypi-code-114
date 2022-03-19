from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Perd:
	"""Perd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("perd", core, parent)

	def set(self, periodicity: enums.EutraPracNbiotPeriodicity, configurationNull=repcap.ConfigurationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:NIOT:CFG<CH0>:PERD \n
		Snippet: driver.source.bb.eutra.uplink.prach.niot.cfg.perd.set(periodicity = enums.EutraPracNbiotPeriodicity._10240, configurationNull = repcap.ConfigurationNull.Default) \n
		Sets NPRACH periodicity. \n
			:param periodicity: 40| 80| 160| 240| 320| 640| 1280| 2560 | 5120| 10240
			:param configurationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cfg')
		"""
		param = Conversions.enum_scalar_to_str(periodicity, enums.EutraPracNbiotPeriodicity)
		configurationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(configurationNull, repcap.ConfigurationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:NIOT:CFG{configurationNull_cmd_val}:PERD {param}')

	# noinspection PyTypeChecker
	def get(self, configurationNull=repcap.ConfigurationNull.Default) -> enums.EutraPracNbiotPeriodicity:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:NIOT:CFG<CH0>:PERD \n
		Snippet: value: enums.EutraPracNbiotPeriodicity = driver.source.bb.eutra.uplink.prach.niot.cfg.perd.get(configurationNull = repcap.ConfigurationNull.Default) \n
		Sets NPRACH periodicity. \n
			:param configurationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cfg')
			:return: periodicity: 40| 80| 160| 240| 320| 640| 1280| 2560 | 5120| 10240"""
		configurationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(configurationNull, repcap.ConfigurationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:NIOT:CFG{configurationNull_cmd_val}:PERD?')
		return Conversions.str_to_scalar_enum(response, enums.EutraPracNbiotPeriodicity)
