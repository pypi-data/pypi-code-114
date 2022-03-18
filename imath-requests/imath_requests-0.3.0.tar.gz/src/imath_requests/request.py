"""
request.py
====================================
Request handelling and data structures for interacting with iMath REST API
"""

import requests
import base64
from datetime import datetime, timezone
from abc import ABC, abstractmethod
from requests import Response


class RequestError(Exception):
    """Base class for other request exceptions"""
    pass


class ResponseError(RequestError):
    """Exception for bad response"""
    def __init__(self, response: Response):
        self.message = "Server responded with exception.\n"
        self.message += "Status Code: {}\n".format(response.status_code)
        json_data = response.json()
        if 'exceptionClass' in json_data and 'message' in json_data:
            self.message += "Exception: {}\n".format(
                json_data['exceptionClass'])
            self.message += "Message: {}\n".format(
                json_data['message'])
        else:
            self.message += "Description: {}".format(
                response.text)
        super().__init__(self.message)


class HttpRequestMethodNotSupportedError(ResponseError):
    """Exception for Http Request Method Not Supported"""
    @staticmethod
    def _server_class() -> str:
        return "org.springframework.web.HttpRequestMethodNotSupportedException"


class iMathResponseError(ResponseError):
    """Exception for bad response from iMath backend exceptions"""
    @staticmethod
    def _server_class_base() -> str:
        return "at.abf.research.imath.restbackend.exception"


class EntityExistsError(iMathResponseError):
    """Exception for entity already exists"""

    @staticmethod
    def _server_class() -> str:
        return \
            iMathResponseError._server_class_base() + ".EntityExistsException"


class RequestData(ABC):
    @abstractmethod
    def to_json(self) -> dict:
        # MUST be implimented by child class
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def from_json():
        # MUST be implimented by child class
        raise NotImplementedError

    def __str__(self) -> str:
        return str(self.to_json())


def _generate_server_header(username, password):
    """
    Get header for iMath REST API.

    Parameters
    ----------
    username : str
        username for iMath REST API
    password : str
        password for iMath REST API

    Returns
    -------
    dict
        header for iMath REST API

    """
    auth_string = "{}:{}".format(username, password)
    auth_string_b64 = base64.b64encode(auth_string.encode()).decode()
    return {
        "Authorization": "Basic {}".format(auth_string_b64)
    }


def _get_url(ip: str) -> str:
    return 'http://{}/imath-rest-backend/part'.format(ip)


def _response_exception(resp: Response):
    json_data = resp.json()
    if 'exceptionClass' in json_data and 'message' in json_data:
        exception_class_name = json_data['exceptionClass']
        exceptions = [
            HttpRequestMethodNotSupportedError,
            EntityExistsError]
        for exception in exceptions:
            if exception_class_name == exception._server_class():
                raise exception(resp)
    raise ResponseError(resp)


def post(json_data: dict, ip, username, password, client=None):
    url = _get_url(ip)
    if client is None:
        header = _generate_server_header(username, password)
        resp = requests.post(url, json=[json_data], headers=header)
    else:
        resp = client.post(url, json=[json_data])
    status_code = resp.status_code
    if (100 <= status_code and status_code <= 399):
        return resp
    else:
        _response_exception(resp)


def post_data(request_data: RequestData, ip, username, password, client=None):
    json_data = request_data.to_json()
    return post(json_data, ip, username, password, client)


# TODO get response
# def get(ip: str, username: str, password: str):
#         url = _get_url(ip)
#         header = _generate_server_header(username, password)
#         res = requests.get(url, headers=header)
#         status_code = res.status_code
#         if (100 <= status_code and status_code <= 399):
#             json = res.json()
#             return cls.from_json(json)
#         else:
#             _response_exception(res)


class Pose3D():
    """
    Pose 3D class.

    Store pose data as x, y, z

    Attributes
    ----------
    x: float
        X component of pose
    y: float
        Y component of pose
    z: float
        Z component of pose

    """

    def __init__(
            self, x: float, y: float, z: float):
        """
        Meta data construction.

        Parameters
        ----------
        x: float
            X component of pose
        y: float
            Y component of pose
        z: float
            Z component of pose

        """
        self.x = x
        self.y = y
        self.z = z


