from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pparameter:
	"""Pparameter commands group definition. 12 total commands, 5 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pparameter", core, parent)

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	@property
	def pchannel(self):
		"""pchannel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pchannel'):
			from .Pchannel import Pchannel
			self._pchannel = Pchannel(self._core, self._cmd_group)
		return self._pchannel

	@property
	def piChannel(self):
		"""piChannel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_piChannel'):
			from .PiChannel import PiChannel
			self._piChannel = PiChannel(self._core, self._cmd_group)
		return self._piChannel

	@property
	def schannel(self):
		"""schannel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_schannel'):
			from .Schannel import Schannel
			self._schannel = Schannel(self._core, self._cmd_group)
		return self._schannel

	@property
	def tchannel(self):
		"""tchannel commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_tchannel'):
			from .Tchannel import Tchannel
			self._tchannel = Tchannel(self._core, self._cmd_group)
		return self._tchannel

	# noinspection PyTypeChecker
	def get_crest(self) -> enums.CresFactMode:
		"""SCPI: [SOURce<HW>]:BB:C2K:PPARameter:CRESt \n
		Snippet: value: enums.CresFactMode = driver.source.bb.c2K.pparameter.get_crest() \n
		This command selects the desired range for the crest factor of the test scenario. The crest factor of the signal is kept
		in the desired range by automatically setting appropriate Walsh codes and timing offsets. The setting takes effect only
		after execution of command [:SOURce<hw>]:BB:C2K:PPARameter:EXECute.
		The setting of command [:SOURce<hw>]:BB:C2K:BSTation<st>:CGRoup<di0>:COFFset<ch>:WCODe is adjusted according to the
		selection. \n
			:return: crest: MINimum| AVERage| WORSt MINimum The crest factor is minimized. The Walsh codes are spaced as closely as possible. AVERage An average crest factor is set. The Walsh codes are distributed uniformly over the code domain. WORSt The crest factor is set to an unfavorable value (i.e. maximum) . The Walsh codes are as wildly spaced as possible.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:PPARameter:CRESt?')
		return Conversions.str_to_scalar_enum(response, enums.CresFactMode)

	def set_crest(self, crest: enums.CresFactMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:PPARameter:CRESt \n
		Snippet: driver.source.bb.c2K.pparameter.set_crest(crest = enums.CresFactMode.AVERage) \n
		This command selects the desired range for the crest factor of the test scenario. The crest factor of the signal is kept
		in the desired range by automatically setting appropriate Walsh codes and timing offsets. The setting takes effect only
		after execution of command [:SOURce<hw>]:BB:C2K:PPARameter:EXECute.
		The setting of command [:SOURce<hw>]:BB:C2K:BSTation<st>:CGRoup<di0>:COFFset<ch>:WCODe is adjusted according to the
		selection. \n
			:param crest: MINimum| AVERage| WORSt MINimum The crest factor is minimized. The Walsh codes are spaced as closely as possible. AVERage An average crest factor is set. The Walsh codes are distributed uniformly over the code domain. WORSt The crest factor is set to an unfavorable value (i.e. maximum) . The Walsh codes are as wildly spaced as possible.
		"""
		param = Conversions.enum_scalar_to_str(crest, enums.CresFactMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:PPARameter:CRESt {param}')

	# noinspection PyTypeChecker
	def get_rconfiguration(self) -> enums.Cdma2KradioConf:
		"""SCPI: [SOURce<HW>]:BB:C2K:PPARameter:RCONfiguration \n
		Snippet: value: enums.Cdma2KradioConf = driver.source.bb.c2K.pparameter.get_rconfiguration() \n
		Selects the radio configuration for the traffic channel. The setting takes effect only after execution of command
		[:SOURce<hw>]:BB:C2K:PPARameter:EXECute. \n
			:return: rconfiguration: 1| 2| 3| 4| 5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:PPARameter:RCONfiguration?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KradioConf)

	def set_rconfiguration(self, rconfiguration: enums.Cdma2KradioConf) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:PPARameter:RCONfiguration \n
		Snippet: driver.source.bb.c2K.pparameter.set_rconfiguration(rconfiguration = enums.Cdma2KradioConf._1) \n
		Selects the radio configuration for the traffic channel. The setting takes effect only after execution of command
		[:SOURce<hw>]:BB:C2K:PPARameter:EXECute. \n
			:param rconfiguration: 1| 2| 3| 4| 5
		"""
		param = Conversions.enum_scalar_to_str(rconfiguration, enums.Cdma2KradioConf)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:PPARameter:RCONfiguration {param}')

	def clone(self) -> 'Pparameter':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pparameter(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
