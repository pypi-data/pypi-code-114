from enum import Enum


class ProblemType(Enum):
    """
    Possible project problem types.
    """

    Classification = "Classification"
    ObjectDetection = "ObjectDetection"
    SemanticSegmentation = "SemanticSegmentation"
    InstanceSegmentation = "InstanceSegmentation"
    ImageRegression = "ImageRegression"
    Keypoints = "Keypoints"

    @classmethod
    def has(cls, value):
        try:
            cls(value)
            return True
        except ValueError:
            return False
