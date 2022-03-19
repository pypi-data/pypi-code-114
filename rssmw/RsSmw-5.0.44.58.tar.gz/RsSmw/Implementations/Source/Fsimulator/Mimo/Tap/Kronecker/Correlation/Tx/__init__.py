from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tx:
	"""Tx commands group definition. 116 total commands, 29 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tx", core, parent)

	@property
	def ac(self):
		"""ac commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ac'):
			from .Ac import Ac
			self._ac = Ac(self._core, self._cmd_group)
		return self._ac

	@property
	def ad(self):
		"""ad commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ad'):
			from .Ad import Ad
			self._ad = Ad(self._core, self._cmd_group)
		return self._ad

	@property
	def ae(self):
		"""ae commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ae'):
			from .Ae import Ae
			self._ae = Ae(self._core, self._cmd_group)
		return self._ae

	@property
	def af(self):
		"""af commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_af'):
			from .Af import Af
			self._af = Af(self._core, self._cmd_group)
		return self._af

	@property
	def ag(self):
		"""ag commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ag'):
			from .Ag import Ag
			self._ag = Ag(self._core, self._cmd_group)
		return self._ag

	@property
	def ah(self):
		"""ah commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ah'):
			from .Ah import Ah
			self._ah = Ah(self._core, self._cmd_group)
		return self._ah

	@property
	def bc(self):
		"""bc commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_bc'):
			from .Bc import Bc
			self._bc = Bc(self._core, self._cmd_group)
		return self._bc

	@property
	def bd(self):
		"""bd commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_bd'):
			from .Bd import Bd
			self._bd = Bd(self._core, self._cmd_group)
		return self._bd

	@property
	def be(self):
		"""be commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_be'):
			from .Be import Be
			self._be = Be(self._core, self._cmd_group)
		return self._be

	@property
	def bf(self):
		"""bf commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_bf'):
			from .Bf import Bf
			self._bf = Bf(self._core, self._cmd_group)
		return self._bf

	@property
	def bg(self):
		"""bg commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_bg'):
			from .Bg import Bg
			self._bg = Bg(self._core, self._cmd_group)
		return self._bg

	@property
	def bh(self):
		"""bh commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_bh'):
			from .Bh import Bh
			self._bh = Bh(self._core, self._cmd_group)
		return self._bh

	@property
	def cd(self):
		"""cd commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cd'):
			from .Cd import Cd
			self._cd = Cd(self._core, self._cmd_group)
		return self._cd

	@property
	def ce(self):
		"""ce commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ce'):
			from .Ce import Ce
			self._ce = Ce(self._core, self._cmd_group)
		return self._ce

	@property
	def cf(self):
		"""cf commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cf'):
			from .Cf import Cf
			self._cf = Cf(self._core, self._cmd_group)
		return self._cf

	@property
	def cg(self):
		"""cg commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cg'):
			from .Cg import Cg
			self._cg = Cg(self._core, self._cmd_group)
		return self._cg

	@property
	def ch(self):
		"""ch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ch'):
			from .Ch import Ch
			self._ch = Ch(self._core, self._cmd_group)
		return self._ch

	@property
	def de(self):
		"""de commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_de'):
			from .De import De
			self._de = De(self._core, self._cmd_group)
		return self._de

	@property
	def df(self):
		"""df commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_df'):
			from .Df import Df
			self._df = Df(self._core, self._cmd_group)
		return self._df

	@property
	def dg(self):
		"""dg commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_dg'):
			from .Dg import Dg
			self._dg = Dg(self._core, self._cmd_group)
		return self._dg

	@property
	def dh(self):
		"""dh commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_dh'):
			from .Dh import Dh
			self._dh = Dh(self._core, self._cmd_group)
		return self._dh

	@property
	def ef(self):
		"""ef commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ef'):
			from .Ef import Ef
			self._ef = Ef(self._core, self._cmd_group)
		return self._ef

	@property
	def eg(self):
		"""eg commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_eg'):
			from .Eg import Eg
			self._eg = Eg(self._core, self._cmd_group)
		return self._eg

	@property
	def eh(self):
		"""eh commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_eh'):
			from .Eh import Eh
			self._eh = Eh(self._core, self._cmd_group)
		return self._eh

	@property
	def fg(self):
		"""fg commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fg'):
			from .Fg import Fg
			self._fg = Fg(self._core, self._cmd_group)
		return self._fg

	@property
	def fh(self):
		"""fh commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fh'):
			from .Fh import Fh
			self._fh = Fh(self._core, self._cmd_group)
		return self._fh

	@property
	def gh(self):
		"""gh commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_gh'):
			from .Gh import Gh
			self._gh = Gh(self._core, self._cmd_group)
		return self._gh

	@property
	def row(self):
		"""row commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_row'):
			from .Row import Row
			self._row = Row(self._core, self._cmd_group)
		return self._row

	@property
	def ab(self):
		"""ab commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ab'):
			from .Ab import Ab
			self._ab = Ab(self._core, self._cmd_group)
		return self._ab

	def clone(self) -> 'Tx':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tx(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
