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
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:SIGNal:L5Band:L5S:DATA:NMESsage:TYPE \n
		Snippet: driver.source.bb.gnss.svid.gps.signal.l5Band.l5S.data.nmessage.typePy.set(data = enums.DataSourGnss.DLISt, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the data source used for the generation of the navigation message. \n
			:param data: ZERO| ONE| PATTern| PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt| RNData| ZNData ZERO|ONE|PATTern|PN9|PN11|PN15|PN16|PN20|PN21|PN23|DLISt Arbitrary data source. Define the pattern and load an existing data list file with the commands: [:SOURcehw]:BB:GNSS:SVIDch:GPS:SIGNal:L1Band:CA:DATA:NMESsage:PATTern [:SOURcehw]:BB:GNSS:SVIDch:GPS:SIGNal:L1Band:CA:DATA:NMESsage:DSELect RNData Summary indication for real navigation data. Current navigation message type depends on the GNSS system and the RF band, e.g. for GPS in L1 RNData means LNAV. ZNData Zero navigation data Sets the orbit and clock correction parameters in the broadcasted navigation message to zero.
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DataSourGnss)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:SIGNal:L5Band:L5S:DATA:NMESsage:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> enums.DataSourGnss:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GPS:SIGNal:L5Band:L5S:DATA:NMESsage:TYPE \n
		Snippet: value: enums.DataSourGnss = driver.source.bb.gnss.svid.gps.signal.l5Band.l5S.data.nmessage.typePy.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the data source used for the generation of the navigation message. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: data: ZERO| ONE| PATTern| PN9| PN11| PN15| PN16| PN20| PN21| PN23| DLISt| RNData| ZNData ZERO|ONE|PATTern|PN9|PN11|PN15|PN16|PN20|PN21|PN23|DLISt Arbitrary data source. Define the pattern and load an existing data list file with the commands: [:SOURcehw]:BB:GNSS:SVIDch:GPS:SIGNal:L1Band:CA:DATA:NMESsage:PATTern [:SOURcehw]:BB:GNSS:SVIDch:GPS:SIGNal:L1Band:CA:DATA:NMESsage:DSELect RNData Summary indication for real navigation data. Current navigation message type depends on the GNSS system and the RF band, e.g. for GPS in L1 RNData means LNAV. ZNData Zero navigation data Sets the orbit and clock correction parameters in the broadcasted navigation message to zero."""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GPS:SIGNal:L5Band:L5S:DATA:NMESsage:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourGnss)
