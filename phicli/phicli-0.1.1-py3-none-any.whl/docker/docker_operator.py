from typing import List, Optional, cast, Dict, Any
from pathlib import Path

from docker.models.containers import Container
from phidata.infra.docker.api_client import DockerApiClient
from phidata.infra.docker.config import DockerConfig
from phidata.infra.docker.exceptions import DockerConfigException
from phidata.infra.docker.manager import DockerManager
from phidata.infra.docker.utils.container import execute_command
from phidata.product import DataProduct
from phidata.workflow import Workflow
from phidata.types.context import PathContext, RunContext

from phi.types.run_status import RunStatus
from phi.utils.cli_console import (
    print_error,
    print_heading,
    print_info,
    print_warning,
    print_subheading,
)
from phi.utils.log import logger


def deploy_docker_config(
    config: DockerConfig,
    name_filter: Optional[str] = None,
    type_filter: Optional[str] = None,
    dry_run: Optional[bool] = False,
) -> bool:

    # Step 1: Get the DockerManager
    docker_manager: DockerManager = config.get_docker_manager()
    if docker_manager is None:
        raise DockerConfigException("DockerManager unavailable")

    # Step 2: If dry_run, print the resources and return True
    if dry_run:
        docker_manager.create_resources_dry_run(
            name_filter=name_filter, type_filter=type_filter
        )
        return True

    # Step 3: Create resources
    env = config.env
    print_heading(
        "Deploying docker config{}\n".format(
            f" for env: {env}" if env is not None else ""
        )
    )
    try:
        success: bool = docker_manager.create_resources(
            name_filter=name_filter, type_filter=type_filter
        )
        if not success:
            return False
    except Exception:
        raise

    # Step 4: Validate resources are created
    resource_creation_valid: bool = docker_manager.validate_resources_are_created(
        name_filter=name_filter, type_filter=type_filter
    )
    if not resource_creation_valid:
        logger.error("DockerResource creation could not be validated")
        return False

    print_info("Docker config deployed")
    return True


def shutdown_docker_config(
    config: DockerConfig,
    name_filter: Optional[str] = None,
    type_filter: Optional[str] = None,
    dry_run: Optional[bool] = False,
) -> bool:

    # Step 1: Get the DockerManager
    docker_manager: DockerManager = config.get_docker_manager()
    if docker_manager is None:
        raise DockerConfigException("DockerManager unavailable")

    # Step 2: If dry_run, print the resources and return True
    if dry_run:
        docker_manager.delete_resources_dry_run(
            name_filter=name_filter, type_filter=type_filter
        )
        return True

    # Step 3: Delete resources
    env = config.env
    print_heading(
        "Shutting down docker config{}\n".format(
            f" for env: {env}" if env is not None else ""
        )
    )
    try:
        success: bool = docker_manager.delete_resources(
            name_filter=name_filter, type_filter=type_filter
        )
        if not success:
            return False
    except Exception:
        raise

    # Step 4: Validate resources are delete
    resources_deletion_valid: bool = docker_manager.validate_resources_are_deleted(
        name_filter=name_filter, type_filter=type_filter
    )
    if not resources_deletion_valid:
        logger.error("DockerResource deletion could not be validated")
        return False

    print_info("Workspace shutdown")
    return True


