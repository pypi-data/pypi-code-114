from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpcch:
	"""Dpcch commands group definition. 8 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpcch", core, parent)

	@property
	def tpc(self):
		"""tpc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tpc'):
			from .Tpc import Tpc
			self._tpc = Tpc(self._core, self._cmd_group)
		return self._tpc

	def get_sformat(self) -> int:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:SFORmat \n
		Snippet: value: int = driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.get_sformat() \n
		Sets the slot format for the DPCCH. The slot format defines the FBI mode and the TFCI status. \n
			:return: sformat: integer Range: 0 to 5
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:SFORmat?')
		return Conversions.str_to_int(response)

	def set_sformat(self, sformat: int) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:WSIGnal:DPCCh:SFORmat \n
		Snippet: driver.source.bb.w3Gpp.ts25141.wsignal.dpcch.set_sformat(sformat = 1) \n
		Sets the slot format for the DPCCH. The slot format defines the FBI mode and the TFCI status. \n
			:param sformat: integer Range: 0 to 5
		"""
		param = Conversions.decimal_value_to_str(sformat)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:WSIGnal:DPCCh:SFORmat {param}')

	def clone(self) -> 'Dpcch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dpcch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
