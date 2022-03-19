from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InpMethod:
	"""InpMethod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inpMethod", core, parent)

	def set(self, inp_method: enums.FmStereoInpMeth, groupNull=repcap.GroupNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:INPMethod \n
		Snippet: driver.source.bb.stereo.grps.gt.inpMethod.set(inp_method = enums.FmStereoInpMeth.PARameters, groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param inp_method: No help available
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
		"""
		param = Conversions.enum_scalar_to_str(inp_method, enums.FmStereoInpMeth)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:INPMethod {param}')

	# noinspection PyTypeChecker
	def get(self, groupNull=repcap.GroupNull.Default) -> enums.FmStereoInpMeth:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:INPMethod \n
		Snippet: value: enums.FmStereoInpMeth = driver.source.bb.stereo.grps.gt.inpMethod.get(groupNull = repcap.GroupNull.Default) \n
		No command help available \n
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
			:return: inp_method: No help available"""
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:INPMethod?')
		return Conversions.str_to_scalar_enum(response, enums.FmStereoInpMeth)
