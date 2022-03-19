from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Profile:
	"""Profile commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("profile", core, parent)

	def set(self, profile: enums.FadingProfileB, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:DEL30:GROup<ST>:PATH<CH>:PROFile \n
		Snippet: driver.source.fsimulator.mdelay.del30.group.path.profile.set(profile = enums.FadingProfileB.BELLindoor, fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Selects the fading profile for the paths. \n
			:param profile: SPATh| RAYLeigh| PDOPpler| RICE| CPHase| OGAUs| TGAUs| DGAUs| WDOPpler| WRICe| GDOPpler| GFD8| GFD1| WATTerson| CUSTom| SCM | BELLindoor| BELVehicle SPAT static transmission path PDOPpler | RAYLeigh | RICE | CUSTom | SCM pure Doppler | Rayleigh | Rice | Custom | SCM CPHase constant phase OGAUs | TGAUs | DGAUs | GDOPpler | GFD8 | GFD1 GAUS1 | GAUS2 | GAUSDAB | Gauss Doppler | Gauss (0.08 fd) | Gauss (0.01 fd) WATTerson Gauss (Watterson) WDOPpler | WRICe WiMAX Doppler | WiMAX Rice BELLindoor|BELVehicle Bell Shape tgn Indoor, Bell Shape tgn Moving Vehicle
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.enum_scalar_to_str(profile, enums.FadingProfileB)
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MDELay:DEL30:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:PROFile {param}')

	# noinspection PyTypeChecker
	def get(self, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> enums.FadingProfileB:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:DEL30:GROup<ST>:PATH<CH>:PROFile \n
		Snippet: value: enums.FadingProfileB = driver.source.fsimulator.mdelay.del30.group.path.profile.get(fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Selects the fading profile for the paths. \n
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: profile: SPATh| RAYLeigh| PDOPpler| RICE| CPHase| OGAUs| TGAUs| DGAUs| WDOPpler| WRICe| GDOPpler| GFD8| GFD1| WATTerson| CUSTom| SCM | BELLindoor| BELVehicle SPAT static transmission path PDOPpler | RAYLeigh | RICE | CUSTom | SCM pure Doppler | Rayleigh | Rice | Custom | SCM CPHase constant phase OGAUs | TGAUs | DGAUs | GDOPpler | GFD8 | GFD1 GAUS1 | GAUS2 | GAUSDAB | Gauss Doppler | Gauss (0.08 fd) | Gauss (0.01 fd) WATTerson Gauss (Watterson) WDOPpler | WRICe WiMAX Doppler | WiMAX Rice BELLindoor|BELVehicle Bell Shape tgn Indoor, Bell Shape tgn Moving Vehicle"""
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MDELay:DEL30:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:PROFile?')
		return Conversions.str_to_scalar_enum(response, enums.FadingProfileB)
