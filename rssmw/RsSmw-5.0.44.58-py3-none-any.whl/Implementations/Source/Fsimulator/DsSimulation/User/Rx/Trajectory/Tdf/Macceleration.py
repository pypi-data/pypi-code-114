from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Macceleration:
	"""Macceleration commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("macceleration", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:RX:TRAJectory:TDF:MACCeleration:STATe \n
		Snippet: value: bool = driver.source.fsimulator.dsSimulation.user.rx.trajectory.tdf.macceleration.get_state() \n
		No command help available \n
			:return: traj_tdf_acc_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:RX:TRAJectory:TDF:MACCeleration:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, traj_tdf_acc_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:RX:TRAJectory:TDF:MACCeleration:STATe \n
		Snippet: driver.source.fsimulator.dsSimulation.user.rx.trajectory.tdf.macceleration.set_state(traj_tdf_acc_state = False) \n
		No command help available \n
			:param traj_tdf_acc_state: No help available
		"""
		param = Conversions.bool_to_str(traj_tdf_acc_state)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:USER:RX:TRAJectory:TDF:MACCeleration:STATe {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:RX:TRAJectory:TDF:MACCeleration \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.user.rx.trajectory.tdf.macceleration.get_value() \n
		No command help available \n
			:return: traj_tdf_acc_max: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:RX:TRAJectory:TDF:MACCeleration?')
		return Conversions.str_to_float(response)

	def set_value(self, traj_tdf_acc_max: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:RX:TRAJectory:TDF:MACCeleration \n
		Snippet: driver.source.fsimulator.dsSimulation.user.rx.trajectory.tdf.macceleration.set_value(traj_tdf_acc_max = 1.0) \n
		No command help available \n
			:param traj_tdf_acc_max: No help available
		"""
		param = Conversions.decimal_value_to_str(traj_tdf_acc_max)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:USER:RX:TRAJectory:TDF:MACCeleration {param}')
