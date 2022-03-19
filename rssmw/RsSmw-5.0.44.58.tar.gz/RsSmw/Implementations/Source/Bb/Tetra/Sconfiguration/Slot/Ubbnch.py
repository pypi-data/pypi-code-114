from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ubbnch:
	"""Ubbnch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ubbnch", core, parent)

	def set(self, ubbnch: bool, slot=repcap.Slot.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:SLOT<ST>:UBBNch \n
		Snippet: driver.source.bb.tetra.sconfiguration.slot.ubbnch.set(ubbnch = False, slot = repcap.Slot.Default) \n
		Enables/disables auto coding of the data. If enabled, the selection of the data source is disabled. \n
			:param ubbnch: 1| ON| 0| OFF
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
		"""
		param = Conversions.bool_to_str(ubbnch)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:SLOT{slot_cmd_val}:UBBNch {param}')

	def get(self, slot=repcap.Slot.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SCONfiguration:SLOT<ST>:UBBNch \n
		Snippet: value: bool = driver.source.bb.tetra.sconfiguration.slot.ubbnch.get(slot = repcap.Slot.Default) \n
		Enables/disables auto coding of the data. If enabled, the selection of the data source is disabled. \n
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slot')
			:return: ubbnch: 1| ON| 0| OFF"""
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TETRa:SCONfiguration:SLOT{slot_cmd_val}:UBBNch?')
		return Conversions.str_to_bool(response)
