from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mcod:
	"""Mcod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcod", core, parent)

	def set(self, mod_cod: enums.DvbS2XmodCod, modCodSet=repcap.ModCodSet.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:MTAB:SET<ST>:MCOD \n
		Snippet: driver.source.bb.dvb.dvbx.mtab.set.mcod.set(mod_cod = enums.DvbS2XmodCod.APSK128_X_N34, modCodSet = repcap.ModCodSet.Default) \n
		Selects the MODCOD. \n
			:param mod_cod: QPSK_S_14| QPSK_S_13| QPSK_S_25| QPSK_S_12| QPSK_S_35| QPSK_S_23| QPSK_S_34| QPSK_S_45| QPSK_S_56| QPSK_S_89| QPSK_S_910| PSK8_S_35| PSK8_S_23| PSK8_S_34| PSK8_S_56| PSK8_S_89| PSK8_S_910| APSK16_S_23| APSK16_S_34| APSK16_S_45| APSK16_S_56| APSK16_S_89| APSK16_S_910| APSK32_S_34| APSK32_S_45| APSK32_S_56| APSK32_S_89| APSK32_S_910| QPSK_X_N1345| QPSK_X_N920| QPSK_X_N1120| APSK8_X_N59L| APSK8_X_N2645L| PSK8_X_N2336| PSK8_X_N2536| PSK8_X_N1318| APSK16_X_N12L| APSK16_X_N815L| APSK16_X_N59L| APSK16_X_N2645| APSK16_X_N35| APSK16_X_N35L| APSK16_X_N2845| APSK16_X_N2336| APSK16_X_N23L| APSK16_X_N2536| APSK16_X_N1318| APSK16_X_N79| APSK16_X_N7790| APSK32_X_N23L| APSK32_X_N3245| APSK32_X_N1115| APSK32_X_N79| APSK64_X_N3245L| APSK64_X_N1115| APSK64_X_N79| APSK64_X_N45| APSK64_X_N56| APSK128_X_N34| APSK128_X_N79| APSK256_X_N2945L| APSK256_X_N23L| APSK256_X_N3145L| APSK256_X_N3245| APSK256_X_N1115L| APSK256_X_N34| QPSK_X_S1145| QPSK_X_S415| QPSK_X_S1445| QPSK_X_S715| QPSK_X_S815| QPSK_X_S3245| PSK8_X_S715| PSK8_X_S815| PSK8_X_S2645| PSK8_X_S3245| APSK16_X_S715| APSK16_X_S815| APSK16_X_S2645| APSK16_X_S35| APSK16_X_S3245| APSK32_X_S23| APSK32_X_S3245| QPSK_X_VN29| BPSK_X_VM15| BPSK_X_VM1145| BPSK_X_VM13| BPSK_X_VS15S| BPSK_X_VS1145| BPSK_X_VS15| BPSK_X_VS415| BPSK_X_VS13| QPSK_X_M15
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
		"""
		param = Conversions.enum_scalar_to_str(mod_cod, enums.DvbS2XmodCod)
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:MTAB:SET{modCodSet_cmd_val}:MCOD {param}')

	# noinspection PyTypeChecker
	def get(self, modCodSet=repcap.ModCodSet.Default) -> enums.DvbS2XmodCod:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:MTAB:SET<ST>:MCOD \n
		Snippet: value: enums.DvbS2XmodCod = driver.source.bb.dvb.dvbx.mtab.set.mcod.get(modCodSet = repcap.ModCodSet.Default) \n
		Selects the MODCOD. \n
			:param modCodSet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Set')
			:return: mod_cod: QPSK_S_14| QPSK_S_13| QPSK_S_25| QPSK_S_12| QPSK_S_35| QPSK_S_23| QPSK_S_34| QPSK_S_45| QPSK_S_56| QPSK_S_89| QPSK_S_910| PSK8_S_35| PSK8_S_23| PSK8_S_34| PSK8_S_56| PSK8_S_89| PSK8_S_910| APSK16_S_23| APSK16_S_34| APSK16_S_45| APSK16_S_56| APSK16_S_89| APSK16_S_910| APSK32_S_34| APSK32_S_45| APSK32_S_56| APSK32_S_89| APSK32_S_910| QPSK_X_N1345| QPSK_X_N920| QPSK_X_N1120| APSK8_X_N59L| APSK8_X_N2645L| PSK8_X_N2336| PSK8_X_N2536| PSK8_X_N1318| APSK16_X_N12L| APSK16_X_N815L| APSK16_X_N59L| APSK16_X_N2645| APSK16_X_N35| APSK16_X_N35L| APSK16_X_N2845| APSK16_X_N2336| APSK16_X_N23L| APSK16_X_N2536| APSK16_X_N1318| APSK16_X_N79| APSK16_X_N7790| APSK32_X_N23L| APSK32_X_N3245| APSK32_X_N1115| APSK32_X_N79| APSK64_X_N3245L| APSK64_X_N1115| APSK64_X_N79| APSK64_X_N45| APSK64_X_N56| APSK128_X_N34| APSK128_X_N79| APSK256_X_N2945L| APSK256_X_N23L| APSK256_X_N3145L| APSK256_X_N3245| APSK256_X_N1115L| APSK256_X_N34| QPSK_X_S1145| QPSK_X_S415| QPSK_X_S1445| QPSK_X_S715| QPSK_X_S815| QPSK_X_S3245| PSK8_X_S715| PSK8_X_S815| PSK8_X_S2645| PSK8_X_S3245| APSK16_X_S715| APSK16_X_S815| APSK16_X_S2645| APSK16_X_S35| APSK16_X_S3245| APSK32_X_S23| APSK32_X_S3245| QPSK_X_VN29| BPSK_X_VM15| BPSK_X_VM1145| BPSK_X_VM13| BPSK_X_VS15S| BPSK_X_VS1145| BPSK_X_VS15| BPSK_X_VS415| BPSK_X_VS13| QPSK_X_M15"""
		modCodSet_cmd_val = self._cmd_group.get_repcap_cmd_value(modCodSet, repcap.ModCodSet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:DVBX:MTAB:SET{modCodSet_cmd_val}:MCOD?')
		return Conversions.str_to_scalar_enum(response, enums.DvbS2XmodCod)