def run_workflows_docker(
    workflow_file: str,
    workflows: Dict[str, Workflow],
    run_context: RunContext,
    docker_config: DockerConfig,
    target_app: Optional[str] = None,
    workflow_name: Optional[str] = None,
    use_dag_id: Optional[str] = None,
) -> bool:
    from phidata.app.devbox import DevboxArgs, default_devbox_name
    from phidata.infra.docker.resource.types import (
        DockerResourceType,
        DockerContainer,
    )

    logger.debug("Running Workflow in DockerContainer")
    # Step 1: Get the DockerManager
    docker_manager: DockerManager = docker_config.get_docker_manager()
    if docker_manager is None:
        raise DockerConfigException("DockerManager unavailable")

    # Step 2: Check if a Devbox is available for running the Workflow
    # If available get the DevboxArgs
    devbox_app_name = target_app or docker_config.devbox_name or default_devbox_name
    logger.debug(f"Using App: {devbox_app_name}")
    devbox_app = docker_config.get_app_by_name(devbox_app_name)
    if devbox_app is None:
        print_error("Devbox not available")
        return False
    devbox_app_args: Optional[Any] = devbox_app.args
    # logger.debug(f"DevboxArgs: {devbox_app_args}")
    if devbox_app_args is None or not isinstance(devbox_app_args, DevboxArgs):
        print_error("DevboxArgs invalid")
        return False
    devbox_app_args = cast(DevboxArgs, devbox_app_args)

    # Step 3: Build the PathContext for the workflows.
    # NOTE: The PathContext uses directories relative to the
    # workspace_parent_container_path
    workspace_name = docker_config.workspace_root_path.stem
    workspace_root_container_path = Path(
        devbox_app_args.workspace_parent_container_path
    ).joinpath(workspace_name)
    scripts_dir_container_path = workspace_root_container_path.joinpath(
        docker_config.scripts_dir
    )
    storage_dir_container_path = workspace_root_container_path.joinpath(
        docker_config.storage_dir
    )
    meta_dir_container_path = workspace_root_container_path.joinpath(
        docker_config.meta_dir
    )
    products_dir_container_path = workspace_root_container_path.joinpath(
        docker_config.products_dir
    )
    notebooks_dir_container_path = workspace_root_container_path.joinpath(
        docker_config.notebooks_dir
    )
    workspace_config_dir_container_path = workspace_root_container_path.joinpath(
        docker_config.workspace_config_dir
    )
    workflow_file_path = Path(products_dir_container_path).joinpath(workflow_file)
    wf_path_context: PathContext = PathContext(
        scripts_dir=scripts_dir_container_path,
        storage_dir=storage_dir_container_path,
        meta_dir=meta_dir_container_path,
        products_dir=products_dir_container_path,
        notebooks_dir=notebooks_dir_container_path,
        workspace_config_dir=workspace_config_dir_container_path,
        workflow_file=workflow_file_path,
    )
    logger.debug(f"PathContext: {wf_path_context.json(indent=4)}")

    # Step 4: Get the container to run the Workflow
    devbox_containers: Optional[
        List[DockerResourceType]
    ] = docker_manager.get_resources(
        name_filter=devbox_app_name, type_filter="DockerContainer"
    )
    # logger.debug(f"devbox_containers: {devbox_containers}")
    if devbox_containers is None:
        logger.error(f"DockerContainer:{devbox_app_name} not found")
        return False
    if len(devbox_containers) > 1:
        print_warning(
            "Running commands in multiple containers is not yet supported. "
            + "Running in the first container. "
        )
    devbox_container: DockerContainer = devbox_containers[0]
    # logger.debug("devbox_container: ")
    # logger.debug("Name: {}".format(devbox_container.name))
    # logger.debug("Class: {}".format(devbox_container.__class__))
    # logger.debug("Resource: {}".format(devbox_container))
    docker_client: DockerApiClient = docker_manager.docker_worker.docker_client
    active_container: Optional[Container] = devbox_container.read(docker_client)
    # logger.debug("active_container: {}".format(active_container.attrs))
    # logger.debug("Class: {}".format(active_container.__class__))
    # logger.debug("Type: {}".format(type(active_container)))
    if active_container is None or not isinstance(active_container, Container):
        print_error("Container not available, please check your workspace is deployed.")
        return False

    # Step 5: Run single Workflow if workflow_name is provided
    if workflow_name is not None:
        if workflow_name not in workflows:
            print_error(
                "Could not find '{}' in {}".format(
                    workflow_name, "[{}]".format(", ".join(workflows.keys()))
                )
            )
            return False

        wf_run_success: bool = False
        workflow_to_run = workflows[workflow_name]
        _name = workflow_name or workflow_to_run.name
        print_subheading(f"\nRunning {_name}")
        # Pass down context
        workflow_to_run.run_context = run_context
        workflow_to_run.path_context = wf_path_context
        # Use DataProduct dag_id if provided
        if use_dag_id is not None:
            workflow_to_run.dag_id = use_dag_id
        wf_run_success = workflow_to_run.run_in_docker_container(
            active_container=active_container, docker_env=docker_config.docker_env
        )

        print_subheading("\nWorkflow run status:")
        print_info("{}: {}".format(_name, "Success" if wf_run_success else "Fail"))
        print_info("")
        return wf_run_success
    # Step 6: Run all Workflows if workflow_name is None
    else:
        wf_run_status: List[RunStatus] = []
        for wf_name, wf_obj in workflows.items():
            _name = wf_name or wf_obj.name
            print_subheading(f"\nRunning {_name}")
            # Pass down context
            wf_obj.run_context = run_context
            wf_obj.path_context = wf_path_context
            run_success = wf_obj.run_in_docker_container(
                active_container=active_container, docker_env=docker_config.docker_env
            )
            wf_run_status.append(RunStatus(_name, run_success))

        print_subheading("\nWorkflow run status:")
        print_info(
            "\n".join(
                [
                    "{}: {}".format(wf.name, "Success" if wf.success else "Fail")
                    for wf in wf_run_status
                ]
            )
        )
        print_info("")
        for _run in wf_run_status:
            if not _run.success:
                return False
        return True


