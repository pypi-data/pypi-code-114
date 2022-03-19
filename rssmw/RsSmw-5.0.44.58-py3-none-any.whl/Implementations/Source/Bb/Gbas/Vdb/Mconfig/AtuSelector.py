from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AtuSelector:
	"""AtuSelector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("atuSelector", core, parent)

	def set(self, tch_unit: enums.GbasAppTchUnitSel, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:ATUSelector \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.atuSelector.set(tch_unit = enums.GbasAppTchUnitSel.FEET, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Requires 'Mode > GBAS' (LAAS) header information. Sets the units for the approach TCH,
		see [:SOURce<hw>]:BB:GBAS:VDB<ch>:MCONfig:ATCHeight. \n
			:param tch_unit: FEET| MET
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.enum_scalar_to_str(tch_unit, enums.GbasAppTchUnitSel)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:ATUSelector {param}')

	# noinspection PyTypeChecker
	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> enums.GbasAppTchUnitSel:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:ATUSelector \n
		Snippet: value: enums.GbasAppTchUnitSel = driver.source.bb.gbas.vdb.mconfig.atuSelector.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Requires 'Mode > GBAS' (LAAS) header information. Sets the units for the approach TCH,
		see [:SOURce<hw>]:BB:GBAS:VDB<ch>:MCONfig:ATCHeight. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: tch_unit: FEET| MET"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:ATUSelector?')
		return Conversions.str_to_scalar_enum(response, enums.GbasAppTchUnitSel)
