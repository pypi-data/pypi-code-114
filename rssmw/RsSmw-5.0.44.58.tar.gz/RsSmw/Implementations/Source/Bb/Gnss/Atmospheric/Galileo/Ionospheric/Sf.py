from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sf:
	"""Sf commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Region, default value after init: Region.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sf", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_region_get', 'repcap_region_set', repcap.Region.Nr1)

	def repcap_region_set(self, region: repcap.Region) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Region.Default
		Default value after init: Region.Nr1"""
		self._cmd_group.set_repcap_enum_value(region)

	def repcap_region_get(self) -> repcap.Region:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, sf: int, region=repcap.Region.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:GALileo:IONospheric:SF<CH> \n
		Snippet: driver.source.bb.gnss.atmospheric.galileo.ionospheric.sf.set(sf = 1, region = repcap.Region.Default) \n
		No command help available \n
			:param sf: No help available
			:param region: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sf')
		"""
		param = Conversions.decimal_value_to_str(sf)
		region_cmd_val = self._cmd_group.get_repcap_cmd_value(region, repcap.Region)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:GALileo:IONospheric:SF{region_cmd_val} {param}')

	def get(self, region=repcap.Region.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:GALileo:IONospheric:SF<CH> \n
		Snippet: value: int = driver.source.bb.gnss.atmospheric.galileo.ionospheric.sf.get(region = repcap.Region.Default) \n
		No command help available \n
			:param region: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sf')
			:return: sf: No help available"""
		region_cmd_val = self._cmd_group.get_repcap_cmd_value(region, repcap.Region)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:GALileo:IONospheric:SF{region_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Sf':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sf(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
