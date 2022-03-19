from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def set(self, filename: str, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:PRERrors:FILE \n
		Snippet: driver.source.bb.gnss.svid.navic.prErrors.file.set(filename = '1', satelliteSvid = repcap.SatelliteSvid.Default) \n
		Loads a pseudorange error file with extension *.rs_perr from the default directory. \n
			:param filename: string
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.value_to_quoted_str(filename)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:PRERrors:FILE {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:NAVic:PRERrors:FILE \n
		Snippet: value: str = driver.source.bb.gnss.svid.navic.prErrors.file.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Loads a pseudorange error file with extension *.rs_perr from the default directory. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: filename: string"""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:NAVic:PRERrors:FILE?')
		return trim_str_response(response)
