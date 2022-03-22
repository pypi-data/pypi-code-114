import os
import pandas as pd
import sys
import time

from datupapi.extract.io import IO
from datupapi.training.deepar import DeepAR
from datupapi.utils.utils import Utils


def main():
    io = IO(config_file='config.yml', logfile='data_training', log_path='output/logs')
    trng = DeepAR(config_file='config.yml', logfile='data_training', log_path='output/logs')
    utls = Utils(config_file='config.yml', logfile='data_training', log_path='output/logs')

    io.logger.debug('Data training starting...')
    timestamp = utls.set_timestamp()
    res_backtests_clean = utls.delete_datalake_objects(datalake=trng.datalake, datalake_path=trng.backtest_export_path)
    res_dataset = trng.create_dataset_deepar(dataset_name=trng.tenant_id + '_dataset_' + timestamp,
                                             use_location=trng.use_location)
    if len(trng.dataset_import_path) == 2:
        related_cols = io.download_object_csv(datalake_path=io.dataset_import_path[1], num_records=1).columns
        res_related = trng.create_dataset_deepar(dataset_name=trng.tenant_id + '_related_' + timestamp,
                                                 dataset_type='RELATED_TIME_SERIES',
                                                 related_dataset_dims=related_cols,
                                                 use_location=trng.use_location)
        res_datasetgroup = trng.create_dataset_group_deepar(dataset_group_name=trng.tenant_id + '_datasetgroup_' + timestamp,
                                                            dataset_arns=[res_dataset, res_related])
        res_import = trng.create_dataset_import_deepar(import_job=trng.tenant_id + '_import_' + timestamp,
                                                       dataset_arn=res_dataset,
                                                       import_path=trng.dataset_import_path[0])
        trng.check_status(arn_target=res_import, check_type='import')
        res_import_related = trng.create_dataset_import_deepar(import_job=trng.tenant_id + '_import_related' + timestamp,
                                                               dataset_arn=res_related,
                                                               import_type='RELATED_TIME_SERIES',
                                                               import_path=trng.dataset_import_path[1])
        trng.check_status(arn_target=res_import, check_type='import')
    else:
        res_datasetgroup = trng.create_dataset_group_deepar(dataset_group_name=trng.tenant_id + '_datasetgroup_' + timestamp,
                                                            dataset_arns=[res_dataset])
        res_import = trng.create_dataset_import_deepar(import_job=trng.tenant_id + '_import_' + timestamp,
                                                       dataset_arn=res_dataset,
                                                       import_path=trng.dataset_import_path[0])
    trng.check_status(arn_target=res_import, check_type='import')

    if trng.use_automl:
        res_predictor = trng.create_predictor_automl(predictor_name=trng.tenant_id + '_predictor_' + timestamp,
                                                     dataset_group_arn=res_datasetgroup,
                                                     use_location=trng.use_location)
    else:
        res_predictor = trng.create_predictor_deepar(predictor_name=trng.tenant_id + '_predictor_' + timestamp,
                                                     dataset_group_arn=res_datasetgroup,
                                                     use_location=trng.use_location)
    trng.check_status(arn_target=res_predictor, check_type='predictor')
    res_backtest_export = trng.create_backtest_export_deepar(export_job=trng.tenant_id + '_backtest_export_' + timestamp,
                                                             predictor_arn=res_predictor,
                                                             export_path=trng.backtest_export_path)
    io.logger.debug('Data training completed...')
    io.upload_log()
    # Microservice response
    response = {
        'ConfigFileUri': os.path.join('s3://', io.datalake, io.config_path, 'config.yml'),
        'DatasetGroupArn': res_datasetgroup,
        'PredictorArn': res_predictor
    }
    io.upload_json_file(message=response, json_name='training_response', datalake_path=io.response_path)


if __name__ == '__main__':
    main()
    sys.exit(0)