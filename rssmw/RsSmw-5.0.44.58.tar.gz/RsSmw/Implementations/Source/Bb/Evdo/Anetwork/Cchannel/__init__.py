from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cchannel:
	"""Cchannel commands group definition. 5 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cchannel", core, parent)

	@property
	def revision(self):
		"""revision commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_revision'):
			from .Revision import Revision
			self._revision = Revision(self._core, self._cmd_group)
		return self._revision

	def get_ps_offset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:CCHannel:PSOFfset \n
		Snippet: value: int = driver.source.bb.evdo.anetwork.cchannel.get_ps_offset() \n
		Sets the offset (in slots) from the start of control channel cycle to the start of the synchronous message capsule that
		contains the Sync Message. \n
			:return: ps_offset: integer Range: 0 to 3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:ANETwork:CCHannel:PSOFfset?')
		return Conversions.str_to_int(response)

	def set_ps_offset(self, ps_offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:CCHannel:PSOFfset \n
		Snippet: driver.source.bb.evdo.anetwork.cchannel.set_ps_offset(ps_offset = 1) \n
		Sets the offset (in slots) from the start of control channel cycle to the start of the synchronous message capsule that
		contains the Sync Message. \n
			:param ps_offset: integer Range: 0 to 3
		"""
		param = Conversions.decimal_value_to_str(ps_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:ANETwork:CCHannel:PSOFfset {param}')

	# noinspection PyTypeChecker
	def get_rate(self) -> enums.EvdoDataRate:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:CCHannel:RATE \n
		Snippet: value: enums.EvdoDataRate = driver.source.bb.evdo.anetwork.cchannel.get_rate() \n
		Sets the rate that the control channel messages are transmitted at. \n
			:return: rate: DR4K8| DR9K6| DR19K2| DR38K4| DR76K8| DR153K6| DR307K2| DR614K4| DR921K6| DR1228K8| DR1536K| DR1843K2| DR2457K6| DR3072K| DR460K8| DR768K| DR1075K2| DR2150K4| DR3686K4| DR4300K8| DR4915K2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:ANETwork:CCHannel:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoDataRate)

	def set_rate(self, rate: enums.EvdoDataRate) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:CCHannel:RATE \n
		Snippet: driver.source.bb.evdo.anetwork.cchannel.set_rate(rate = enums.EvdoDataRate.DR1075K2) \n
		Sets the rate that the control channel messages are transmitted at. \n
			:param rate: DR4K8| DR9K6| DR19K2| DR38K4| DR76K8| DR153K6| DR307K2| DR614K4| DR921K6| DR1228K8| DR1536K| DR1843K2| DR2457K6| DR3072K| DR460K8| DR768K| DR1075K2| DR2150K4| DR3686K4| DR4300K8| DR4915K2
		"""
		param = Conversions.enum_scalar_to_str(rate, enums.EvdoDataRate)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:ANETwork:CCHannel:RATE {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:CCHannel:STATe \n
		Snippet: value: bool = driver.source.bb.evdo.anetwork.cchannel.get_state() \n
		Enables or disables the control channel messages. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:ANETwork:CCHannel:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:ANETwork:CCHannel:STATe \n
		Snippet: driver.source.bb.evdo.anetwork.cchannel.set_state(state = False) \n
		Enables or disables the control channel messages. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:ANETwork:CCHannel:STATe {param}')

	def clone(self) -> 'Cchannel':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cchannel(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
