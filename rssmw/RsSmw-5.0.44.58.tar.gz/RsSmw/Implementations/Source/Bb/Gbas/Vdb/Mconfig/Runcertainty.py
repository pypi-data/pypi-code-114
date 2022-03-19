from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Runcertainty:
	"""Runcertainty commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("runcertainty", core, parent)

	def set(self, runc: int, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:RUNCertainty \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.runcertainty.set(runc = 1, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Set the refractivity uncertainty. \n
			:param runc: integer Range: 0 to 255
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.decimal_value_to_str(runc)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:RUNCertainty {param}')

	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:RUNCertainty \n
		Snippet: value: int = driver.source.bb.gbas.vdb.mconfig.runcertainty.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Set the refractivity uncertainty. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: runc: integer Range: 0 to 255"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:RUNCertainty?')
		return Conversions.str_to_int(response)
