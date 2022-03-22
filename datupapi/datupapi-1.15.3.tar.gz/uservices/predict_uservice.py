import os
import pandas as pd
import sys

from datupapi.extract.io import IO
from datupapi.predict.forecast import Forecast
from datupapi.utils.utils import Utils


def main():
    io = IO(config_file='config.yml', logfile='data_prediction', log_path='output/logs')
    pred = Forecast(config_file='config.yml', logfile='data_prediction', log_path='output/logs')
    utls = Utils(config_file='config.yml', logfile='data_prediction', log_path='output/logs')

    io.logger.debug('Data prediction starting...')
    timestamp = utls.set_timestamp()
    res_forecast_clean = utls.delete_datalake_objects(datalake=pred.datalake, datalake_path=pred.forecast_export_path)
    request = io.download_json_file(json_name='training_response', datalake_path=io.response_path)
    res_forecast = pred.create_forecast_deepar(forecast_name=pred.tenant_id +'_forecast_' + timestamp,
                                               predictor_arn=request['PredictorArn'])
    pred.check_status(arn_target=res_forecast, check_type='forecast')
    res_forecast_export = pred.create_forecast_export_deepar(export_job=pred.tenant_id + '_forecast_export_' + timestamp,
                                                             forecast_arn=res_forecast,
                                                             export_path=pred.forecast_export_path)
    pred.check_status(arn_target=res_forecast_export, check_type='export')
    io.logger.debug('Data prediction completed...')
    io.upload_log()
    # Microservice response
    response = {
        'ConfigFileUri': os.path.join('s3://', io.datalake, io.config_path, 'config.yml'),
        'ForecastArn': res_forecast
    }
    io.upload_json_file(message=response, json_name='predict_response', datalake_path=io.response_path)

if __name__ == '__main__':
    main()
    sys.exit(0)