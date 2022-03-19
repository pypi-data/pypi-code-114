from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Parameter:
	"""Parameter commands group definition. 8 total commands, 0 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("parameter", core, parent)

	def get_apco_25(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:APCO25 \n
		Snippet: value: float = driver.source.bb.xmRadio.satellite.filterPy.parameter.get_apco_25() \n
		No command help available \n
			:return: apco_25: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:APCO25?')
		return Conversions.str_to_float(response)

	def set_apco_25(self, apco_25: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:APCO25 \n
		Snippet: driver.source.bb.xmRadio.satellite.filterPy.parameter.set_apco_25(apco_25 = 1.0) \n
		No command help available \n
			:param apco_25: No help available
		"""
		param = Conversions.decimal_value_to_str(apco_25)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:APCO25 {param}')

	def get_cosine(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:COSine \n
		Snippet: value: float = driver.source.bb.xmRadio.satellite.filterPy.parameter.get_cosine() \n
		No command help available \n
			:return: cosine: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:COSine?')
		return Conversions.str_to_float(response)

	def set_cosine(self, cosine: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:COSine \n
		Snippet: driver.source.bb.xmRadio.satellite.filterPy.parameter.set_cosine(cosine = 1.0) \n
		No command help available \n
			:param cosine: No help available
		"""
		param = Conversions.decimal_value_to_str(cosine)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:COSine {param}')

	def get_gauss(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:GAUSs \n
		Snippet: value: float = driver.source.bb.xmRadio.satellite.filterPy.parameter.get_gauss() \n
		No command help available \n
			:return: gauss: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:GAUSs?')
		return Conversions.str_to_float(response)

	def set_gauss(self, gauss: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:GAUSs \n
		Snippet: driver.source.bb.xmRadio.satellite.filterPy.parameter.set_gauss(gauss = 1.0) \n
		No command help available \n
			:param gauss: No help available
		"""
		param = Conversions.decimal_value_to_str(gauss)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:GAUSs {param}')

	def get_lpass_evm(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:LPASSEVM \n
		Snippet: value: float = driver.source.bb.xmRadio.satellite.filterPy.parameter.get_lpass_evm() \n
		No command help available \n
			:return: lpass_evm: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:LPASSEVM?')
		return Conversions.str_to_float(response)

	def set_lpass_evm(self, lpass_evm: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:LPASSEVM \n
		Snippet: driver.source.bb.xmRadio.satellite.filterPy.parameter.set_lpass_evm(lpass_evm = 1.0) \n
		No command help available \n
			:param lpass_evm: No help available
		"""
		param = Conversions.decimal_value_to_str(lpass_evm)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:LPASSEVM {param}')

	def get_lpass(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:LPASs \n
		Snippet: value: float = driver.source.bb.xmRadio.satellite.filterPy.parameter.get_lpass() \n
		No command help available \n
			:return: lpass: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:LPASs?')
		return Conversions.str_to_float(response)

	def set_lpass(self, lpass: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:LPASs \n
		Snippet: driver.source.bb.xmRadio.satellite.filterPy.parameter.set_lpass(lpass = 1.0) \n
		No command help available \n
			:param lpass: No help available
		"""
		param = Conversions.decimal_value_to_str(lpass)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:LPASs {param}')

	def get_pgauss(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:PGAuss \n
		Snippet: value: float = driver.source.bb.xmRadio.satellite.filterPy.parameter.get_pgauss() \n
		No command help available \n
			:return: pgauss: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:PGAuss?')
		return Conversions.str_to_float(response)

	def set_pgauss(self, pgauss: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:PGAuss \n
		Snippet: driver.source.bb.xmRadio.satellite.filterPy.parameter.set_pgauss(pgauss = 1.0) \n
		No command help available \n
			:param pgauss: No help available
		"""
		param = Conversions.decimal_value_to_str(pgauss)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:PGAuss {param}')

	def get_rcosine(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:RCOSine \n
		Snippet: value: float = driver.source.bb.xmRadio.satellite.filterPy.parameter.get_rcosine() \n
		No command help available \n
			:return: rcosine: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:RCOSine?')
		return Conversions.str_to_float(response)

	def set_rcosine(self, rcosine: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:RCOSine \n
		Snippet: driver.source.bb.xmRadio.satellite.filterPy.parameter.set_rcosine(rcosine = 1.0) \n
		No command help available \n
			:param rcosine: No help available
		"""
		param = Conversions.decimal_value_to_str(rcosine)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:RCOSine {param}')

	def get_sphase(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:SPHase \n
		Snippet: value: float = driver.source.bb.xmRadio.satellite.filterPy.parameter.get_sphase() \n
		No command help available \n
			:return: sphase: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:SPHase?')
		return Conversions.str_to_float(response)

	def set_sphase(self, sphase: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:XMRadio:SATellite:FILTer:PARameter:SPHase \n
		Snippet: driver.source.bb.xmRadio.satellite.filterPy.parameter.set_sphase(sphase = 1.0) \n
		No command help available \n
			:param sphase: No help available
		"""
		param = Conversions.decimal_value_to_str(sphase)
		self._core.io.write(f'SOURce<HwInstance>:BB:XMRadio:SATellite:FILTer:PARameter:SPHase {param}')
