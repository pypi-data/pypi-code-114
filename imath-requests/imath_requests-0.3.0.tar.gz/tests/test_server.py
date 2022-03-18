"""
test_server.py
====================================
Unit testing for server module
"""

import unittest
from imath_requests.server import create_app
from imath_requests.request import Pose3D
from imath_requests.request import PartInspectionData
from imath_requests.request import ImageInspectionData
from imath_requests.request import DefectData, DefectType, MetaData
from imath_requests.request import post_data


class TestPartDataEndpoint(unittest.TestCase):
    """
    Unit testing for part data endpoint of app in Server module.

    """
    def setUp(self):
        self.endpoint = '/imath-rest-backend/part'
        app, _ = create_app({'TESTING': True})
        self.client = app.test_client()

    def test_get(self):
        self.client.get(self.endpoint, follow_redirects=True)

    def test_post(self):
        json_data = {
            "partId": "Part_I3DR_test_003",
            "source": "I3DR_test",
            "identifiedTime": 1647606457463.4841,
            "partData": [
                {
                    "key": "supplier",
                    "string": "I3DR"
                }
            ],
            "images": [
                {
                    "imageFileName": "I3DR_test_003.tif",
                    "capturedBy": "I3DR_test_camera",
                    "capturedTime": 1647606457463.4841,
                    "positionX": 0,
                    "positionY": 0,
                    "positionZ": 0,
                    "dimensionX": 5000,
                    "dimensionY": 1,
                    "dimensionZ": 0,
                    "defects": [
                        {
                            "defectType": {
                                "code": "315"
                            },
                            "identifiedBy": "I3DR_test_user",
                            "identifiedTime": 1647606457463.4841,
                            "positionX": 0, "positionY": 0,
                            "positionZ": 0, "dimensionX": 0,
                            "dimensionY": 0, "dimensionZ": 0
                        }
                    ]
                }
            ]}
        self.client.post(self.endpoint, data=json_data, follow_redirects=True)

    def test_post_data(self):
        inspection_time = 1647606457463.4841
        data_source = 'I3DR_test'
        identified_by = 'I3DR_test_user'
        captured_by = 'I3DR_test_camera'
        supplier = 'I3DR'
        part_id = 'Part_I3DR_test_003'
        image_name = "I3DR_test_003.tif"
        defect_code = "315"
        image_position = Pose3D(0, 0, 0)
        image_dimension = Pose3D(5000, 1, 0)
        defect_position = Pose3D(0, 0, 0)
        defect_dimension = Pose3D(5000, 1, 0)
        part_inspection_data = PartInspectionData(
            part_id, data_source, inspection_time,
            [
                ImageInspectionData(
                    image_name,
                    captured_by, inspection_time,
                    image_position, image_dimension,
                    [
                        DefectData(
                            DefectType(defect_code),
                            identified_by, inspection_time,
                            defect_position, defect_dimension)
                    ]
                )
            ],
            [
                MetaData("supplier", supplier)
            ]
        )
        resp = post_data(
            part_inspection_data, None, None, None,
            self.client)
        self.assertEqual(resp.status_code, 201)
