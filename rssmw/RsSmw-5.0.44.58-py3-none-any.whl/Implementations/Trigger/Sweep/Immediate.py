from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: TRIGger<HW>:[SWEep]:[IMMediate] \n
		Snippet: driver.trigger.sweep.immediate.set(inputIx = repcap.InputIx.Default) \n
			INTRO_CMD_HELP: Performs a single sweep and immediately starts the activated, corresponding sweep: \n
			- FSWeep - RF frequency
			- PSWeep - RF level
			- LFFSweep - LF frequency
			- SWEep - all sweeps
			INTRO_CMD_HELP: Effective in the following configuration: \n
			- TRIG:FSW|LFFS|PSW|[:SWE]:SOURSING
			- SOUR:SWE:FREQ|POW:MODEAUTO or SOUR:LFO:SWE:[FREQ:]MODEAUTO
		Alternatively, you can use the IMMediate command instead of the respective SWEep:[FREQ:]|POW:EXECute command. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'TRIGger{inputIx_cmd_val}:SWEep:IMMediate')

	def set_with_opc(self, inputIx=repcap.InputIx.Default, opc_timeout_ms: int = -1) -> None:
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		"""SCPI: TRIGger<HW>:[SWEep]:[IMMediate] \n
		Snippet: driver.trigger.sweep.immediate.set_with_opc(inputIx = repcap.InputIx.Default) \n
			INTRO_CMD_HELP: Performs a single sweep and immediately starts the activated, corresponding sweep: \n
			- FSWeep - RF frequency
			- PSWeep - RF level
			- LFFSweep - LF frequency
			- SWEep - all sweeps
			INTRO_CMD_HELP: Effective in the following configuration: \n
			- TRIG:FSW|LFFS|PSW|[:SWE]:SOURSING
			- SOUR:SWE:FREQ|POW:MODEAUTO or SOUR:LFO:SWE:[FREQ:]MODEAUTO
		Alternatively, you can use the IMMediate command instead of the respective SWEep:[FREQ:]|POW:EXECute command. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'TRIGger{inputIx_cmd_val}:SWEep:IMMediate', opc_timeout_ms)
