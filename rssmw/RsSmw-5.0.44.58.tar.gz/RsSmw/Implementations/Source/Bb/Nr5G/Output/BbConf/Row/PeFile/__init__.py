from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeFile:
	"""PeFile commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("peFile", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	def set(self, phy_exp_file: str, rowNull=repcap.RowNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:BBConf:ROW<CH0>:PEFile \n
		Snippet: driver.source.bb.nr5G.output.bbConf.row.peFile.set(phy_exp_file = '1', rowNull = repcap.RowNull.Default) \n
		No command help available \n
			:param phy_exp_file: No help available
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
		"""
		param = Conversions.value_to_quoted_str(phy_exp_file)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:OUTPut:BBConf:ROW{rowNull_cmd_val}:PEFile {param}')

	def get(self, rowNull=repcap.RowNull.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:BBConf:ROW<CH0>:PEFile \n
		Snippet: value: str = driver.source.bb.nr5G.output.bbConf.row.peFile.get(rowNull = repcap.RowNull.Default) \n
		No command help available \n
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:return: phy_exp_file: No help available"""
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:OUTPut:BBConf:ROW{rowNull_cmd_val}:PEFile?')
		return trim_str_response(response)

	def clone(self) -> 'PeFile':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PeFile(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
