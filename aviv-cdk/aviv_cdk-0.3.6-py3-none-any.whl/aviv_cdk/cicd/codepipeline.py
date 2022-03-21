from constructs import Construct
import typing
from aws_cdk import (
    Stack,
    Stage,
    aws_codestarconnections,
    pipelines
)
from connections import GithubConnection

class Stack(Stack):
    source: pipelines.CodePipelineSource
    codepipeline: pipelines.CodePipeline
    connection: aws_codestarconnections.CfnConnection
    waves: typing.Dict[str, pipelines.Wave]={}
    stages: typing.Dict[str, typing.Dict[str, Stage]]={}

    def __init__(self, scope: Construct, id: str, *, source: dict, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.connection = GithubConnection(self, 'connection', connection_name=f"{id}-connection")
        self.source = pipelines.CodePipelineSource.connection(
            connection_arn=self.connection.attr_connection_arn,
            **source
        )
        self.codepipeline = pipelines.CodePipeline(
            self, 'cdkp',
            self_mutation=False,
            cross_account_keys=True,
            synth=pipelines.ShellStep(
                'Synth',
                commands=[
                    'pip install aws-cdk-lib',
                    'npm install -g aws-cdk',
                    'cdk synth'
                ],
                input=self.source
            )
        )
