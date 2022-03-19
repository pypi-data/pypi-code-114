from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scof:
	"""Scof commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scof", core, parent)

	def set(self, subcarrier_offset: enums.EutraPracNbiotSubcarrierOffset, configurationNull=repcap.ConfigurationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:NIOT:CFG<CH0>:SCOF \n
		Snippet: driver.source.bb.eutra.uplink.prach.niot.cfg.scof.set(subcarrier_offset = enums.EutraPracNbiotSubcarrierOffset._0, configurationNull = repcap.ConfigurationNull.Default) \n
		Sets the NPRACH subcarrier offset. \n
			:param subcarrier_offset: 0| 2| 12| 18| 24| 34| 36 | 6| 42| 48| 54| 60| 72| 78| 84| 90| 102| 108
			:param configurationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cfg')
		"""
		param = Conversions.enum_scalar_to_str(subcarrier_offset, enums.EutraPracNbiotSubcarrierOffset)
		configurationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(configurationNull, repcap.ConfigurationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:NIOT:CFG{configurationNull_cmd_val}:SCOF {param}')

	# noinspection PyTypeChecker
	def get(self, configurationNull=repcap.ConfigurationNull.Default) -> enums.EutraPracNbiotSubcarrierOffset:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:NIOT:CFG<CH0>:SCOF \n
		Snippet: value: enums.EutraPracNbiotSubcarrierOffset = driver.source.bb.eutra.uplink.prach.niot.cfg.scof.get(configurationNull = repcap.ConfigurationNull.Default) \n
		Sets the NPRACH subcarrier offset. \n
			:param configurationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cfg')
			:return: subcarrier_offset: 0| 2| 12| 18| 24| 34| 36 | 6| 42| 48| 54| 60| 72| 78| 84| 90| 102| 108"""
		configurationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(configurationNull, repcap.ConfigurationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:NIOT:CFG{configurationNull_cmd_val}:SCOF?')
		return Conversions.str_to_scalar_enum(response, enums.EutraPracNbiotSubcarrierOffset)
