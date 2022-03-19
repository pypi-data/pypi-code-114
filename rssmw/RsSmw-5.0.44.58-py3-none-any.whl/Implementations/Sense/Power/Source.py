from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.PowSensSource, channel=repcap.Channel.Default) -> None:
		"""SCPI: SENSe<CH>:[POWer]:SOURce \n
		Snippet: driver.sense.power.source.set(source = enums.PowSensSource.A, channel = repcap.Channel.Default) \n
		Determines the signal to be measured. Note: When measuring the RF signal, the sensor considers the corresponding
		correction factor at that frequency, and uses the level setting of the instrument as reference level. \n
			:param source: A| USER| RF | B
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.PowSensSource)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe{channel_cmd_val}:POWer:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, channel=repcap.Channel.Default) -> enums.PowSensSource:
		"""SCPI: SENSe<CH>:[POWer]:SOURce \n
		Snippet: value: enums.PowSensSource = driver.sense.power.source.get(channel = repcap.Channel.Default) \n
		Determines the signal to be measured. Note: When measuring the RF signal, the sensor considers the corresponding
		correction factor at that frequency, and uses the level setting of the instrument as reference level. \n
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sense')
			:return: source: A| USER| RF | B"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe{channel_cmd_val}:POWer:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.PowSensSource)
