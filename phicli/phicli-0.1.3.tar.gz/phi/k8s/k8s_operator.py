from pathlib import Path
from typing import List, Optional, cast, Dict, Tuple, Any

from phidata.infra.base import InfraConfig
from phidata.infra.k8s.api_client import K8sApiClient
from phidata.infra.k8s.config import K8sConfig
from phidata.infra.k8s.exceptions import K8sConfigException
from phidata.infra.k8s.manager import K8sManager
from phidata.infra.k8s.resource.types import K8sResourceType
from phidata.workspace import WorkspaceConfig
from phidata.workflow import Workflow
from phidata.types.context import PathContext, RunContext

from phi.workspace.phi_ws_data import PhiWsData
from phi.workspace.ws_enums import WorkspaceEnv
from phi.types.run_status import RunStatus
from phi.utils.filesystem import delete_files_in_dir
from phi.utils.cli_console import (
    print_error,
    print_heading,
    print_subheading,
    print_info,
)
from phi.utils.log import logger


def deploy_k8s_config(
    config: K8sConfig,
    name_filter: Optional[str] = None,
    type_filter: Optional[str] = None,
    dry_run: Optional[bool] = False,
) -> bool:

    # Step 1: Get the K8sManager
    k8s_manager: K8sManager = config.get_k8s_manager()
    if k8s_manager is None:
        raise K8sConfigException("K8sManager unavailable")

    # Step 3: If dry_run, print the resources and return True
    if dry_run:
        k8s_manager.create_resources_dry_run(
            name_filter=name_filter, type_filter=type_filter
        )
        return True

    # Step 3: Create resources
    env = config.env
    print_subheading(
        "Deploying k8s config{}\n".format(f" for env: {env}" if env is not None else "")
    )
    try:
        success: bool = k8s_manager.create_resources(
            name_filter=name_filter, type_filter=type_filter
        )
        if not success:
            return False
    except Exception:
        raise

    # Step 4: Validate resources are created
    resource_creation_valid: bool = k8s_manager.validate_resources_are_created(
        name_filter=name_filter, type_filter=type_filter
    )
    if not resource_creation_valid:
        logger.error("K8sResource creation could not be validated")
        return False

    print_info("K8s config deployed")
    return True


def shutdown_k8s_config(
    config: K8sConfig,
    name_filter: Optional[str] = None,
    type_filter: Optional[str] = None,
    dry_run: Optional[bool] = False,
) -> bool:

    # Step 1: Get the K8sManager
    k8s_manager: K8sManager = config.get_k8s_manager()
    if k8s_manager is None:
        raise K8sConfigException("K8sManager unavailable")

    # Step 2: If dry_run, print the resources and return True
    if dry_run:
        k8s_manager.delete_resources_dry_run(
            name_filter=name_filter, type_filter=type_filter
        )
        return True

    # Step 3: Delete resources
    env = config.env
    print_subheading(
        "Shutting down k8s config{}\n".format(
            f" for env: {env}" if env is not None else ""
        )
    )
    try:
        success: bool = k8s_manager.delete_resources(
            name_filter=name_filter, type_filter=type_filter
        )
        if not success:
            return False
    except Exception:
        raise

    # Step 4: Validate resources are deleted
    resources_deletion_valid: bool = k8s_manager.validate_resources_are_deleted(
        name_filter=name_filter, type_filter=type_filter
    )
    if not resources_deletion_valid:
        logger.error("K8sResource deletion could not be validated")
        return False

    print_info("K8s config shutdown")
    return True


