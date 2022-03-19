from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Profile:
	"""Profile commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("profile", core, parent)

	def set(self, profile: enums.FadBdProf, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:PATH<CH>:PROFile \n
		Snippet: driver.source.fsimulator.birthDeath.path.profile.set(profile = enums.FadBdProf.PDOPpler, path = repcap.Path.Default) \n
		This command queries the fading profile. In birth death propagation, the pure Doppler profile is used. \n
			:param profile: PDOPpler
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.enum_scalar_to_str(profile, enums.FadBdProf)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:PATH{path_cmd_val}:PROFile {param}')

	# noinspection PyTypeChecker
	def get(self, path=repcap.Path.Default) -> enums.FadBdProf:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:PATH<CH>:PROFile \n
		Snippet: value: enums.FadBdProf = driver.source.fsimulator.birthDeath.path.profile.get(path = repcap.Path.Default) \n
		This command queries the fading profile. In birth death propagation, the pure Doppler profile is used. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: profile: PDOPpler"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:PATH{path_cmd_val}:PROFile?')
		return Conversions.str_to_scalar_enum(response, enums.FadBdProf)
