from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GsaDesignator:
	"""GsaDesignator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gsaDesignator", core, parent)

	def set(self, gsad: enums.GbasGrdStAcDes, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:GSADesignator \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.gsaDesignator.set(gsad = enums.GbasGrdStAcDes.GADA, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the ground station accuracy designator. \n
			:param gsad: GADA| GADB| GADC
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.enum_scalar_to_str(gsad, enums.GbasGrdStAcDes)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:GSADesignator {param}')

	# noinspection PyTypeChecker
	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> enums.GbasGrdStAcDes:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:GSADesignator \n
		Snippet: value: enums.GbasGrdStAcDes = driver.source.bb.gbas.vdb.mconfig.gsaDesignator.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Sets the ground station accuracy designator. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: gsad: GADA| GADB| GADC"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:GSADesignator?')
		return Conversions.str_to_scalar_enum(response, enums.GbasGrdStAcDes)
