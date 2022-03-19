from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ssid:
	"""Ssid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssid", core, parent)

	def set(self, ssid: enums.GbasSsid, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:SSID \n
		Snippet: driver.source.bb.gbas.vdb.ssid.set(ssid = enums.GbasSsid.A, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the Station Slot Identifier SSID of the ground station. \n
			:param ssid: A| B| C| D| E| F| G| H
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.enum_scalar_to_str(ssid, enums.GbasSsid)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:SSID {param}')

	# noinspection PyTypeChecker
	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> enums.GbasSsid:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:SSID \n
		Snippet: value: enums.GbasSsid = driver.source.bb.gbas.vdb.ssid.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the Station Slot Identifier SSID of the ground station. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: ssid: A| B| C| D| E| F| G| H"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:SSID?')
		return Conversions.str_to_scalar_enum(response, enums.GbasSsid)
