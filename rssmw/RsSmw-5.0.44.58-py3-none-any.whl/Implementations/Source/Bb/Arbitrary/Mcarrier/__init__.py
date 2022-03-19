from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mcarrier:
	"""Mcarrier commands group definition. 37 total commands, 9 Subgroups, 4 group commands
	Repeated Capability: Carrier, default value after init: Carrier.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcarrier", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_carrier_get', 'repcap_carrier_set', repcap.Carrier.Nr1)

	def repcap_carrier_set(self, carrier: repcap.Carrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Carrier.Default
		Default value after init: Carrier.Nr1"""
		self._cmd_group.set_repcap_enum_value(carrier)

	def repcap_carrier_get(self) -> repcap.Carrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def carrier(self):
		"""carrier commands group. 7 Sub-classes, 3 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import Carrier
			self._carrier = Carrier(self._core, self._cmd_group)
		return self._carrier

	@property
	def cfactor(self):
		"""cfactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cfactor'):
			from .Cfactor import Cfactor
			self._cfactor = Cfactor(self._core, self._cmd_group)
		return self._cfactor

	@property
	def clipping(self):
		"""clipping commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_clipping'):
			from .Clipping import Clipping
			self._clipping = Clipping(self._core, self._cmd_group)
		return self._clipping

	@property
	def cload(self):
		"""cload commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cload'):
			from .Cload import Cload
			self._cload = Cload(self._core, self._cmd_group)
		return self._cload

	@property
	def create(self):
		"""create commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_create'):
			from .Create import Create
			self._create = Create(self._core, self._cmd_group)
		return self._create

	@property
	def edit(self):
		"""edit commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_edit'):
			from .Edit import Edit
			self._edit = Edit(self._core, self._cmd_group)
		return self._edit

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	def get_clock(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CLOCk \n
		Snippet: value: float = driver.source.bb.arbitrary.mcarrier.get_clock() \n
		Queries the resulting sample rate at which the multi-carrier waveform is output by the arbitrary waveform generator. The
		output clock rate depends on the number of carriers, carrier spacing, and input sample rate of the leftmost or rightmost
		carriers. \n
			:return: clock: float Range: 400 to Max
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:CLOCk?')
		return Conversions.str_to_float(response)

	def get_ofile(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:OFILe \n
		Snippet: value: str = driver.source.bb.arbitrary.mcarrier.get_ofile() \n
		Defines the output file name for the multi-carrier waveform (file extension *.wv) . This file name is required to
		calculate the waveform with the commands [:SOURce<hw>]:BB:ARBitrary:MCARrier:CLOad or
		[:SOURce<hw>]:BB:ARBitrary:MCARrier:CREate. \n
			:return: ofile: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:OFILe?')
		return trim_str_response(response)

	def set_ofile(self, ofile: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:OFILe \n
		Snippet: driver.source.bb.arbitrary.mcarrier.set_ofile(ofile = '1') \n
		Defines the output file name for the multi-carrier waveform (file extension *.wv) . This file name is required to
		calculate the waveform with the commands [:SOURce<hw>]:BB:ARBitrary:MCARrier:CLOad or
		[:SOURce<hw>]:BB:ARBitrary:MCARrier:CREate. \n
			:param ofile: string
		"""
		param = Conversions.value_to_quoted_str(ofile)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:OFILe {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:PRESet \n
		Snippet: driver.source.bb.arbitrary.mcarrier.preset() \n
		Sets all the multi-carrier parameters to their default values. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:PRESet \n
		Snippet: driver.source.bb.arbitrary.mcarrier.preset_with_opc() \n
		Sets all the multi-carrier parameters to their default values. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:PRESet', opc_timeout_ms)

	def get_samples(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:SAMPles \n
		Snippet: value: int = driver.source.bb.arbitrary.mcarrier.get_samples() \n
		Queries the resulting file size. \n
			:return: samples: integer Range: 0 to INT_MAX, Unit: samples
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:SAMPles?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Mcarrier':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mcarrier(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
