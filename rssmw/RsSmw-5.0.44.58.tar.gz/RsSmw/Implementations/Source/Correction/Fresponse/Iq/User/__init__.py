from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 21 total commands, 4 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)

	@property
	def alevel(self):
		"""alevel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_alevel'):
			from .Alevel import Alevel
			self._alevel = Alevel(self._core, self._cmd_group)
		return self._alevel

	@property
	def apply(self):
		"""apply commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import Apply
			self._apply = Apply(self._core, self._cmd_group)
		return self._apply

	@property
	def flist(self):
		"""flist commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_flist'):
			from .Flist import Flist
			self._flist = Flist(self._core, self._cmd_group)
		return self._flist

	@property
	def slist(self):
		"""slist commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_slist'):
			from .Slist import Slist
			self._slist = Slist(self._core, self._cmd_group)
		return self._slist

	def get_load(self) -> str:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:LOAD \n
		Snippet: value: str = driver.source.correction.fresponse.iq.user.get_load() \n
		No command help available \n
			:return: freq_resp_iq_rcl: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:LOAD?')
		return trim_str_response(response)

	def set_load(self, freq_resp_iq_rcl: str) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:LOAD \n
		Snippet: driver.source.correction.fresponse.iq.user.set_load(freq_resp_iq_rcl = '1') \n
		No command help available \n
			:param freq_resp_iq_rcl: No help available
		"""
		param = Conversions.value_to_quoted_str(freq_resp_iq_rcl)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:LOAD {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:PRESet \n
		Snippet: driver.source.correction.fresponse.iq.user.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:PRESet \n
		Snippet: driver.source.correction.fresponse.iq.user.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:PRESet', opc_timeout_ms)

	def get_store(self) -> str:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:STORe \n
		Snippet: value: str = driver.source.correction.fresponse.iq.user.get_store() \n
		No command help available \n
			:return: freq_resp_iq_save: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:STORe?')
		return trim_str_response(response)

	def set_store(self, freq_resp_iq_save: str) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:STORe \n
		Snippet: driver.source.correction.fresponse.iq.user.set_store(freq_resp_iq_save = '1') \n
		No command help available \n
			:param freq_resp_iq_save: No help available
		"""
		param = Conversions.value_to_quoted_str(freq_resp_iq_save)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:STORe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:[STATe] \n
		Snippet: value: bool = driver.source.correction.fresponse.iq.user.get_state() \n
		No command help available \n
			:return: freq_corr_iq_stat: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, freq_corr_iq_stat: bool) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:[STATe] \n
		Snippet: driver.source.correction.fresponse.iq.user.set_state(freq_corr_iq_stat = False) \n
		No command help available \n
			:param freq_corr_iq_stat: No help available
		"""
		param = Conversions.bool_to_str(freq_corr_iq_stat)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:STATe {param}')

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
