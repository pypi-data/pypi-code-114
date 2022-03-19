from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tcase:
	"""Tcase commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcase", core, parent)

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	# noinspection PyTypeChecker
	def get_value(self) -> enums.Ts25141Tc:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:TCASe \n
		Snippet: value: enums.Ts25141Tc = driver.source.bb.w3Gpp.ts25141.tcase.get_value() \n
		Selects a test case defined by the standard. The signal generator is preset according to the selected standard. Depending
		on the selected test case, the parameters of the TS25141 commands are preset. For most test cases also the parameters of
		one or more of the subsystems SOURce:AWGN, SOURce:W3GPp, SOURce:DM and SOURce:FSIM are preset. The preset parameters are
		activated with command BB:W3GP:TS25141:TCAS:EXEC \n
			:return: tcase: TC642| TC66| TC72| TC73| TC74| TC75| TC76| TC78| TC821| TC831| TC832| TC833| TC834| TC84| TC85| TC86| TC881| TC882| TC883| TC884| TC891| TC892| TC893| TC894
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:TCASe?')
		return Conversions.str_to_scalar_enum(response, enums.Ts25141Tc)

	def set_value(self, tcase: enums.Ts25141Tc) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:TCASe \n
		Snippet: driver.source.bb.w3Gpp.ts25141.tcase.set_value(tcase = enums.Ts25141Tc.TC642) \n
		Selects a test case defined by the standard. The signal generator is preset according to the selected standard. Depending
		on the selected test case, the parameters of the TS25141 commands are preset. For most test cases also the parameters of
		one or more of the subsystems SOURce:AWGN, SOURce:W3GPp, SOURce:DM and SOURce:FSIM are preset. The preset parameters are
		activated with command BB:W3GP:TS25141:TCAS:EXEC \n
			:param tcase: TC642| TC66| TC72| TC73| TC74| TC75| TC76| TC78| TC821| TC831| TC832| TC833| TC834| TC84| TC85| TC86| TC881| TC882| TC883| TC884| TC891| TC892| TC893| TC894
		"""
		param = Conversions.enum_scalar_to_str(tcase, enums.Ts25141Tc)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:TCASe {param}')

	def clone(self) -> 'Tcase':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tcase(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
