from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Shiptoship:
	"""Shiptoship commands group definition. 18 total commands, 3 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("shiptoship", core, parent)

	@property
	def rx(self):
		"""rx commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_rx'):
			from .Rx import Rx
			self._rx = Rx(self._core, self._cmd_group)
		return self._rx

	@property
	def tx(self):
		"""tx commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_tx'):
			from .Tx import Tx
			self._tx = Tx(self._core, self._cmd_group)
		return self._tx

	@property
	def water(self):
		"""water commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_water'):
			from .Water import Water
			self._water = Water(self._core, self._cmd_group)
		return self._water

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:PRESet \n
		Snippet: driver.source.fsimulator.dsSimulation.shiptoship.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:PRESet \n
		Snippet: driver.source.fsimulator.dsSimulation.shiptoship.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:PRESet', opc_timeout_ms)

	def get_ttime(self) -> str:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:TTIMe \n
		Snippet: value: str = driver.source.fsimulator.dsSimulation.shiptoship.get_ttime() \n
		No command help available \n
			:return: turn_time: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:TTIMe?')
		return trim_str_response(response)

	def set_ttime(self, turn_time: str) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:TTIMe \n
		Snippet: driver.source.fsimulator.dsSimulation.shiptoship.set_ttime(turn_time = '1') \n
		No command help available \n
			:param turn_time: No help available
		"""
		param = Conversions.value_to_quoted_str(turn_time)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:TTIMe {param}')

	def get_xdistance(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:XDIStance \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.shiptoship.get_xdistance() \n
		No command help available \n
			:return: xdistance: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:XDIStance?')
		return Conversions.str_to_float(response)

	def set_xdistance(self, xdistance: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:XDIStance \n
		Snippet: driver.source.fsimulator.dsSimulation.shiptoship.set_xdistance(xdistance = 1.0) \n
		No command help available \n
			:param xdistance: No help available
		"""
		param = Conversions.decimal_value_to_str(xdistance)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:XDIStance {param}')

	def get_ydistance(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:YDIStance \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.shiptoship.get_ydistance() \n
		No command help available \n
			:return: ydistance: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:YDIStance?')
		return Conversions.str_to_float(response)

	def set_ydistance(self, ydistance: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:YDIStance \n
		Snippet: driver.source.fsimulator.dsSimulation.shiptoship.set_ydistance(ydistance = 1.0) \n
		No command help available \n
			:param ydistance: No help available
		"""
		param = Conversions.decimal_value_to_str(ydistance)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:YDIStance {param}')

	def clone(self) -> 'Shiptoship':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Shiptoship(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
