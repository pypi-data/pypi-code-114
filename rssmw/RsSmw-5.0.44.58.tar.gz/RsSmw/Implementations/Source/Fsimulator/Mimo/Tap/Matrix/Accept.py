from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Accept:
	"""Accept commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("accept", core, parent)

	def set(self, mimoTap=repcap.MimoTap.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:MATRix:ACCept \n
		Snippet: driver.source.fsimulator.mimo.tap.matrix.accept.set(mimoTap = repcap.MimoTap.Default) \n
		Accepts the values for the phase/imaginary and the real/ration part of the correlation. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
		"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:MATRix:ACCept')

	def set_with_opc(self, mimoTap=repcap.MimoTap.Default, opc_timeout_ms: int = -1) -> None:
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:MATRix:ACCept \n
		Snippet: driver.source.fsimulator.mimo.tap.matrix.accept.set_with_opc(mimoTap = repcap.MimoTap.Default) \n
		Accepts the values for the phase/imaginary and the real/ration part of the correlation. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:MATRix:ACCept', opc_timeout_ms)
