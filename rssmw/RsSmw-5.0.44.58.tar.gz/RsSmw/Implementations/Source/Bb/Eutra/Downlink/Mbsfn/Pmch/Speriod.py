from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Speriod:
	"""Speriod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("speriod", core, parent)

	def set(self, sched_period: enums.EutraMchSchedPer, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:PMCH<CH0>:SPERiod \n
		Snippet: driver.source.bb.eutra.downlink.mbsfn.pmch.speriod.set(sched_period = enums.EutraMchSchedPer.SPM, indexNull = repcap.IndexNull.Default) \n
		Defines the MCH scheduling period, i.e. the periodicity used for providing MCH scheduling information at lower layers
		(MAC) applicable for an MCH. \n
			:param sched_period: SPM| SPRF8| SPRF16| SPRF32| SPRF64| SPRF128| SPRF256| SPRF512| SPRF1024
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Pmch')
		"""
		param = Conversions.enum_scalar_to_str(sched_period, enums.EutraMchSchedPer)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:PMCH{indexNull_cmd_val}:SPERiod {param}')

	# noinspection PyTypeChecker
	def get(self, indexNull=repcap.IndexNull.Default) -> enums.EutraMchSchedPer:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:MBSFn:PMCH<CH0>:SPERiod \n
		Snippet: value: enums.EutraMchSchedPer = driver.source.bb.eutra.downlink.mbsfn.pmch.speriod.get(indexNull = repcap.IndexNull.Default) \n
		Defines the MCH scheduling period, i.e. the periodicity used for providing MCH scheduling information at lower layers
		(MAC) applicable for an MCH. \n
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Pmch')
			:return: sched_period: SPM| SPRF8| SPRF16| SPRF32| SPRF64| SPRF128| SPRF256| SPRF512| SPRF1024"""
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:MBSFn:PMCH{indexNull_cmd_val}:SPERiod?')
		return Conversions.str_to_scalar_enum(response, enums.EutraMchSchedPer)
