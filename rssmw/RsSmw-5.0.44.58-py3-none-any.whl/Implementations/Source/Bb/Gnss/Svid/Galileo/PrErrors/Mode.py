from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, pr_erors_mode: enums.PseudorangeMode, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:PRERrors:MODE \n
		Snippet: driver.source.bb.gnss.svid.galileo.prErrors.mode.set(pr_erors_mode = enums.PseudorangeMode.CONStant, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets how the pseudorange errors are defined. \n
			:param pr_erors_mode: FSBas| CONStant| PROFile| FILE FSBas Extracted from the imported SBAS corrections, if [:SOURcehw]:BB:GNSS:ECModeSYNC. CONStant Set with the command [:SOURcehw]:BB:GNSS:SVIDch:GPS:PRERrors:VALue PROFile Defined with the command pairs [:SOURcehw]:BB:GNSS:SVIDch:GPS:PRERrors:PROFilegr:REFerence and [:SOURcehw]:BB:GNSS:SVIDch:GPS:PRERrors:PROFilegr:VALue FILE Sets pseudorange errors according to a file with extension *.rs_perr. Select the file via [:SOURcehw]:BB:GNSS:SVIDch:GPS:PRERrors:FILE.
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
		"""
		param = Conversions.enum_scalar_to_str(pr_erors_mode, enums.PseudorangeMode)
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:PRERrors:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> enums.PseudorangeMode:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:PRERrors:MODE \n
		Snippet: value: enums.PseudorangeMode = driver.source.bb.gnss.svid.galileo.prErrors.mode.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets how the pseudorange errors are defined. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: pr_erors_mode: FSBas| CONStant| PROFile| FILE FSBas Extracted from the imported SBAS corrections, if [:SOURcehw]:BB:GNSS:ECModeSYNC. CONStant Set with the command [:SOURcehw]:BB:GNSS:SVIDch:GPS:PRERrors:VALue PROFile Defined with the command pairs [:SOURcehw]:BB:GNSS:SVIDch:GPS:PRERrors:PROFilegr:REFerence and [:SOURcehw]:BB:GNSS:SVIDch:GPS:PRERrors:PROFilegr:VALue FILE Sets pseudorange errors according to a file with extension *.rs_perr. Select the file via [:SOURcehw]:BB:GNSS:SVIDch:GPS:PRERrors:FILE."""
		satelliteSvid_cmd_val = self._cmd_group.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:PRERrors:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PseudorangeMode)
