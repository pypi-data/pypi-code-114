import os
import pandas as pd
import sys
import boto3

from datupapi.extract.io import IO
from datupapi.prepare.format import Format
from datupapi.utils.utils import Utils


def normalization(texto):
    tupla = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"),(",", ""),(".", ""),(":", ""),(";", ""),
             ("-", ""),("¡", ""),("!", ""),("¿", ""),("?", ""),
             ("'", ""),("#", ""),("$", ""),("%", ""),("&", ""),("/", "_"),('<', ""),('>', ""),('[', ""),
             (']', ""),('*', ""),('-', ""),('+', ""),('°', ""),('¬', ""),('{', ""),('}', ""),('\n', ""),('\t', ""),
             ('"',""),('«',""),('»',""),("@",""),(" ","_"))
    for a, b in tupla:
        texto = texto.replace(a, b)
    return texto


def main():

    DOCKER_CONFIG_PATH = 'config.yml'
    io = IO(config_file=DOCKER_CONFIG_PATH, logfile='data_export', log_path='output/logs')
    fmt = Format(config_file=DOCKER_CONFIG_PATH, logfile='data_export', log_path='output/logs')
    utls = Utils(config_file=DOCKER_CONFIG_PATH, logfile='data_export', log_path='output/logs')

    io.logger.debug('Results export starting...')
    file_name = 'DatupResults' + fmt.tenant_id + str(utls.set_timestamp())[0:8] + '.xlsx'
    excel_handler = pd.ExcelWriter(os.path.join(io.LOCAL_PATH, file_name))

    if fmt.location:
        try:
            df_mfcst = io.download_csv(q_name='Qmfcst-mo', datalake_path=io.results_path, date_cols=['Date']) \
                         .sort_values(by=['Date'], ascending=False) \
                         .set_index('Date') \
                         .to_excel(excel_handler, 'Qmfcst-mo')
        except:
            df_fcst = io.download_csv(q_name='Qfcst', datalake_path=io.results_path, date_cols=['Date']) \
                        .sort_values(by=['Date'], ascending=False) \
                        .set_index('Date') \
                        .to_excel(excel_handler, 'Qfcst')
        # Multiforecast monthly
        if fmt.dataset_frequency == 'W':
            try:
                df_mfcst_m = io.download_csv(q_name='Qmfcst-mo', datalake_path=io.results_path, date_cols=['Date']) \
                               .sort_values(by=['Date'], ascending=True) \
                               .set_index('Date') \
                               .to_excel(excel_handler, 'Qmfcst-mo')
            except:
                df_mfcst = io.download_csv(q_name='Qfcst-upsample', datalake_path=io.results_path, date_cols=['Date']) \
                             .sort_values(by=['Date'], ascending=True) \
                             .set_index('Date') \
                             .to_excel(excel_handler, 'Qfcst-mo')
    else:
        try:
            df_mfcst = io.download_csv(q_name='Qmfcst-mo', datalake_path=io.results_path, date_cols=['Date'])\
                         .sort_values(by=['Date'], ascending=False) \
                         .set_index('Date') \
                         .to_excel(excel_handler, 'Qmfcst-mo')
        except:
            df_fcst = io.download_csv(q_name='Qfcst', datalake_path=io.results_path, date_cols=['Date']) \
                        .sort_values(by=['Date'], ascending=False) \
                        .set_index('Date') \
                        .to_excel(excel_handler, 'Qfcst')
        # Multiforecast monthly
        if fmt.dataset_frequency == 'W':
            try:
                df_mfcst_m = io.download_csv(q_name='Qmfcst-mo', datalake_path=io.results_path, date_cols=['Date']) \
                               .sort_values(by=[ 'Date'], ascending=False) \
                               .set_index('Date') \
                               .to_excel(excel_handler, 'Qmfcst-mo')
            except:
                df_mfcst = io.download_csv(q_name='Qfcst-upsample', datalake_path=io.results_path, date_cols=['Date']) \
                             .sort_values(by=['Date'], ascending=False) \
                             .set_index('Date') \
                             .to_excel(excel_handler, 'Qfcst-mo')
    # Qrank
    if fmt.export_item_ranking:
        df_rank = io.download_csv(q_name='Qrank', datalake_path=io.results_path) \
                    .sort_values(by=['Ranking'], ascending=True) \
                    .set_index('Item') \
                    .to_excel(excel_handler, 'Qrank')

    if fmt.sku_impct:
        impct, corr, causal = {}, {}, {}
        for index, item in enumerate(fmt.sku_impct):
            impct[index] = io.download_csv(q_name='Qimpct',
                                           datalake_path=io.results_path + "/importancia/" + normalization(item))
            impct[index] = impct[index].round(2)
            impct[index].columns = ["Item", (normalization(item))]
            corr[index] = io.download_csv(q_name='Qcorrelation',
                                          datalake_path=io.results_path + "/importancia/" + normalization(item))
            causal[index] = io.download_csv(q_name='Qcausal',
                                            datalake_path=io.results_path + "/importancia/" + normalization(item))
            causal[index].columns = ["item_id", "Causality_" + normalization(item)]
        pd.concat(impct, axis=1).to_excel(excel_handler, 'Qimportance')
        pd.concat(corr, axis=1).to_excel(excel_handler, 'Qcorrelation')
        pd.concat(causal, axis=1).to_excel(excel_handler, 'Qcausality')

    excel_handler.save()
    io.upload_object(datalake_name=io.sftp_export, object_name=file_name)
    io.logger.debug('Results export completed...')
    io.upload_log()

    # Microservice response
    response = {
        'ConfigFileUri': os.path.join('s3://', io.datalake, io.config_path, 'config.yml')
    }
    io.upload_json_file(message=response, json_name='export_response', datalake_path=io.response_path)

if __name__ == '__main__':
    main()
    sys.exit(0)



