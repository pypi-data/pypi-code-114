from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Xfer:
	"""Xfer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("xfer", core, parent)

	def set_rf(self, data: str) -> None:
		"""SCPI: XFER:RF \n
		Snippet: driver.xfer.set_rf(data = '1') \n
		No command help available \n
			:param data: No help available
		"""
		param = Conversions.value_to_quoted_str(data)
		self._core.io.write(f'XFER:RF {param}')
