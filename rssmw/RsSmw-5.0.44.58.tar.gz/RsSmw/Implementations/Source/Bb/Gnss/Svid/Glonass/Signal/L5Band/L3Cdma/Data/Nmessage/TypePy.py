from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, data: enums.DataSourGnss, satelliteSvid=repcap.SatelliteSvid.Default, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:SIGNal:L5Band:L3CDma<US>:DATA:NMESsage:TYPE \n
		Snippet: driver.source.bb.gnss.svid.glonass.signal.l5Band.l3Cdma.data.nmessage.typePy.set(data = enums.DataSourGnss.DLISt, satelliteSvid = repcap.SatelliteSvid.Default, index = repcap.Index.Default) \n
		No command help available \n
			:param data: No help available
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'L3Cdma')
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DataSourGnss)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:SIGNal:L5Band:L3CDma{index_cmd_val}:DATA:NMESsage:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, satelliteSvid=repcap.SatelliteSvid.Default, index=repcap.Index.Default) -> enums.DataSourGnss:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GLONass:SIGNal:L5Band:L3CDma<US>:DATA:NMESsage:TYPE \n
		Snippet: value: enums.DataSourGnss = driver.source.bb.gnss.svid.glonass.signal.l5Band.l3Cdma.data.nmessage.typePy.get(satelliteSvid = repcap.SatelliteSvid.Default, index = repcap.Index.Default) \n
		No command help available \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'L3Cdma')
			:return: data: No help available"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GLONass:SIGNal:L5Band:L3CDma{index_cmd_val}:DATA:NMESsage:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourGnss)
