from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Common:
	"""Common commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("common", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:SRATe:COMMon:STATe \n
		Snippet: value: bool = driver.source.iq.output.digital.symbolRate.common.get_state() \n
		No command help available \n
			:return: dig_iq_hs_com_state: No help available
		"""
		response = self._core.io.query_str('SOURce:IQ:OUTPut:DIGital:SRATe:COMMon:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, dig_iq_hs_com_state: bool) -> None:
		"""SCPI: [SOURce]:IQ:OUTPut:DIGital:SRATe:COMMon:STATe \n
		Snippet: driver.source.iq.output.digital.symbolRate.common.set_state(dig_iq_hs_com_state = False) \n
		No command help available \n
			:param dig_iq_hs_com_state: No help available
		"""
		param = Conversions.bool_to_str(dig_iq_hs_com_state)
		self._core.io.write(f'SOURce:IQ:OUTPut:DIGital:SRATe:COMMon:STATe {param}')
