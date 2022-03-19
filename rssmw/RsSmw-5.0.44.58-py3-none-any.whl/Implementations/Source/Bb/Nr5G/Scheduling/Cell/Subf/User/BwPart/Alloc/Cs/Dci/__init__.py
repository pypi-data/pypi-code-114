from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup
from .............Internal.RepeatedCapability import RepeatedCapability
from ............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dci:
	"""Dci commands group definition. 236 total commands, 232 Subgroups, 0 group commands
	Repeated Capability: IndexNull, default value after init: IndexNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dci", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_indexNull_get', 'repcap_indexNull_set', repcap.IndexNull.Nr0)

	def repcap_indexNull_set(self, indexNull: repcap.IndexNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to IndexNull.Default
		Default value after init: IndexNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(indexNull)

	def repcap_indexNull_get(self) -> repcap.IndexNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def aggLevel(self):
		"""aggLevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aggLevel'):
			from .AggLevel import AggLevel
			self._aggLevel = AggLevel(self._core, self._cmd_group)
		return self._aggLevel

	@property
	def ai1(self):
		"""ai1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai1'):
			from .Ai1 import Ai1
			self._ai1 = Ai1(self._core, self._cmd_group)
		return self._ai1

	@property
	def ai10(self):
		"""ai10 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai10'):
			from .Ai10 import Ai10
			self._ai10 = Ai10(self._core, self._cmd_group)
		return self._ai10

	@property
	def ai11(self):
		"""ai11 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai11'):
			from .Ai11 import Ai11
			self._ai11 = Ai11(self._core, self._cmd_group)
		return self._ai11

	@property
	def ai12(self):
		"""ai12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai12'):
			from .Ai12 import Ai12
			self._ai12 = Ai12(self._core, self._cmd_group)
		return self._ai12

	@property
	def ai13(self):
		"""ai13 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai13'):
			from .Ai13 import Ai13
			self._ai13 = Ai13(self._core, self._cmd_group)
		return self._ai13

	@property
	def ai14(self):
		"""ai14 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai14'):
			from .Ai14 import Ai14
			self._ai14 = Ai14(self._core, self._cmd_group)
		return self._ai14

	@property
	def ai15(self):
		"""ai15 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai15'):
			from .Ai15 import Ai15
			self._ai15 = Ai15(self._core, self._cmd_group)
		return self._ai15

	@property
	def ai16(self):
		"""ai16 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai16'):
			from .Ai16 import Ai16
			self._ai16 = Ai16(self._core, self._cmd_group)
		return self._ai16

	@property
	def ai2(self):
		"""ai2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai2'):
			from .Ai2 import Ai2
			self._ai2 = Ai2(self._core, self._cmd_group)
		return self._ai2

	@property
	def ai3(self):
		"""ai3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai3'):
			from .Ai3 import Ai3
			self._ai3 = Ai3(self._core, self._cmd_group)
		return self._ai3

	@property
	def ai4(self):
		"""ai4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai4'):
			from .Ai4 import Ai4
			self._ai4 = Ai4(self._core, self._cmd_group)
		return self._ai4

	@property
	def ai5(self):
		"""ai5 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai5'):
			from .Ai5 import Ai5
			self._ai5 = Ai5(self._core, self._cmd_group)
		return self._ai5

	@property
	def ai6(self):
		"""ai6 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai6'):
			from .Ai6 import Ai6
			self._ai6 = Ai6(self._core, self._cmd_group)
		return self._ai6

	@property
	def ai7(self):
		"""ai7 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai7'):
			from .Ai7 import Ai7
			self._ai7 = Ai7(self._core, self._cmd_group)
		return self._ai7

	@property
	def ai8(self):
		"""ai8 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai8'):
			from .Ai8 import Ai8
			self._ai8 = Ai8(self._core, self._cmd_group)
		return self._ai8

	@property
	def ai9(self):
		"""ai9 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ai9'):
			from .Ai9 import Ai9
			self._ai9 = Ai9(self._core, self._cmd_group)
		return self._ai9

	@property
	def antPorts(self):
		"""antPorts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_antPorts'):
			from .AntPorts import AntPorts
			self._antPorts = AntPorts(self._core, self._cmd_group)
		return self._antPorts

	@property
	def ar1(self):
		"""ar1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar1'):
			from .Ar1 import Ar1
			self._ar1 = Ar1(self._core, self._cmd_group)
		return self._ar1

	@property
	def ar10(self):
		"""ar10 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar10'):
			from .Ar10 import Ar10
			self._ar10 = Ar10(self._core, self._cmd_group)
		return self._ar10

	@property
	def ar11(self):
		"""ar11 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar11'):
			from .Ar11 import Ar11
			self._ar11 = Ar11(self._core, self._cmd_group)
		return self._ar11

	@property
	def ar12(self):
		"""ar12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar12'):
			from .Ar12 import Ar12
			self._ar12 = Ar12(self._core, self._cmd_group)
		return self._ar12

	@property
	def ar13(self):
		"""ar13 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar13'):
			from .Ar13 import Ar13
			self._ar13 = Ar13(self._core, self._cmd_group)
		return self._ar13

	@property
	def ar14(self):
		"""ar14 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar14'):
			from .Ar14 import Ar14
			self._ar14 = Ar14(self._core, self._cmd_group)
		return self._ar14

	@property
	def ar15(self):
		"""ar15 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar15'):
			from .Ar15 import Ar15
			self._ar15 = Ar15(self._core, self._cmd_group)
		return self._ar15

	@property
	def ar16(self):
		"""ar16 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar16'):
			from .Ar16 import Ar16
			self._ar16 = Ar16(self._core, self._cmd_group)
		return self._ar16

	@property
	def ar2(self):
		"""ar2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar2'):
			from .Ar2 import Ar2
			self._ar2 = Ar2(self._core, self._cmd_group)
		return self._ar2

	@property
	def ar3(self):
		"""ar3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar3'):
			from .Ar3 import Ar3
			self._ar3 = Ar3(self._core, self._cmd_group)
		return self._ar3

	@property
	def ar4(self):
		"""ar4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar4'):
			from .Ar4 import Ar4
			self._ar4 = Ar4(self._core, self._cmd_group)
		return self._ar4

	@property
	def ar5(self):
		"""ar5 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar5'):
			from .Ar5 import Ar5
			self._ar5 = Ar5(self._core, self._cmd_group)
		return self._ar5

	@property
	def ar6(self):
		"""ar6 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar6'):
			from .Ar6 import Ar6
			self._ar6 = Ar6(self._core, self._cmd_group)
		return self._ar6

	@property
	def ar7(self):
		"""ar7 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar7'):
			from .Ar7 import Ar7
			self._ar7 = Ar7(self._core, self._cmd_group)
		return self._ar7

	@property
	def ar8(self):
		"""ar8 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar8'):
			from .Ar8 import Ar8
			self._ar8 = Ar8(self._core, self._cmd_group)
		return self._ar8

	@property
	def ar9(self):
		"""ar9 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ar9'):
			from .Ar9 import Ar9
			self._ar9 = Ar9(self._core, self._cmd_group)
		return self._ar9

	@property
	def bitLength(self):
		"""bitLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bitLength'):
			from .BitLength import BitLength
			self._bitLength = BitLength(self._core, self._cmd_group)
		return self._bitLength

	@property
	def boind(self):
		"""boind commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_boind'):
			from .Boind import Boind
			self._boind = Boind(self._core, self._cmd_group)
		return self._boind

	@property
	def bwind(self):
		"""bwind commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwind'):
			from .Bwind import Bwind
			self._bwind = Bwind(self._core, self._cmd_group)
		return self._bwind

	@property
	def caCpext(self):
		"""caCpext commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_caCpext'):
			from .CaCpext import CaCpext
			self._caCpext = CaCpext(self._core, self._cmd_group)
		return self._caCpext

	@property
	def caind(self):
		"""caind commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_caind'):
			from .Caind import Caind
			self._caind = Caind(self._core, self._cmd_group)
		return self._caind

	@property
	def candidate(self):
		"""candidate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_candidate'):
			from .Candidate import Candidate
			self._candidate = Candidate(self._core, self._cmd_group)
		return self._candidate

	@property
	def cbgfi(self):
		"""cbgfi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbgfi'):
			from .Cbgfi import Cbgfi
			self._cbgfi = Cbgfi(self._core, self._cmd_group)
		return self._cbgfi

	@property
	def cbgti(self):
		"""cbgti commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbgti'):
			from .Cbgti import Cbgti
			self._cbgti = Cbgti(self._core, self._cmd_group)
		return self._cbgti

	@property
	def cd1(self):
		"""cd1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd1'):
			from .Cd1 import Cd1
			self._cd1 = Cd1(self._core, self._cmd_group)
		return self._cd1

	@property
	def cd10(self):
		"""cd10 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd10'):
			from .Cd10 import Cd10
			self._cd10 = Cd10(self._core, self._cmd_group)
		return self._cd10

	@property
	def cd11(self):
		"""cd11 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd11'):
			from .Cd11 import Cd11
			self._cd11 = Cd11(self._core, self._cmd_group)
		return self._cd11

	@property
	def cd12(self):
		"""cd12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd12'):
			from .Cd12 import Cd12
			self._cd12 = Cd12(self._core, self._cmd_group)
		return self._cd12

	@property
	def cd13(self):
		"""cd13 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd13'):
			from .Cd13 import Cd13
			self._cd13 = Cd13(self._core, self._cmd_group)
		return self._cd13

	@property
	def cd14(self):
		"""cd14 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd14'):
			from .Cd14 import Cd14
			self._cd14 = Cd14(self._core, self._cmd_group)
		return self._cd14

	@property
	def cd15(self):
		"""cd15 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd15'):
			from .Cd15 import Cd15
			self._cd15 = Cd15(self._core, self._cmd_group)
		return self._cd15

	@property
	def cd16(self):
		"""cd16 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd16'):
			from .Cd16 import Cd16
			self._cd16 = Cd16(self._core, self._cmd_group)
		return self._cd16

	@property
	def cd2(self):
		"""cd2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd2'):
			from .Cd2 import Cd2
			self._cd2 = Cd2(self._core, self._cmd_group)
		return self._cd2

	@property
	def cd3(self):
		"""cd3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd3'):
			from .Cd3 import Cd3
			self._cd3 = Cd3(self._core, self._cmd_group)
		return self._cd3

	@property
	def cd4(self):
		"""cd4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd4'):
			from .Cd4 import Cd4
			self._cd4 = Cd4(self._core, self._cmd_group)
		return self._cd4

	@property
	def cd5(self):
		"""cd5 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd5'):
			from .Cd5 import Cd5
			self._cd5 = Cd5(self._core, self._cmd_group)
		return self._cd5

	@property
	def cd6(self):
		"""cd6 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd6'):
			from .Cd6 import Cd6
			self._cd6 = Cd6(self._core, self._cmd_group)
		return self._cd6

	@property
	def cd7(self):
		"""cd7 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd7'):
			from .Cd7 import Cd7
			self._cd7 = Cd7(self._core, self._cmd_group)
		return self._cd7

	@property
	def cd8(self):
		"""cd8 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd8'):
			from .Cd8 import Cd8
			self._cd8 = Cd8(self._core, self._cmd_group)
		return self._cd8

	@property
	def cd9(self):
		"""cd9 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cd9'):
			from .Cd9 import Cd9
			self._cd9 = Cd9(self._core, self._cmd_group)
		return self._cd9

	@property
	def ci10(self):
		"""ci10 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci10'):
			from .Ci10 import Ci10
			self._ci10 = Ci10(self._core, self._cmd_group)
		return self._ci10

	@property
	def ci11(self):
		"""ci11 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci11'):
			from .Ci11 import Ci11
			self._ci11 = Ci11(self._core, self._cmd_group)
		return self._ci11

	@property
	def ci12(self):
		"""ci12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci12'):
			from .Ci12 import Ci12
			self._ci12 = Ci12(self._core, self._cmd_group)
		return self._ci12

	@property
	def ci13(self):
		"""ci13 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci13'):
			from .Ci13 import Ci13
			self._ci13 = Ci13(self._core, self._cmd_group)
		return self._ci13

	@property
	def ci14(self):
		"""ci14 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci14'):
			from .Ci14 import Ci14
			self._ci14 = Ci14(self._core, self._cmd_group)
		return self._ci14

	@property
	def ci15(self):
		"""ci15 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci15'):
			from .Ci15 import Ci15
			self._ci15 = Ci15(self._core, self._cmd_group)
		return self._ci15

	@property
	def ci16(self):
		"""ci16 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci16'):
			from .Ci16 import Ci16
			self._ci16 = Ci16(self._core, self._cmd_group)
		return self._ci16

	@property
	def ci2(self):
		"""ci2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci2'):
			from .Ci2 import Ci2
			self._ci2 = Ci2(self._core, self._cmd_group)
		return self._ci2

	@property
	def ci3(self):
		"""ci3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci3'):
			from .Ci3 import Ci3
			self._ci3 = Ci3(self._core, self._cmd_group)
		return self._ci3

	@property
	def ci4(self):
		"""ci4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci4'):
			from .Ci4 import Ci4
			self._ci4 = Ci4(self._core, self._cmd_group)
		return self._ci4

	@property
	def ci5(self):
		"""ci5 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci5'):
			from .Ci5 import Ci5
			self._ci5 = Ci5(self._core, self._cmd_group)
		return self._ci5

	@property
	def ci6(self):
		"""ci6 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci6'):
			from .Ci6 import Ci6
			self._ci6 = Ci6(self._core, self._cmd_group)
		return self._ci6

	@property
	def ci7(self):
		"""ci7 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci7'):
			from .Ci7 import Ci7
			self._ci7 = Ci7(self._core, self._cmd_group)
		return self._ci7

	@property
	def ci8(self):
		"""ci8 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci8'):
			from .Ci8 import Ci8
			self._ci8 = Ci8(self._core, self._cmd_group)
		return self._ci8

	@property
	def ci9(self):
		"""ci9 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci9'):
			from .Ci9 import Ci9
			self._ci9 = Ci9(self._core, self._cmd_group)
		return self._ci9

	@property
	def cl1(self):
		"""cl1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl1'):
			from .Cl1 import Cl1
			self._cl1 = Cl1(self._core, self._cmd_group)
		return self._cl1

	@property
	def cl10(self):
		"""cl10 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl10'):
			from .Cl10 import Cl10
			self._cl10 = Cl10(self._core, self._cmd_group)
		return self._cl10

	@property
	def cl11(self):
		"""cl11 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl11'):
			from .Cl11 import Cl11
			self._cl11 = Cl11(self._core, self._cmd_group)
		return self._cl11

	@property
	def cl12(self):
		"""cl12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl12'):
			from .Cl12 import Cl12
			self._cl12 = Cl12(self._core, self._cmd_group)
		return self._cl12

	@property
	def cl13(self):
		"""cl13 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl13'):
			from .Cl13 import Cl13
			self._cl13 = Cl13(self._core, self._cmd_group)
		return self._cl13

	@property
	def cl14(self):
		"""cl14 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl14'):
			from .Cl14 import Cl14
			self._cl14 = Cl14(self._core, self._cmd_group)
		return self._cl14

	@property
	def cl15(self):
		"""cl15 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl15'):
			from .Cl15 import Cl15
			self._cl15 = Cl15(self._core, self._cmd_group)
		return self._cl15

	@property
	def cl16(self):
		"""cl16 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl16'):
			from .Cl16 import Cl16
			self._cl16 = Cl16(self._core, self._cmd_group)
		return self._cl16

	@property
	def cl17(self):
		"""cl17 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl17'):
			from .Cl17 import Cl17
			self._cl17 = Cl17(self._core, self._cmd_group)
		return self._cl17

	@property
	def cl18(self):
		"""cl18 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl18'):
			from .Cl18 import Cl18
			self._cl18 = Cl18(self._core, self._cmd_group)
		return self._cl18

	@property
	def cl19(self):
		"""cl19 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl19'):
			from .Cl19 import Cl19
			self._cl19 = Cl19(self._core, self._cmd_group)
		return self._cl19

	@property
	def cl2(self):
		"""cl2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl2'):
			from .Cl2 import Cl2
			self._cl2 = Cl2(self._core, self._cmd_group)
		return self._cl2

	@property
	def cl20(self):
		"""cl20 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl20'):
			from .Cl20 import Cl20
			self._cl20 = Cl20(self._core, self._cmd_group)
		return self._cl20

	@property
	def cl21(self):
		"""cl21 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl21'):
			from .Cl21 import Cl21
			self._cl21 = Cl21(self._core, self._cmd_group)
		return self._cl21

	@property
	def cl22(self):
		"""cl22 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl22'):
			from .Cl22 import Cl22
			self._cl22 = Cl22(self._core, self._cmd_group)
		return self._cl22

	@property
	def cl3(self):
		"""cl3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl3'):
			from .Cl3 import Cl3
			self._cl3 = Cl3(self._core, self._cmd_group)
		return self._cl3

	@property
	def cl4(self):
		"""cl4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl4'):
			from .Cl4 import Cl4
			self._cl4 = Cl4(self._core, self._cmd_group)
		return self._cl4

	@property
	def cl5(self):
		"""cl5 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl5'):
			from .Cl5 import Cl5
			self._cl5 = Cl5(self._core, self._cmd_group)
		return self._cl5

	@property
	def cl6(self):
		"""cl6 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl6'):
			from .Cl6 import Cl6
			self._cl6 = Cl6(self._core, self._cmd_group)
		return self._cl6

	@property
	def cl7(self):
		"""cl7 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl7'):
			from .Cl7 import Cl7
			self._cl7 = Cl7(self._core, self._cmd_group)
		return self._cl7

	@property
	def cl8(self):
		"""cl8 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl8'):
			from .Cl8 import Cl8
			self._cl8 = Cl8(self._core, self._cmd_group)
		return self._cl8

	@property
	def cl9(self):
		"""cl9 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl9'):
			from .Cl9 import Cl9
			self._cl9 = Cl9(self._core, self._cmd_group)
		return self._cl9

	@property
	def cpdsch(self):
		"""cpdsch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cpdsch'):
			from .Cpdsch import Cpdsch
			self._cpdsch = Cpdsch(self._core, self._cmd_group)
		return self._cpdsch

	@property
	def csiRequest(self):
		"""csiRequest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csiRequest'):
			from .CsiRequest import CsiRequest
			self._csiRequest = CsiRequest(self._core, self._cmd_group)
		return self._csiRequest

	@property
	def dai1(self):
		"""dai1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dai1'):
			from .Dai1 import Dai1
			self._dai1 = Dai1(self._core, self._cmd_group)
		return self._dai1

	@property
	def dai2(self):
		"""dai2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dai2'):
			from .Dai2 import Dai2
			self._dai2 = Dai2(self._core, self._cmd_group)
		return self._dai2

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def dfiFlag(self):
		"""dfiFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dfiFlag'):
			from .DfiFlag import DfiFlag
			self._dfiFlag = DfiFlag(self._core, self._cmd_group)
		return self._dfiFlag

	@property
	def di1(self):
		"""di1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_di1'):
			from .Di1 import Di1
			self._di1 = Di1(self._core, self._cmd_group)
		return self._di1

	@property
	def di10(self):
		"""di10 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_di10'):
			from .Di10 import Di10
			self._di10 = Di10(self._core, self._cmd_group)
		return self._di10

	@property
	def di2(self):
		"""di2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_di2'):
			from .Di2 import Di2
			self._di2 = Di2(self._core, self._cmd_group)
		return self._di2

	@property
	def di3(self):
		"""di3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_di3'):
			from .Di3 import Di3
			self._di3 = Di3(self._core, self._cmd_group)
		return self._di3

	@property
	def di4(self):
		"""di4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_di4'):
			from .Di4 import Di4
			self._di4 = Di4(self._core, self._cmd_group)
		return self._di4

	@property
	def di5(self):
		"""di5 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_di5'):
			from .Di5 import Di5
			self._di5 = Di5(self._core, self._cmd_group)
		return self._di5

	@property
	def di6(self):
		"""di6 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_di6'):
			from .Di6 import Di6
			self._di6 = Di6(self._core, self._cmd_group)
		return self._di6

	@property
	def di7(self):
		"""di7 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_di7'):
			from .Di7 import Di7
			self._di7 = Di7(self._core, self._cmd_group)
		return self._di7

	@property
	def di8(self):
		"""di8 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_di8'):
			from .Di8 import Di8
			self._di8 = Di8(self._core, self._cmd_group)
		return self._di8

	@property
	def di9(self):
		"""di9 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_di9'):
			from .Di9 import Di9
			self._di9 = Di9(self._core, self._cmd_group)
		return self._di9

	@property
	def dlist(self):
		"""dlist commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dlist'):
			from .Dlist import Dlist
			self._dlist = Dlist(self._core, self._cmd_group)
		return self._dlist

	@property
	def dmsqInit(self):
		"""dmsqInit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmsqInit'):
			from .DmsqInit import DmsqInit
			self._dmsqInit = DmsqInit(self._core, self._cmd_group)
		return self._dmsqInit

	@property
	def dmss(self):
		"""dmss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmss'):
			from .Dmss import Dmss
			self._dmss = Dmss(self._core, self._cmd_group)
		return self._dmss

	@property
	def fmt(self):
		"""fmt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fmt'):
			from .Fmt import Fmt
			self._fmt = Fmt(self._core, self._cmd_group)
		return self._fmt

	@property
	def frdRes(self):
		"""frdRes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frdRes'):
			from .FrdRes import FrdRes
			self._frdRes = FrdRes(self._core, self._cmd_group)
		return self._frdRes

	@property
	def frhFlag(self):
		"""frhFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frhFlag'):
			from .FrhFlag import FrhFlag
			self._frhFlag = FrhFlag(self._core, self._cmd_group)
		return self._frhFlag

	@property
	def haaBitmap(self):
		"""haaBitmap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_haaBitmap'):
			from .HaaBitmap import HaaBitmap
			self._haaBitmap = HaaBitmap(self._core, self._cmd_group)
		return self._haaBitmap

	@property
	def haproc(self):
		"""haproc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_haproc'):
			from .Haproc import Haproc
			self._haproc = Haproc(self._core, self._cmd_group)
		return self._haproc

	@property
	def hqaRequest(self):
		"""hqaRequest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hqaRequest'):
			from .HqaRequest import HqaRequest
			self._hqaRequest = HqaRequest(self._core, self._cmd_group)
		return self._hqaRequest

	@property
	def identifier(self):
		"""identifier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_identifier'):
			from .Identifier import Identifier
			self._identifier = Identifier(self._core, self._cmd_group)
		return self._identifier

	@property
	def index(self):
		"""index commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_index'):
			from .Index import Index
			self._index = Index(self._core, self._cmd_group)
		return self._index

	@property
	def initPattern(self):
		"""initPattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_initPattern'):
			from .InitPattern import InitPattern
			self._initPattern = InitPattern(self._core, self._cmd_group)
		return self._initPattern

	@property
	def insPatt(self):
		"""insPatt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_insPatt'):
			from .InsPatt import InsPatt
			self._insPatt = InsPatt(self._core, self._cmd_group)
		return self._insPatt

	@property
	def lsbsfn(self):
		"""lsbsfn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lsbsfn'):
			from .Lsbsfn import Lsbsfn
			self._lsbsfn = Lsbsfn(self._core, self._cmd_group)
		return self._lsbsfn

	@property
	def moffs(self):
		"""moffs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_moffs'):
			from .Moffs import Moffs
			self._moffs = Moffs(self._core, self._cmd_group)
		return self._moffs

	@property
	def nfIndicator(self):
		"""nfIndicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nfIndicator'):
			from .NfIndicator import NfIndicator
			self._nfIndicator = NfIndicator(self._core, self._cmd_group)
		return self._nfIndicator

	@property
	def nrpGroups(self):
		"""nrpGroups commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrpGroups'):
			from .NrpGroups import NrpGroups
			self._nrpGroups = NrpGroups(self._core, self._cmd_group)
		return self._nrpGroups

	@property
	def olIndicator(self):
		"""olIndicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_olIndicator'):
			from .OlIndicator import OlIndicator
			self._olIndicator = OlIndicator(self._core, self._cmd_group)
		return self._olIndicator

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	@property
	def pdsharq(self):
		"""pdsharq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdsharq'):
			from .Pdsharq import Pdsharq
			self._pdsharq = Pdsharq(self._core, self._cmd_group)
		return self._pdsharq

	@property
	def pe1(self):
		"""pe1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pe1'):
			from .Pe1 import Pe1
			self._pe1 = Pe1(self._core, self._cmd_group)
		return self._pe1

	@property
	def pe2(self):
		"""pe2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pe2'):
			from .Pe2 import Pe2
			self._pe2 = Pe2(self._core, self._cmd_group)
		return self._pe2

	@property
	def pe3(self):
		"""pe3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pe3'):
			from .Pe3 import Pe3
			self._pe3 = Pe3(self._core, self._cmd_group)
		return self._pe3

	@property
	def pe4(self):
		"""pe4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pe4'):
			from .Pe4 import Pe4
			self._pe4 = Pe4(self._core, self._cmd_group)
		return self._pe4

	@property
	def pe5(self):
		"""pe5 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pe5'):
			from .Pe5 import Pe5
			self._pe5 = Pe5(self._core, self._cmd_group)
		return self._pe5

	@property
	def pe6(self):
		"""pe6 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pe6'):
			from .Pe6 import Pe6
			self._pe6 = Pe6(self._core, self._cmd_group)
		return self._pe6

	@property
	def pe7(self):
		"""pe7 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pe7'):
			from .Pe7 import Pe7
			self._pe7 = Pe7(self._core, self._cmd_group)
		return self._pe7

	@property
	def pe8(self):
		"""pe8 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pe8'):
			from .Pe8 import Pe8
			self._pe8 = Pe8(self._core, self._cmd_group)
		return self._pe8

	@property
	def pe9(self):
		"""pe9 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pe9'):
			from .Pe9 import Pe9
			self._pe9 = Pe9(self._core, self._cmd_group)
		return self._pe9

	@property
	def pgIndex(self):
		"""pgIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pgIndex'):
			from .PgIndex import PgIndex
			self._pgIndex = PgIndex(self._core, self._cmd_group)
		return self._pgIndex

	@property
	def pindicator(self):
		"""pindicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pindicator'):
			from .Pindicator import Pindicator
			self._pindicator = Pindicator(self._core, self._cmd_group)
		return self._pindicator

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def prbBundling(self):
		"""prbBundling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prbBundling'):
			from .PrbBundling import PrbBundling
			self._prbBundling = PrbBundling(self._core, self._cmd_group)
		return self._prbBundling

	@property
	def precInfo(self):
		"""precInfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_precInfo'):
			from .PrecInfo import PrecInfo
			self._precInfo = PrecInfo(self._core, self._cmd_group)
		return self._precInfo

	@property
	def ptdmrs(self):
		"""ptdmrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ptdmrs'):
			from .Ptdmrs import Ptdmrs
			self._ptdmrs = Ptdmrs(self._core, self._cmd_group)
		return self._ptdmrs

	@property
	def pucresInd(self):
		"""pucresInd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pucresInd'):
			from .PucresInd import PucresInd
			self._pucresInd = PucresInd(self._core, self._cmd_group)
		return self._pucresInd

	@property
	def resved(self):
		"""resved commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resved'):
			from .Resved import Resved
			self._resved = Resved(self._core, self._cmd_group)
		return self._resved

	@property
	def rmind(self):
		"""rmind commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmind'):
			from .Rmind import Rmind
			self._rmind = Rmind(self._core, self._cmd_group)
		return self._rmind

	@property
	def rnti(self):
		"""rnti commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rnti'):
			from .Rnti import Rnti
			self._rnti = Rnti(self._core, self._cmd_group)
		return self._rnti

	@property
	def sgs1(self):
		"""sgs1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgs1'):
			from .Sgs1 import Sgs1
			self._sgs1 = Sgs1(self._core, self._cmd_group)
		return self._sgs1

	@property
	def sgs2(self):
		"""sgs2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgs2'):
			from .Sgs2 import Sgs2
			self._sgs2 = Sgs2(self._core, self._cmd_group)
		return self._sgs2

	@property
	def sgs3(self):
		"""sgs3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgs3'):
			from .Sgs3 import Sgs3
			self._sgs3 = Sgs3(self._core, self._cmd_group)
		return self._sgs3

	@property
	def sgs4(self):
		"""sgs4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgs4'):
			from .Sgs4 import Sgs4
			self._sgs4 = Sgs4(self._core, self._cmd_group)
		return self._sgs4

	@property
	def si1(self):
		"""si1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si1'):
			from .Si1 import Si1
			self._si1 = Si1(self._core, self._cmd_group)
		return self._si1

	@property
	def si10(self):
		"""si10 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si10'):
			from .Si10 import Si10
			self._si10 = Si10(self._core, self._cmd_group)
		return self._si10

	@property
	def si11(self):
		"""si11 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si11'):
			from .Si11 import Si11
			self._si11 = Si11(self._core, self._cmd_group)
		return self._si11

	@property
	def si12(self):
		"""si12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si12'):
			from .Si12 import Si12
			self._si12 = Si12(self._core, self._cmd_group)
		return self._si12

	@property
	def si13(self):
		"""si13 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si13'):
			from .Si13 import Si13
			self._si13 = Si13(self._core, self._cmd_group)
		return self._si13

	@property
	def si14(self):
		"""si14 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si14'):
			from .Si14 import Si14
			self._si14 = Si14(self._core, self._cmd_group)
		return self._si14

	@property
	def si15(self):
		"""si15 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si15'):
			from .Si15 import Si15
			self._si15 = Si15(self._core, self._cmd_group)
		return self._si15

	@property
	def si16(self):
		"""si16 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si16'):
			from .Si16 import Si16
			self._si16 = Si16(self._core, self._cmd_group)
		return self._si16

	@property
	def si2(self):
		"""si2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si2'):
			from .Si2 import Si2
			self._si2 = Si2(self._core, self._cmd_group)
		return self._si2

	@property
	def si3(self):
		"""si3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si3'):
			from .Si3 import Si3
			self._si3 = Si3(self._core, self._cmd_group)
		return self._si3

	@property
	def si4(self):
		"""si4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si4'):
			from .Si4 import Si4
			self._si4 = Si4(self._core, self._cmd_group)
		return self._si4

	@property
	def si5(self):
		"""si5 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si5'):
			from .Si5 import Si5
			self._si5 = Si5(self._core, self._cmd_group)
		return self._si5

	@property
	def si6(self):
		"""si6 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si6'):
			from .Si6 import Si6
			self._si6 = Si6(self._core, self._cmd_group)
		return self._si6

	@property
	def si7(self):
		"""si7 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si7'):
			from .Si7 import Si7
			self._si7 = Si7(self._core, self._cmd_group)
		return self._si7

	@property
	def si8(self):
		"""si8 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si8'):
			from .Si8 import Si8
			self._si8 = Si8(self._core, self._cmd_group)
		return self._si8

	@property
	def si9(self):
		"""si9 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_si9'):
			from .Si9 import Si9
			self._si9 = Si9(self._core, self._cmd_group)
		return self._si9

	@property
	def siInd(self):
		"""siInd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_siInd'):
			from .SiInd import SiInd
			self._siInd = SiInd(self._core, self._cmd_group)
		return self._siInd

	@property
	def smind(self):
		"""smind commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smind'):
			from .Smind import Smind
			self._smind = Smind(self._core, self._cmd_group)
		return self._smind

	@property
	def smsgs(self):
		"""smsgs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smsgs'):
			from .Smsgs import Smsgs
			self._smsgs = Smsgs(self._core, self._cmd_group)
		return self._smsgs

	@property
	def sr1(self):
		"""sr1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sr1'):
			from .Sr1 import Sr1
			self._sr1 = Sr1(self._core, self._cmd_group)
		return self._sr1

	@property
	def sr10(self):
		"""sr10 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sr10'):
			from .Sr10 import Sr10
			self._sr10 = Sr10(self._core, self._cmd_group)
		return self._sr10

	@property
	def sr11(self):
		"""sr11 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sr11'):
			from .Sr11 import Sr11
			self._sr11 = Sr11(self._core, self._cmd_group)
		return self._sr11

	@property
	def sr2(self):
		"""sr2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sr2'):
			from .Sr2 import Sr2
			self._sr2 = Sr2(self._core, self._cmd_group)
		return self._sr2

	@property
	def sr3(self):
		"""sr3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sr3'):
			from .Sr3 import Sr3
			self._sr3 = Sr3(self._core, self._cmd_group)
		return self._sr3

	@property
	def sr4(self):
		"""sr4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sr4'):
			from .Sr4 import Sr4
			self._sr4 = Sr4(self._core, self._cmd_group)
		return self._sr4

	@property
	def sr5(self):
		"""sr5 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sr5'):
			from .Sr5 import Sr5
			self._sr5 = Sr5(self._core, self._cmd_group)
		return self._sr5

	@property
	def sr6(self):
		"""sr6 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sr6'):
			from .Sr6 import Sr6
			self._sr6 = Sr6(self._core, self._cmd_group)
		return self._sr6

	@property
	def sr7(self):
		"""sr7 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sr7'):
			from .Sr7 import Sr7
			self._sr7 = Sr7(self._core, self._cmd_group)
		return self._sr7

	@property
	def sr8(self):
		"""sr8 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sr8'):
			from .Sr8 import Sr8
			self._sr8 = Sr8(self._core, self._cmd_group)
		return self._sr8

	@property
	def sr9(self):
		"""sr9 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sr9'):
			from .Sr9 import Sr9
			self._sr9 = Sr9(self._core, self._cmd_group)
		return self._sr9

	@property
	def srsRequest(self):
		"""srsRequest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srsRequest'):
			from .SrsRequest import SrsRequest
			self._srsRequest = SrsRequest(self._core, self._cmd_group)
		return self._srsRequest

	@property
	def srsResInd(self):
		"""srsResInd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srsResInd'):
			from .SrsResInd import SrsResInd
			self._srsResInd = SrsResInd(self._core, self._cmd_group)
		return self._srsResInd

	@property
	def ssp(self):
		"""ssp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssp'):
			from .Ssp import Ssp
			self._ssp = Ssp(self._core, self._cmd_group)
		return self._ssp

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def tb1(self):
		"""tb1 commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tb1'):
			from .Tb1 import Tb1
			self._tb1 = Tb1(self._core, self._cmd_group)
		return self._tb1

	@property
	def tb2(self):
		"""tb2 commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tb2'):
			from .Tb2 import Tb2
			self._tb2 = Tb2(self._core, self._cmd_group)
		return self._tb2

	@property
	def tbScaling(self):
		"""tbScaling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbScaling'):
			from .TbScaling import TbScaling
			self._tbScaling = TbScaling(self._core, self._cmd_group)
		return self._tbScaling

	@property
	def tci(self):
		"""tci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tci'):
			from .Tci import Tci
			self._tci = Tci(self._core, self._cmd_group)
		return self._tci

	@property
	def tidRes(self):
		"""tidRes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tidRes'):
			from .TidRes import TidRes
			self._tidRes = TidRes(self._core, self._cmd_group)
		return self._tidRes

	@property
	def tp1(self):
		"""tp1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp1'):
			from .Tp1 import Tp1
			self._tp1 = Tp1(self._core, self._cmd_group)
		return self._tp1

	@property
	def tp10(self):
		"""tp10 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp10'):
			from .Tp10 import Tp10
			self._tp10 = Tp10(self._core, self._cmd_group)
		return self._tp10

	@property
	def tp11(self):
		"""tp11 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp11'):
			from .Tp11 import Tp11
			self._tp11 = Tp11(self._core, self._cmd_group)
		return self._tp11

	@property
	def tp12(self):
		"""tp12 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp12'):
			from .Tp12 import Tp12
			self._tp12 = Tp12(self._core, self._cmd_group)
		return self._tp12

	@property
	def tp13(self):
		"""tp13 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp13'):
			from .Tp13 import Tp13
			self._tp13 = Tp13(self._core, self._cmd_group)
		return self._tp13

	@property
	def tp14(self):
		"""tp14 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp14'):
			from .Tp14 import Tp14
			self._tp14 = Tp14(self._core, self._cmd_group)
		return self._tp14

	@property
	def tp15(self):
		"""tp15 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp15'):
			from .Tp15 import Tp15
			self._tp15 = Tp15(self._core, self._cmd_group)
		return self._tp15

	@property
	def tp16(self):
		"""tp16 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp16'):
			from .Tp16 import Tp16
			self._tp16 = Tp16(self._core, self._cmd_group)
		return self._tp16

	@property
	def tp17(self):
		"""tp17 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp17'):
			from .Tp17 import Tp17
			self._tp17 = Tp17(self._core, self._cmd_group)
		return self._tp17

	@property
	def tp18(self):
		"""tp18 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp18'):
			from .Tp18 import Tp18
			self._tp18 = Tp18(self._core, self._cmd_group)
		return self._tp18

	@property
	def tp19(self):
		"""tp19 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp19'):
			from .Tp19 import Tp19
			self._tp19 = Tp19(self._core, self._cmd_group)
		return self._tp19

	@property
	def tp2(self):
		"""tp2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp2'):
			from .Tp2 import Tp2
			self._tp2 = Tp2(self._core, self._cmd_group)
		return self._tp2

	@property
	def tp20(self):
		"""tp20 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp20'):
			from .Tp20 import Tp20
			self._tp20 = Tp20(self._core, self._cmd_group)
		return self._tp20

	@property
	def tp21(self):
		"""tp21 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp21'):
			from .Tp21 import Tp21
			self._tp21 = Tp21(self._core, self._cmd_group)
		return self._tp21

	@property
	def tp22(self):
		"""tp22 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp22'):
			from .Tp22 import Tp22
			self._tp22 = Tp22(self._core, self._cmd_group)
		return self._tp22

	@property
	def tp3(self):
		"""tp3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp3'):
			from .Tp3 import Tp3
			self._tp3 = Tp3(self._core, self._cmd_group)
		return self._tp3

	@property
	def tp4(self):
		"""tp4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp4'):
			from .Tp4 import Tp4
			self._tp4 = Tp4(self._core, self._cmd_group)
		return self._tp4

	@property
	def tp5(self):
		"""tp5 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp5'):
			from .Tp5 import Tp5
			self._tp5 = Tp5(self._core, self._cmd_group)
		return self._tp5

	@property
	def tp6(self):
		"""tp6 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp6'):
			from .Tp6 import Tp6
			self._tp6 = Tp6(self._core, self._cmd_group)
		return self._tp6

	@property
	def tp7(self):
		"""tp7 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp7'):
			from .Tp7 import Tp7
			self._tp7 = Tp7(self._core, self._cmd_group)
		return self._tp7

	@property
	def tp8(self):
		"""tp8 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp8'):
			from .Tp8 import Tp8
			self._tp8 = Tp8(self._core, self._cmd_group)
		return self._tp8

	@property
	def tp9(self):
		"""tp9 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tp9'):
			from .Tp9 import Tp9
			self._tp9 = Tp9(self._core, self._cmd_group)
		return self._tp9

	@property
	def tpucch(self):
		"""tpucch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpucch'):
			from .Tpucch import Tpucch
			self._tpucch = Tpucch(self._core, self._cmd_group)
		return self._tpucch

	@property
	def tpusch(self):
		"""tpusch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpusch'):
			from .Tpusch import Tpusch
			self._tpusch = Tpusch(self._core, self._cmd_group)
		return self._tpusch

	@property
	def ulSchInd(self):
		"""ulSchInd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulSchInd'):
			from .UlSchInd import UlSchInd
			self._ulSchInd = UlSchInd(self._core, self._cmd_group)
		return self._ulSchInd

	@property
	def usage(self):
		"""usage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usage'):
			from .Usage import Usage
			self._usage = Usage(self._core, self._cmd_group)
		return self._usage

	@property
	def usInd(self):
		"""usInd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usInd'):
			from .UsInd import UsInd
			self._usInd = UsInd(self._core, self._cmd_group)
		return self._usInd

	@property
	def vtprb(self):
		"""vtprb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vtprb'):
			from .Vtprb import Vtprb
			self._vtprb = Vtprb(self._core, self._cmd_group)
		return self._vtprb

	@property
	def wa1(self):
		"""wa1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wa1'):
			from .Wa1 import Wa1
			self._wa1 = Wa1(self._core, self._cmd_group)
		return self._wa1

	@property
	def wa10(self):
		"""wa10 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wa10'):
			from .Wa10 import Wa10
			self._wa10 = Wa10(self._core, self._cmd_group)
		return self._wa10

	@property
	def wa2(self):
		"""wa2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wa2'):
			from .Wa2 import Wa2
			self._wa2 = Wa2(self._core, self._cmd_group)
		return self._wa2

	@property
	def wa3(self):
		"""wa3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wa3'):
			from .Wa3 import Wa3
			self._wa3 = Wa3(self._core, self._cmd_group)
		return self._wa3

	@property
	def wa4(self):
		"""wa4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wa4'):
			from .Wa4 import Wa4
			self._wa4 = Wa4(self._core, self._cmd_group)
		return self._wa4

	@property
	def wa5(self):
		"""wa5 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wa5'):
			from .Wa5 import Wa5
			self._wa5 = Wa5(self._core, self._cmd_group)
		return self._wa5

	@property
	def wa6(self):
		"""wa6 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wa6'):
			from .Wa6 import Wa6
			self._wa6 = Wa6(self._core, self._cmd_group)
		return self._wa6

	@property
	def wa7(self):
		"""wa7 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wa7'):
			from .Wa7 import Wa7
			self._wa7 = Wa7(self._core, self._cmd_group)
		return self._wa7

	@property
	def wa8(self):
		"""wa8 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wa8'):
			from .Wa8 import Wa8
			self._wa8 = Wa8(self._core, self._cmd_group)
		return self._wa8

	@property
	def wa9(self):
		"""wa9 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wa9'):
			from .Wa9 import Wa9
			self._wa9 = Wa9(self._core, self._cmd_group)
		return self._wa9

	@property
	def zcrTrigg(self):
		"""zcrTrigg commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zcrTrigg'):
			from .ZcrTrigg import ZcrTrigg
			self._zcrTrigg = ZcrTrigg(self._core, self._cmd_group)
		return self._zcrTrigg

	def clone(self) -> 'Dci':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dci(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
