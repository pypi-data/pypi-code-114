from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sttm:
	"""Sttm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sttm", core, parent)

	def set(self, start_time: enums.EutraPracNbiotStartTimeMs, configurationNull=repcap.ConfigurationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:NIOT:CFG<CH0>:STTM \n
		Snippet: driver.source.bb.eutra.uplink.prach.niot.cfg.sttm.set(start_time = enums.EutraPracNbiotStartTimeMs._10, configurationNull = repcap.ConfigurationNull.Default) \n
		Sets the start time of the specific NPRACH configuration. \n
			:param start_time: 8| 16| 64| 128| 32| 256| 512| 1024 | 10| 20| 40| 80| 160| 320| 640| 1280| 2560| 5120
			:param configurationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cfg')
		"""
		param = Conversions.enum_scalar_to_str(start_time, enums.EutraPracNbiotStartTimeMs)
		configurationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(configurationNull, repcap.ConfigurationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:NIOT:CFG{configurationNull_cmd_val}:STTM {param}')

	# noinspection PyTypeChecker
	def get(self, configurationNull=repcap.ConfigurationNull.Default) -> enums.EutraPracNbiotStartTimeMs:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:NIOT:CFG<CH0>:STTM \n
		Snippet: value: enums.EutraPracNbiotStartTimeMs = driver.source.bb.eutra.uplink.prach.niot.cfg.sttm.get(configurationNull = repcap.ConfigurationNull.Default) \n
		Sets the start time of the specific NPRACH configuration. \n
			:param configurationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cfg')
			:return: start_time: 8| 16| 64| 128| 32| 256| 512| 1024 | 10| 20| 40| 80| 160| 320| 640| 1280| 2560| 5120"""
		configurationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(configurationNull, repcap.ConfigurationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:NIOT:CFG{configurationNull_cmd_val}:STTM?')
		return Conversions.str_to_scalar_enum(response, enums.EutraPracNbiotStartTimeMs)
