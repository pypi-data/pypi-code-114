from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Subc:
	"""Subc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subc", core, parent)

	def set(self, subcarriers: enums.EutraPracNbiotSubcarriers, configurationNull=repcap.ConfigurationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:NIOT:CFG<CH0>:SUBC \n
		Snippet: driver.source.bb.eutra.uplink.prach.niot.cfg.subc.set(subcarriers = enums.EutraPracNbiotSubcarriers._12, configurationNull = repcap.ConfigurationNull.Default) \n
		Sets the number of NPRACH subcarriers. \n
			:param subcarriers: 12| 24| 36| 48
			:param configurationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cfg')
		"""
		param = Conversions.enum_scalar_to_str(subcarriers, enums.EutraPracNbiotSubcarriers)
		configurationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(configurationNull, repcap.ConfigurationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:NIOT:CFG{configurationNull_cmd_val}:SUBC {param}')

	# noinspection PyTypeChecker
	def get(self, configurationNull=repcap.ConfigurationNull.Default) -> enums.EutraPracNbiotSubcarriers:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:NIOT:CFG<CH0>:SUBC \n
		Snippet: value: enums.EutraPracNbiotSubcarriers = driver.source.bb.eutra.uplink.prach.niot.cfg.subc.get(configurationNull = repcap.ConfigurationNull.Default) \n
		Sets the number of NPRACH subcarriers. \n
			:param configurationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cfg')
			:return: subcarriers: 12| 24| 36| 48"""
		configurationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(configurationNull, repcap.ConfigurationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:NIOT:CFG{configurationNull_cmd_val}:SUBC?')
		return Conversions.str_to_scalar_enum(response, enums.EutraPracNbiotSubcarriers)
