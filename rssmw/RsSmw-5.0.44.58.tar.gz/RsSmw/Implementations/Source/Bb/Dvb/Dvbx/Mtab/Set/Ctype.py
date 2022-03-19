from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ctype:
	"""Ctype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ctype", core, parent)

	def set(self, ctype: enums.DvbS2XcodeType, modCodSet=repcap.ModCodSet.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:MTAB:SET<ST>:CTYPe \n
		Snippet: driver.source.bb.dvb.dvbx.mtab.set.ctype.set(ctype = enums.DvbS2XcodeType.MEDium, modCodSet = repcap.ModCodSet.Default) \n
		Selects the code type. \n
			:param ctype: NORMal| MEDium| SHORt
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
		"""
		param = Conversions.enum_scalar_to_str(ctype, enums.DvbS2XcodeType)
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:MTAB:SET{modCodSet_cmd_val}:CTYPe {param}')

	# noinspection PyTypeChecker
	def get(self, modCodSet=repcap.ModCodSet.Default) -> enums.DvbS2XcodeType:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:MTAB:SET<ST>:CTYPe \n
		Snippet: value: enums.DvbS2XcodeType = driver.source.bb.dvb.dvbx.mtab.set.ctype.get(modCodSet = repcap.ModCodSet.Default) \n
		Selects the code type. \n
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
			:return: ctype: NORMal| MEDium| SHORt"""
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:DVBX:MTAB:SET{modCodSet_cmd_val}:CTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.DvbS2XcodeType)
