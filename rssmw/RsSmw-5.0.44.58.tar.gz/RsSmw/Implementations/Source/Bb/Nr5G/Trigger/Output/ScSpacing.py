from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScSpacing:
	"""ScSpacing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scSpacing", core, parent)

	def set(self, scs: enums.EidNr5GscsGeneral, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:SCSPacing \n
		Snippet: driver.source.bb.nr5G.trigger.output.scSpacing.set(scs = enums.EidNr5GscsGeneral.SCS120, output = repcap.Output.Default) \n
		Defines the subcarrier spacing (SCS) value for a UL/DL pattern containing a marker. The available values depend on the
		set 'Deployment' value. \n
			:param scs: SCS15| SCS30| SCS60| SCS120| SCS240| SCS480| SCS960
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(scs, enums.EidNr5GscsGeneral)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:SCSPacing {param}')

	# noinspection PyTypeChecker
	def get(self, output=repcap.Output.Default) -> enums.EidNr5GscsGeneral:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:SCSPacing \n
		Snippet: value: enums.EidNr5GscsGeneral = driver.source.bb.nr5G.trigger.output.scSpacing.get(output = repcap.Output.Default) \n
		Defines the subcarrier spacing (SCS) value for a UL/DL pattern containing a marker. The available values depend on the
		set 'Deployment' value. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: scs: SCS15| SCS30| SCS60| SCS120| SCS240| SCS480| SCS960"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:SCSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.EidNr5GscsGeneral)
