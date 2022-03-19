from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Npar:
	"""Npar commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: AntennaPortIx, default value after init: AntennaPortIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npar", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_antennaPortIx_get', 'repcap_antennaPortIx_set', repcap.AntennaPortIx.Nr1)

	def repcap_antennaPortIx_set(self, antennaPortIx: repcap.AntennaPortIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AntennaPortIx.Default
		Default value after init: AntennaPortIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(antennaPortIx)

	def repcap_antennaPortIx_get(self) -> repcap.AntennaPortIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, npar: int, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default, antennaPortIx=repcap.AntennaPortIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:[SUBF<ST0>]:ALLoc<CH0>:PUCCh:NPAR<AP> \n
		Snippet: driver.source.bb.eutra.uplink.subf.alloc.pucch.npar.set(npar = 1, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default, antennaPortIx = repcap.AntennaPortIx.Default) \n
		Sets the resource index for the supported PUCCH formats. \n
			:param npar: integer n(x) _PUCCH_max depends on the PUCCH format; to query the value, use the corresponding command, for example [:SOURcehw]:BB:EUTRa:UL:PUCCh:N1EMax?. Range: 0 to n(x) _PUCCH_max
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param antennaPortIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Npar')
		"""
		param = Conversions.decimal_value_to_str(npar)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		antennaPortIx_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortIx, repcap.AntennaPortIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUCCh:NPAR{antennaPortIx_cmd_val} {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default, antennaPortIx=repcap.AntennaPortIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:[SUBF<ST0>]:ALLoc<CH0>:PUCCh:NPAR<AP> \n
		Snippet: value: int = driver.source.bb.eutra.uplink.subf.alloc.pucch.npar.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default, antennaPortIx = repcap.AntennaPortIx.Default) \n
		Sets the resource index for the supported PUCCH formats. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param antennaPortIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Npar')
			:return: npar: integer n(x) _PUCCH_max depends on the PUCCH format; to query the value, use the corresponding command, for example [:SOURcehw]:BB:EUTRa:UL:PUCCh:N1EMax?. Range: 0 to n(x) _PUCCH_max"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		antennaPortIx_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortIx, repcap.AntennaPortIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUCCh:NPAR{antennaPortIx_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Npar':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Npar(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
