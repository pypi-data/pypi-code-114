from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dshape:
	"""Dshape commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dshape", core, parent)

	def set(self, doppler_shape: enums.FadProfCustRange, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DEL:GROup<ST>:PATH<CH>:CUSTom:DSHape \n
		Snippet: driver.source.fsimulator.delPy.group.path.custom.dshape.set(doppler_shape = enums.FadProfCustRange.FLAT, fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Sets the doppler shape of the virtual profile. \n
			:param doppler_shape: FLAT| RAYLeigh
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.enum_scalar_to_str(doppler_shape, enums.FadProfCustRange)
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DEL:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:CUSTom:DSHape {param}')

	# noinspection PyTypeChecker
	def get(self, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> enums.FadProfCustRange:
		"""SCPI: [SOURce<HW>]:FSIMulator:DEL:GROup<ST>:PATH<CH>:CUSTom:DSHape \n
		Snippet: value: enums.FadProfCustRange = driver.source.fsimulator.delPy.group.path.custom.dshape.get(fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Sets the doppler shape of the virtual profile. \n
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: doppler_shape: FLAT| RAYLeigh"""
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:DEL:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:CUSTom:DSHape?')
		return Conversions.str_to_scalar_enum(response, enums.FadProfCustRange)
