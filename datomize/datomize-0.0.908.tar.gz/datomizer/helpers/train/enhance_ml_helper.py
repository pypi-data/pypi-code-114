import json
import requests
from datomizer import DatoMapper
from datomizer.utils import constants, general


def create_enhance_ml_request(target_table, target_column, metric_list=[], algorithm_list=[]) -> dict:
    return {"tableName": target_table, "targetColumn": target_column,
            "metricList": metric_list, "algorithmList": algorithm_list}


def enhance_ml_evaluate(dato_mapper: DatoMapper, target_table, target_column, metric_list=[], algorithm_list=[]) -> int:
    dato_mapper.wait()
    response_json = dato_mapper.datomizer.get_response_json(requests.put,
                                                            url=constants.MANAGEMENT_PUT_ENHANCE_ML_EVALUATE_FLOW,
                                                            url_params=[dato_mapper.business_unit_id,
                                                                        dato_mapper.project_id,
                                                                        dato_mapper.flow_id],
                                                            headers={"Content-Type": "application/json"},
                                                            data=json.dumps(create_enhance_ml_request(target_table,
                                                                                                      target_column,
                                                                                                      metric_list,
                                                                                                      algorithm_list)))
    return response_json


def get_train_iteration_by_target(dato_mapper: DatoMapper, target_table, target_column) -> dict:
    flow = dato_mapper.get_flow()
    iteration = [t for t in flow[general.TRAIN_ITERATIONS]
                 if t[general.ENHANCE_ML_TARGET_TABLE] == target_table
                 and t[general.ENHANCE_ML_TARGET_COLUMN == target_column]][0]
    return iteration

