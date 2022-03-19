from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Restart:
	"""Restart commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("restart", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:RESTart \n
		Snippet: driver.source.fsimulator.restart.set() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:RESTart')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:RESTart \n
		Snippet: driver.source.fsimulator.restart.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:FSIMulator:RESTart', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FadRestMode:
		"""SCPI: [SOURce<HW>]:FSIMulator:RESTart:MODE \n
		Snippet: value: enums.FadRestMode = driver.source.fsimulator.restart.get_mode() \n
		Selects how a restart of fading simulation is triggered. \n
			:return: mode: AUTO| BBTRigger| AAUT BBTRigger Restarts the fading process synchronously with received baseband trigger signal. AAUT Not supported in the current version.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:RESTart:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FadRestMode)

	def set_mode(self, mode: enums.FadRestMode) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:RESTart:MODE \n
		Snippet: driver.source.fsimulator.restart.set_mode(mode = enums.FadRestMode.AAUT) \n
		Selects how a restart of fading simulation is triggered. \n
			:param mode: AUTO| BBTRigger| AAUT BBTRigger Restarts the fading process synchronously with received baseband trigger signal. AAUT Not supported in the current version.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FadRestMode)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:RESTart:MODE {param}')

	# noinspection PyTypeChecker
	def get_rmode(self) -> enums.TrigRunMode:
		"""SCPI: [SOURce<HW>]:FSIMulator:RESTart:RMODE \n
		Snippet: value: enums.TrigRunMode = driver.source.fsimulator.restart.get_rmode() \n
		No command help available \n
			:return: run_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:RESTart:RMODE?')
		return Conversions.str_to_scalar_enum(response, enums.TrigRunMode)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TrigSourRest:
		"""SCPI: [SOURce<HW>]:FSIMulator:RESTart:SOURce \n
		Snippet: value: enums.TrigSourRest = driver.source.fsimulator.restart.get_source() \n
		No command help available \n
			:return: rest_sour: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:RESTart:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TrigSourRest)

	def set_source(self, rest_sour: enums.TrigSourRest) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:RESTart:SOURce \n
		Snippet: driver.source.fsimulator.restart.set_source(rest_sour = enums.TrigSourRest.EGC1) \n
		No command help available \n
			:param rest_sour: No help available
		"""
		param = Conversions.enum_scalar_to_str(rest_sour, enums.TrigSourRest)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:RESTart:SOURce {param}')
