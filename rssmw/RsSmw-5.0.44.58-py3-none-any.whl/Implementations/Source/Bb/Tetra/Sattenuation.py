from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sattenuation:
	"""Sattenuation commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Slot, default value after init: Slot.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sattenuation", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_slot_get', 'repcap_slot_set', repcap.Slot.Nr1)

	def repcap_slot_set(self, slot: repcap.Slot) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Slot.Default
		Default value after init: Slot.Nr1"""
		self._cmd_group.set_repcap_enum_value(slot)

	def repcap_slot_get(self) -> repcap.Slot:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, sattenuation: float, slot=repcap.Slot.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SATTenuation<CH> \n
		Snippet: driver.source.bb.tetra.sattenuation.set(sattenuation = 1.0, slot = repcap.Slot.Default) \n
		Enters four different values for level attenuation. The frame editor can be used to set the level attenuation for the
		four slots to one of these predefined values independently of one another. The entered value determines the slot output
		power (slot power = RF power - attenuation) . 0 dB attenuation corresponds to 'Slot Level' = Full. This feature is
		provided to set a sequence of slots to different levels in order to measure transmission stability. The frame editor is
		likewise used to assign the 'Slot Level' attribute Attenuated to individual slots. \n
			:param sattenuation: float Range: 0 to 50
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sattenuation')
		"""
		param = Conversions.decimal_value_to_str(sattenuation)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		self._core.io.write(f'SOURce<HwInstance>:BB:TETRa:SATTenuation{slot_cmd_val} {param}')

	def get(self, slot=repcap.Slot.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:TETRa:SATTenuation<CH> \n
		Snippet: value: float = driver.source.bb.tetra.sattenuation.get(slot = repcap.Slot.Default) \n
		Enters four different values for level attenuation. The frame editor can be used to set the level attenuation for the
		four slots to one of these predefined values independently of one another. The entered value determines the slot output
		power (slot power = RF power - attenuation) . 0 dB attenuation corresponds to 'Slot Level' = Full. This feature is
		provided to set a sequence of slots to different levels in order to measure transmission stability. The frame editor is
		likewise used to assign the 'Slot Level' attribute Attenuated to individual slots. \n
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sattenuation')
			:return: sattenuation: float Range: 0 to 50"""
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TETRa:SATTenuation{slot_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Sattenuation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sattenuation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
