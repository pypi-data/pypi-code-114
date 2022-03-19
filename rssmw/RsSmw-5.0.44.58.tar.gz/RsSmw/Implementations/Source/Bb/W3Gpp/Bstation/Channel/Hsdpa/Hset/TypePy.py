from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.HsHsetScchType, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:TYPE \n
		Snippet: driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.typePy.set(type_py = enums.HsHsetScchType.LOPeration, baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the HS-SCCH type. \n
			:param type_py: NORMal| LOPeration| MIMO NORMal Normal operation mode. LOPeration HS-SCCH less operation mode. MIMO HS-SCCH Type 3 mode is defined for MIMO operation. Enabling this operation mode, enables the MIMO parameters [:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:HSDPa:MIMO:CVPBdi, [:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:HSDPa:MIMO:MODulationdi, [:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:HSDPa:MIMO:PWPattern and [:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:HSDPa:MIMO:STAPattern and all Stream 2 parameters.
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.HsHsetScchType)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, baseStation=repcap.BaseStation.Default, channelNull=repcap.ChannelNull.Default) -> enums.HsHsetScchType:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:CHANnel<CH0>:HSDPa:HSET:TYPE \n
		Snippet: value: enums.HsHsetScchType = driver.source.bb.w3Gpp.bstation.channel.hsdpa.hset.typePy.get(baseStation = repcap.BaseStation.Default, channelNull = repcap.ChannelNull.Default) \n
		Sets the HS-SCCH type. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: type_py: NORMal| LOPeration| MIMO NORMal Normal operation mode. LOPeration HS-SCCH less operation mode. MIMO HS-SCCH Type 3 mode is defined for MIMO operation. Enabling this operation mode, enables the MIMO parameters [:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:HSDPa:MIMO:CVPBdi, [:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:HSDPa:MIMO:MODulationdi, [:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:HSDPa:MIMO:PWPattern and [:SOURcehw]:BB:W3GPp:BSTationst:CHANnelch0:HSDPa:MIMO:STAPattern and all Stream 2 parameters."""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:CHANnel{channelNull_cmd_val}:HSDPa:HSET:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.HsHsetScchType)
