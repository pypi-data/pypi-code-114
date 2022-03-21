import requests
from constructs import Construct
from aws_cdk import CfnOutput
from aws_cdk import (
    aws_iam,
    aws_ssm
)


class SamlProvider(aws_iam.SamlProvider):
    def __init__(
            self,
            scope: Construct,
            id: str,
            name: str,
            metadata_document: aws_iam.SamlMetadataDocument=None,
            saml_metadata_url: str=None,
            saml_metadata_file: str=None,
            saml_metadata_document: str=None,
            ssm_parameter_name: str=None
            ) -> None:
        """Create an IAM SAML Identity Provider

        Args:
            scope (Construct): [description]
            id (str): [description]
            name (str): IAM idp Name
            idp_url (str, optional): [description]. Defaults to None.
            saml_metadata_document (str, optional): [description]. Defaults to None.
        """
        if saml_metadata_url and not saml_metadata_document:
            saml_metadata_document = self.from_url(url=saml_metadata_url)
        if saml_metadata_document:
            metadata_document = aws_iam.SamlMetadataDocument.from_xml(xml=saml_metadata_document)
        elif saml_metadata_file:
            metadata_document = aws_iam.SamlMetadataDocument.from_file(path=saml_metadata_file)
        if not metadata_document:
            raise AttributeError("Need saml_metadata_url or saml_metadata_document")

        super().__init__(
            scope, id,
            name=name,
            metadata_document=metadata_document
        )
        CfnOutput(self.stack, f"{self.node.id}-arn", value=self.saml_provider_arn)
        if ssm_parameter_name:
            # self.ssm_parameter_name = ssm_parameter_name
            aws_ssm.StringParameter(self.stack, f"{self.node.id}-ssm", string_value=self.saml_provider_arn, parameter_name=ssm_parameter_name)
            CfnOutput(self.stack, f"{self.node.id}-ssm-name", value=ssm_parameter_name)

    def from_url(self, url: str) -> str:
        resp = requests.get(url=url)
        return resp.text

def SamlFederatedPrincipal(federated: str) -> aws_iam.FederatedPrincipal:
    return aws_iam.FederatedPrincipal(
        federated=federated,
        conditions={
            'StringEquals': {'SAML:aud': 'https://signin.aws.amazon.com/saml'}
        },
        assume_role_action='sts:AssumeRoleWithSAML'
    )
