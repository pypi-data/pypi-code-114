import json
import click
import random
import questionary

import autodl
from common._version import __version__
from cli.examples import example_model_names
from cli.analyze import analyze_model_file

from common.config.s3 import use_environment
from common.config.settings import supported_quants, supported_domains, supported_batch_sizes, Environment

@click.group()
@click.version_option(version=__version__)
def main():
    pass

# cannot use click prompt kwargs feature for the command options, because we want to infer input dimensions and the model name
def prompt_for_missing_model_info(
    model_name, quantization, domain, task, channels, width, height, batch_size,
    inferred_model_name, inferred_quantization, inferred_channels, inferred_width, inferred_height, inferred_batch_size
):
    # TODO - attempt reading model details from some configCache files
    if model_name is None:
        model_name = questionary.text(
            f"Please give a name to your model to be used in AutoDL (for example: '{random.choice(example_model_names)}')\n  Model name:",
            validate=lambda name: len(name) > 0,
            default=inferred_model_name,
        ).unsafe_ask()
    if quantization is None:
        quantization = questionary.select(
            "Choose quantization for the model",
            choices=supported_quants,
            use_shortcuts=True,
            default=inferred_quantization,
        ).unsafe_ask()
    if domain is None:
        doms = [dom['domain'] for dom in supported_domains]
        domain = questionary.select(
            "Choose problem domain for the model",
            choices=doms,
            use_shortcuts=True,
        ).unsafe_ask()
    if task is None:
        dom_tasks = [task for dom in supported_domains if dom['domain'] == domain for task in dom['tasks']]
        task = questionary.select(
            "Choose task type for the model",
            choices=dom_tasks,
            use_shortcuts=True,
        ).unsafe_ask()
    if channels is None:
        channels = questionary.text(
            "Specify channel count for the model input",
            validate=lambda name: name.isnumeric(),
            default=str(inferred_channels) if inferred_channels else '',
        ).unsafe_ask()
    if width is None:
        width = questionary.text(
            "Specify input width for the model",
            validate=lambda name: name.isnumeric(),
            default=str(inferred_width) if inferred_width else '',
        ).unsafe_ask()
    if height is None:
        height = questionary.text(
            "Specify input height for the model",
            validate=lambda name: name.isnumeric(),
            default=str(inferred_height) if inferred_height else '',
        ).unsafe_ask()
    if batch_size is None:
        batch_size = questionary.select(
            "Specify input batch size for the model",
            choices = [str(bs) for bs in supported_batch_sizes],
            use_shortcuts=True,
            default=str(inferred_batch_size) if inferred_batch_size else None,
        ).unsafe_ask()

    return model_name, quantization, domain, task, channels, width, height, batch_size


@main.command()
@click.argument('model_file_path')
@click.argument('model_script_args', nargs=-1)
@click.option('-n', '--name', 'model_name',
    help="Name of the model to be used in AutoDL.",
)
@click.option('-e', '--environment', '--env',
    type=click.Choice(Environment.__members__, case_sensitive=False),
    default='production',
    callback=lambda c, p, v: getattr(Environment, v),
    help="Environment to upload the model to.",
)
@click.option('-q', '--quantization', '--quants',
    type=click.Choice(supported_quants, case_sensitive=False),
    help="Quantization for the model.",
)
@click.option('-d', '--domain',
    type=click.Choice([dom['domain'] for dom in supported_domains], case_sensitive=False),
    help="Domain of the problem the model is addressing.",
)
@click.option('-t', '--task',
    type=click.Choice([task for dom in supported_domains for task in dom['tasks']], case_sensitive=False),
    help="The task type the model is solving.",
)
@click.option('-c', '--channels',
    type=int,
    help="The channel count for the model input.",
)
@click.option('-w', '--width',
    type=int,
    help="The model input width.",
)
@click.option('-h', '--height',
    type=int,
    help="The model input height.",
)
@click.option('-b', '--batch_size',
    type=int,
    help="The model input batch_size to benchmark for.",
)
@click.option('-y', '--yes', 'auto_confirm', is_flag=True, help="Skip all confirmation input from the user.")
def submit_model(model_file_path,
                model_script_args,
                model_name,
                auto_confirm,
                quantization,
                domain,
                task,
                channels,
                width,
                height,
                batch_size,
                **kwargs):
    # Priority: flags, then configCache, then inference, then interactive user input
    environment = kwargs['environment']
    use_environment(environment)

    model_file, inferred_model_name, framework, inferred_quantization, inferred_channels, inferred_width, inferred_height, inferred_batch_size = analyze_model_file(model_file_path, model_script_args)

    model_name, quantization, domain, task, channels, width, height, batch_size = prompt_for_missing_model_info(
        model_name, quantization, domain, task, channels, width, height, batch_size,
        inferred_model_name, inferred_quantization, inferred_channels, inferred_width, inferred_height, inferred_batch_size
    )
    model_config = {
        "name": model_name,
        "framework": framework,
        "quantization": quantization,
        "from_onspecta": False, # TODO we should disallow this param in the API
        "domain": domain,
        "task": task,
        "channels": channels,
        "height": height,
        "width": width,
        "batch_size": batch_size,
    }

    if not auto_confirm:
        click.confirm(
            text = "\n"
                + "The details for your model are as follows:\n"
                + f"{json.dumps(model_config, indent=4)}\n"
                + "\n"
                + "Are you sure you want to upload that to AutoDL?",
            abort=True,
            default=True
        )

    model_link = autodl.uploadModel(model_config, model_file)
    print(f'Done! See {model_link}')

if __name__ == '__main__':
    main()
