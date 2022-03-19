from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Direction:
	"""Direction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("direction", core, parent)

	def set(self, direction: enums.ConnDirection, tmConnector=repcap.TmConnector.Default) -> None:
		"""SCPI: OUTPut<HW>:TM<CH>:DIRection \n
		Snippet: driver.output.tm.direction.set(direction = enums.ConnDirection.INPut, tmConnector = repcap.TmConnector.Default) \n
		Determines whether the connector is used as an input or an output. \n
			:param direction: INPut| OUTPut
			:param tmConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tm')
		"""
		param = Conversions.enum_scalar_to_str(direction, enums.ConnDirection)
		tmConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(tmConnector, repcap.TmConnector)
		self._core.io.write(f'OUTPut<HwInstance>:TM{tmConnector_cmd_val}:DIRection {param}')

	# noinspection PyTypeChecker
	def get(self, tmConnector=repcap.TmConnector.Default) -> enums.ConnDirection:
		"""SCPI: OUTPut<HW>:TM<CH>:DIRection \n
		Snippet: value: enums.ConnDirection = driver.output.tm.direction.get(tmConnector = repcap.TmConnector.Default) \n
		Determines whether the connector is used as an input or an output. \n
			:param tmConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tm')
			:return: direction: INPut| OUTPut"""
		tmConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(tmConnector, repcap.TmConnector)
		response = self._core.io.query_str(f'OUTPut<HwInstance>:TM{tmConnector_cmd_val}:DIRection?')
		return Conversions.str_to_scalar_enum(response, enums.ConnDirection)
