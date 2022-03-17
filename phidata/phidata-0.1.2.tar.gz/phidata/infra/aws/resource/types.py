from collections import OrderedDict
from typing import Dict, List, Type, Union

from phidata.infra.aws.resource.base import AwsResource
from phidata.infra.aws.resource.acm.certificate import AcmCertificate
from phidata.infra.aws.resource.cloudformation import CloudFormationStack
from phidata.infra.aws.resource.eks.cluster import EksCluster
from phidata.infra.aws.resource.eks.fargate_profile import EksFargateProfile
from phidata.infra.aws.resource.eks.node_group import EksNodeGroup
from phidata.infra.aws.resource.iam.role import IamRole
from phidata.infra.aws.resource.iam.policy import IamPolicy
from phidata.infra.aws.resource.glue.crawler import GlueCrawlerResource
from phidata.infra.aws.resource.s3 import S3Bucket

# Use this as a type for an object which can hold any Aws Resource
AwsResourceType = Union[
    AcmCertificate,
    CloudFormationStack,
    EksCluster,
    EksFargateProfile,
    EksNodeGroup,
    IamRole,
    IamPolicy,
    GlueCrawlerResource,
    S3Bucket,
]

# Use this as an ordered list to iterate over all Aws Resource Classes
# This list is the order in which resources should be installed as well.
AwsResourceTypeList: List[Type[AwsResource]] = [
    IamRole,
    IamPolicy,
    S3Bucket,
    AcmCertificate,
    GlueCrawlerResource,
    CloudFormationStack,
    EksCluster,
    EksFargateProfile,
    EksNodeGroup,
]

# Map Aws resource alias' to their type
_aws_resource_type_names: Dict[str, Type[AwsResource]] = {
    aws_type.__name__.lower(): aws_type for aws_type in AwsResourceTypeList
}
_aws_resource_type_aliases: Dict[str, Type[AwsResource]] = {
    "s3": S3Bucket,
}

AwsResourceAliasToTypeMap: Dict[str, Type[AwsResource]] = dict(
    **_aws_resource_type_names, **_aws_resource_type_aliases
)

# Maps each AwsResource to an install weight
# lower weight AwsResource(s) get installed first
AwsResourceInstallOrder: Dict[str, int] = OrderedDict(
    {
        resource_type.__name__: idx
        for idx, resource_type in enumerate(AwsResourceTypeList, start=1)
    }
)
