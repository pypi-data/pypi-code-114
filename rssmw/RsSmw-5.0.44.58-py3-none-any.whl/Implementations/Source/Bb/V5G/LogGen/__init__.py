from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LogGen:
	"""LogGen commands group definition. 21 total commands, 2 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("logGen", core, parent)

	@property
	def downlink(self):
		"""downlink commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import Downlink
			self._downlink = Downlink(self._core, self._cmd_group)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 3 Sub-classes, 7 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import Uplink
			self._uplink = Uplink(self._core, self._cmd_group)
		return self._uplink

	def get_gs_log_file(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:GSLogfile \n
		Snippet: value: bool = driver.source.bb.v5G.logGen.get_gs_log_file() \n
		No command help available \n
			:return: gen_sum_log: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:LOGGen:GSLogfile?')
		return Conversions.str_to_bool(response)

	def set_gs_log_file(self, gen_sum_log: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:GSLogfile \n
		Snippet: driver.source.bb.v5G.logGen.set_gs_log_file(gen_sum_log = False) \n
		No command help available \n
			:param gen_sum_log: No help available
		"""
		param = Conversions.bool_to_str(gen_sum_log)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:LOGGen:GSLogfile {param}')

	def get_lfp(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:LFP \n
		Snippet: value: str = driver.source.bb.v5G.logGen.get_lfp() \n
		No command help available \n
			:return: preamble: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:LOGGen:LFP?')
		return trim_str_response(response)

	def set_lfp(self, preamble: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:LFP \n
		Snippet: driver.source.bb.v5G.logGen.set_lfp(preamble = '1') \n
		No command help available \n
			:param preamble: No help available
		"""
		param = Conversions.value_to_quoted_str(preamble)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:LOGGen:LFP {param}')

	def get_output(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:OUTPut \n
		Snippet: value: str = driver.source.bb.v5G.logGen.get_output() \n
		No command help available \n
			:return: output_path: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:LOGGen:OUTPut?')
		return trim_str_response(response)

	def set_output(self, output_path: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:OUTPut \n
		Snippet: driver.source.bb.v5G.logGen.set_output(output_path = '1') \n
		No command help available \n
			:param output_path: No help available
		"""
		param = Conversions.value_to_quoted_str(output_path)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:LOGGen:OUTPut {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:STATe \n
		Snippet: value: bool = driver.source.bb.v5G.logGen.get_state() \n
		No command help available \n
			:return: logging_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:LOGGen:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, logging_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:STATe \n
		Snippet: driver.source.bb.v5G.logGen.set_state(logging_state = False) \n
		No command help available \n
			:param logging_state: No help available
		"""
		param = Conversions.bool_to_str(logging_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:LOGGen:STATe {param}')

	def clone(self) -> 'LogGen':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LogGen(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
