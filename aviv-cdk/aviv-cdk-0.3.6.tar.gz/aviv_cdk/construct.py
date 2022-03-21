import json
import typing
from constructs import Construct
from aws_cdk import (
    CfnOutput
)

class SampleConstruct(Construct):
    config: dict

    def __init__(self, scope: Construct, id: str, *, config) -> None:
        super().__init__(scope, id)

        self.config = config