class MetaData(RequestData):
    """
    Meta data helper class.

    Includes addition functions creating json
    data from meta data for easy use in REST API.

    Attributes
    ----------
    property: str
        Name of meta data
    value: str/int/float
        value of meta data

    """

    __valid_types = [str, int, float]
    __type_names = ["string", "int", "float"]

    def __init__(
            self, property: str, value: any):
        """
        Meta data construction.

        Parameters
        ----------
        property: str
            Name of meta data
        value: str/int/float
            value of meta data

        """
        self.property = property
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if (type(value) not in MetaData.__valid_types):
            err_msg = "Invalid type for part property value. "
            err_msg += "MUST be str, int, or float."
            raise TypeError(err_msg)
        self._value = value
        iter = zip(MetaData.__valid_types, MetaData.__type_names)
        for valid_type, type_name in iter:
            if type(value) == valid_type:
                self.value_type = type_name
                break

    def to_json(self) -> dict:
        """
        Convert MetaData into json string for use in REST API.

        Returns
        -------
        dict
            Json formatted string

        """
        return {
            "key": self.property,
            self.value_type: self.value
        }

    @staticmethod
    def from_json(json_data: dict) -> 'MetaData':
        if 'key' not in json_data:
            raise ValueError("Invalid json for part property. Missing 'key'.")

        iter = zip(MetaData.__valid_types, MetaData.__type_names)
        for valid_types, type_name in iter:
            if type_name in json_data:
                return MetaData(
                    json_data['key'], valid_types(json_data[type_name]))


class DefectType(RequestData):
    """
    Defect data helper class.

    TODO: Add description

    Attributes
    ----------
    code : str
        defect code

    """

    def __init__(self, code: str):
        """
        Defect data helper class.

        Parameters
        ----------
        code : str
            defect code

        """
        self.code = code

    def to_json(self) -> dict:
        """
        Convert DefectType into json string for use in REST API.

        Returns
        -------
        dict
            Json formatted string

        """
        return {
            "code": self.code,
        }

    @staticmethod
    def from_json(json_data: str) -> 'DefectType':
        code = json_data['code']
        return DefectType(code)


class DefectData(RequestData):
    """
    Defect data helper class.

    TODO: Add description

    Attributes
    ----------
    defect_type : DefectType
        defect type
    identified_by : str
        Data source e.g. I3DR_DESKTOP_ABC123
    timestamp : str
        Timestamp e.g. 1516193959559
    position : Position
        Position of defect
    dimension : Dimension
        Dimension of defect

    """

    def __init__(
            self, defect_type: DefectType, identified_by: str, timestamp: str,
            position: Pose3D, dimension: Pose3D):
        """
        Image Inspection data helper class.

        Parameters
        ----------
        defect_type : DefectType
            defect type
        identified_by : str
            Data source e.g. I3DR_DESKTOP_ABC123
        timestamp : str
            Timestamp e.g. 1516193959559
        position : Position
            Position of defect
        dimension : Dimension
            Dimension of defect

        """
        self.defect_type = defect_type
        self.identified_by = identified_by
        self.timestamp = timestamp
        self.position = position
        self.dimension = dimension

    def to_json(self) -> dict:
        """
        Convert ImageInspectionData into json string for use in REST API.

        Returns
        -------
        dict
            Json formatted string

        """
        return {
            "defectType": self.defect_type.to_json(),
            "identifiedBy": self.identified_by,
            "identifiedTime": self.timestamp,
            "positionX": self.position.x,
            "positionY": self.position.y,
            "positionZ": self.position.z,
            "dimensionX": self.dimension.x,
            "dimensionY": self.dimension.y,
            "dimensionZ": self.dimension.z
        }

    @staticmethod
    def from_json(json_data: str) -> 'ImageInspectionData':
        defect_type = DefectType.from_json(json_data['defectType'])
        identified_by = json_data['identifiedBy']
        timestamp = json_data['identifiedTime']
        position = Pose3D(
            json_data['positionX'],
            json_data['positionY'],
            json_data['positionZ'])
        dimension = Pose3D(
            json_data['dimensionX'],
            json_data['dimensionY'],
            json_data['dimensionZ'])
        return DefectData(
            defect_type, identified_by, timestamp, position, dimension)


