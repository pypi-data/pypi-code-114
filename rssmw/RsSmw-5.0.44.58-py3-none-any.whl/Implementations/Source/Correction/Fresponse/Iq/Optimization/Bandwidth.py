from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AutoManualMode:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:OPTimization:BANDwidth:MODE \n
		Snippet: value: enums.AutoManualMode = driver.source.correction.fresponse.iq.optimization.bandwidth.get_mode() \n
		No command help available \n
			:return: fr_resp_iq_opt_bw_mo: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:OPTimization:BANDwidth:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)

	def set_mode(self, fr_resp_iq_opt_bw_mo: enums.AutoManualMode) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:OPTimization:BANDwidth:MODE \n
		Snippet: driver.source.correction.fresponse.iq.optimization.bandwidth.set_mode(fr_resp_iq_opt_bw_mo = enums.AutoManualMode.AUTO) \n
		No command help available \n
			:param fr_resp_iq_opt_bw_mo: No help available
		"""
		param = Conversions.enum_scalar_to_str(fr_resp_iq_opt_bw_mo, enums.AutoManualMode)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:OPTimization:BANDwidth:MODE {param}')

	def get_value(self) -> int:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:OPTimization:BANDwidth:[VALue] \n
		Snippet: value: int = driver.source.correction.fresponse.iq.optimization.bandwidth.get_value() \n
		No command help available \n
			:return: fr_resp_iq_opt_bw_va: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:OPTimization:BANDwidth:VALue?')
		return Conversions.str_to_int(response)

	def set_value(self, fr_resp_iq_opt_bw_va: int) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:OPTimization:BANDwidth:[VALue] \n
		Snippet: driver.source.correction.fresponse.iq.optimization.bandwidth.set_value(fr_resp_iq_opt_bw_va = 1) \n
		No command help available \n
			:param fr_resp_iq_opt_bw_va: No help available
		"""
		param = Conversions.decimal_value_to_str(fr_resp_iq_opt_bw_va)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:OPTimization:BANDwidth:VALue {param}')
