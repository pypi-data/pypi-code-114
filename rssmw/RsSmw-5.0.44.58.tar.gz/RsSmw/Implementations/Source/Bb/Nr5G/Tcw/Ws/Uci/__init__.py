from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uci:
	"""Uci commands group definition. 5 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uci", core, parent)

	@property
	def cguci(self):
		"""cguci commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cguci'):
			from .Cguci import Cguci
			self._cguci = Cguci(self._core, self._cmd_group)
		return self._cguci

	@property
	def csi1(self):
		"""csi1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csi1'):
			from .Csi1 import Csi1
			self._csi1 = Csi1(self._core, self._cmd_group)
		return self._csi1

	@property
	def csi2(self):
		"""csi2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csi2'):
			from .Csi2 import Csi2
			self._csi2 = Csi2(self._core, self._cmd_group)
		return self._csi2

	# noinspection PyTypeChecker
	def get_bits(self) -> enums.UciBits:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:WS:UCI:BITS \n
		Snippet: value: enums.UciBits = driver.source.bb.nr5G.tcw.ws.uci.get_bits() \n
		Set the number of UCI bits used. Defines the size of the uplink control information bits carried in the PUCCH channel.
		They consist of the HARQ feedback, CSI and SR. \n
			:return: uci_bits: B_7| B_40
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:WS:UCI:BITS?')
		return Conversions.str_to_scalar_enum(response, enums.UciBits)

	def set_bits(self, uci_bits: enums.UciBits) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:WS:UCI:BITS \n
		Snippet: driver.source.bb.nr5G.tcw.ws.uci.set_bits(uci_bits = enums.UciBits.B_40) \n
		Set the number of UCI bits used. Defines the size of the uplink control information bits carried in the PUCCH channel.
		They consist of the HARQ feedback, CSI and SR. \n
			:param uci_bits: B_7| B_40
		"""
		param = Conversions.enum_scalar_to_str(uci_bits, enums.UciBits)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:WS:UCI:BITS {param}')

	# noinspection PyTypeChecker
	def get_csi_part(self) -> enums.CsiPart:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:WS:UCI:CSIPart \n
		Snippet: value: enums.CsiPart = driver.source.bb.nr5G.tcw.ws.uci.get_csi_part() \n
		Defines the CSI part selected for the test case. The PUCCH-based CSI and the PUSCH-based CSI reporting, always padding
		the CSI report to the worst-case UCI payload size would result in too large overhead. For these cases, the CSI content is
		instead divided into two CSI parts. \n
			:return: csi_part: CSIP_1| CSIP_2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:WS:UCI:CSIPart?')
		return Conversions.str_to_scalar_enum(response, enums.CsiPart)

	def set_csi_part(self, csi_part: enums.CsiPart) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:WS:UCI:CSIPart \n
		Snippet: driver.source.bb.nr5G.tcw.ws.uci.set_csi_part(csi_part = enums.CsiPart.CSIP_1) \n
		Defines the CSI part selected for the test case. The PUCCH-based CSI and the PUSCH-based CSI reporting, always padding
		the CSI report to the worst-case UCI payload size would result in too large overhead. For these cases, the CSI content is
		instead divided into two CSI parts. \n
			:param csi_part: CSIP_1| CSIP_2
		"""
		param = Conversions.enum_scalar_to_str(csi_part, enums.CsiPart)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:WS:UCI:CSIPart {param}')

	def clone(self) -> 'Uci':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uci(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
