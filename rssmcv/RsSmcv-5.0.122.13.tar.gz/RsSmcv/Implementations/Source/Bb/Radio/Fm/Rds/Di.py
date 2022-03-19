from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Di:
	"""Di commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("di", core, parent)

	def get_artificial(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:DI:ARTificial \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.di.get_artificial() \n
		Enables/disables 'artificial head' decoder identification. \n
			:return: di_artifical: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:DI:ARTificial?')
		return Conversions.str_to_bool(response)

	def set_artificial(self, di_artifical: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:DI:ARTificial \n
		Snippet: driver.source.bb.radio.fm.rds.di.set_artificial(di_artifical = False) \n
		Enables/disables 'artificial head' decoder identification. \n
			:param di_artifical: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(di_artifical)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:DI:ARTificial {param}')

	def get_compressed(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:DI:COMPressed \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.di.get_compressed() \n
		Enables/disables compressed decoder identification. \n
			:return: di_compressed: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:DI:COMPressed?')
		return Conversions.str_to_bool(response)

	def set_compressed(self, di_compressed: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:DI:COMPressed \n
		Snippet: driver.source.bb.radio.fm.rds.di.set_compressed(di_compressed = False) \n
		Enables/disables compressed decoder identification. \n
			:param di_compressed: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(di_compressed)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:DI:COMPressed {param}')

	def get_dynamic(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:DI:DYNamic \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.di.get_dynamic() \n
		Enables/disables dynamic decoder identification. \n
			:return: di_dynamic: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:DI:DYNamic?')
		return Conversions.str_to_bool(response)

	def set_dynamic(self, di_dynamic: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:DI:DYNamic \n
		Snippet: driver.source.bb.radio.fm.rds.di.set_dynamic(di_dynamic = False) \n
		Enables/disables dynamic decoder identification. \n
			:param di_dynamic: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(di_dynamic)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:DI:DYNamic {param}')

	def get_stereo(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:DI:STEReo \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.di.get_stereo() \n
		Enables/disables stereo decoder identification. \n
			:return: di_stereo: 1| ON| 0| OFF ON Stereo transmission OFF Mono transmission
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:DI:STEReo?')
		return Conversions.str_to_bool(response)

	def set_stereo(self, di_stereo: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:DI:STEReo \n
		Snippet: driver.source.bb.radio.fm.rds.di.set_stereo(di_stereo = False) \n
		Enables/disables stereo decoder identification. \n
			:param di_stereo: 1| ON| 0| OFF ON Stereo transmission OFF Mono transmission
		"""
		param = Conversions.bool_to_str(di_stereo)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:DI:STEReo {param}')
