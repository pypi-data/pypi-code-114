"""
Autogenerated state module using `pop-create-idem <https://gitlab.com/saltstack/pop/pop-create-idem>`__

hub.exec.boto3.client.ec2.bundle_instance
hub.exec.boto3.client.ec2.describe_instances
hub.exec.boto3.client.ec2.import_instance
hub.exec.boto3.client.ec2.monitor_instances
hub.exec.boto3.client.ec2.reboot_instances
hub.exec.boto3.client.ec2.run_instances
hub.exec.boto3.client.ec2.start_instances
hub.exec.boto3.client.ec2.stop_instances
hub.exec.boto3.client.ec2.terminate_instances
hub.exec.boto3.client.ec2.unmonitor_instances
resource = hub.tool.boto3.resource.create(ctx, "ec2", "Instance", name)
hub.tool.boto3.resource.exec(resource, attach_classic_link_vpc, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, attach_volume, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, console_output, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, create_image, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, create_tags, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, describe_attribute, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, detach_classic_link_vpc, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, detach_volume, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, modify_attribute, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, monitor, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, password_data, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, reboot, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, report_status, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, reset_attribute, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, reset_kernel, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, reset_ramdisk, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, reset_source_dest_check, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, start, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, stop, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, terminate, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, unmonitor, *args, **kwargs)
"""
import copy
from collections import OrderedDict
from typing import Any
from typing import Dict
from typing import List

__contracts__ = ["resource"]

TREQ = {
    "absent": {
        "require": [
            "aws.ec2.subnet.absent",
            "aws.iam.role.absent",
        ],
    },
    "present": {
        "require": [
            "aws.ec2.subnet.present",
            "aws.iam.role.present",
        ],
    },
}


