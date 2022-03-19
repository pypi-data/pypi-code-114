from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Map:
	"""Map commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("map", core, parent)

	def set(self, sensor_id: str, mapping: enums.ErFpowSensMapping) -> None:
		"""SCPI: SLISt:SENSor:MAP \n
		Snippet: driver.slist.sensor.map.set(sensor_id = '1', mapping = enums.ErFpowSensMapping.SENS1) \n
		Assigns a sensor directly to one of the sensor channels, using the sensor name and serial number. To find out the the
		sensor name and ID, you can get it from the label of the R&S NRP, or using the command method RsSmw.Slist.Scan.state.
		This command detects all R&S NRP power sensors connected in the LAN or via 'USBTMC protocol. \n
			:param sensor_id: string
			:param mapping: enum
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sensor_id', sensor_id, DataType.String), ArgSingle('mapping', mapping, DataType.Enum, enums.ErFpowSensMapping))
		self._core.io.write(f'SLISt:SENSor:MAP {param}'.rstrip())
