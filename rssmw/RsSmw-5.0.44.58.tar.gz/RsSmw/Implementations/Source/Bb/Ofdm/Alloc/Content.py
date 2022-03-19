from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Content:
	"""Content commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("content", core, parent)

	def set(self, content_type: enums.C5GcontentType, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:CONTent \n
		Snippet: driver.source.bb.ofdm.alloc.content.set(content_type = enums.C5GcontentType.DATA, allocationNull = repcap.AllocationNull.Default) \n
		Sets the content type. \n
			:param content_type: DATA| PREamble| PILot| REServed DATA Default value for FBMC and GFDM modulations. PREamble Default value for the first allocation of the UFMC modulation. DATA|PILot|REServed Selects the content type for f-OFDM/OFDM modulations.
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(content_type, enums.C5GcontentType)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:CONTent {param}')

	# noinspection PyTypeChecker
	def get(self, allocationNull=repcap.AllocationNull.Default) -> enums.C5GcontentType:
		"""SCPI: [SOURce<HW>]:BB:OFDM:ALLoc<CH0>:CONTent \n
		Snippet: value: enums.C5GcontentType = driver.source.bb.ofdm.alloc.content.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the content type. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: content_type: DATA| PREamble| PILot| REServed DATA Default value for FBMC and GFDM modulations. PREamble Default value for the first allocation of the UFMC modulation. DATA|PILot|REServed Selects the content type for f-OFDM/OFDM modulations."""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:ALLoc{allocationNull_cmd_val}:CONTent?')
		return Conversions.str_to_scalar_enum(response, enums.C5GcontentType)
