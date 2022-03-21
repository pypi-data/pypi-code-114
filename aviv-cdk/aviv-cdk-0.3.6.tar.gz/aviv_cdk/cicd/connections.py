from constructs import Construct
from aws_cdk import (
    aws_codestarconnections,
    aws_ssm,
    CfnOutput
)


class GithubConnection(aws_codestarconnections.CfnConnection):
    def __init__(self, scope: Construct, id: str, connection_name: str, *, host_arn: str=None, provider_type: str='GitHub', tags: dict=None, ssm_parameter_prefix: str='/github/connections', **kwargs) -> None:
        super().__init__(scope, id, connection_name=connection_name, host_arn=host_arn, provider_type=provider_type, tags=tags)
        CfnOutput(
            self, "output",
            value=self.attr_connection_arn,
            description="Validate with Github [app connection](https://console.aws.amazon.com/codesuite/settings/connections)"
        )
        if ssm_parameter_prefix:
            aws_ssm.StringParameter(
                self, "ssm",
                string_value=self.attr_connection_arn,
                parameter_name=f"{ssm_parameter_prefix}/{connection_name}"
            )
