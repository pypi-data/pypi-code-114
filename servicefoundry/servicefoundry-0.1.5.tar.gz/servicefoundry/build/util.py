import pkg_resources
import logging
import os
import shutil
import requests

logger = logging.getLogger()


def read_text(file_name, name=__name__):
    return pkg_resources.resource_string(name, file_name).decode("utf-8")


def clean_dir(dir_name):
    if os.path.isfile(dir_name):
        os.remove(dir_name)
    if os.path.isdir(dir_name):
        shutil.rmtree(dir_name)


def create_file_from_content(file_name, content):
    with open(file_name, "w") as text_file:
        text_file.write(content)


def upload_package_to_s3(metadata, package_file):
    with open(package_file, "rb") as file_to_upload:
        files = {"file": file_to_upload}
        http_response = requests.post(
            metadata["url"], data=metadata["fields"], files=files
        )

        if http_response.status_code not in [204, 201]:
            raise RuntimeError(f"Failed to upload to S3 {http_response.content}")
