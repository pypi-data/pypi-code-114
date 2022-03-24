from typing import Optional, List

from phi.conf.phi_conf import PhiWsData
from phi.utils.cli_console import (
    print_error,
    print_info,
    print_heading,
    print_info,
)
from phi.utils.log import logger
from phi.workspace.ws_enums import WorkspaceEnv


def run_command(
    command: str,
    ws_data: PhiWsData,
    target_env: WorkspaceEnv,
    target_app: Optional[str] = None,
) -> None:
    """Run a command in devbox or databox."""

    if ws_data is None or ws_data.ws_config is None:
        print_error("WorkspaceConfig invalid")
        return
    ws_config = ws_data.ws_config

    # Final run status
    run_status: bool = False
    if target_env == WorkspaceEnv.dev:
        from phi.docker.docker_operator import run_command_docker
        from phidata.infra.docker.config import DockerConfig

        docker_configs: Optional[List[DockerConfig]] = ws_config.docker
        docker_config_to_use: Optional[DockerConfig] = None
        if docker_configs is not None and isinstance(docker_configs, list):
            if len(docker_configs) == 1:
                docker_config_to_use = docker_configs[0]
            else:
                for dc in docker_configs:
                    if dc.env == target_env:
                        docker_config_to_use = dc
                        break
        if docker_config_to_use is None:
            print_error(f"No DockerConfig found for env: {target_env.value}")
            return

        ######################################################################
        # NOTE: VERY IMPORTANT TO GET RIGHT
        # Update DockerConfig data using WorkspaceConfig
        # 1. Pass down the paths from the WorkspaceConfig
        #       These paths are used everywhere from Infra to Apps
        # 2. Pass down docker_env which is used to set the env variables
        #       when running the docker command
        ######################################################################

        # The ws_dir_path is the ROOT directory for the workspace
        docker_config_to_use.workspace_root_path = ws_data.ws_dir_path
        docker_config_to_use.workspace_config_file_path = ws_data.ws_config_file_path
        docker_config_to_use.scripts_dir = ws_config.scripts_dir
        docker_config_to_use.storage_dir = ws_config.storage_dir
        docker_config_to_use.meta_dir = ws_config.meta_dir
        docker_config_to_use.products_dir = ws_config.products_dir
        docker_config_to_use.notebooks_dir = ws_config.notebooks_dir
        docker_config_to_use.workspace_config_dir = ws_config.workspace_config_dir
        docker_config_to_use.docker_env = ws_config.docker_env

        run_status = run_command_docker(
            command=command,
            docker_config=docker_config_to_use,
            target_app=target_app,
        )

    if run_status:
        print_heading("Command run success")
    else:
        print_error("Command run failure")
