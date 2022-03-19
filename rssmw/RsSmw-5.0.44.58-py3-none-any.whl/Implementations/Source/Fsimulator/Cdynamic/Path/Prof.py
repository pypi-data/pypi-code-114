from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prof:
	"""Prof commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prof", core, parent)

	def set(self, prof: enums.FadProfUdyn, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:CDYNamic:PATH<CH>:PROF \n
		Snippet: driver.source.fsimulator.cdynamic.path.prof.set(prof = enums.FadProfUdyn.PDOPpler, path = repcap.Path.Default) \n
		Sets the fading profile. \n
			:param prof: PDOPpler| RAYLeigh| SPATh PDOPpler Pure Doppler profile available in the first four paths (PATH1|2|3|4) RAYLeigh Rayleigh profile available for all paths SPATh Static path profile available for all paths
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.enum_scalar_to_str(prof, enums.FadProfUdyn)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:CDYNamic:PATH{path_cmd_val}:PROF {param}')

	# noinspection PyTypeChecker
	def get(self, path=repcap.Path.Default) -> enums.FadProfUdyn:
		"""SCPI: [SOURce<HW>]:FSIMulator:CDYNamic:PATH<CH>:PROF \n
		Snippet: value: enums.FadProfUdyn = driver.source.fsimulator.cdynamic.path.prof.get(path = repcap.Path.Default) \n
		Sets the fading profile. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: prof: PDOPpler| RAYLeigh| SPATh PDOPpler Pure Doppler profile available in the first four paths (PATH1|2|3|4) RAYLeigh Rayleigh profile available for all paths SPATh Static path profile available for all paths"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:CDYNamic:PATH{path_cmd_val}:PROF?')
		return Conversions.str_to_scalar_enum(response, enums.FadProfUdyn)
