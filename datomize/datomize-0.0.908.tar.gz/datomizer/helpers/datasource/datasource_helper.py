import requests
import tempfile
from pathlib import Path
from typing import Tuple
from datomizer import Datomizer
from datomizer.utils import constants, general


def create_origin_private_datasource_put_presigned(datomizer: Datomizer, path: str) -> Tuple[int, str]:
    datasource = datomizer.get_response_json(requests.post, url=constants.MANAGEMENT_POST_ADD_ORIGIN_PRIVATE_DATASOURCE)
    put_presigned_response = datomizer.get_response_json(requests.get,
                                                         url=constants.MANAGEMENT_GET_PUT_PRESIGNED_URL,
                                                         url_params=[datasource[general.ID], path])
    return datasource[general.ID], put_presigned_response[general.URL]


def create_origin_private_datasource_from_path(datomizer: Datomizer, path: Path):
    datasource_id, put_presigned_url = create_origin_private_datasource_put_presigned(datomizer, path.name)
    upload_temp_file(path, put_presigned_url)
    return datasource_id


def create_origin_private_datasource_from_df(datomizer: Datomizer, df, name="temp") -> int:
    if not name.endswith(".csv"):
        name = name + ".csv"

    datasource_id, put_presigned_url = create_origin_private_datasource_put_presigned(datomizer, name)
    upload_dataframe(put_presigned_url, df, name)
    return datasource_id


def create_target_private_datasource(datomizer: Datomizer) -> int:
    datasource = datomizer.get_response_json(requests.post, url=constants.MANAGEMENT_POST_ADD_TARGET_PRIVATE_DATASOURCE)
    return datasource[general.ID]


def upload_dataframe(presigned_url: str, df, name: str) -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        path = f"{temp_dir}/{name}"
        df_type = f"{type(df).__module__}.{type(df).__name__}"
        if df_type == "pandas.core.frame.DataFrame":
            df.to_csv(path)
        upload_temp_file(path, presigned_url)


def upload_temp_file(path, presigned_url):
    with open(path, 'r') as temp_file:
        header = {"Content-Type": "text/csv"}
        response = requests.put(url=presigned_url, data=temp_file, headers=header)
        Datomizer.validate_response(response, "Upload to put presigned url")
