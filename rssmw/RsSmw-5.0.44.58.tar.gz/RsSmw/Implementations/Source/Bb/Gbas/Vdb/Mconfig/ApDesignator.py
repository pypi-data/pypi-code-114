from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApDesignator:
	"""ApDesignator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apDesignator", core, parent)

	def set(self, ap_per_des: enums.GbasAppPerDes, vdbTransmitter=repcap.VdbTransmitter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:APDesignator \n
		Snippet: driver.source.bb.gbas.vdb.mconfig.apDesignator.set(ap_per_des = enums.GbasAppPerDes.GAB, vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Requires 'Mode > GBAS' (LAAS) header information. Sets the approach performance designator. \n
			:param ap_per_des: GAB| GC| GCD
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
		"""
		param = Conversions.enum_scalar_to_str(ap_per_des, enums.GbasAppPerDes)
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:APDesignator {param}')

	# noinspection PyTypeChecker
	def get(self, vdbTransmitter=repcap.VdbTransmitter.Default) -> enums.GbasAppPerDes:
		"""SCPI: [SOURce<HW>]:BB:GBAS:VDB<CH>:MCONfig:APDesignator \n
		Snippet: value: enums.GbasAppPerDes = driver.source.bb.gbas.vdb.mconfig.apDesignator.get(vdbTransmitter = repcap.VdbTransmitter.Default) \n
		Requires 'Mode > GBAS' (LAAS) header information. Sets the approach performance designator. \n
			:param vdbTransmitter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Vdb')
			:return: ap_per_des: GAB| GC| GCD"""
		vdbTransmitter_cmd_val = self._cmd_group.get_repcap_cmd_value(vdbTransmitter, repcap.VdbTransmitter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GBAS:VDB{vdbTransmitter_cmd_val}:MCONfig:APDesignator?')
		return Conversions.str_to_scalar_enum(response, enums.GbasAppPerDes)
