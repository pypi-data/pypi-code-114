from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdf:
	"""Tdf commands group definition. 6 total commands, 2 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdf", core, parent)

	@property
	def enu(self):
		"""enu commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_enu'):
			from .Enu import Enu
			self._enu = Enu(self._core, self._cmd_group)
		return self._enu

	@property
	def macceleration(self):
		"""macceleration commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_macceleration'):
			from .Macceleration import Macceleration
			self._macceleration = Macceleration(self._core, self._cmd_group)
		return self._macceleration

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:TX:TRAJectory:TDF:CATalog \n
		Snippet: value: List[str] = driver.source.fsimulator.dsSimulation.user.tx.trajectory.tdf.get_catalog() \n
		No command help available \n
			:return: filenames: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:TX:TRAJectory:TDF:CATalog?')
		return Conversions.str_to_str_list(response)

	# noinspection PyTypeChecker
	def get_ebehavior(self) -> enums.FadDssUsrTrajBeh:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:TX:TRAJectory:TDF:EBEHavior \n
		Snippet: value: enums.FadDssUsrTrajBeh = driver.source.fsimulator.dsSimulation.user.tx.trajectory.tdf.get_ebehavior() \n
		No command help available \n
			:return: traj_tdf_behavior: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:TX:TRAJectory:TDF:EBEHavior?')
		return Conversions.str_to_scalar_enum(response, enums.FadDssUsrTrajBeh)

	def set_ebehavior(self, traj_tdf_behavior: enums.FadDssUsrTrajBeh) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:TX:TRAJectory:TDF:EBEHavior \n
		Snippet: driver.source.fsimulator.dsSimulation.user.tx.trajectory.tdf.set_ebehavior(traj_tdf_behavior = enums.FadDssUsrTrajBeh.JUMP) \n
		No command help available \n
			:param traj_tdf_behavior: No help available
		"""
		param = Conversions.enum_scalar_to_str(traj_tdf_behavior, enums.FadDssUsrTrajBeh)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:USER:TX:TRAJectory:TDF:EBEHavior {param}')

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:TX:TRAJectory:TDF:SELect \n
		Snippet: value: str = driver.source.fsimulator.dsSimulation.user.tx.trajectory.tdf.get_select() \n
		No command help available \n
			:return: traj_tdf_sel: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:TX:TRAJectory:TDF:SELect?')
		return trim_str_response(response)

	def set_select(self, traj_tdf_sel: str) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:TX:TRAJectory:TDF:SELect \n
		Snippet: driver.source.fsimulator.dsSimulation.user.tx.trajectory.tdf.set_select(traj_tdf_sel = '1') \n
		No command help available \n
			:param traj_tdf_sel: No help available
		"""
		param = Conversions.value_to_quoted_str(traj_tdf_sel)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:USER:TX:TRAJectory:TDF:SELect {param}')

	def clone(self) -> 'Tdf':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tdf(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
