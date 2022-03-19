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

	def set(self, data: enums.DataSourGnss, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:SIGNal:L1Band:L1C:DATA:NMESsage:TYPE \n
		Snippet: driver.source.bb.gnss.svid.qzss.signal.l1Band.l1C.data.nmessage.typePy.set(data = enums.DataSourGnss.DLISt, satelliteSvid = repcap.SatelliteSvid.Default) \n
		No command help available \n
			:param data: No help available
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DataSourGnss)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:SIGNal:L1Band:L1C:DATA:NMESsage:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> enums.DataSourGnss:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:QZSS:SIGNal:L1Band:L1C:DATA:NMESsage:TYPE \n
		Snippet: value: enums.DataSourGnss = driver.source.bb.gnss.svid.qzss.signal.l1Band.l1C.data.nmessage.typePy.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		No command help available \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: data: No help available"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:QZSS:SIGNal:L1Band:L1C:DATA:NMESsage:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourGnss)
