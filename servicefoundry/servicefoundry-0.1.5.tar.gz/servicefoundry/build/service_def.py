import json


class ServiceDef:
    def __init__(self, name, build, deployments):
        self.name = name
        self.build: ServiceBuild = build
        self.deployments = deployments

    def get_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


class ServiceBuild:
    def __init__(
        self, service_type, service, version, build_dir, packages, ignore_patterns, port
    ):
        self.type = "ServiceBuild"
        self.service_type = service_type
        self.service = service
        self.version = version
        self.build_dir = build_dir
        self.packages = packages
        self.ignore_patterns = ignore_patterns
        self.port = port


class HealthCheck:
    def __init__(self, endpoint, period_seconds, initial_delay):
        self.endpoint = endpoint
        self.period_seconds = period_seconds
        self.initial_delay = initial_delay


class HttpsService:
    def __init__(
        self,
        namespace,
        port,
        cpu,
        memory,
        cpu_limit,
        memory_limit,
        instances,
        metrics_endpoint,
        env,
        health_check: HealthCheck,
    ):
        self.type = "HttpsService"
        self.namespace = namespace
        self.port = port
        self.cpu = cpu
        self.memory = memory
        self.cpu_limit = cpu_limit
        self.memory_limit = memory_limit
        self.instances = instances
        self.metrics_endpoint = metrics_endpoint
        self.env = env
        self.health_check = health_check
