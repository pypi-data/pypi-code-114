from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dist:
	"""Dist commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dist", core, parent)

	def set(self, dist_npdcch_npdsc: enums.EutraNbiotDciDistNpdcchNpdsch, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:DIST \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.alloc.dist.set(dist_npdcch_npdsc = enums.EutraNbiotDciDistNpdcchNpdsch.MIN, allocationNull = repcap.AllocationNull.Default) \n
		Sets how the distance between the NPDCCH to NPDSCH is determined. \n
			:param dist_npdcch_npdsc: STD| MIN| ZERO ZERO disables the NPDSCH SIB1-NR and NPUCCH transmissions. The NPDSCH is transmitted immediately after the NPDCCH. Use this value to increase the number of NPDSCH allocations.
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(dist_npdcch_npdsc, enums.EutraNbiotDciDistNpdcchNpdsch)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:DIST {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.EutraNbiotDciDistNpdcchNpdsch:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:DIST \n
		Snippet: value: enums.EutraNbiotDciDistNpdcchNpdsch = driver.source.bb.eutra.downlink.niot.dci.alloc.dist.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets how the distance between the NPDCCH to NPDSCH is determined. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dist_npdcch_npdsc: STD| MIN| ZERO ZERO disables the NPDSCH SIB1-NR and NPUCCH transmissions. The NPDSCH is transmitted immediately after the NPDCCH. Use this value to increase the number of NPDSCH allocations."""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:DIST?')
		return Conversions.str_to_scalar_enum(response, enums.EutraNbiotDciDistNpdcchNpdsch)
