from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Transition:
	"""Transition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("transition", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.BasebandPulseTransType:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:TRANsition:TYPE \n
		Snippet: value: enums.BasebandPulseTransType = driver.source.bb.general.pulm.transition.get_type_py() \n
		Sets the transition type of the pulse modulation signal. \n
			:return: pulm_trans_type: SMOothed| FAST
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PULM:TRANsition:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.BasebandPulseTransType)

	def set_type_py(self, pulm_trans_type: enums.BasebandPulseTransType) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:TRANsition:TYPE \n
		Snippet: driver.source.bb.general.pulm.transition.set_type_py(pulm_trans_type = enums.BasebandPulseTransType.FAST) \n
		Sets the transition type of the pulse modulation signal. \n
			:param pulm_trans_type: SMOothed| FAST
		"""
		param = Conversions.enum_scalar_to_str(pulm_trans_type, enums.BasebandPulseTransType)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PULM:TRANsition:TYPE {param}')
