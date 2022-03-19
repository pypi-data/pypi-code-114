from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	def set(self, base_mod_type: enums.C5GbaseMod, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:MODulation \n
		Snippet: driver.source.bb.ofdm.alloc.modulation.set(base_mod_type = enums.C5GbaseMod.BPSK, allocationNull = repcap.AllocationNull.Default) \n
		Sets the modulation type of an allocation. \n
			:param base_mod_type: BPSK| QPSK| QAM16| QAM64| QAM256| SCMA| CIQ CIQ Custom IQ data file, loaded with the command [:SOURcehw]:BB:OFDM:ALLocch0:CIQFile.
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(base_mod_type, enums.C5GbaseMod)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:MODulation {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.C5GbaseMod:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:MODulation \n
		Snippet: value: enums.C5GbaseMod = driver.source.bb.ofdm.alloc.modulation.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the modulation type of an allocation. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: base_mod_type: BPSK| QPSK| QAM16| QAM64| QAM256| SCMA| CIQ CIQ Custom IQ data file, loaded with the command [:SOURcehw]:BB:OFDM:ALLocch0:CIQFile."""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.C5GbaseMod)