async def present(
    hub,
    ctx,
    name: str,
    block_device_mappings: List = None,
    image_id: str = None,
    instance_type: str = None,
    ipv6_address_count: int = None,
    ipv6_addresses: List = None,
    kernel_id: str = None,
    key_name: str = None,
    monitoring: Dict = None,
    placement: Dict = None,
    ramdisk_id: str = None,
    security_group_ids: List = None,
    security_groups: List = None,
    subnet: str = None,
    user_data: str = None,
    additional_info: str = None,
    disable_api_termination: bool = None,
    ebs_optimized: bool = None,
    iam_instance_profile: Dict = None,
    instance_initiated_shutdown_behavior: str = None,
    network_interfaces: List = None,
    private_ip_address: str = None,
    elastic_gpu_specification: List = None,
    elastic_inference_accelerators: List = None,
    tags: Dict[str, str] = None,
    launch_template: Dict = None,
    instance_market_options: Dict = None,
    credit_specification: Dict = None,
    cpu_options: Dict = None,
    capacity_reservation_specification: Dict = None,
    hibernation_options: Dict = None,
    license_specifications: List = None,
    metadata_options: Dict = None,
    enclave_options: Dict = None,
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Launches the specified number of instances using an AMI for which you have permissions. You can specify a number
    of options, or leave the default options. The following rules apply:   [EC2-VPC] If you don't specify a subnet
    ID, we choose a default subnet from your default VPC for you. If you don't have a default VPC, you must specify
    a subnet ID in the request.   [EC2-Classic] If don't specify an Availability Zone, we choose one for you.   Some
    instance types must be launched into a VPC. If you do not have a default VPC, or if you do not specify a subnet
    ID, the request fails. For more information, see Instance types available only in a VPC.   [EC2-VPC] All
    instances have a network interface with a primary private IPv4 address. If you don't specify this address, we
    choose one from the IPv4 range of your subnet.   Not all instance types support IPv6 addresses. For more
    information, see Instance types.   If you don't specify a security group ID, we use the default security group.
    For more information, see Security groups.   If any of the AMIs have a product code attached for which the user
    has not subscribed, the request fails.   You can create a launch template, which is a resource that contains the
    parameters to launch an instance. When you launch an instance using RunInstances, you can specify the launch
    template instead of specifying the launch parameters. To ensure faster instance launches, break up large
    requests into smaller batches. For example, create five separate launch requests for 100 instances each instead
    of one launch request for 500 instances. An instance is ready for you to use when it's in the running state. You
    can check the state of your instance using DescribeInstances. You can tag instances and EBS volumes during
    launch, after launch, or both. For more information, see CreateTags and Tagging your Amazon EC2 resources. Linux
    instances have access to the public key of the key pair at boot. You can use this key to provide secure access
    to the instance. Amazon EC2 public images use this feature to provide secure access without passwords. For more
    information, see Key pairs. For troubleshooting, see What to do if an instance immediately terminates, and
    Troubleshooting connecting to your instance.

    Args:
        name(Text): A name, ID, or JMES search path to identify the resource.
        block_device_mappings(List, optional): The block device mapping entries. Defaults to None.
        image_id(Text, optional): The ID of the AMI. An AMI ID is required to launch an instance and must be specified here or in
            a launch template. Defaults to None.
        instance_type(Text, optional): The instance type. For more information, see Instance types in the Amazon EC2 User Guide.
            Default: m1.small. Defaults to None.
        ipv6_address_count(int, optional): [EC2-VPC] The number of IPv6 addresses to associate with the primary network interface. Amazon
            EC2 chooses the IPv6 addresses from the range of your subnet. You cannot specify this option and
            the option to assign specific IPv6 addresses in the same request. You can specify this option if
            you've specified a minimum number of instances to launch. You cannot specify this option and the
            network interfaces option in the same request. Defaults to None.
        ipv6_addresses(List, optional): [EC2-VPC] The IPv6 addresses from the range of the subnet to associate with the primary network
            interface. You cannot specify this option and the option to assign a number of IPv6 addresses in
            the same request. You cannot specify this option if you've specified a minimum number of
            instances to launch. You cannot specify this option and the network interfaces option in the
            same request. Defaults to None.
        kernel_id(Text, optional): The ID of the kernel.  We recommend that you use PV-GRUB instead of kernels and RAM disks. For
            more information, see  PV-GRUB in the Amazon EC2 User Guide. Defaults to None.
        key_name(Text, optional): The name of the key pair. You can create a key pair using CreateKeyPair or ImportKeyPair.  If
            you do not specify a key pair, you can't connect to the instance unless you choose an AMI that
            is configured to allow users another way to log in. Defaults to None.
        monitoring(Dict, optional): Specifies whether detailed monitoring is enabled for the instance. Defaults to None.
        placement(Dict, optional): The placement for the instance. Defaults to None.
        ramdisk_id(Text, optional): The ID of the RAM disk to select. Some kernels require additional drivers at launch. Check the
            kernel requirements for information about whether you need to specify a RAM disk. To find kernel
            requirements, go to the Amazon Web Services Resource Center and search for the kernel ID.  We
            recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see  PV-
            GRUB in the Amazon EC2 User Guide. Defaults to None.
        security_group_ids(List, optional): The IDs of the security groups. You can create a security group using CreateSecurityGroup. If
            you specify a network interface, you must specify any security groups as part of the network
            interface. Defaults to None.
        security_groups(List, optional): [EC2-Classic, default VPC] The names of the security groups. For a nondefault VPC, you must use
            security group IDs instead. If you specify a network interface, you must specify any security
            groups as part of the network interface. Default: Amazon EC2 uses the default security group. Defaults to None.
        subnet(Text, optional): [EC2-VPC] The ID of the subnet to launch the instance into. If you specify a network interface,
            you must specify any subnets as part of the network interface. Defaults to None.
        user_data(Text, optional): The user data to make available to the instance. For more information, see Running commands on
            your Linux instance at launch (Linux) and Adding User Data (Windows). If you are using a command
            line tool, base64-encoding is performed for you, and you can load the text from a file.
            Otherwise, you must provide base64-encoded text. User data is limited to 16 KB. Defaults to None.
        additional_info(Text, optional): Reserved. Defaults to None.
        disable_api_termination(bool, optional): If you set this parameter to true, you can't terminate the instance using the Amazon EC2
            console, CLI, or API; otherwise, you can. To change this attribute after launch, use
            ModifyInstanceAttribute. Alternatively, if you set InstanceInitiatedShutdownBehavior to
            terminate, you can terminate the instance by running the shutdown command from the instance.
            Default: false. Defaults to None.
        ebs_optimized(bool, optional): Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides
            dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal
            Amazon EBS I/O performance. This optimization isn't available with all instance types.
            Additional usage charges apply when using an EBS-optimized instance. Default: false. Defaults to None.
        iam_instance_profile(Dict, optional): The name or Amazon Resource Name (ARN) of an IAM instance profile. Defaults to None.
        instance_initiated_shutdown_behavior(Text, optional): Indicates whether an instance stops or terminates when you initiate shutdown from the instance
            (using the operating system command for system shutdown). Default: stop. Defaults to None.
        network_interfaces(List, optional): The network interfaces to associate with the instance. If you specify a network interface, you
            must specify any security groups and subnets as part of the network interface. Defaults to None.
        private_ip_address(Text, optional): [EC2-VPC] The primary IPv4 address. You must specify a value from the IPv4 address range of the
            subnet. Only one private IP address can be designated as primary. You can't specify this option
            if you've specified the option to designate a private IP address as the primary IP address in a
            network interface specification. You cannot specify this option if you're launching more than
            one instance in the request. You cannot specify this option and the network interfaces option in
            the same request. Defaults to None.
        elastic_gpu_specification(List, optional): An elastic GPU to associate with the instance. An Elastic GPU is a GPU resource that you can
            attach to your Windows instance to accelerate the graphics performance of your applications. For
            more information, see Amazon EC2 Elastic GPUs in the Amazon EC2 User Guide. Defaults to None.
        elastic_inference_accelerators(List, optional): An elastic inference accelerator to associate with the instance. Elastic inference accelerators
            are a resource you can attach to your Amazon EC2 instances to accelerate your Deep Learning (DL)
            inference workloads. You cannot specify accelerators from different generations in the same
            request. Defaults to None.
        tags(Dict, optional): The tags to apply to the resources during launch. You can only tag instances and volumes on
            launch. The specified tags are applied to all instances or volumes that are created during
            launch. To tag a resource after it has been created, see CreateTags. Defaults to None.
        launch_template(Dict, optional): The launch template to use to launch the instances. Any parameters that you specify in
            RunInstances override the same parameters in the launch template. You can specify either the
            name or ID of a launch template, but not both. Defaults to None.
        instance_market_options(Dict, optional): The market (purchasing) option for the instances. For RunInstances, persistent Spot Instance
            requests are only supported when InstanceInterruptionBehavior is set to either hibernate or
            stop. Defaults to None.
        credit_specification(Dict, optional): The credit option for CPU usage of the burstable performance instance. Valid values are standard
            and unlimited. To change this attribute after launch, use  ModifyInstanceCreditSpecification.
            For more information, see Burstable performance instances in the Amazon EC2 User Guide. Default:
            standard (T2 instances) or unlimited (T3/T3a instances). Defaults to None.
        cpu_options(Dict, optional): The CPU options for the instance. For more information, see Optimizing CPU options in the Amazon
            EC2 User Guide. Defaults to None.
        capacity_reservation_specification(Dict, optional): Information about the Capacity Reservation targeting option. If you do not specify this
            parameter, the instance's Capacity Reservation preference defaults to open, which enables it to
            run in any open Capacity Reservation that has matching attributes (instance type, platform,
            Availability Zone). Defaults to None.
        hibernation_options(Dict, optional): Indicates whether an instance is enabled for hibernation. For more information, see Hibernate
            your instance in the Amazon EC2 User Guide. You can't enable hibernation and Amazon Web Services
            Nitro Enclaves on the same instance. Defaults to None.
        license_specifications(List, optional): The license configurations. Defaults to None.
        metadata_options(Dict, optional): The metadata options for the instance. For more information, see Instance metadata and user
            data. Defaults to None.
        enclave_options(Dict, optional): Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves. For more
            information, see  What is Amazon Web Services Nitro Enclaves? in the Amazon Web Services Nitro
            Enclaves User Guide. You can't enable Amazon Web Services Nitro Enclaves and hibernation on the
            same instance. Defaults to None.

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            resource_is_present:
              aws.ec2.instance.present:
                - name: value
    """
    result = dict(comment="", old_state=None, new_state=None, name=name, result=True)
    resource = hub.tool.boto3.resource.create(ctx, "ec2", "Instance", name)
    before = await hub.tool.boto3.resource.describe(resource)
    if ctx.get("test", False):
        if before:
            result["comment"] = "Would update aws.ec2.instance"
            result["result"] = True
        else:
            result["comment"] = "Would create aws.ec2.instance"
            result["result"] = True
        return result

    if before:
        result["old_state"] = before
        result["comment"] = f"'{name}' already exists"
        # TODO perform Day2 operation as needed here
    else:
        try:
            ret = await hub.exec.boto3.client.ec2.run_instances(
                ctx,
                ClientToken=name,
                **{
                    "BlockDeviceMappings": block_device_mappings,
                    "ImageId": image_id,
                    "InstanceType": instance_type,
                    "Ipv6AddressCount": ipv6_address_count,
                    "Ipv6Addresses": ipv6_addresses,
                    "KernelId": kernel_id,
                    "KeyName": key_name,
                    "MaxCount": 1,
                    "MinCount": 1,
                    "Monitoring": monitoring,
                    "Placement": placement,
                    "RamdiskId": ramdisk_id,
                    "SecurityGroupIds": security_group_ids,
                    "SecurityGroups": security_groups,
                    "SubnetId": subnet,
                    "UserData": user_data,
                    "AdditionalInfo": additional_info,
                    "DisableApiTermination": disable_api_termination,
                    "EbsOptimized": ebs_optimized,
                    "IamInstanceProfile": iam_instance_profile,
                    "InstanceInitiatedShutdownBehavior": instance_initiated_shutdown_behavior,
                    "NetworkInterfaces": network_interfaces,
                    "PrivateIpAddress": private_ip_address,
                    "ElasticGpuSpecification": elastic_gpu_specification,
                    "ElasticInferenceAccelerators": elastic_inference_accelerators,
                    "LaunchTemplate": launch_template,
                    "InstanceMarketOptions": instance_market_options,
                    "CreditSpecification": credit_specification,
                    "CpuOptions": cpu_options,
                    "CapacityReservationSpecification": capacity_reservation_specification,
                    "HibernationOptions": hibernation_options,
                    "LicenseSpecifications": license_specifications,
                    "MetadataOptions": metadata_options,
                    "EnclaveOptions": enclave_options,
                    "TagSpecifications": [{"ResourceType": "instance", "Tags": tags}]
                    if tags
                    else None,
                },
            )
            result["result"] = ret["result"]
            if not result["result"]:
                result["comment"] = ret["comment"]
                return result
            resource._id = ret["ret"]["Instances"][0]["InstanceId"]
            result["comment"] = f"Created '{resource._id}'"
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = f"{e.__class__.__name__}: {e}"

    try:
        after = await hub.tool.boto3.resource.describe(resource)
        result["new_state"] = after
    except Exception as e:
        result["comment"] = str(e)
        result["result"] = False

    return result


async def absent(hub, ctx, name: str) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Shuts down the specified instances. This operation is idempotent; if you terminate an instance more than once,
    each call succeeds.  If you specify multiple instances and the request fails (for example, because of a single
    incorrect instance ID), none of the instances are terminated. If you terminate multiple instances across
    multiple Availability Zones, and one or more of the specified instances are enabled for termination protection,
    the request fails with the following results:   The specified instances that are in the same Availability Zone
    as the protected instance are not terminated.   The specified instances that are in different Availability
    Zones, where no other specified instances are protected, are successfully terminated.   For example, say you
    have the following instances:   Instance A: us-east-1a; Not protected   Instance B: us-east-1a; Not protected
    Instance C: us-east-1b; Protected   Instance D: us-east-1b; not protected   If you attempt to terminate all of
    these instances in the same request, the request reports failure with the following results:   Instance A and
    Instance B are successfully terminated because none of the specified instances in us-east-1a are enabled for
    termination protection.   Instance C and Instance D fail to terminate because at least one of the specified
    instances in us-east-1b (Instance C) is enabled for termination protection.   Terminated instances remain
    visible after termination (for approximately one hour). By default, Amazon EC2 deletes all EBS volumes that were
    attached when the instance launched. Volumes attached after instance launch continue running. You can stop,
    start, and terminate EBS-backed instances. You can only terminate instance store-backed instances. What happens
    to an instance differs if you stop it or terminate it. For example, when you stop an instance, the root device
    and any other devices attached to the instance persist. When you terminate an instance, any attached EBS volumes
    with the DeleteOnTermination block device mapping parameter set to true are automatically deleted. For more
    information about the differences between stopping and terminating instances, see Instance lifecycle in the
    Amazon EC2 User Guide. For more information about troubleshooting, see Troubleshooting terminating your instance
    in the Amazon EC2 User Guide.

    Args:
        name(Text): The id of the instance

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            resource_is_absent:
              aws.ec2.instance.absent:
                - name: value
    """

    result = dict(comment="", old_state=None, new_state=None, name=name, result=True)
    resource = hub.tool.boto3.resource.create(ctx, "ec2", "Instance", name)
    before = await hub.tool.boto3.resource.describe(resource)

    if not before:
        result["comment"] = f"'{name}' already absent"
    elif ctx.get("test", False):
        result["comment"] = f"Would delete aws.ec2.instance {name}"
        return result
    else:
        result["old_state"] = before
        try:
            ret = await hub.exec.boto3.client.ec2.terminate_instances(
                ctx, **{"InstanceIds": [name]}
            )
            result["result"] = ret["result"]
            if not result["result"]:
                result["comment"] = ret["comment"]
                return result
            result["comment"] = f"Deleted '{name}'"
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = f"{e.__class__.__name__}: {e}"

    return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    result = {}
    ret = await hub.exec.boto3.client.ec2.describe_instances(ctx)

    if not ret["result"]:
        hub.log.debug(f"Could not describe Instances {ret['comment']}")
        return {}

    instances = []
    for reservation in ret["ret"]["Reservations"]:
        instances.extend(reservation["Instances"])
    for instance in instances:
        instance_id = instance["InstanceId"]
        describe_parameters = OrderedDict(
            {
                "BlockDeviceMappings": "block_device_mappings",
                "ImageId": "image_id",
                "InstanceType": "instance_type",
                "KernelId": "kernel_id",
                "KeyName": "key_name",
                "Monitoring": "monitoring",
                "Placement": "placement",
                "SubnetId": "subnet",
                "EbsOptimized": "ebs_optimized",
                "PrivateIpAddress": "private_ip_address",
                "SecurityGroupIds": "security_group_ids",
                "CpuOptions": "cpu_options",
            }
        )
        # TODO: Add more parameters that present function supports
        instance_translated = []
        for parameter_old_key, parameter_new_key in describe_parameters.items():
            if instance.get(parameter_old_key) is not None:
                instance_translated.append(
                    {parameter_new_key: instance.get(parameter_old_key)}
                )

        result[instance_id] = {"aws.ec2.instance.present": instance_translated}
        for i, data in enumerate(instance["NetworkInterfaces"]):
            sub_instance = copy.deepcopy(instance_translated)
            sub_instance.append({"ipv6_addresses": data.get("Ipv6Addresses", [])})
            # The id needs to be in the name
            sub_instance.append({"name": instance["InstanceId"]})
            # Create a new state for this association set
            result[f"{instance_id}-{i}"] = {"aws.ec2.instance.present": sub_instance}
        group_ids = []
        for group in instance.get("SecurityGroups", []):
            group_ids.append(group.get("GroupId"))
        if group_ids:
            instance_translated.append({"security_group_ids": group_ids})
    return result
