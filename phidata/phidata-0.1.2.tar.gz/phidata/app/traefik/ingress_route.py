from collections import OrderedDict
from pathlib import Path
from typing import Optional, Dict, List
from typing_extensions import Literal

from phidata.app import PhidataApp, PhidataAppArgs
from phidata.app.traefik.crds import (
    ingressroute_crd,
    ingressroutetcp_crd,
    ingressrouteudp_crd,
    middleware_crd,
    middlewaretcp_crd,
    serverstransport_crd,
    tlsoption_crd,
    tlsstore_crd,
    traefikservice_crd,
)
from phidata.infra.docker.resource.group import (
    DockerResourceGroup,
    DockerBuildContext,
)
from phidata.infra.k8s.create.apiextensions_k8s_io.v1.custom_object import (
    CreateCustomObject,
)
from phidata.infra.k8s.create.core.v1.service_account import CreateServiceAccount
from phidata.infra.k8s.create.core.v1.container import CreateContainer
from phidata.infra.k8s.create.apps.v1.deployment import CreateDeployment
from phidata.infra.k8s.create.core.v1.secret import CreateSecret
from phidata.infra.k8s.create.core.v1.service import CreateService, ServiceType
from phidata.infra.k8s.create.common.port import CreatePort
from phidata.infra.k8s.create.group import CreateK8sResourceGroup
from phidata.infra.k8s.create.rbac_authorization_k8s_io.v1.cluster_role import (
    CreateClusterRole,
    PolicyRule,
)
from phidata.infra.k8s.create.rbac_authorization_k8s_io.v1.cluste_role_binding import (
    CreateClusterRoleBinding,
)
from phidata.infra.k8s.resource.group import (
    K8sResourceGroup,
    K8sBuildContext,
)
from phidata.utils.common import (
    get_default_service_name,
    get_default_container_name,
    get_default_deploy_name,
    get_default_pod_name,
    get_default_cr_name,
    get_default_crb_name,
    get_default_sa_name,
)
from phidata.utils.enums import ExtendedEnum
from phidata.utils.cli_console import print_error, print_info, print_warning
from phidata.utils.log import logger


class LoadBalancerProvider(ExtendedEnum):
    AWS = "AWS"


class IngressRouteArgs(PhidataAppArgs):
    name: str = "ingressroute"
    version: str = "1"
    enabled: bool = True

    # Image Args
    image_name: str = "traefik"
    image_tag: str = "v2.6"
    # Add env variables to container env
    # keys: var name
    # values: var values
    env: Optional[Dict[str, str]] = None

    domain_name: Optional[str] = None

    web_enabled: bool = False
    web_routes: Optional[List[dict]] = None
    web_container_port: int = 80
    web_service_port: int = 80
    web_node_port: Optional[int] = None
    web_key: str = "web"
    web_ingress_name: str = "web-ingress"
    forward_web_to_websecure: bool = False

    websecure_enabled: bool = False
    websecure_routes: Optional[List[dict]] = None
    websecure_container_port: int = 443
    websecure_service_port: int = 443
    websecure_node_port: Optional[int] = None
    websecure_key: str = "websecure"
    websecure_ingress_name: str = "websecure-ingress"

    dashboard_enabled: bool = (False,)
    dashboard_routes: Optional[List[dict]] = None
    dashboard_container_port: int = 8080
    dashboard_service_port: int = 8080
    dashboard_node_port: Optional[int] = None
    dashboard_key: str = "dashboard"
    dashboard_ingress_name: str = "dashboard-ingress"
    # dashboard auth
    dashboard_auth_users: Optional[str] = None
    dashboard_auth_users_file: Optional[str] = None
    insecure_api_access: bool = False

    # Traefik config
    # Enable Access Logs
    access_logs: bool = True
    # Traefik config file on the host
    traefik_config_file: Optional[str] = None
    # Traefik config file on the container
    traefik_config_file_container_path: Path = Path("/etc/traefik/traefik.yaml")

    # rbac
    sa_name: Optional[str] = None
    cr_name: Optional[str] = None
    crb_name: Optional[str] = None
    # container
    container_name: Optional[str] = None
    container_args: Optional[List[str]] = None
    # deploy
    deploy_name: Optional[str] = None
    pod_name: Optional[str] = None
    # service
    service_name: Optional[str] = None
    service_type: ServiceType = ServiceType.LOAD_BALANCER
    service_annotations: Optional[Dict[str, Optional[str]]] = None

    # On cloud providers which support external load balancers,
    # setting the service_type field to LoadBalancer provisions a load balancer.
    # The actual creation of the load balancer happens asynchronously
    #
    # load_balancer_provider is required if service_type == ServiceType.LOAD_BALANCER
    load_balancer_provider: Optional[LoadBalancerProvider] = None

    # AWS LoadBalancer configuration
    use_nlb: bool = True
    # Specifies the target type to configure for NLB. You can choose between instance and ip.
    # `instance` mode will route traffic to all EC2 instances within cluster on the NodePort opened for your service.
    #       service must be of type NodePort or LoadBalancer for instance targets
    #       for k8s 1.22 and later if spec.allocateLoadBalancerNodePorts is set to false,
    #       NodePort must be allocated manually
    # `ip` mode will route traffic directly to the pod IP.
    #       network plugin must use native AWS VPC networking configuration for pod IP,
    #       for example Amazon VPC CNI plugin.
    nlb_target_type: Optional[Literal["instance", "ip"]] = None
    # Write Access Logs to s3
    access_logs_to_s3: bool = False
    # The name of the aws S3 bucket where the access logs are stored
    access_logs_s3_bucket: Optional[str] = None
    # The logical hierarchy you created for your aws S3 bucket, for example `my-bucket-prefix/prod`
    access_logs_s3_bucket_prefix: Optional[str] = None
    # If provided, TLS termination is added to the LB
    acm_certificate_arn: Optional[str] = None
    acm_certificate_summary_file: Optional[Path] = (None,)
    load_balancer_ip: Optional[str] = None
    # If None, default is internal.
    load_balancer_scheme: Optional[Literal["internal", "internet-facing"]] = None
    load_balancer_source_ranges: Optional[List[str]] = None
    allocate_load_balancer_node_ports: Optional[bool] = None


