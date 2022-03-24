"""
    Storage utility methods

    methods include
    --------------------------
    1. check_if_cloud_storage_and_extract_path
    2. write_txt_to_s3
    3. store_parquet_in_s3
"""
from urllib.parse import urlparse
import boto3
from botocore.client import Config
import pandas
import awswrangler as aw

def check_if_cloud_storage_and_extract_path(path: str, schemes: list = ['s3']):
    """extracts bucket, path and scheme for select schemas or returns path otherwise

    Args:
        path (str): file path
        schemes (list, optional): schemas to extract from. Defaults to ['s3'].

    Returns:
        Tuple(str, str, str): bucket, filepath, scheme
    """
    parsed_url = urlparse(path)

    scheme = parsed_url.scheme
    if scheme in schemes:

        bucket = parsed_url.netloc
        s3_path = parsed_url.path.lstrip('/')
        return bucket, s3_path, scheme

    else:
        return None, path, None

def write_txt_to_s3(storage_path, text):
    """write a txt file to s3

    Args:
        storage_path (str): full path to file in s3
        text (str): text dump / blob to write as txt
    """
    print(f"writing txt to s3 {storage_path}")
    content = text.encode()
    config = Config(
        connect_timeout=10,
        retries={'max_attempts': 3}
    )
    s3_client = boto3.client('s3', config=config)

    base_bucket, file_path, _ = check_if_cloud_storage_and_extract_path(storage_path)
    print(base_bucket, file_path)
    s3_client.put_object(Bucket=base_bucket, Key=file_path, Body=content)

def store_parquet_in_s3(
        body: dict
):
    """Store content in glue table, as parquet in s3, and optiionally re-run glue crawler

    Args:
        body (dict): configuration with required fields

    Raises:
        Exception: '`content` must be supplied'
        Exception: `stage_path`, `glue_database` and `glue_table` must be supplied to stage data
    """
    # pylint: disable=too-many-locals, broad-except, too-many-branches
    (
        content,
        stage_bucket, stage_base_path, stage_filename_prefix,
        glue_database, glue_table, glue_crawler

    ) = (
        body.get('content'),
        body.get('stage_bucket'),
        body.get('stage_base_path'),
        body.get('stage_filename_prefix', ''),
        body.get('glue_database'),
        body.get('glue_table'),
        body.get('glue_crawler')
    )

    if not content:
        raise Exception('`content` must be supplied')

    config = Config(
        connect_timeout=10,
        retries={'max_attempts': 3}
    )

    if stage_bucket and 'testing' not in stage_base_path:
        if not (stage_base_path and glue_database and glue_table):
            raise Exception(
                (
                    '`stage_path`, `glue_database` and `glue_table` '
                    'must be supplied for staging data'
                )
            )

        run_crawler = False

        if glue_crawler:
            # Check if the date partition already exists as we need to re-run the crawler
            # after the first file is placed in that partition
            s3_client = boto3.client('s3', config=config)
            response = s3_client.list_objects(
                Bucket=stage_bucket,
                Prefix=f"{stage_base_path}/{stage_filename_prefix}/"
            )

            if len(response.get('Contents', [])) == 0:
                run_crawler = True

        data_frame = pandas.DataFrame(content)

        aw.s3.to_parquet(
            df=data_frame,
            path=f"s3://{stage_bucket}/{stage_base_path}",
            mode="append",
            dataset=True,
            database=glue_database,
            table=glue_table,
            filename_prefix=f"{stage_filename_prefix}/"
        )

        print(f"Successfully stored staged data at s3://{stage_bucket}/{stage_base_path}/{stage_filename_prefix}/")

        if glue_crawler and run_crawler:
            print(f"Running crawler {glue_crawler}")

            try:
                glue_client = boto3.client('glue')
                glue_client.start_crawler(
                    Name=glue_crawler
                )
            except Exception as ex:
                print(f"Error while trying to start crawler {str(ex)}")
