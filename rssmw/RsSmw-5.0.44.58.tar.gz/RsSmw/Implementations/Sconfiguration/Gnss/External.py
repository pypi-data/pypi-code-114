from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("external", core, parent)

	def get_encoder(self) -> bool:
		"""SCPI: SCONfiguration:GNSS:EXTernal:ENCoder \n
		Snippet: value: bool = driver.sconfiguration.gnss.external.get_encoder() \n
		No command help available \n
			:return: gnss_use_ext_encod: No help available
		"""
		response = self._core.io.query_str('SCONfiguration:GNSS:EXTernal:ENCoder?')
		return Conversions.str_to_bool(response)

	def set_encoder(self, gnss_use_ext_encod: bool) -> None:
		"""SCPI: SCONfiguration:GNSS:EXTernal:ENCoder \n
		Snippet: driver.sconfiguration.gnss.external.set_encoder(gnss_use_ext_encod = False) \n
		No command help available \n
			:param gnss_use_ext_encod: No help available
		"""
		param = Conversions.bool_to_str(gnss_use_ext_encod)
		self._core.io.write(f'SCONfiguration:GNSS:EXTernal:ENCoder {param}')