class IngressRoute(PhidataApp):
    def __init__(
        self,
        name: str = "ingressroute",
        version: str = "1",
        enabled: bool = True,
        # Image Args,
        image_name: str = "traefik",
        image_tag: str = "v2.6",
        # Add env variables to container env,
        # keys: var name,
        # values: var values,
        env: Optional[Dict[str, str]] = None,
        domain_name: Optional[str] = None,
        web_enabled: bool = False,
        web_routes: Optional[List[dict]] = None,
        web_container_port: int = 80,
        web_service_port: int = 80,
        web_node_port: Optional[int] = None,
        web_key: str = "web",
        web_ingress_name: str = "web-ingress",
        forward_web_to_websecure: bool = False,
        websecure_enabled: bool = False,
        websecure_routes: Optional[List[dict]] = None,
        websecure_container_port: int = 443,
        websecure_service_port: int = 443,
        websecure_node_port: Optional[int] = None,
        websecure_key: str = "websecure",
        websecure_ingress_name: str = "websecure-ingress",
        dashboard_enabled: bool = False,
        dashboard_routes: Optional[List[dict]] = None,
        dashboard_container_port: int = 8080,
        dashboard_service_port: int = 8080,
        dashboard_node_port: Optional[int] = None,
        dashboard_key: str = "dashboard",
        dashboard_ingress_name: str = "dashboard-ingress",
        dashboard_auth_users: Optional[str] = None,
        dashboard_auth_users_file: Optional[str] = None,
        insecure_api_access: bool = False,
        # Traefik config
        # Enable Access Logs
        access_logs: bool = True,
        # Traefik config file on the host
        traefik_config_file: Optional[str] = None,
        # Traefik config file on the container
        traefik_config_file_container_path: Path = Path("/etc/traefik/traefik.yaml"),
        # rbac,
        sa_name: Optional[str] = None,
        cr_name: Optional[str] = None,
        crb_name: Optional[str] = None,
        # container,
        container_name: Optional[str] = None,
        container_args: Optional[List[str]] = None,
        # deploy,
        deploy_name: Optional[str] = None,
        pod_name: Optional[str] = None,
        # service,
        service_name: Optional[str] = None,
        service_type: ServiceType = ServiceType.LOAD_BALANCER,
        service_annotations: Optional[Dict[str, Optional[str]]] = None,
        # On cloud providers which support external load balancers,
        # setting the service_type field to LoadBalancer provisions a load balancer.
        # The actual creation of the load balancer happens asynchronously
        #
        # load_balancer_provider is required if service_type == ServiceType.LOAD_BALANCER
        load_balancer_provider: Optional[LoadBalancerProvider] = None,
        # AWS LoadBalancer configuration
        use_nlb: bool = True,
        nlb_target_type: Optional[Literal["instance", "ip"]] = None,
        # Write Access Logs to s3
        access_logs_to_s3: bool = False,
        # The name of the aws S3 bucket where the access logs are stored
        access_logs_s3_bucket: Optional[str] = None,
        # The logical hierarchy you created for your aws S3 bucket, for example `my-bucket-prefix/prod`
        access_logs_s3_bucket_prefix: Optional[str] = None,
        # If provided, TLS termination is added to the LB
        acm_certificate_arn: Optional[str] = None,
        acm_certificate_summary_file: Optional[Path] = None,
        load_balancer_ip: Optional[str] = None,
        load_balancer_scheme: Optional[Literal["internal", "internet-facing"]] = None,
        load_balancer_source_ranges: Optional[List[str]] = None,
        allocate_load_balancer_node_ports: Optional[bool] = None,
    ):
        super().__init__()
        try:
            self.args: IngressRouteArgs = IngressRouteArgs(
                name=name,
                version=version,
                enabled=enabled,
                image_name=image_name,
                image_tag=image_tag,
                env=env,
                domain_name=domain_name,
                web_enabled=web_enabled,
                web_routes=web_routes,
                web_container_port=web_container_port,
                web_service_port=web_service_port,
                web_node_port=web_node_port,
                web_key=web_key,
                web_ingress_name=web_ingress_name,
                forward_web_to_websecure=forward_web_to_websecure,
                websecure_enabled=websecure_enabled,
                websecure_routes=websecure_routes,
                websecure_container_port=websecure_container_port,
                websecure_service_port=websecure_service_port,
                websecure_node_port=websecure_node_port,
                websecure_key=websecure_key,
                websecure_ingress_name=websecure_ingress_name,
                dashboard_enabled=dashboard_enabled,
                dashboard_routes=dashboard_routes,
                dashboard_container_port=dashboard_container_port,
                dashboard_service_port=dashboard_service_port,
                dashboard_node_port=dashboard_node_port,
                dashboard_key=dashboard_key,
                dashboard_ingress_name=dashboard_ingress_name,
                dashboard_auth_users=dashboard_auth_users,
                dashboard_auth_users_file=dashboard_auth_users_file,
                insecure_api_access=insecure_api_access,
                access_logs=access_logs,
                traefik_config_file=traefik_config_file,
                traefik_config_file_container_path=traefik_config_file_container_path,
                sa_name=sa_name,
                cr_name=cr_name,
                crb_name=crb_name,
                container_name=container_name,
                container_args=container_args,
                deploy_name=deploy_name,
                pod_name=pod_name,
                service_name=service_name,
                service_type=service_type,
                service_annotations=service_annotations,
                load_balancer_provider=load_balancer_provider,
                use_nlb=use_nlb,
                nlb_target_type=nlb_target_type,
                access_logs_to_s3=access_logs_to_s3,
                access_logs_s3_bucket=access_logs_s3_bucket,
                access_logs_s3_bucket_prefix=access_logs_s3_bucket_prefix,
                acm_certificate_arn=acm_certificate_arn,
                acm_certificate_summary_file=acm_certificate_summary_file,
                load_balancer_ip=load_balancer_ip,
                load_balancer_scheme=load_balancer_scheme,
                load_balancer_source_ranges=load_balancer_source_ranges,
                allocate_load_balancer_node_ports=allocate_load_balancer_node_ports,
            )
        except Exception:
            logger.error(f"Args for {self.__class__.__name__} are not valid")
            raise

    ######################################################
    ## Docker Resources
    ######################################################

    def get_ingress_route_docker_rg(
        self, docker_build_context: DockerBuildContext
    ) -> Optional[DockerResourceGroup]:
        print_error(f"IngressRoute not available on Docker")
        return None

    def init_docker_resource_groups(
        self, docker_build_context: DockerBuildContext
    ) -> None:
        docker_rg: Optional[DockerResourceGroup] = self.get_ingress_route_docker_rg(
            docker_build_context
        )
        # logger.debug("docker_rg:\n{}".format(docker_rg.json(indent=2)))
        if docker_rg is not None:
            if self.docker_resource_groups is None:
                self.docker_resource_groups = OrderedDict()
            self.docker_resource_groups[docker_rg.name] = docker_rg

    ######################################################
    ## K8s Resources
    ######################################################

    def get_ingress_route_k8s_rg(
        self, k8s_build_context: K8sBuildContext
    ) -> Optional[K8sResourceGroup]:
        logger.debug(f"Init IngressRoute K8sResourceGroup")

        app_name = self.args.name

        sa = CreateServiceAccount(
            sa_name=self.args.sa_name or get_default_sa_name(app_name),
            app_name=app_name,
            namespace=k8s_build_context.namespace,
        )

        cr = CreateClusterRole(
            cr_name=self.args.cr_name or get_default_cr_name(app_name),
            rules=[
                PolicyRule(
                    api_groups=[""],
                    resources=[
                        "services",
                        "endpoints",
                        "secrets",
                    ],
                    verbs=[
                        "get",
                        "list",
                        "watch",
                    ],
                ),
                PolicyRule(
                    api_groups=[
                        "extensions",
                        "networking.k8s.io",
                    ],
                    resources=[
                        "ingresses",
                        "ingressclasses",
                    ],
                    verbs=[
                        "get",
                        "list",
                        "watch",
                    ],
                ),
                PolicyRule(
                    api_groups=[
                        "extensions",
                    ],
                    resources=[
                        "ingresses/status",
                    ],
                    verbs=[
                        "update",
                    ],
                ),
                PolicyRule(
                    api_groups=[
                        "traefik.containo.us",
                    ],
                    resources=[
                        "middlewares",
                        "middlewaretcps",
                        "ingressroutes",
                        "traefikservices",
                        "ingressroutetcps",
                        "ingressrouteudps",
                        "tlsoptions",
                        "tlsstores",
                        "serverstransports",
                    ],
                    verbs=[
                        "get",
                        "list",
                        "watch",
                    ],
                ),
            ],
            app_name=app_name,
        )

        crb = CreateClusterRoleBinding(
            crb_name=get_default_crb_name(app_name),
            cr_name=cr.cr_name,
            service_account_name=sa.sa_name,
            app_name=app_name,
            namespace=k8s_build_context.namespace,
        )

        resource_group = CreateK8sResourceGroup(
            name=app_name,
            enabled=self.args.enabled,
            sa=sa,
            cr=cr,
            crb=crb,
            crds=[
                ingressroute_crd,
                ingressroutetcp_crd,
                ingressrouteudp_crd,
                middleware_crd,
                middlewaretcp_crd,
                serverstransport_crd,
                tlsoption_crd,
                tlsstore_crd,
                traefikservice_crd,
            ],
        )

        ports = []
        custom_objects = []
        container_args = self.args.container_args
        if container_args is None:
            container_args = []
        container_args.append("--providers.kubernetescrd")

        if self.args.access_logs:
            container_args.append("--accesslog")

        if self.args.web_enabled:
            container_args.append(
                f"--entrypoints.{self.args.web_key}.Address=:{self.args.web_service_port}"
            )

            web_port = CreatePort(
                name=self.args.web_key,
                container_port=self.args.web_container_port,
                service_port=self.args.web_service_port,
                target_port=self.args.web_key,
            )
            if (
                self.args.service_type
                in (ServiceType.NODE_PORT, ServiceType.LOAD_BALANCER)
                and self.args.web_node_port is not None
            ):
                web_port.node_port = self.args.web_node_port
            ports.append(web_port)

            web_ingressroute = CreateCustomObject(
                name=self.args.web_ingress_name,
                crd=ingressroute_crd,
                spec={
                    "entryPoints": [self.args.web_key],
                    "routes": self.args.web_routes,
                },
                app_name=app_name,
                namespace=k8s_build_context.namespace,
            )
            custom_objects.append(web_ingressroute)

        if self.args.websecure_enabled:
            container_args.append(
                f"--entrypoints.{self.args.websecure_key}.Address=:{self.args.websecure_service_port}"
            )
            if self.args.forward_web_to_websecure:
                container_args.extend(
                    [
                        f"--entrypoints.{self.args.web_key}.http.redirections.entryPoint.to={self.args.websecure_key}",
                        f"--entrypoints.{self.args.web_key}.http.redirections.entryPoint.scheme=https",
                    ]
                )

            websecure_port = CreatePort(
                name=self.args.websecure_key,
                container_port=self.args.websecure_container_port,
                service_port=self.args.websecure_service_port,
                target_port=self.args.websecure_key,
            )
            if (
                self.args.service_type
                in (ServiceType.NODE_PORT, ServiceType.LOAD_BALANCER)
                and self.args.websecure_node_port is not None
            ):
                websecure_port.node_port = self.args.websecure_node_port
            ports.append(websecure_port)

            websecure_ingressroute = CreateCustomObject(
                name=self.args.websecure_ingress_name,
                crd=ingressroute_crd,
                spec={
                    "entryPoints": [self.args.websecure_key],
                    "routes": self.args.websecure_routes,
                },
                app_name=app_name,
                namespace=k8s_build_context.namespace,
            )
            custom_objects.append(websecure_ingressroute)

        if self.args.dashboard_enabled:
            container_args.append(f"--api=true")
            container_args.append(f"--api.dashboard=true")
            if self.args.insecure_api_access:
                container_args.append(f"--api.insecure")

            dashboard_port = CreatePort(
                name=self.args.dashboard_key,
                container_port=self.args.dashboard_container_port,
                service_port=self.args.dashboard_service_port,
                target_port=self.args.dashboard_key,
            )
            if (
                self.args.service_type
                in (ServiceType.NODE_PORT, ServiceType.LOAD_BALANCER)
                and self.args.dashboard_node_port is not None
            ):
                dashboard_port.node_port = self.args.dashboard_node_port
            ports.append(dashboard_port)

            # create dashboard_auth_middleware if auth provided
            # ref: https://doc.traefik.io/traefik/operations/api/#configuration
            dashboard_auth_middleware = None
            dashboard_auth_users = self.args.dashboard_auth_users
            if (
                dashboard_auth_users is None
                and self.args.dashboard_auth_users_file is not None
            ):
                # TODO: load from file
                pass
            if dashboard_auth_users is not None:
                dashboard_auth_secret = CreateSecret(
                    secret_name="dashboard-auth-secret",
                    app_name=app_name,
                    namespace=k8s_build_context.namespace,
                    data={"users": dashboard_auth_users},
                )
                if resource_group.secrets is None:
                    resource_group.secrets = []
                resource_group.secrets.append(dashboard_auth_secret)

                dashboard_auth_middleware = CreateCustomObject(
                    name="dashboard-auth-middleware",
                    crd=middleware_crd,
                    spec={"basicAuth": {"secret": dashboard_auth_secret.secret_name}},
                    app_name=app_name,
                    namespace=k8s_build_context.namespace,
                )
                custom_objects.append(dashboard_auth_middleware)

            dashboard_routes = self.args.dashboard_routes
            # use default dashboard routes
            if dashboard_routes is None:
                # domain must be provided
                if self.args.domain_name is not None:
                    dashboard_routes = [
                        {
                            "kind": "Rule",
                            "match": f"Host(`traefik.{self.args.domain_name}`)",
                            "middlewares": [
                                {
                                    "name": dashboard_auth_middleware.name,
                                    "namespace": k8s_build_context.namespace,
                                },
                            ]
                            if dashboard_auth_middleware is not None
                            else [],
                            "services": [
                                {
                                    "kind": "TraefikService",
                                    "name": "api@internal",
                                }
                            ],
                        },
                    ]

            # TODO: uncomment if need to add dashboard_entrypoint
            # container_args.append(
            #     f"--entrypoints.{self.args.dashboard_key}.Address=:{self.args.dashboard_service_port}"
            # )
            # # dashboard_entrypoint: default to dashboard_key i.e. 8080
            # dashboard_entrypoint = self.args.dashboard_key
            # # if web/http at 80 is avl, use that
            # if self.args.web_enabled:
            #     dashboard_entrypoint = self.args.web_key
            # # if websecure/https at 443 is avl, then use that over web/http
            # if self.args.websecure_enabled:
            #     dashboard_entrypoint = self.args.websecure_key

            dashboard_ingressroute = CreateCustomObject(
                name=self.args.dashboard_ingress_name,
                crd=ingressroute_crd,
                spec={
                    # "entryPoints": [dashboard_entrypoint],
                    "routes": dashboard_routes,
                },
                app_name=app_name,
                namespace=k8s_build_context.namespace,
            )
            custom_objects.append(dashboard_ingressroute)

        container = CreateContainer(
            container_name=self.args.container_name
            or get_default_container_name(app_name),
            app_name=app_name,
            image_name=self.args.image_name,
            image_tag=self.args.image_tag,
            args=container_args,
            ports=ports,
        )

        deployment = CreateDeployment(
            deploy_name=self.args.deploy_name or get_default_deploy_name(app_name),
            pod_name=self.args.pod_name or get_default_pod_name(app_name),
            app_name=app_name,
            namespace=k8s_build_context.namespace,
            service_account_name=sa.sa_name,
            containers=[container],
            labels=k8s_build_context.labels,
        )

        service_annotations = self.args.service_annotations
        if service_annotations is None:
            service_annotations = OrderedDict()

        # Configure AWS LoadBalancer
        if self.args.load_balancer_provider == LoadBalancerProvider.AWS:
            # https://kubernetes.io/docs/concepts/services-networking/service/#aws-nlb-support
            if self.args.use_nlb:
                service_annotations[
                    "service.beta.kubernetes.io/aws-load-balancer-type"
                ] = "nlb"
            if self.args.nlb_target_type is not None:
                service_annotations[
                    "service.beta.kubernetes.io/aws-load-balancer-nlb-target-type"
                ] = self.args.nlb_target_type

            # New: https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.4/guide/service/annotations/#load-balancer-attributes
            # Deprecated docs: # https://kubernetes.io/docs/concepts/services-networking/service/#elb-access-logs-on-aws
            if self.args.access_logs_to_s3:
                lb_attributes = ""
                lb_attributes += "access_logs.s3.enabled=true"
                if self.args.access_logs_s3_bucket is not None:
                    lb_attributes += (
                        f",access_logs.s3.bucket={self.args.access_logs_s3_bucket}"
                    )
                if self.args.access_logs_s3_bucket_prefix is not None:
                    lb_attributes += f",access_logs.s3.prefix={self.args.access_logs_s3_bucket_prefix}"
                service_annotations[
                    "service.beta.kubernetes.io/aws-load-balancer-attributes"
                ] = lb_attributes

            # https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.4/guide/service/annotations/#ssl-cert
            if self.args.acm_certificate_arn is not None:
                service_annotations[
                    "service.beta.kubernetes.io/aws-load-balancer-ssl-cert"
                ] = self.args.acm_certificate_arn
                service_annotations[
                    "service.beta.kubernetes.io/aws-load-balancer-ssl-ports"
                ] = str(self.args.websecure_service_port)
            # if acm_certificate_summary_file is provided, use that
            if self.args.acm_certificate_summary_file is not None and isinstance(
                self.args.acm_certificate_summary_file, Path
            ):
                if (
                    self.args.acm_certificate_summary_file.exists()
                    and self.args.acm_certificate_summary_file.is_file()
                ):
                    from phidata.infra.aws.resource.acm.certificate import (
                        CertificateSummary,
                    )

                    cert_summary = CertificateSummary.parse_file(
                        self.args.acm_certificate_summary_file
                    )
                    certificate_arn = cert_summary.CertificateArn
                    logger.debug(f"CertificateArn: {certificate_arn}")
                    service_annotations[
                        "service.beta.kubernetes.io/aws-load-balancer-ssl-cert"
                    ] = certificate_arn
                    service_annotations[
                        "service.beta.kubernetes.io/aws-load-balancer-ssl-ports"
                    ] = str(self.args.websecure_service_port)
                else:
                    print_warning(
                        f"Does not exist: {self.args.acm_certificate_summary_file}"
                    )

            if self.args.load_balancer_scheme is not None:
                service_annotations[
                    "sservice.beta.kubernetes.io/aws-load-balancer-scheme"
                ] = self.args.load_balancer_scheme

        service = CreateService(
            service_name=self.args.service_name or get_default_service_name(app_name),
            app_name=app_name,
            namespace=k8s_build_context.namespace,
            service_account_name=sa.sa_name,
            service_type=self.args.service_type,
            deployment=deployment,
            ports=ports,
            labels=k8s_build_context.labels,
            annotations=service_annotations,
            load_balancer_ip=self.args.load_balancer_ip,
            load_balancer_source_ranges=self.args.load_balancer_source_ranges,
            allocate_load_balancer_node_ports=self.args.allocate_load_balancer_node_ports,
        )

        resource_group.services = [service]
        resource_group.deployments = [deployment]
        resource_group.custom_objects = custom_objects

        return resource_group.create()

    def init_k8s_resource_groups(self, k8s_build_context: K8sBuildContext) -> None:
        k8s_rg: Optional[K8sResourceGroup] = self.get_ingress_route_k8s_rg(
            k8s_build_context
        )
        # logger.debug("k8s_rg:\n{}".format(k8s_rg.json(indent=2)))
        if k8s_rg is not None:
            if self.k8s_resource_groups is None:
                self.k8s_resource_groups = OrderedDict()
            self.k8s_resource_groups[k8s_rg.name] = k8s_rg
