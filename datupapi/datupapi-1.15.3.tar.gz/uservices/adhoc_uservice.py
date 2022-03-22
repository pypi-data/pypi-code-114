import os
import sys

from datupapi.extract.io import IO
from datupapi.utils.utils import Utils


def main():
    io = IO(config_file='config.yml', logfile='data_ranking', log_path='output/logs')
    utls = Utils(config_file='config.yml', logfile='data_ranking', log_path='output/logs')

    df = io.download_csv(q_name='Qfcst', datalake_path='dev/ivan/general/tft12w/output/', date_cols=['Date'])
    records = io.populate_bigquery_table(df,
                                         project_id='dev-datupapi-1-329822',
                                         tenant_id='comfandi',
                                         table_name='TblForecast')

    '''message = '<p>Hola Equipo,</p> \
                <p>Datup te informa que nuestra plataforma ha finalizado tus pronosticos. Ingresa a este <a href="http://www.datup.ai">link</a> para descargarlos.</p> \
                <p>Cordialmente,</p> \
                <p>Datup Team</p> \
                <p><a href="http://www.datup.ai">www.datup.ai</a></p>'
    response = utls.send_email_notification(to_emails=['neosagan@gmail.com'],
                                            cc_emails=[],
                                            bcc_emails=['ramiro@datup.ai'],
                                            html_message=message)'''

if __name__ == '__main__':
    main()
    sys.exit(0)