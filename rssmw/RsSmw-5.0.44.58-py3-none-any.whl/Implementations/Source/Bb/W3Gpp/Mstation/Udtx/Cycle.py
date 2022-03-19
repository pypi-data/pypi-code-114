from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cycle:
	"""Cycle commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: TwoStreams, default value after init: TwoStreams.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cycle", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_twoStreams_get', 'repcap_twoStreams_set', repcap.TwoStreams.Nr1)

	def repcap_twoStreams_set(self, twoStreams: repcap.TwoStreams) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TwoStreams.Default
		Default value after init: TwoStreams.Nr1"""
		self._cmd_group.set_repcap_enum_value(twoStreams)

	def repcap_twoStreams_get(self) -> repcap.TwoStreams:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, dtx_cycle: enums.WcdmaUlDtxCycle, twoStreams=repcap.TwoStreams.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:UDTX:CYCLe<CH> \n
		Snippet: driver.source.bb.w3Gpp.mstation.udtx.cycle.set(dtx_cycle = enums.WcdmaUlDtxCycle._1, twoStreams = repcap.TwoStreams.Default) \n
		Sets the offset in subframe between two consecutive DPCCH bursts within the corresponding UE-DTX cycle, i.e. determines
		how often the DPCCH bursts are transmitted. The UE-DTX cycle 2 is an integer multiple of the UE-DTX cycle 1, i.e.
		has less frequent DPCCH transmission instants. Note: The allowed values depend on the selected E-DCH TTI. \n
			:param dtx_cycle: 1| 4| 5| 8| 10| 16| 20| 32| 40| 64| 80| 128| 160
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cycle')
		"""
		param = Conversions.enum_scalar_to_str(dtx_cycle, enums.WcdmaUlDtxCycle)
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:UDTX:CYCLe{twoStreams_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, twoStreams=repcap.TwoStreams.Default) -> enums.WcdmaUlDtxCycle:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:UDTX:CYCLe<CH> \n
		Snippet: value: enums.WcdmaUlDtxCycle = driver.source.bb.w3Gpp.mstation.udtx.cycle.get(twoStreams = repcap.TwoStreams.Default) \n
		Sets the offset in subframe between two consecutive DPCCH bursts within the corresponding UE-DTX cycle, i.e. determines
		how often the DPCCH bursts are transmitted. The UE-DTX cycle 2 is an integer multiple of the UE-DTX cycle 1, i.e.
		has less frequent DPCCH transmission instants. Note: The allowed values depend on the selected E-DCH TTI. \n
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cycle')
			:return: dtx_cycle: 1| 4| 5| 8| 10| 16| 20| 32| 40| 64| 80| 128| 160"""
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation:UDTX:CYCLe{twoStreams_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.WcdmaUlDtxCycle)

	def clone(self) -> 'Cycle':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cycle(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
