from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Create:
	"""Create commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("create", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CREate \n
		Snippet: driver.source.bb.arbitrary.mcarrier.create.set() \n
		Creates a multi-carrier waveform using the current settings of the carrier table.
		Use the command [:SOURce<hw>]:BB:ARBitrary:MCARrier:OFILe to define the multi-carrier waveform file name.
		The file extension is *.wv. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CREate')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CREate \n
		Snippet: driver.source.bb.arbitrary.mcarrier.create.set_with_opc() \n
		Creates a multi-carrier waveform using the current settings of the carrier table.
		Use the command [:SOURce<hw>]:BB:ARBitrary:MCARrier:OFILe to define the multi-carrier waveform file name.
		The file extension is *.wv. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CREate', opc_timeout_ms)
