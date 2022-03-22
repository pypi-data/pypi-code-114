import json
import os
import sys
import time
import dask.dataframe as dd
import pandas as pd

from datupapi.extract.io import IO
from datupapi.prepare.format import Format
from datupapi.prepare.format_dask import FormatDask


def main():
    io = IO(config_file='config.yml', logfile='data_io', log_path='output/logs')
    ddfmt = FormatDask(config_file='config.yml', logfile='data_io', log_path='output/logs')

    io.logger.debug('Data extraction starting...')
    # df_xls = io.download_excel(q_name='Base de Datos CNCH_3.xlsx',
    #                            sheet_name='Venta 2015-2021',
    #                            datalake_path='dev/ramiro/as-is',
    #                            types={'Mes': str, 'Semana': str},
    #                            header_=0, num_records=10)
    df = io.download_csv(q_name='ventas2019', datalake_path='dev/ivan/as-is', date_cols=['ComprasVentas.Fecha'], types={'unidades': 'float64', 'precio venta': 'float64'}, decimal=',')
    ddf = dd.from_pandas(df, npartitions=6)
    df_res = ddfmt.resample_dataset(ddf,
                                    date_col_='ComprasVentas.Fecha',
                                    item_col_='Articulo.PLU',
                                    frequency_='W',
                                    agg_dict_={'unidades': 'sum', 'precio venta': 'sum'},
                                    meta_dict_={'unidades': 'float64', 'precio venta': 'float64'})
    df_res = ddfmt.resample_dataset_with_location(ddf, date_col_='ComprasVentas.Fecha',
                                                      item_col_='Articulo.PLU',
                                                      location_col_='ComprasVentas.Id_NumCentroCostos',
                                                      frequency_='W',
                                                      agg_dict_={'unidades': 'sum', 'precio venta': 'sum'},
                                                      meta_dict_={'unidades': 'float64', 'precio venta': 'float64'})

    io.upload_csv(df_xls,
                  q_name='Qraw',
                  datalake_path='dev/ramiro/output/sales')
    io.logger.debug('Data extraction completed...')
    io.upload_log()
    # Microservice response
    response = {
        'ConfigFileUri': os.path.join('s3://', io.datalake, io.config_path, 'config.yml')
    }
    io.upload_json_file(message=response, json_name='extract_response', datalake_path=io.response_path)


if __name__ == '__main__':
    main()
    sys.exit(0)