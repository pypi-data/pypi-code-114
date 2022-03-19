from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Esequencer:
	"""Esequencer commands group definition. 115 total commands, 12 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("esequencer", core, parent)

	@property
	def archive(self):
		"""archive commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_archive'):
			from .Archive import Archive
			self._archive = Archive(self._core, self._cmd_group)
		return self._archive

	@property
	def asequencing(self):
		"""asequencing commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_asequencing'):
			from .Asequencing import Asequencing
			self._asequencing = Asequencing(self._core, self._cmd_group)
		return self._asequencing

	@property
	def clock(self):
		"""clock commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def dfinding(self):
		"""dfinding commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dfinding'):
			from .Dfinding import Dfinding
			self._dfinding = Dfinding(self._core, self._cmd_group)
		return self._dfinding

	@property
	def pramp(self):
		"""pramp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pramp'):
			from .Pramp import Pramp
			self._pramp = Pramp(self._core, self._cmd_group)
		return self._pramp

	@property
	def psequencer(self):
		"""psequencer commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_psequencer'):
			from .Psequencer import Psequencer
			self._psequencer = Psequencer(self._core, self._cmd_group)
		return self._psequencer

	@property
	def rtci(self):
		"""rtci commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_rtci'):
			from .Rtci import Rtci
			self._rtci = Rtci(self._core, self._cmd_group)
		return self._rtci

	@property
	def sequencer(self):
		"""sequencer commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_sequencer'):
			from .Sequencer import Sequencer
			self._sequencer = Sequencer(self._core, self._cmd_group)
		return self._sequencer

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def stream(self):
		"""stream commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_stream'):
			from .Stream import Stream
			self._stream = Stream(self._core, self._cmd_group)
		return self._stream

	@property
	def trigger(self):
		"""trigger commands group. 6 Sub-classes, 3 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def user(self):
		"""user commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	def get_error(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:ERRor \n
		Snippet: value: str = driver.source.bb.esequencer.get_error() \n
		Queries detected xml format errors. \n
			:return: error: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:ERRor?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ExtSeqMode:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:MODE \n
		Snippet: value: enums.ExtSeqMode = driver.source.bb.esequencer.get_mode() \n
		Selects the processing mode for the extended sequencer. \n
			:return: mode: USER| PSEQuencer| DFINding| RTCI USER Processes user defined extended sequences. PSEQuencer Processes files created with the signal generation software R&S Pulse Sequencer. DFINding Processes files containing sequences with extended direction finding of the antennas. The files are created with the signal generation software R&S Pulse Sequencer. RTCI Processes files containing sequences of precalculated waveform.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ExtSeqMode)

	def set_mode(self, mode: enums.ExtSeqMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:MODE \n
		Snippet: driver.source.bb.esequencer.set_mode(mode = enums.ExtSeqMode.ASEQuencing) \n
		Selects the processing mode for the extended sequencer. \n
			:param mode: USER| PSEQuencer| DFINding| RTCI USER Processes user defined extended sequences. PSEQuencer Processes files created with the signal generation software R&S Pulse Sequencer. DFINding Processes files containing sequences with extended direction finding of the antennas. The files are created with the signal generation software R&S Pulse Sequencer. RTCI Processes files containing sequences of precalculated waveform.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ExtSeqMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:MODE {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:PRESet \n
		Snippet: driver.source.bb.esequencer.preset() \n
		Sets all the parameters of the extended sequencer to their default values (*RST values specified for the commands) . Not
		affected is the state set with the command [:SOURce<hw>]:BB:ESEQuencer:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:PRESet \n
		Snippet: driver.source.bb.esequencer.preset_with_opc() \n
		Sets all the parameters of the extended sequencer to their default values (*RST values specified for the commands) . Not
		affected is the state set with the command [:SOURce<hw>]:BB:ESEQuencer:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:ESEQuencer:PRESet', opc_timeout_ms)

	def get_seq_count(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:SEQCount \n
		Snippet: value: int = driver.source.bb.esequencer.get_seq_count() \n
		Queries the number of sequencers. \n
			:return: numb_of_sequencer: integer Number of available sequencers depends on the installed options. Range: 1 to 6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:SEQCount?')
		return Conversions.str_to_int(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:STATe \n
		Snippet: value: bool = driver.source.bb.esequencer.get_state() \n
		Activates signal generation, and deactivates all digital standards, digital modulation modes and other sweeps in the
		corresponding path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:STATe \n
		Snippet: driver.source.bb.esequencer.set_state(state = False) \n
		Activates signal generation, and deactivates all digital standards, digital modulation modes and other sweeps in the
		corresponding path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:STATe {param}')

	def get_str_count(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:STRCount \n
		Snippet: value: int = driver.source.bb.esequencer.get_str_count() \n
		Queries the number of streams. \n
			:return: numb_of_streams: integer Range: 2 to 2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:STRCount?')
		return Conversions.str_to_int(response)

	def set_str_count(self, numb_of_streams: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:STRCount \n
		Snippet: driver.source.bb.esequencer.set_str_count(numb_of_streams = 1) \n
		Queries the number of streams. \n
			:param numb_of_streams: integer Range: 2 to 2
		"""
		param = Conversions.decimal_value_to_str(numb_of_streams)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:STRCount {param}')

	def clone(self) -> 'Esequencer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Esequencer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
