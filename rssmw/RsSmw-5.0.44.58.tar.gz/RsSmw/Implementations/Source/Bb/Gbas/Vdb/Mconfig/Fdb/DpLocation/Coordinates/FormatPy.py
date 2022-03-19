from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, format_py: enums.PositionFormat, vdbTransmitter=repcap.VdbTransmitter.Default, fdbTransmitter=repcap.FdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:FDB<ST>:DPLocation:COORdinates:FORMat \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.fdb.dpLocation.coordinates.formatPy.set(format_py = enums.PositionFormat.DECimal, vdbTransmitter = repcap.VdbTransmitter.Default, fdbTransmitter = repcap.FdbTransmitter.Default) \n
		Sets the format in which the latitude and longitude are set. \n
			:param format_py: DMS| DECimal
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param fdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fdb')
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.PositionFormat)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		fdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(fdbTransmitter, repcap.FdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:FDB{fdbTransmitter_cmd_val}:DPLocation:COORdinates:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default, fdbTransmitter=repcap.FdbTransmitter.Default) -> enums.PositionFormat:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:FDB<ST>:DPLocation:COORdinates:FORMat \n
		Snippet: value: enums.PositionFormat = driver.source.bb.gbas.vdb.mconfig.fdb.dpLocation.coordinates.formatPy.get(vdbTransmitter = repcap.VdbTransmitter.Default, fdbTransmitter = repcap.FdbTransmitter.Default) \n
		Sets the format in which the latitude and longitude are set. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:param fdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fdb')
			:return: format_py: DMS| DECimal"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		fdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(fdbTransmitter, repcap.FdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:FDB{fdbTransmitter_cmd_val}:DPLocation:COORdinates:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.PositionFormat)
