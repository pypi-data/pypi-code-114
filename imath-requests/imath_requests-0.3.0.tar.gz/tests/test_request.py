"""
test_request.py
====================================
Unit testing for request module
"""

import unittest
from imath_requests.request import Pose3D
from imath_requests.request import PartInspectionData
from imath_requests.request import ImageInspectionData
from imath_requests.request import DefectData, DefectType, MetaData


class TestPose3D(unittest.TestCase):
    """
    Unit testing for Pose3D class in requests module.

    """
    def test_init_position(self):
        pose = Pose3D(44.2, 17.4, 0.0)
        assert(pose.x == 44.2)
        assert(pose.y == 17.4)
        assert(pose.z == 0.0)


class TestPartInspectionData(unittest.TestCase):
    """
    Unit testing for PartInspectionData class in requests module.

    """
    def test_init(self):
        """
        Test generation of part inspection data class
        """
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
        assert(part_inspection_data.id == part_id)
        assert(part_inspection_data.source == data_source)
        assert(part_inspection_data.timestamp == inspection_time)
        assert(len(part_inspection_data.images) == 1)
        image = part_inspection_data.images[0]
        assert(image.filename == image_name)
        assert(image.captured_by == captured_by)
        assert(image.timestamp == inspection_time)
        assert(image.position.x == image_position.x)
        assert(image.position.y == image_position.y)
        assert(image.position.z == image_position.z)
        assert(image.dimension.x == image_dimension.x)
        assert(image.dimension.y == image_dimension.y)
        assert(image.dimension.z == image_dimension.z)
        assert(len(image.defects) == 1)
        defect = image.defects[0]
        assert(defect.defect_type.code == defect_code)
        assert(defect.identified_by == identified_by)
        assert(defect.timestamp == inspection_time)
        assert(defect.position.x == defect_position.x)
        assert(defect.position.y == defect_position.y)
        assert(defect.position.z == defect_position.z)
        assert(defect.dimension.x == defect_dimension.x)
        assert(defect.dimension.y == defect_dimension.y)
        assert(defect.dimension.z == defect_dimension.z)
        assert(part_inspection_data.meta_datas[0].property == "supplier")
        assert(part_inspection_data.meta_datas[0].value == supplier)

    def test_json(self):
        """
        Tests part data json generation.

        """
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
        json_expected = {
            "partId": part_id,
            "source": data_source,
            "identifiedTime": inspection_time,
            "partData": [
                {
                    "key": "supplier",
                    "string": supplier
                }
            ],
            "images": [
                {
                    "imageFileName": image_name,
                    "capturedBy": captured_by,
                    "capturedTime": inspection_time,
                    "positionX": image_position.x,
                    "positionY": image_position.y,
                    "positionZ": image_position.z,
                    "dimensionX": image_dimension.x,
                    "dimensionY": image_dimension.y,
                    "dimensionZ": image_dimension.z,
                    "defects": [
                        {
                            "defectType": {
                                "code": defect_code
                            },
                            "identifiedBy": identified_by,
                            "identifiedTime": inspection_time,
                            "positionX": defect_position.x,
                            "positionY": defect_position.y,
                            "positionZ": defect_position.z,
                            "dimensionX": defect_dimension.x,
                            "dimensionY": defect_dimension.y,
                            "dimensionZ": defect_dimension.z,
                        }
                    ]
                }
            ]}
        part_inspection_data.to_json()
        assert(part_inspection_data.to_json() == json_expected)


if __name__ == '__main__':
    unittest.main()
