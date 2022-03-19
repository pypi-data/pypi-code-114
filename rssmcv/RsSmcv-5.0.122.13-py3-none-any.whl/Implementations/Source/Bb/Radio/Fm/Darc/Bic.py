from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bic:
	"""Bic commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: BlockIdCode, default value after init: BlockIdCode.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bic", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_blockIdCode_get', 'repcap_blockIdCode_set', repcap.BlockIdCode.Nr1)

	def repcap_blockIdCode_set(self, blockIdCode: repcap.BlockIdCode) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BlockIdCode.Default
		Default value after init: BlockIdCode.Nr1"""
		self._cmd_group.set_repcap_enum_value(blockIdCode)

	def repcap_blockIdCode_get(self) -> repcap.BlockIdCode:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, darc_bic: str, blockIdCode=repcap.BlockIdCode.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:DARC:BIC<CH> \n
		Snippet: driver.source.bb.radio.fm.darc.bic.set(darc_bic = '1', blockIdCode = repcap.BlockIdCode.Default) \n
		Specifies data for block identification codes 1 to 3. \n
			:param darc_bic: string
			:param blockIdCode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bic')
		"""
		param = Conversions.value_to_quoted_str(darc_bic)
		blockIdCode_cmd_val = self._cmd_group.get_repcap_cmd_value(blockIdCode, repcap.BlockIdCode)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:DARC:BIC{blockIdCode_cmd_val} {param}')

	def get(self, blockIdCode=repcap.BlockIdCode.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:DARC:BIC<CH> \n
		Snippet: value: str = driver.source.bb.radio.fm.darc.bic.get(blockIdCode = repcap.BlockIdCode.Default) \n
		Specifies data for block identification codes 1 to 3. \n
			:param blockIdCode: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bic')
			:return: darc_bic: string"""
		blockIdCode_cmd_val = self._cmd_group.get_repcap_cmd_value(blockIdCode, repcap.BlockIdCode)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:RADio:FM:DARC:BIC{blockIdCode_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'Bic':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bic(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