def save_k8s_resources(
    ws_data: PhiWsData,
    target_env: Optional[WorkspaceEnv] = None,
    target_name: Optional[str] = None,
    target_type: Optional[str] = None,
) -> None:
    """Saves the K8s resources"""

    if ws_data is None or ws_data.ws_config is None:
        print_error("WorkspaceConfig invalid")
        return

    ws_name: str = ws_data.ws_name
    # print_heading(f"Building K8s manifests for {ws_name}")

    # Step 1: Get the K8sConfigs to build
    configs_to_build: List[InfraConfig] = []
    if target_env is None:
        if ws_data.ws_config.k8s is not None:
            configs_to_build.extend(ws_data.ws_config.k8s)
    else:
        for config in ws_data.ws_config.k8s:
            if config.env is None:
                continue
            if config.env.lower() not in WorkspaceEnv.values_list():
                print_error(f"{config.env} not supported")
                continue
            config_env = WorkspaceEnv.from_str(config.env)
            if config_env == target_env:
                configs_to_build.append(config)

    num_configs_to_build = len(configs_to_build)
    num_configs_built = 0
    for config in configs_to_build:
        env = config.env
        print_heading(
            "\nBuilding K8s manifests{}\n".format(
                f" for env: {env}" if env is not None else ""
            )
        )
        if not isinstance(config, InfraConfig):
            print_error(f"{config} is not an instance of InfraConfig")
            continue
        if not isinstance(config, K8sConfig):
            print_error(f"{config} is not an instance of K8sConfig")
            continue
        if not config.is_valid():
            print_error("K8sConfig invalid")
            continue
        if not config.enabled:
            logger.debug(
                f"{config.__class__.__name__} for env {config.__class__.env} disabled"
            )
            num_configs_built += 1
            continue

        # NOTE: Very important step
        # If the paths arent updated then the Manager object cannot be created
        # Update the workspace_root_path and workspace_config_file_path
        config.workspace_dir_path = ws_data.ws_dir_path
        config.workspace_config_file_path = ws_data.ws_config_file_path

        # Step 2: Get the K8sManager
        k8s_manager: K8sManager = config.get_k8s_manager()
        if k8s_manager is None:
            raise K8sConfigException("K8sManager unavailable")

        # Step 3: Get the K8sResources
        k8s_resources: Dict[str, List[K8sResourceType]] = k8s_manager.read_resources(
            name_filter=target_name, type_filter=target_type
        )

        # Step 4: Prep the directory to write to
        workspace_config_file_path: Optional[Path] = ws_data.ws_config_file_path
        if workspace_config_file_path is None:
            print_error("workspace_config_file_path invalid")
            continue
        workspace_config_dir: Path = workspace_config_file_path.parent.resolve()
        if workspace_config_dir is None:
            print_error("workspace_config_dir invalid")
            continue

        resources_dir: Path = workspace_config_dir.joinpath(config.resources_dir)
        if config.env is not None:
            resources_dir = resources_dir.joinpath(config.env)
        if config.args.name is not None:
            resources_dir = resources_dir.joinpath(config.args.name)

        # delete directory to save resources if needed
        if resources_dir.exists():
            print_info(f"Deleting {str(resources_dir)}")
            if resources_dir.is_file():
                resources_dir.unlink()
            elif resources_dir.is_dir():
                delete_files_in_dir(resources_dir)
        print_info(f"Saving to {str(resources_dir)}")
        resources_dir.mkdir(exist_ok=True, parents=True)

        for rg_name, resources_list in k8s_resources.items():
            print_info(f"Processing {rg_name}")
            rg_dir: Path = resources_dir.joinpath(rg_name)
            rg_dir.mkdir(exist_ok=True)
            for resource in resources_list:
                if resource is not None:
                    resource_name = resource.get_resource_name()
                    resource_file: Path = rg_dir.joinpath(f"{resource_name}.yaml")
                    try:
                        manifest_yaml = resource.get_k8s_manifest_yaml(
                            default_flow_style=False
                        )  # use default_style='"' for debugging
                        if manifest_yaml is not None:
                            logger.debug(f"Writing {str(resource_file)}")
                            resource_file.write_text(manifest_yaml)
                    except Exception as e:
                        logger.error(f"Could not parse {resource_name}")
                        continue
        num_configs_built += 1

    print_info(f"\n# Configs built: {num_configs_built}/{num_configs_to_build}")