class ImageInspectionData(RequestData):
    """
    Image Inspection data helper class.

    TODO: Add description

    Attributes
    ----------
    filename : str
        Image filename
    captured_by : str
        Data source e.g. I3DR_DESKTOP_ABC123
    timestamp : str
        Timestamp e.g. 1516193959559
    position: Pose3D
        Position of defect
    dimension: Pose3D
        Dimension of defect
    defects: list
        List of DefectData

    """

    def __init__(
            self, filename: str, captured_by: str, timestamp: str,
            position: Pose3D, dimension: Pose3D, defects: list):
        """
        Image Inspection data helper class.

        Parameters
        ----------
        filename : str
            Image filename
        captured_by : str
            Data source e.g. I3DR_DESKTOP_ABC123
        timestamp : str
            Timestamp e.g. 1516193959559
        position: Pose3D
            Position of defect
        dimension: Pose3D
            Dimension of defect
        defects: list
            List of DefectData

        """
        self.filename = filename
        self.captured_by = captured_by
        self.timestamp = timestamp
        self.position = position
        self.dimension = dimension
        self.defects = defects

    def to_json(self) -> dict:
        """
        Convert ImageInspectionData into json string for use in REST API.

        Returns
        -------
        dict
            Json formatted string

        """
        defects_json_list = []
        for defect in self.defects:
            defects_json_list.append(defect.to_json())
        return {
            "imageFileName": self.filename,
            "capturedBy": self.captured_by,
            "capturedTime": self.timestamp,
            "positionX": self.position.x,
            "positionY": self.position.y,
            "positionZ": self.position.z,
            "dimensionX": self.dimension.x,
            "dimensionY": self.dimension.y,
            "dimensionZ": self.dimension.z,
            "defects": defects_json_list
        }

    @staticmethod
    def from_json(json_data: str) -> 'ImageInspectionData':
        filename = json_data['imageFileName']
        captured_by = json_data['capturedBy']
        timestamp = json_data['capturedTime']
        position = Pose3D(
            json_data['positionX'],
            json_data['positionY'],
            json_data['positionZ'])
        dimension = Pose3D(
            json_data['dimensionX'],
            json_data['dimensionY'],
            json_data['dimensionZ'])
        defects = []
        for defect in json_data['defects']:
            defects.append(DefectData.from_json(defect))
        return ImageInspectionData(
            filename, captured_by, timestamp, position, dimension, defects)


class PartInspectionData(RequestData):
    """
    Part Inspection data helper class.

    TODO: Add description

    Attributes
    ----------
    id : str
        Unique part ID e.g. Part1234
    source : str
        Data source e.g. I3DR_DESKTOP_ABC123
    timestamp : str
        Timestamp e.g. 1516193959559
    images: list
        List of ImageInspectionData
    meta_datas: list
        List of MetaData

    """

    def __init__(
            self, id: str, source: str, timestamp: str,
            images: list, meta_datas: list):
        """
        Image Meta Data construction.

        Parameters
        ----------
        id : str
            Unique part ID e.g. Part1234
        source : str
            Data source e.g. I3DR_DESKTOP_ABC123
        timestamp : str
            Timestamp e.g. 1516193959559
        images: list
            List of ImageInspectionData
        meta_datas: list
            List of MetaData

        """
        self.id = id
        self.source = source
        self.timestamp = timestamp
        self.images = images
        self.meta_datas = meta_datas

    def to_json(self) -> dict:
        """
        Convert InspectionData into json string for use in REST API.

        Returns
        -------
        dict
            Json formatted string

        """
        images_json_list = []
        for image in self.images:
            images_json_list.append(image.to_json())
        meta_data_json_list = []
        for meta_data in self.meta_datas:
            meta_data_json_list.append(meta_data.to_json())
        return {
            "partId": self.id,
            "source": self.source,
            "identifiedTime": self.timestamp,
            "partData": meta_data_json_list,
            "images": images_json_list
        }

    @staticmethod
    def from_json(json_data: str) -> 'PartInspectionData':
        id = json_data['partId']
        source = json_data['source']
        timestamp = json_data['identifiedTime']
        images = []
        for image in json_data['images']:
            images.append(ImageInspectionData.from_json(image))
        meta_datas = []
        for meta_data in json_data['partData']:
            meta_datas.append(MetaData.from_json(meta_data))
        return PartInspectionData(id, source, timestamp, images, meta_datas)


def timestamp(dt: datetime):
    return dt.replace(tzinfo=timezone.utc).timestamp() * 1000


if __name__ == "__main__":
    import os
    import json

    if 'IMATH_SERVER_IP' in os.environ:
        server_ip = os.environ['IMATH_SERVER_IP']
    else:
        server_ip = '127.0.0.1:5000'
    if 'IMATH_USERNAME' in os.environ:
        server_username = os.environ['IMATH_USERNAME']
    else:
        server_username = 'test'
    if 'IMATH_PASSWORD' in os.environ:
        server_password = os.environ['IMATH_PASSWORD']
    else:
        server_password = 'test'

    inspection_time = timestamp(datetime.now())
    data_source = 'I3DR_test'
    identified_by = 'I3DR_test_user'
    captured_by = 'I3DR_test_camera'
    supplier = 'I3DR'
    part_inspection_data = PartInspectionData(
        'Part_I3DR_test_003', data_source, inspection_time,
        [
            ImageInspectionData(
                "I3DR_test_003.tif",
                captured_by, inspection_time,
                Pose3D(0, 0, 0), Pose3D(5000, 1, 0),
                [
                    DefectData(
                        DefectType("315"), identified_by, inspection_time,
                        Pose3D(0, 0, 0), Pose3D(0, 0, 0))
                ]
            )
        ],
        [
            MetaData("supplier", supplier)
        ]
    )
    print(json.dumps(part_inspection_data.to_json()))
    resp = post_data(part_inspection_data,
                     server_ip, server_username, server_password)
    print(resp)
