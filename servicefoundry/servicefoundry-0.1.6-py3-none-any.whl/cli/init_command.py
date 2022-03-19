import logging
import os
import os.path

import click
import questionary

from ..build.util import create_file_from_content
from .servicedef.servicedef_generator import generate_service_def

logger = logging.getLogger(__name__)


def get_init_command():
    @click.command(help="Initialize new service for servicefoundry")
    def init():
        # Prompt for name (default to user class name)
        service_name: str = click.prompt(
            "Enter the name of the service",
            type=click.STRING,
            default=os.path.basename(os.getcwd()),
        )
        service_name = service_name.lower()

        service_type = questionary.select(
            "Select build would you prefer?",
            choices=[
                "FastAPIBuild",
                "StreamLitBuild",
                "DockerBuild",
            ],
        ).ask()
        build_type = None
        build_dict = {}

        if service_type == "DockerBuild":
            print("Sorry build is not available")
        elif service_type == "StreamLitBuild":
            print("Sorry build is not available")

        elif service_type == "FastAPIBuild":
            build_type = "service_auto_build"
            build_dict["version"] = ask_python_version()

            fastapi_service_ready = questionary.select(
                "Do you have a FastAPI service file ready?",
                choices=["Yes", "GenerateHelloWorld"],
            ).ask()

            if fastapi_service_ready == "Yes":
                build_dict["service_file"]: str = click.prompt(
                    "Provide the location of fastapi service file:",
                    type=click.Path,
                )
            else:
                build_dict["service_file"]: str = click.prompt(
                    "Please provide the location for generating sample fastapi service file:",
                    type=click.STRING,
                    default=f"{service_name}.py",
                )

            build_dict["packages"] = ask_requirement_file()

        stages = (
            questionary.select(
                "Which deployment stage would you prefer?",
                choices=[
                    "Beta",
                    "Beta|Prod",
                    "Beta|Gamma",
                    "Beta|Gamma|Prod",
                ],
            )
            .ask()
            .split("|")
        )

        stage_params = {}
        for stage in stages:
            stage_params[stage] = {}
            stage_params[stage]["namespace"]: str = click.prompt(
                f"Please provide the workspace name of {stage} stage?",
                type=click.STRING,
                default=f"MyWorkspace",
            )

        generate_service_def(
            service_name=service_name,
            build_type=build_type,
            build_dict=build_dict,
            stage_params=stage_params,
        )

    def ask_requirement_file():
        if os.path.exists("requirements.txt"):
            return "requirements.txt"

        else:
            requirement_choice: str = questionary.select(
                "Do you have requirements.txt?",
                choices=[
                    "Yes",
                    "CreateRequirementFile",
                    "AutoPackage(Get dependency from code dependency)",
                ],
            ).ask()

            if requirement_choice == "Yes":
                return click.prompt(
                    "Please provide the path of requirement.txt?",
                    type=click.Path,
                )
            elif requirement_choice == "CreateRequirementFile":
                create_file_from_content("requirements.txt", "")
                return "requirements.txt"
            else:
                return "auto"

    def ask_python_version():
        return questionary.select(
            "Which python version do you want to use?",
            choices=[
                "python:3.7",
                "python:3.8",
                "python:3.9",
                "python:3.10",
                "python:3.11",
                "python:3.12",
                "python:3.13",
                "python:3.14",
            ],
        ).ask()

    return init
