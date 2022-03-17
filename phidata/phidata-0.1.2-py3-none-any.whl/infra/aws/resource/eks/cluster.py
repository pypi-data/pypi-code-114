from pathlib import Path
from textwrap import dedent
from typing import Optional, Any, Dict, List, Union

from botocore.exceptions import ClientError

from phidata.infra.aws.api_client import AwsApiClient
from phidata.infra.aws.resource.base import AwsResource
from phidata.infra.aws.resource.iam.role import IamRole
from phidata.infra.aws.resource.cloudformation import CloudFormationStack
from phidata.utils.cli_console import print_info, print_error
from phidata.utils.log import logger


class EksCluster(AwsResource):
    """
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html
    """

    resource_type = "EksCluster"
    service_name = "eks"

    # The unique name to give to your cluster.
    name: str
    # version: The desired Kubernetes version for your cluster.
    # If you don't specify a value here, the latest version available in Amazon EKS is used.
    version: Optional[str] = None

    # role: The IAM role that provides permissions for the Kubernetes control plane to make calls
    # to Amazon Web Services API operations on your behalf.
    # If role is None, a default role is created using role_name
    role: Optional[IamRole] = None
    # Name for the default role when role is None, use "name-role" if not provided
    role_name: Optional[str] = None

    # resources_vpc_config: The VPC configuration that's used by the cluster control plane.
    # Amazon EKS VPC resources have specific requirements to work properly with Kubernetes.
    # You must specify at least two subnets. You can specify up to five security groups.
    # If resources_vpc_config is None, a default CloudFormationStack is created and
    # the vpc_config from that stack is used.
    resources_vpc_config: Optional[Dict[str, Union[List[str], bool]]] = None
    # The CloudFormationStack to build resources_vpc_config if provided
    vpc_stack: Optional[CloudFormationStack] = None
    # If resources_vpc_config and vpc_stack are None
    # create a default CloudFormationStack using vpc_stack_name, use "name-vpc-stack" if vpc_stack_name is None
    vpc_stack_name: Optional[str] = None
    vpc_stack_template_url: str = "https://amazon-eks.s3.us-west-2.amazonaws.com/cloudformation/2020-10-29/amazon-eks-vpc-private-subnets.yaml"

    # The Kubernetes network configuration for the cluster.
    kubernetes_network_config: Optional[Dict[str, str]] = None
    # Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs.
    # By default, cluster control plane logs aren't exported to CloudWatch Logs.
    logging: Optional[Dict[str, List[dict]]] = None
    # Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
    client_request_token: Optional[str] = None
    # The metadata to apply to the cluster to assist with categorization and organization.
    # Each tag consists of a key and an optional value. You define both.
    tags: Optional[Dict[str, str]] = None
    # The encryption configuration for the cluster.
    encryption_config: Optional[
        List[Dict[str, Union[List[str], Dict[str, str]]]]
    ] = None

    skip_delete = False
    # bump the wait time for Eks to 30 seconds
    waiter_delay = 30
    # If True, updates the kubeconfig
    update_kubeconfig: bool = True
    # The kubeconfig_path to update
    kubeconfig_path: Path = Path.home().joinpath(".kube").joinpath("config").resolve()
    kubeconfig_cluster_name: Optional[str] = None
    kubeconfig_cluster_user: Optional[str] = None
    kubeconfig_cluster_context: Optional[str] = None

    def _create(self, aws_client: AwsApiClient) -> bool:
        """Creates the EksCluster

        Args:
            aws_client: The AwsApiClient for the current cluster
        """

        logger.debug(
            "Creating {} | {}".format(
                self.get_resource_type(), self.get_resource_name()
            )
        )
        try:
            # Create the IamRole
            eks_iam_role = self.get_eks_iam_role()
            try:
                print_info(f"Creating IamRole: {eks_iam_role.name}")
                eks_iam_role.create(aws_client)
                eks_iam_role_arn = eks_iam_role.read(aws_client).arn
                logger.debug(f"eks_iam_role_arn: {eks_iam_role_arn}")
            except Exception as e:
                print_error("IamRole creation failed, please try again")
                print_error(e)
                return False

            # Create the CloudFormationStack and resources_vpc_config
            vpc_stack = self.get_eks_vpc_stack()
            try:
                print_info(f"Creating Stack: {vpc_stack.name}")
                vpc_stack.create(aws_client)
                resources_vpc_config = self.get_eks_resources_vpc_config(
                    aws_client, vpc_stack
                )
            except Exception as e:
                print_error("Stack creation failed, please try again")
                print_error(e)
                return False

            # Generate create_cluster_args
            non_null_create_cluster_args = {}
            # create a dict of args which are not null, otherwise aws type validation fails
            if self.version:
                non_null_create_cluster_args["version"] = self.version
            if self.kubernetes_network_config:
                non_null_create_cluster_args[
                    "kubernetesNetworkConfig"
                ] = self.kubernetes_network_config
            if self.logging:
                non_null_create_cluster_args["logging"] = self.logging
            if self.client_request_token:
                non_null_create_cluster_args[
                    "clientRequestToken"
                ] = self.client_request_token
            if self.tags:
                non_null_create_cluster_args["tags"] = self.tags
            if self.encryption_config:
                non_null_create_cluster_args[
                    "encryptionConfig"
                ] = self.encryption_config

            ## Create Cluster
            # Get the service_client
            service_client = self.get_service_client(aws_client)
            # logger.debug(f"ServiceClient: {service_client}")
            # logger.debug(f"ServiceClient type: {type(service_client)}")
            try:
                print_info(f"Creating EksCluster: {self.name}")
                create_cluster_response = service_client.create_cluster(
                    name=self.name,
                    roleArn=eks_iam_role_arn,
                    resourcesVpcConfig=resources_vpc_config,
                    **non_null_create_cluster_args,
                )
                # logger.debug(f"EksCluster: {create_cluster_response}")
                # logger.debug(f"EksCluster type: {type(create_cluster_response)}")

                ## Validate Cluster creation
                creation_time = create_cluster_response.get("cluster", {}).get(
                    "createdAt", None
                )
                cluster_status = create_cluster_response.get("cluster", {}).get(
                    "status", None
                )
                logger.debug(f"creation_time: {creation_time}")
                logger.debug(f"cluster_status: {cluster_status}")
                if creation_time is not None:
                    print_info(f"EksCluster created: {self.name}")
                    self.active_resource = create_cluster_response
                    return True
            except Exception as e:
                print_error(
                    "EksCluster could not be created, this operation is known to be buggy."
                )
                print_error("Please deploy the workspace again.")
                print_error(e)
                return False
        except Exception as e:
            print_error(
                f"Received error while creating {self.get_resource_type()}, this operation is known to be buggy."
            )
            print_error("Please try again.")
            print_error(e)
        return False

    def post_create(self, aws_client: AwsApiClient) -> bool:
        ## Wait for Cluster to be created
        if self.wait_for_completion:
            try:
                print_info(
                    "Waiting for EksCluster to be created, this can take up to 10 minutes"
                )
                waiter = self.get_service_client(aws_client).get_waiter(
                    "cluster_active"
                )
                waiter.wait(
                    name=self.name,
                    WaiterConfig={
                        "Delay": self.waiter_delay,
                        "MaxAttempts": self.waiter_max_attempts,
                    },
                )
            except Exception as e:
                print_error(
                    f"Received error while waiting for {self.get_resource_type()} creation, this operation is known to be buggy."
                )
                print_error("Please try again.")
                print_error(e)
                return False

        # Update kubeconfig if needed
        if self.update_kubeconfig:
            self.load_kubeconfig(aws_client)
        return True

    def _read(self, aws_client: AwsApiClient) -> Optional[Any]:
        """Returns the EksCluster

        Args:
            aws_client: The AwsApiClient for the current cluster
        """
        logger.debug(
            "Reading {} {}".format(self.get_resource_type(), self.get_resource_name())
        )
        try:
            service_client = self.get_service_client(aws_client)
            describe_cluster_response = service_client.describe_cluster(name=self.name)
            # logger.debug(f"EksCluster: {describe_cluster_response}")
            # logger.debug(f"EksCluster type: {type(describe_cluster_response)}")

            creation_time = describe_cluster_response.get("cluster", {}).get(
                "createdAt", None
            )
            cluster_status = describe_cluster_response.get("cluster", {}).get(
                "status", None
            )
            logger.debug(f"EksCluster creation_time: {creation_time}")
            logger.debug(f"EksCluster status: {cluster_status}")
            if creation_time is not None:
                logger.debug(f"EksCluster found: {self.name}")
                self.active_resource = describe_cluster_response
        except ClientError as ce:
            logger.debug(f"ClientError: {ce}")
            pass
        except Exception as e:
            print_error(f"Received error while reading {self.get_resource_type()}.")
            print_error("Please try again.")
            print_error(e)
        return self.active_resource

    def _delete(self, aws_client: AwsApiClient) -> bool:
        """Deletes the EksCluster
        Deletes the Amazon EKS cluster control plane.
        If you have active services in your cluster that are associated with a load balancer,
        you must delete those services before deleting the cluster so that the load balancers
        are deleted properly. Otherwise, you can have orphaned resources in your VPC
        that prevent you from being able to delete the VPC.

        Args:
            aws_client: The AwsApiClient for the current cluster
        """

        logger.debug(
            "Deleting {} | {}".format(
                self.get_resource_type(), self.get_resource_name()
            )
        )
        try:
            # Delete the IamRole
            eks_iam_role = self.get_eks_iam_role()
            try:
                print_info(f"Deleting IamRole: {eks_iam_role.name}")
                eks_iam_role.delete(aws_client)
            except Exception as e:
                print_error(
                    "IamRole deletion failed, please try again or delete manually"
                )
                print_error(e)

            # Delete the CloudFormationStack if needed
            resources_vpc_config = self.resources_vpc_config
            if resources_vpc_config is None:
                # indicated vpc stack is created by this cluster
                vpc_stack = self.get_eks_vpc_stack()
                try:
                    print_info(f"Deleting Stack: {vpc_stack.name}")
                    vpc_stack.delete(aws_client)
                except Exception as e:
                    print_error(
                        "Stack deletion failed, please try again or delete manually"
                    )
                    print_error(e)

            # Delete the EksCluster
            service_client = self.get_service_client(aws_client)
            self.active_resource = None
            self.active_resource_class = None
            delete_cluster_response = service_client.delete_cluster(name=self.name)
            # logger.debug(f"EksCluster: {delete_cluster_response}")
            # logger.debug(f"EksCluster type: {type(delete_cluster_response)}")
            print_info(f"EksCluster deleted: {self.name}")
            return True
        except Exception as e:
            print_error(
                f"Received error while deleting {self.get_resource_type()}, this operation is known to be buggy."
            )
            print_error("Please try again or delete resources manually.")
            print_error(e)
        return False

    def post_delete(self, aws_client: AwsApiClient) -> bool:
        ## Wait for Cluster to be deleted
        if self.wait_for_deletion:
            try:
                print_info(
                    "Waiting for EksCluster to be deleted, this can take up to 10 minutes"
                )
                waiter = self.get_service_client(aws_client).get_waiter(
                    "cluster_deleted"
                )
                waiter.wait(
                    name=self.name,
                    WaiterConfig={
                        "Delay": self.waiter_delay,
                        "MaxAttempts": self.waiter_max_attempts,
                    },
                )
            except Exception as e:
                print_error(
                    f"Received error while waiting for {self.get_resource_type()} deletion, this operation is known to be buggy."
                )
                print_error("Please try again.")
                print_error(e)

        # Update kubeconfig if needed
        if self.update_kubeconfig:
            return self.clean_kubeconfig(aws_client)
        return True

    def get_eks_iam_role(self) -> IamRole:
        if self.role is not None:
            return self.role
        return IamRole(
            name=self.role_name or f"{self.name}-role",
            assume_role_policy_document=dedent(
                """\
            {
              "Version": "2012-10-17",
              "Statement": [
                {
                  "Effect": "Allow",
                  "Principal": {
                    "Service": "eks.amazonaws.com"
                  },
                  "Action": "sts:AssumeRole"
                }
              ]
            }
            """
            ),
            policy_arns=["arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"],
        )

    def get_eks_vpc_stack(self) -> CloudFormationStack:
        if self.vpc_stack is not None:
            return self.vpc_stack
        return CloudFormationStack(
            name=self.vpc_stack_name or f"{self.name}-vpc-stack",
            template_url=self.vpc_stack_template_url,
        )

    def get_eks_resources_vpc_config(
        self, aws_client: AwsApiClient, vpc_stack: CloudFormationStack
    ) -> Dict[str, Union[List[str], bool]]:
        if self.resources_vpc_config is not None:
            return self.resources_vpc_config

        # Build resources_vpc_config using vpc_stack
        # get the VPC physical_resource_id
        # vpc_stack_resource = vpc_stack.get_stack_resource(aws_client, "VPC")
        # vpc_physical_resource_id = (
        #     vpc_stack_resource.physical_resource_id
        #     if vpc_stack_resource is not None
        #     else None
        # )
        # # logger.debug(f"vpc_physical_resource_id: {vpc_physical_resource_id}")

        # get the ControlPlaneSecurityGroup physical_resource_id
        sg_stack_resource = vpc_stack.get_stack_resource(
            aws_client, "ControlPlaneSecurityGroup"
        )
        sg_physical_resource_id = (
            sg_stack_resource.physical_resource_id
            if sg_stack_resource is not None
            else None
        )
        # logger.debug(f"sg_physical_resource_id: {sg_physical_resource_id}")

        private_subnets: Optional[List[str]] = vpc_stack.get_private_subnets(aws_client)
        public_subnets: Optional[List[str]] = vpc_stack.get_public_subnets(aws_client)
        subnet_ids: List[str] = []
        if private_subnets is not None:
            subnet_ids.extend(private_subnets)
        if public_subnets is not None:
            subnet_ids.extend(public_subnets)

        resources_vpc_config = {
            "subnetIds": subnet_ids,
            "securityGroupIds": [sg_physical_resource_id],
        }
        return resources_vpc_config

    def get_kubeconfig_cluster_name(self) -> str:
        return self.kubeconfig_cluster_name or f"{self.name}-eks"

    def get_kubeconfig_user_name(self) -> str:
        return self.kubeconfig_cluster_user or f"{self.name}-eks"

    def get_kubeconfig_context_name(self) -> str:
        return self.kubeconfig_cluster_context or f"{self.name}-eks"

    def load_kubeconfig(self, aws_client: AwsApiClient) -> None:
        eks_cluster = self._read(aws_client)
        # logger.debug(f"EksCluster: {eks_cluster}")
        # logger.debug(f"EksCluster type: {type(eks_cluster)}")

        try:
            cluster_cert = (
                eks_cluster.get("cluster", {})
                .get("certificateAuthority", {})
                .get("data", None)
            )
            # logger.debug(f"cluster_cert: {cluster_cert}")
            cluster_endpoint = eks_cluster.get("cluster", {}).get("endpoint", None)
            # logger.debug(f"cluster_endpoint: {cluster_endpoint}")
            cluster_arn = eks_cluster.get("cluster", {}).get("arn", None)
            # logger.debug(f"cluster_arn: {cluster_arn}")
        except Exception as e:
            print_error(f"Cannot read EKSCluster")
            print_error(e)
            return

        import yaml
        from phidata.infra.k8s.enums.api_version import ApiVersion
        from phidata.infra.k8s.enums.kind import Kind
        from phidata.infra.k8s.resource.kubeconfig import (
            Kubeconfig,
            KubeconfigCluster,
            KubeconfigClusterConfig,
            KubeconfigContext,
            KubeconfigContextSpec,
            KubeconfigUser,
        )

        kubeconfig: Optional[Kubeconfig] = None
        new_cluster = KubeconfigCluster(
            name=self.get_kubeconfig_cluster_name(),
            cluster=KubeconfigClusterConfig(
                server=str(cluster_endpoint),
                certificate_authority_data=str(cluster_cert),
            ),
        )
        new_user = KubeconfigUser(
            name=self.get_kubeconfig_user_name(),
            user={
                "exec": {
                    "apiVersion": ApiVersion.CLIENT_AUTHENTICATION_V1ALPHA1.value,
                    "command": "aws",
                    "args": [
                        "eks",
                        "get-token",
                        "--cluster-name",
                        self.name,
                    ],
                }
            },
        )
        new_context = KubeconfigContext(
            name=self.get_kubeconfig_context_name(),
            context=KubeconfigContextSpec(
                cluster=new_cluster.name,
                user=new_user.name,
            ),
        )
        current_context = new_context.name
        cluster_config: KubeconfigCluster

        # If write_kubeconfig = False, then no changes to kubeconfig needed
        write_kubeconfig = False
        if (
            self.kubeconfig_path is not None
            and self.kubeconfig_path.exists()
            and self.kubeconfig_path.is_file()
        ):
            try:
                print_info(f"Reading kubeconfig at {self.kubeconfig_path}")
                kubeconfig_dict = yaml.safe_load(self.kubeconfig_path.read_text())

                kubeconfig = Kubeconfig(**kubeconfig_dict)

                # Update Kubeconfig.clusters:
                # If a cluster with the same name exists in Kubeconfig.clusters -
                #   check if server and cert values match, if not, remove the existing cluster
                #   and add the new cluster config. Mark cluster_config_exists = True
                # If a cluster with the same name does not exist in Kubeconfig.clusters -
                #   add the new cluster config
                cluster_config_exists = False
                for idx, _cluster in enumerate(kubeconfig.clusters, start=0):
                    if _cluster.name == new_cluster.name:
                        cluster_config_exists = True
                        if (
                            _cluster.cluster.server != new_cluster.cluster.server
                            or _cluster.cluster.certificate_authority_data
                            != new_cluster.cluster.certificate_authority_data
                        ):
                            logger.debug(
                                "Kubeconfig.cluster mismatch, updating cluster config"
                            )
                            removed_cluster_config = kubeconfig.clusters.pop(idx)
                            # logger.debug(
                            #     f"removed_cluster_config: {removed_cluster_config}"
                            # )
                            kubeconfig.clusters.append(new_cluster)
                            write_kubeconfig = True
                if not cluster_config_exists:
                    logger.debug("Adding Kubeconfig.cluster")
                    kubeconfig.clusters.append(new_cluster)
                    write_kubeconfig = True

                # Update Kubeconfig.users:
                # If a user with the same name exists in Kubeconfig.users -
                #   check if user spec matches, if not, remove the existing user
                #   and add the new user config. Mark user_config_exists = True
                # If a user with the same name does not exist in Kubeconfig.users -
                #   add the new user config
                user_config_exists = False
                for idx, _user in enumerate(kubeconfig.users, start=0):
                    if _user.name == new_user.name:
                        user_config_exists = True
                        if _user.user != new_user.user:
                            logger.debug(
                                "Kubeconfig.user mismatch, updating user config"
                            )
                            removed_user_config = kubeconfig.users.pop(idx)
                            # logger.debug(f"removed_user_config: {removed_user_config}")
                            kubeconfig.users.append(new_user)
                            write_kubeconfig = True
                if not user_config_exists:
                    logger.debug("Adding Kubeconfig.user")
                    kubeconfig.users.append(new_user)
                    write_kubeconfig = True

                # Update Kubeconfig.contexts:
                # If a context with the same name exists in Kubeconfig.contexts -
                #   check if context spec matches, if not, remove the existing context
                #   and add the new context. Mark context_config_exists = True
                # If a context with the same name does not exist in Kubeconfig.contexts -
                #   add the new context config
                context_config_exists = False
                for idx, _context in enumerate(kubeconfig.contexts, start=0):
                    if _context.name == new_context.name:
                        context_config_exists = True
                        if _context.context != new_context.context:
                            logger.debug(
                                "Kubeconfig.context mismatch, updating context config"
                            )
                            removed_context_config = kubeconfig.contexts.pop(idx)
                            # logger.debug(
                            #     f"removed_context_config: {removed_context_config}"
                            # )
                            kubeconfig.contexts.append(new_context)
                            write_kubeconfig = True
                if not context_config_exists:
                    logger.debug("Adding Kubeconfig.context")
                    kubeconfig.contexts.append(new_context)
                    write_kubeconfig = True

                if (
                    kubeconfig.current_context is None
                    or kubeconfig.current_context != current_context
                ):
                    logger.debug("Updating Kubeconfig.current_context")
                    kubeconfig.current_context = current_context
                    write_kubeconfig = True
            except Exception as e:
                print_error(f"Cannot update kubeconfig at {self.kubeconfig_path}")
                print_error(e)
                kubeconfig = None

        # Create new kubeconfig
        if kubeconfig is None:
            print_info(f"Creating new kubeconfig")
            kubeconfig = Kubeconfig(
                api_version=ApiVersion.CORE_V1,
                kind=Kind.CONFIG,
                clusters=[new_cluster],
                users=[new_user],
                contexts=[new_context],
                current_context=current_context,
            )
            write_kubeconfig = True

        # if kubeconfig:
        #     logger.debug("Kubeconfig:\n{}".format(kubeconfig.json(exclude_none=True, by_alias=True, indent=4)))
        if write_kubeconfig:
            try:
                print_info("Writing kubeconfig")
                kubeconfig_dict = kubeconfig.dict(exclude_none=True, by_alias=True)
                self.kubeconfig_path.write_text(yaml.safe_dump(kubeconfig_dict))
                print_info("Kubeconfig updated")
            except Exception as e:
                print_error(f"Cannot write to {self.kubeconfig_path}")
                print_error(e)
        else:
            print_info("Kubeconfig up-to-date")

    def clean_kubeconfig(self, aws_client: AwsApiClient) -> bool:
        logger.debug(f"TO_DO: Cleaning kubeconfig at {str(self.kubeconfig_path)}")
