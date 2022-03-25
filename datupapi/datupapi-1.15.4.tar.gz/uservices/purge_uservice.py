import os
import sys

from datupapi.extract.io import IO
from datupapi.training.deepar import DeepAR
from datupapi.predict.forecast import Forecast
from datupapi.utils.utils import Utils


def main():
    io = IO(config_file='config.yml', logfile='resources_purge', log_path='output/logs')
    trng = DeepAR(config_file='config.yml', logfile='resources_purge', log_path='output/logs')
    fcst = Forecast(config_file='config.yml', logfile='resources_purge', log_path='output/logs')

    io.logger.debug('Resources purging starting...')
    request_predict = io.download_json_file(json_name='predict_response', datalake_path=io.response_path)
    request_training = io.download_json_file(json_name='training_response', datalake_path=io.response_path)
    fcst.delete_forecast_deepar(arn_forecast=request_predict['ForecastArn'])
    trng.delete_predictor_deepar(arn_predictor=request_training['PredictorArn'])
    trng.delete_dataset_group_deepar(arn_datasetgroup=request_training['DatasetGroupArn'])
    io.logger.debug('Resources purging completed...')
    io.upload_log()
    # Microservice response
    response = {
        'ConfigFileUri': os.path.join('s3://', io.datalake, io.config_path, 'config.yml')
    }
    io.upload_json_file(message=response, json_name='purge_response', datalake_path=io.response_path)


if __name__ == '__main__':
    main()
    sys.exit(0)