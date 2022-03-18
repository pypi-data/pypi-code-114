import json
import requests
import tornado
import os
import tarfile

from io import BytesIO
from jupyter_server.base.handlers import APIHandler
import base64


TRANSFORM_NB_ROUTE = "TRANSFORM_NB"


def create_file_packet(nb_filename: str) -> dict:
    """Create a file packet for the transform docker container
    Args:
      filename: the name of the file to be sent to the transform docker container
    Returns:
      A dict that is the file packet for the transform docker container
    """
    f = open(nb_filename, "rb").read()
    data = {
        "file_name": nb_filename,
        "file_data": base64.b64encode(f).decode("utf-8"),
    }
    return data


def call_transform_nb(filename: str, api_key: str, domain: str) -> dict:
    """Call the transform docker container
    Args:
      filename: the name of the file to be sent to the transform docker container
    Returns:
      A dict that is the response from the transform docker container
    """
    data = create_file_packet(filename)

    response = requests.post(
        url=os.path.join("http://", domain, TRANSFORM_NB_ROUTE),
        json=data,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
        },
    )
    return response


class TransformJupyterRouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        self.finish(
            json.dumps(
                {"data": "This is /jlab-ext-example/TRANSFORM_NB endpoint!"})
        )

    @tornado.web.authenticated
    def post(self):
        # input_data is a dictionary with a key "name"
        input_data = self.get_json_body()

        nb_filename = input_data["name"]

        api_key, domain = input_data["apiKey"], input_data["transformDomain"]

        response = call_transform_nb(nb_filename, api_key, domain)
        json_response = response.json()

        if json_response.get("message") == "Limit Exceeded":
            self.finish(json.dumps({"message": "Limit Exceeded"}))
            return

        # get dirname of nb_filename
        dirname = os.path.dirname(nb_filename)
        # untar the tar file
        tar_file_content = base64.b64decode(json_response["tar_file_data"])

        # extract tar without writing to disk
        tar_file = tarfile.open(fileobj=BytesIO(tar_file_content), mode="r:gz")

        # save and extract to disk
        tar_file.extractall(path=dirname)

        self.finish(json.dumps("finish transformation"))
