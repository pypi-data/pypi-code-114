import enum
import json
import os
import random
import sys

import autodl
import click
from autodl import Environment
from cli.analyze import analyze_model_file
from cli.examples import example_model_names

from common.config import settings


@click.group()
@click.version_option(version="0.2.0")
def main():
    pass


def prompt_for_missing_model_info(
    model_name,
    quantization,
    domain,
    task,
    channels,
    width,
    height,
    batch_size,
    inferred_model_name,
    inferred_quantization,
    inferred_channels,
    inferred_width,
    inferred_height,
    inferred_batch_size,
):
    # TODO - attempt reading model details from some configCache files
    if model_name is None:
        model_name = click.prompt(
            f"Please give a name to your model to be used in AutoDL (for example: '{random.choice(example_model_names)}')\nModel name",
            type=str,
            default=inferred_model_name,
        )
    if quantization is None:
        quantization = click.prompt(
            "Choose quantization for the model",
            type=click.Choice(settings.supported_quants, case_sensitive=False),
            default=inferred_quantization,
        )
    if domain is None:
        doms = [dom["domain"] for dom in settings.supported_domains]
        domain = click.prompt(
            "Choose problem domain for the model",
            type=click.Choice(doms, case_sensitive=False),
            default=doms[0],
        )
    if task is None:
        dom_tasks = [
            task
            for dom in settings.supported_domains
            if dom["domain"] == domain
            for task in dom["tasks"]
        ]

        task = click.prompt(
            "Choose task type for the model",
            type=click.Choice(dom_tasks, case_sensitive=False),
            default=dom_tasks[0],
        )
    if channels is None:
        channels = click.prompt(
            "Specify channel count for the model input",
            type=int,
            default=inferred_channels,
        )
    if width is None:
        width = click.prompt(
            "Specify input width for the model",
            type=int,
            default=inferred_width,
        )
    if height is None:
        height = click.prompt(
            "Specify input height for the model",
            type=int,
            default=inferred_height,
        )
    if batch_size is None:
        batch_size = click.prompt(
            "Specify input batch size for the model",
            type=int,
            default=inferred_batch_size,
        )

    return (
        model_name,
        quantization,
        domain,
        task,
        channels,
        width,
        height,
        batch_size,
    )


@main.command()
@click.argument("model_file_path")
@click.option(
    "-n", "--name", "model_name", help="Name of the model to be used in AutoDL."
)
@click.option(
    "-e",
    "--environment",
    "--env",
    type=click.Choice(Environment.__members__, case_sensitive=False),
    default="production",
    callback=lambda c, p, v: getattr(Environment, v),
    help="Environment to upload the model to.",
)
@click.option(
    "-q",
    "--quantization",
    "--quants",
    type=click.Choice(settings.supported_quants, case_sensitive=False),
    help="Quantization for the model.",
)
@click.option(
    "-d",
    "--domain",
    type=click.Choice(
        [dom["domain"] for dom in settings.supported_domains],
        case_sensitive=False,
    ),
    help="Domain of the problem the model is addressing.",
)
@click.option(
    "-t",
    "--task",
    type=click.Choice(
        [task for dom in settings.supported_domains for task in dom["tasks"]],
        case_sensitive=False,
    ),
    help="The task type the model is solving.",
)
@click.option(
    "-c", "--channels", type=int, help="The channel count for the model input."
)
@click.option("-w", "--width", type=int, help="The model input width.")
@click.option("-h", "--height", type=int, help="The model input height.")
@click.option(
    "-b",
    "--batch_size",
    type=int,
    help="The model input batch_size to benchmark for.",
)
@click.option(
    "-y",
    "--yes",
    "auto_confirm",
    is_flag=True,
    help="Skip all confirmation input from the user.",
)
def submit_model(
    model_file_path,
    model_name,
    auto_confirm,
    quantization,
    domain,
    task,
    channels,
    width,
    height,
    batch_size,
    **kwargs,
):
    # Priority: flags, then configCache, then inference, then interactive user input
    environment = kwargs["environment"]
    autodl.use_environment(environment)

    (
        model_file,
        inferred_model_name,
        framework,
        inferred_quantization,
        inferred_channels,
        inferred_width,
        inferred_height,
        inferred_batch_size,
    ) = analyze_model_file(model_file_path)

    (
        model_name,
        quantization,
        domain,
        task,
        channels,
        width,
        height,
        batch_size,
    ) = prompt_for_missing_model_info(
        model_name,
        quantization,
        domain,
        task,
        channels,
        width,
        height,
        batch_size,
        inferred_model_name,
        inferred_quantization,
        inferred_channels,
        inferred_width,
        inferred_height,
        inferred_batch_size,
    )
    model_config = {
        "name": model_name,
        "framework": framework,
        "quantization": quantization,
        "from_onspecta": False,  # TODO we should disallow this param in the API
        "domain": domain,
        "task": task,
        "channels": channels,
        "height": height,
        "width": width,
        "batch_size": batch_size,
    }

    if not auto_confirm:
        click.confirm(
            text="\n"
            + "The details for your model are as follows:\n"
            + f"{json.dumps(model_config, indent=4)}\n"
            + "\n"
            + "Are you sure you want to upload that to AutoDL?",
            abort=True,
            default=True,
        )

    model_link = autodl.uploadModel(model_config, model_file)
    print(f"Done! See {model_link}")


if __name__ == "__main__":
    main()