def run_data_products_docker(
    workflow_file: str,
    data_products: Dict[str, DataProduct],
    run_context: RunContext,
    docker_config: DockerConfig,
    target_app: Optional[str] = None,
) -> bool:
    from phidata.app.devbox import DevboxArgs, default_devbox_name
    from phidata.infra.docker.resource.types import (
        DockerResourceType,
        DockerContainer,
    )

    logger.debug("Running DataProducts in DockerContainer")
    # Step 1: Get the DockerManager
    docker_manager: DockerManager = docker_config.get_docker_manager()
    if docker_manager is None:
        raise DockerConfigException("DockerManager unavailable")

    # Step 2: Check if a DevboxApp is available for running the DataProduct
    # If available get the DevboxAppArgs
    devbox_app_name = target_app or docker_config.devbox_name or default_devbox_name
    logger.debug(f"Using App: {devbox_app_name}")
    devbox_app = docker_config.get_app_by_name(devbox_app_name)
    if devbox_app is None:
        print_error("Devbox not available")
        return False
    devbox_app_args: Optional[Any] = devbox_app.args
    # logger.debug(f"DevboxAppArgs: {devbox_app_args}")
    if devbox_app_args is None or not isinstance(devbox_app_args, DevboxArgs):
        print_error("DevboxArgs invalid")
        return False
    devbox_app_args = cast(DevboxArgs, devbox_app_args)

    # Step 3: Build the PathContext for the DataProducts.
    # NOTE: The PathContext uses directories relative to the workspace_parent_container_path
    workspace_name = docker_config.workspace_root_path.stem
    workspace_root_container_path = Path(
        devbox_app_args.workspace_parent_container_path
    ).joinpath(workspace_name)
    scripts_dir_container_path = workspace_root_container_path.joinpath(
        docker_config.scripts_dir
    )
    storage_dir_container_path = workspace_root_container_path.joinpath(
        docker_config.storage_dir
    )
    meta_dir_container_path = workspace_root_container_path.joinpath(
        docker_config.meta_dir
    )
    products_dir_container_path = workspace_root_container_path.joinpath(
        docker_config.products_dir
    )
    notebooks_dir_container_path = workspace_root_container_path.joinpath(
        docker_config.notebooks_dir
    )
    workspace_config_dir_container_path = workspace_root_container_path.joinpath(
        docker_config.workspace_config_dir
    )
    workflow_file_path = Path(products_dir_container_path).joinpath(workflow_file)
    dp_path_context: PathContext = PathContext(
        scripts_dir=scripts_dir_container_path,
        storage_dir=storage_dir_container_path,
        meta_dir=meta_dir_container_path,
        products_dir=products_dir_container_path,
        notebooks_dir=notebooks_dir_container_path,
        workspace_config_dir=workspace_config_dir_container_path,
        workflow_file=workflow_file_path,
    )
    logger.debug(f"PathContext: {dp_path_context.json(indent=4)}")

    # Step 4: Get the container to run the DataProduct
    devbox_containers: Optional[
        List[DockerResourceType]
    ] = docker_manager.get_resources(
        name_filter=devbox_app_name, type_filter="DockerContainer"
    )
    if devbox_containers is None:
        logger.error(f"DockerContainer:{devbox_app_name} not found")
        return False
    if len(devbox_containers) > 1:
        print_info(
            "Running commands in multiple containers is not yet supported. "
            + "Running in the first container. "
        )
    devbox_container: DockerContainer = devbox_containers[0]
    # logger.debug("devbox_container: ")
    # logger.debug("Name: {}".format(devbox_container.name))
    # logger.debug("Class: {}".format(devbox_container.__class__))
    # logger.debug("Resource: {}".format(devbox_container))
    docker_client: DockerApiClient = docker_manager.docker_worker.docker_client
    active_container: Optional[Container] = devbox_container.read(docker_client)
    # logger.debug("active_container: {}".format(active_container.attrs))
    # logger.debug("Class: {}".format(active_container.__class__))
    # logger.debug("Type: {}".format(type(active_container)))
    if active_container is None or not isinstance(active_container, Container):
        print_error("Container not available, please check your workspace is deployed.")
        return False

    # Step 5: Run the DataProducts
    dp_run_status: List[RunStatus] = []
    for dp_name, dp_obj in data_products.items():
        _name = dp_name or dp_obj.name
        print_subheading(f"\nRunning {_name}")
        # Pass down context
        dp_obj.run_context = run_context
        dp_obj.path_context = dp_path_context
        run_success = dp_obj.run_in_docker_container(
            active_container=active_container, docker_env=docker_config.docker_env
        )
        dp_run_status.append(RunStatus(_name, run_success))

    print_subheading("DataProduct run status:")
    print_info(
        "\n".join(
            [
                "{}: {}".format(wf.name, "Success" if wf.success else "Fail")
                for wf in dp_run_status
            ]
        )
    )
    print_info("")
    for _run in dp_run_status:
        if not _run.success:
            return False
    return True


