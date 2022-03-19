from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rletter:
	"""Rletter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rletter", core, parent)

	def set(self, rlet: enums.GbasRunLet, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:RLETter \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.rletter.set(rlet = enums.GbasRunLet.LETC, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the runway letter. \n
			:param rlet: NLETter| LETR| LETL| LETC
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.enum_scalar_to_str(rlet, enums.GbasRunLet)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:RLETter {param}')

	# noinspection PyTypeChecker
	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> enums.GbasRunLet:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:RLETter \n
		Snippet: value: enums.GbasRunLet = driver.source.bb.gbas.vdb.mconfig.rletter.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the runway letter. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: rlet: NLETter| LETR| LETL| LETC"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:RLETter?')
		return Conversions.str_to_scalar_enum(response, enums.GbasRunLet)
