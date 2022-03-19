from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gvector:
	"""Gvector commands group definition. 131 total commands, 66 Subgroups, 1 group commands
	Repeated Capability: GainVector, default value after init: GainVector.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gvector", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_gainVector_get', 'repcap_gainVector_set', repcap.GainVector.Nr1)

	def repcap_gainVector_set(self, gainVector: repcap.GainVector) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to GainVector.Default
		Default value after init: GainVector.Nr1"""
		self._cmd_group.set_repcap_enum_value(gainVector)

	def repcap_gainVector_get(self) -> repcap.GainVector:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def aa(self):
		"""aa commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_aa'):
			from .Aa import Aa
			self._aa = Aa(self._core, self._cmd_group)
		return self._aa

	@property
	def ab(self):
		"""ab commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ab'):
			from .Ab import Ab
			self._ab = Ab(self._core, self._cmd_group)
		return self._ab

	@property
	def ac(self):
		"""ac commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ac'):
			from .Ac import Ac
			self._ac = Ac(self._core, self._cmd_group)
		return self._ac

	@property
	def ad(self):
		"""ad commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ad'):
			from .Ad import Ad
			self._ad = Ad(self._core, self._cmd_group)
		return self._ad

	@property
	def ae(self):
		"""ae commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ae'):
			from .Ae import Ae
			self._ae = Ae(self._core, self._cmd_group)
		return self._ae

	@property
	def af(self):
		"""af commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_af'):
			from .Af import Af
			self._af = Af(self._core, self._cmd_group)
		return self._af

	@property
	def ag(self):
		"""ag commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ag'):
			from .Ag import Ag
			self._ag = Ag(self._core, self._cmd_group)
		return self._ag

	@property
	def ah(self):
		"""ah commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ah'):
			from .Ah import Ah
			self._ah = Ah(self._core, self._cmd_group)
		return self._ah

	@property
	def ba(self):
		"""ba commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ba'):
			from .Ba import Ba
			self._ba = Ba(self._core, self._cmd_group)
		return self._ba

	@property
	def bb(self):
		"""bb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bb'):
			from .Bb import Bb
			self._bb = Bb(self._core, self._cmd_group)
		return self._bb

	@property
	def bc(self):
		"""bc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bc'):
			from .Bc import Bc
			self._bc = Bc(self._core, self._cmd_group)
		return self._bc

	@property
	def bd(self):
		"""bd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bd'):
			from .Bd import Bd
			self._bd = Bd(self._core, self._cmd_group)
		return self._bd

	@property
	def be(self):
		"""be commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_be'):
			from .Be import Be
			self._be = Be(self._core, self._cmd_group)
		return self._be

	@property
	def bf(self):
		"""bf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bf'):
			from .Bf import Bf
			self._bf = Bf(self._core, self._cmd_group)
		return self._bf

	@property
	def bg(self):
		"""bg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bg'):
			from .Bg import Bg
			self._bg = Bg(self._core, self._cmd_group)
		return self._bg

	@property
	def bh(self):
		"""bh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bh'):
			from .Bh import Bh
			self._bh = Bh(self._core, self._cmd_group)
		return self._bh

	@property
	def ca(self):
		"""ca commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ca'):
			from .Ca import Ca
			self._ca = Ca(self._core, self._cmd_group)
		return self._ca

	@property
	def cb(self):
		"""cb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cb'):
			from .Cb import Cb
			self._cb = Cb(self._core, self._cmd_group)
		return self._cb

	@property
	def cc(self):
		"""cc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import Cc
			self._cc = Cc(self._core, self._cmd_group)
		return self._cc

	@property
	def cd(self):
		"""cd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cd'):
			from .Cd import Cd
			self._cd = Cd(self._core, self._cmd_group)
		return self._cd

	@property
	def ce(self):
		"""ce commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ce'):
			from .Ce import Ce
			self._ce = Ce(self._core, self._cmd_group)
		return self._ce

	@property
	def cf(self):
		"""cf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cf'):
			from .Cf import Cf
			self._cf = Cf(self._core, self._cmd_group)
		return self._cf

	@property
	def cg(self):
		"""cg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cg'):
			from .Cg import Cg
			self._cg = Cg(self._core, self._cmd_group)
		return self._cg

	@property
	def ch(self):
		"""ch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ch'):
			from .Ch import Ch
			self._ch = Ch(self._core, self._cmd_group)
		return self._ch

	@property
	def da(self):
		"""da commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_da'):
			from .Da import Da
			self._da = Da(self._core, self._cmd_group)
		return self._da

	@property
	def db(self):
		"""db commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_db'):
			from .Db import Db
			self._db = Db(self._core, self._cmd_group)
		return self._db

	@property
	def dc(self):
		"""dc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dc'):
			from .Dc import Dc
			self._dc = Dc(self._core, self._cmd_group)
		return self._dc

	@property
	def dd(self):
		"""dd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dd'):
			from .Dd import Dd
			self._dd = Dd(self._core, self._cmd_group)
		return self._dd

	@property
	def de(self):
		"""de commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_de'):
			from .De import De
			self._de = De(self._core, self._cmd_group)
		return self._de

	@property
	def df(self):
		"""df commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_df'):
			from .Df import Df
			self._df = Df(self._core, self._cmd_group)
		return self._df

	@property
	def dg(self):
		"""dg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dg'):
			from .Dg import Dg
			self._dg = Dg(self._core, self._cmd_group)
		return self._dg

	@property
	def dh(self):
		"""dh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dh'):
			from .Dh import Dh
			self._dh = Dh(self._core, self._cmd_group)
		return self._dh

	@property
	def ea(self):
		"""ea commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ea'):
			from .Ea import Ea
			self._ea = Ea(self._core, self._cmd_group)
		return self._ea

	@property
	def eb(self):
		"""eb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_eb'):
			from .Eb import Eb
			self._eb = Eb(self._core, self._cmd_group)
		return self._eb

	@property
	def ec(self):
		"""ec commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ec'):
			from .Ec import Ec
			self._ec = Ec(self._core, self._cmd_group)
		return self._ec

	@property
	def ed(self):
		"""ed commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ed'):
			from .Ed import Ed
			self._ed = Ed(self._core, self._cmd_group)
		return self._ed

	@property
	def ee(self):
		"""ee commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ee'):
			from .Ee import Ee
			self._ee = Ee(self._core, self._cmd_group)
		return self._ee

	@property
	def ef(self):
		"""ef commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ef'):
			from .Ef import Ef
			self._ef = Ef(self._core, self._cmd_group)
		return self._ef

	@property
	def eg(self):
		"""eg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_eg'):
			from .Eg import Eg
			self._eg = Eg(self._core, self._cmd_group)
		return self._eg

	@property
	def eh(self):
		"""eh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_eh'):
			from .Eh import Eh
			self._eh = Eh(self._core, self._cmd_group)
		return self._eh

	@property
	def fa(self):
		"""fa commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fa'):
			from .Fa import Fa
			self._fa = Fa(self._core, self._cmd_group)
		return self._fa

	@property
	def fb(self):
		"""fb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fb'):
			from .Fb import Fb
			self._fb = Fb(self._core, self._cmd_group)
		return self._fb

	@property
	def fc(self):
		"""fc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fc'):
			from .Fc import Fc
			self._fc = Fc(self._core, self._cmd_group)
		return self._fc

	@property
	def fd(self):
		"""fd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fd'):
			from .Fd import Fd
			self._fd = Fd(self._core, self._cmd_group)
		return self._fd

	@property
	def fe(self):
		"""fe commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fe'):
			from .Fe import Fe
			self._fe = Fe(self._core, self._cmd_group)
		return self._fe

	@property
	def ff(self):
		"""ff commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ff'):
			from .Ff import Ff
			self._ff = Ff(self._core, self._cmd_group)
		return self._ff

	@property
	def fg(self):
		"""fg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fg'):
			from .Fg import Fg
			self._fg = Fg(self._core, self._cmd_group)
		return self._fg

	@property
	def fh(self):
		"""fh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fh'):
			from .Fh import Fh
			self._fh = Fh(self._core, self._cmd_group)
		return self._fh

	@property
	def ga(self):
		"""ga commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ga'):
			from .Ga import Ga
			self._ga = Ga(self._core, self._cmd_group)
		return self._ga

	@property
	def gain(self):
		"""gain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	@property
	def gb(self):
		"""gb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gb'):
			from .Gb import Gb
			self._gb = Gb(self._core, self._cmd_group)
		return self._gb

	@property
	def gc(self):
		"""gc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gc'):
			from .Gc import Gc
			self._gc = Gc(self._core, self._cmd_group)
		return self._gc

	@property
	def gd(self):
		"""gd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gd'):
			from .Gd import Gd
			self._gd = Gd(self._core, self._cmd_group)
		return self._gd

	@property
	def ge(self):
		"""ge commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ge'):
			from .Ge import Ge
			self._ge = Ge(self._core, self._cmd_group)
		return self._ge

	@property
	def gf(self):
		"""gf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gf'):
			from .Gf import Gf
			self._gf = Gf(self._core, self._cmd_group)
		return self._gf

	@property
	def gg(self):
		"""gg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gg'):
			from .Gg import Gg
			self._gg = Gg(self._core, self._cmd_group)
		return self._gg

	@property
	def gh(self):
		"""gh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gh'):
			from .Gh import Gh
			self._gh = Gh(self._core, self._cmd_group)
		return self._gh

	@property
	def ha(self):
		"""ha commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ha'):
			from .Ha import Ha
			self._ha = Ha(self._core, self._cmd_group)
		return self._ha

	@property
	def hb(self):
		"""hb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hb'):
			from .Hb import Hb
			self._hb = Hb(self._core, self._cmd_group)
		return self._hb

	@property
	def hc(self):
		"""hc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hc'):
			from .Hc import Hc
			self._hc = Hc(self._core, self._cmd_group)
		return self._hc

	@property
	def hd(self):
		"""hd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hd'):
			from .Hd import Hd
			self._hd = Hd(self._core, self._cmd_group)
		return self._hd

	@property
	def he(self):
		"""he commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_he'):
			from .He import He
			self._he = He(self._core, self._cmd_group)
		return self._he

	@property
	def hf(self):
		"""hf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hf'):
			from .Hf import Hf
			self._hf = Hf(self._core, self._cmd_group)
		return self._hf

	@property
	def hg(self):
		"""hg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hg'):
			from .Hg import Hg
			self._hg = Hg(self._core, self._cmd_group)
		return self._hg

	@property
	def hh(self):
		"""hh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hh'):
			from .Hh import Hh
			self._hh = Hh(self._core, self._cmd_group)
		return self._hh

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	def preset(self, mimoTap=repcap.MimoTap.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:GVECtor:PRESet \n
		Snippet: driver.source.fsimulator.mimo.tap.gvector.preset(mimoTap = repcap.MimoTap.Default) \n
		The command presets the vector matrix to an unitary matrix. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
		"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:GVECtor:PRESet')

	def preset_with_opc(self, mimoTap=repcap.MimoTap.Default, opc_timeout_ms: int = -1) -> None:
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:GVECtor:PRESet \n
		Snippet: driver.source.fsimulator.mimo.tap.gvector.preset_with_opc(mimoTap = repcap.MimoTap.Default) \n
		The command presets the vector matrix to an unitary matrix. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:GVECtor:PRESet', opc_timeout_ms)

	def clone(self) -> 'Gvector':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gvector(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