def run_command_docker(
    command: str,
    docker_config: DockerConfig,
    target_app: Optional[str] = None,
) -> bool:
    from phidata.app.devbox import DevboxArgs, default_devbox_name
    from phidata.infra.docker.resource.types import (
        DockerResourceType,
        DockerContainer,
    )

    logger.debug("Running command in DockerContainer")
    # Step 1: Get the DockerManager
    docker_manager: DockerManager = docker_config.get_docker_manager()
    if docker_manager is None:
        raise DockerConfigException("DockerManager unavailable")

    # Step 2: Check if a Devbox is available for running the DataProduct
    # If available get the DevboxArgs
    devbox_app_name = target_app or docker_config.devbox_name or default_devbox_name
    logger.debug(f"Using App: {devbox_app_name}")
    devbox_app = docker_config.get_app_by_name(devbox_app_name)
    if devbox_app is None:
        print_error("Devbox not available")
        return False
    devbox_app_args: Optional[Any] = devbox_app.args
    # logger.debug(f"DevboxArgs: {devbox_app_args}")
    if devbox_app_args is None or not isinstance(devbox_app_args, DevboxArgs):
        print_error("DevboxArgs invalid")
        return False
    devbox_app_args = cast(DevboxArgs, devbox_app_args)

    # Step 3: Get the container to run the command
    devbox_containers: Optional[
        List[DockerResourceType]
    ] = docker_manager.get_resources(
        name_filter=devbox_app_name, type_filter="DockerContainer"
    )
    # logger.debug(f"devbox_containers: {devbox_containers}")
    if devbox_containers is None:
        logger.error(f"DockerContainer:{devbox_app_name} not found")
        return False
    if len(devbox_containers) > 1:
        print_info(
            "Running commands in multiple containers is not yet supported. "
            + "Running in the first container. "
        )
    devbox_container: DockerContainer = devbox_containers[0]
    # logger.debug("devbox_container: ")
    # logger.debug("Name: {}".format(devbox_container.name))
    # logger.debug("Class: {}".format(devbox_container.__class__))
    # logger.debug("Resource: {}".format(devbox_container))
    docker_client: DockerApiClient = docker_manager.docker_worker.docker_client
    active_container: Optional[Container] = devbox_container.read(docker_client)
    # logger.debug("active_container: {}".format(active_container.attrs))
    # logger.debug("Class: {}".format(active_container.__class__))
    # logger.debug("Type: {}".format(type(active_container)))
    if active_container is None or not isinstance(active_container, Container):
        print_error("Container not available, please check your workspace is deployed.")
        return False

    # Step 4: Run the command
    print_subheading(f"Running command: `{command}`")
    run_status = execute_command(
        cmd=command,
        container=active_container,
        docker_env=docker_config.docker_env,
    )
    logger.debug(f"Run status: {run_status}")
    return run_status
