from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rep:
	"""Rep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rep", core, parent)

	def set(self, repetitions: enums.EutraIotRepetitions, configurationNull=repcap.ConfigurationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:NIOT:CFG<CH0>:REP \n
		Snippet: driver.source.bb.eutra.uplink.prach.niot.cfg.rep.set(repetitions = enums.EutraIotRepetitions.R1, configurationNull = repcap.ConfigurationNull.Default) \n
		Queries the number of NPRACH repetitions per preamble attempt. \n
			:param repetitions: R1| R2| R4| R8| R16| R32| R64| R128 | R192| R256| R384| R512| R768| R1024| R1536| R2048| R12| R24
			:param configurationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cfg')
		"""
		param = Conversions.enum_scalar_to_str(repetitions, enums.EutraIotRepetitions)
		configurationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(configurationNull, repcap.ConfigurationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:NIOT:CFG{configurationNull_cmd_val}:REP {param}')

	# noinspection PyTypeChecker
	def get(self, configurationNull=repcap.ConfigurationNull.Default) -> enums.EutraIotRepetitions:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:NIOT:CFG<CH0>:REP \n
		Snippet: value: enums.EutraIotRepetitions = driver.source.bb.eutra.uplink.prach.niot.cfg.rep.get(configurationNull = repcap.ConfigurationNull.Default) \n
		Queries the number of NPRACH repetitions per preamble attempt. \n
			:param configurationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cfg')
			:return: repetitions: R1| R2| R4| R8| R16| R32| R64| R128 | R192| R256| R384| R512| R768| R1024| R1536| R2048| R12| R24"""
		configurationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(configurationNull, repcap.ConfigurationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:NIOT:CFG{configurationNull_cmd_val}:REP?')
		return Conversions.str_to_scalar_enum(response, enums.EutraIotRepetitions)
