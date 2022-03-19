from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pred:
	"""Pred commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pred", core, parent)

	@property
	def apply(self):
		"""apply commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import Apply
			self._apply = Apply(self._core, self._cmd_group)
		return self._apply

	def get_cnf_marker(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:PRED:CNFMarker \n
		Snippet: value: bool = driver.source.bb.nfc.pred.get_cnf_marker() \n
		If enabled marker 1 is positioned after the first idle. \n
			:return: conf: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:PRED:CNFMarker?')
		return Conversions.str_to_bool(response)

	def set_cnf_marker(self, conf: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:PRED:CNFMarker \n
		Snippet: driver.source.bb.nfc.pred.set_cnf_marker(conf = False) \n
		If enabled marker 1 is positioned after the first idle. \n
			:param conf: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(conf)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:PRED:CNFMarker {param}')

	# noinspection PyTypeChecker
	def get_sequence(self) -> enums.NfcPredef:
		"""SCPI: [SOURce<HW>]:BB:NFC:PRED:SEQuence \n
		Snippet: value: enums.NfcPredef = driver.source.bb.nfc.pred.get_sequence() \n
		Available only for 'Transmission Mode > Poll' and 'Transmission Mode > PCD to PICC'. Selects a predefined sequence. \n
			:return: sequence: FPS| BPA| BPS| APA| APS FPS Predefined NFC-F sequence with the elements: IDLE, SENSF_REQ, IDLE, BLANK BPA Predefined NFC-B sequence with the elements: IDLE, ALL_REQ, IDLE, BLANK or a predefined EMV Type A sequence with the elements: IDLE, WUPB, IDLE, BLANK BPS Predefined NFC-B sequence with the elements: IDLE, SENS_REQ, IDLE, BLANK or a predefined EMV Type B sequence with the elements: IDLE, REQB, IDLE, BLANK APA Predefined NFC-A sequence with the elements: IDLE, ALL_REQ, IDLE, BLANK or a predefined EMV Type A sequence with the elements: IDLE, WUPA, IDLE, BLANK APS Predefined NFC-A sequence with the elements: IDLE, SENS_REQ, IDLE, BLANK or a predefined EMV Type A sequence with the elements: IDLE, REQA, IDLE, BLANK
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:PRED:SEQuence?')
		return Conversions.str_to_scalar_enum(response, enums.NfcPredef)

	def set_sequence(self, sequence: enums.NfcPredef) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:PRED:SEQuence \n
		Snippet: driver.source.bb.nfc.pred.set_sequence(sequence = enums.NfcPredef.APA) \n
		Available only for 'Transmission Mode > Poll' and 'Transmission Mode > PCD to PICC'. Selects a predefined sequence. \n
			:param sequence: FPS| BPA| BPS| APA| APS FPS Predefined NFC-F sequence with the elements: IDLE, SENSF_REQ, IDLE, BLANK BPA Predefined NFC-B sequence with the elements: IDLE, ALL_REQ, IDLE, BLANK or a predefined EMV Type A sequence with the elements: IDLE, WUPB, IDLE, BLANK BPS Predefined NFC-B sequence with the elements: IDLE, SENS_REQ, IDLE, BLANK or a predefined EMV Type B sequence with the elements: IDLE, REQB, IDLE, BLANK APA Predefined NFC-A sequence with the elements: IDLE, ALL_REQ, IDLE, BLANK or a predefined EMV Type A sequence with the elements: IDLE, WUPA, IDLE, BLANK APS Predefined NFC-A sequence with the elements: IDLE, SENS_REQ, IDLE, BLANK or a predefined EMV Type A sequence with the elements: IDLE, REQA, IDLE, BLANK
		"""
		param = Conversions.enum_scalar_to_str(sequence, enums.NfcPredef)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:PRED:SEQuence {param}')

	def clone(self) -> 'Pred':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pred(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
