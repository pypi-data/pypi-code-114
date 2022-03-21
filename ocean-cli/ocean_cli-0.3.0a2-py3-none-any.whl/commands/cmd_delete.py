import click
import inquirer

from ocean import api, code, utils
from ocean.main import pass_env
from ocean.commands import cmd_get
from ocean.utils import NotRequiredIf, sprint, PrintType


@click.group(cls=utils.AliasedGroup)
def cli():
    pass


@cli.command()
@pass_env
def image(ctx):
    req = cmd_get._image(ctx)
    items = [item for item in req.items if item[0] != "public"]
    if len(items) <= 0:
        sprint("No images to delete.", PrintType.FAILED)
        return

    choices = [req.fstring.format(*item) for item in items]
    choice = inquirer.list_input("Images", choices=choices)
    name = items[choices.index(choice)][-2]
    sprint(name)

    _image(ctx, name)
    sprint(f"Image Deleted.", PrintType.SUCCESS)


def _image(ctx, name):
    data = {"imageName": name, "imageType": "user"}
    api.delete(ctx, code.API_IMAGE, data=data)


# Workloads
@cli.command()
@click.option("-A", "--all", is_flag=True, help="Delete all instances.")
@click.option(
    "-n",
    "--name",
    # prompt=True,
    cls=NotRequiredIf,
    not_required_if="all",
    help="instance name to delete.",
)
@pass_env
def instance(ctx, name, all):

    if name:
        name = name.split(",")
    else:
        name = []

    res = api.get(ctx, code.API_INSTANCE)
    body = utils.dict_to_namespace(res.json())

    for pod in body.pods:
        if all or (pod.name in name):
            res = api.delete(
                ctx,
                code.API_INSTANCE,
                data={"podUid": pod.podUid, "serviceUid": pod.serviceUid},
            )
            sprint(f"Instance `{pod.name}` Deleted.", PrintType.SUCCESS)
            if not all:
                name.remove(pod.name)

    if len(name) > 0:
        sprint(f"Instance `{', '.join(name)}` not found.", PrintType.FAILED)
    return


@cli.command()
@click.option("-A", "--all", is_flag=True, help="Delete all jobs.")
@click.option(
    "-n",
    "--name",
    prompt=True,
    cls=NotRequiredIf,
    not_required_if="all",
    help="job name to delete.",
)
@pass_env
def job(ctx, name, all):
    if all:
        res = api.get(ctx, code.API_JOB)
        body = utils.dict_to_namespace(res.json())
        names = [jobInfo.name for jobInfo in body.jobsInfos]
    else:
        if name:
            names = name.split(",")

    for job in names:
        _job(ctx, job)


def _job(ctx, name=None):
    # get jobs
    job_ids = []

    res = api.get(ctx, code.API_JOB)
    body = utils.dict_to_namespace(res.json())
    for jobInfo in body.jobsInfos:
        if jobInfo.name == name:
            job_ids = list(map(lambda x: f"{x.uid}", jobInfo.jobs))
            break
    else:
        sprint(f"Job `{name}` not found.", PrintType.FAILED)
        return
    res = api.delete(ctx, code.API_JOB, data={"jobUids": job_ids})
    sprint(f"Job `{name}` Deleted.", PrintType.SUCCESS)


@cli.command()
@click.option("--name", "-n", required=True, help="volume name.")
@pass_env
def volume(ctx, name):

    volname = api.get_volume_id_from_volume_name(ctx, name)
    if volname:
        api.delete(ctx, f"{code.API_VOLUME}/{volname}")
        sprint(f"Volume `{name}` Created.", PrintType.SUCCESS)
        return

    sprint(f"Volume `{name}` not found.", PrintType.FAILED)


@cli.command()
@click.option("-A", "--all", is_flag=True, help="Delete all requests.")
@pass_env
def request(ctx, all):
    req = cmd_get._request(ctx)
    uids = []
    if all:
        uids = [item[-1] for item in req.items]
    else:
        choices = [req.fstring.format(*item) for item in req.items]
        choice = inquirer.list_input("Request", choices=choices)
        uids = [req.items[choices.index(choice)][-1]]

    for uid in uids:
        _request(ctx, uid)
    sprint(f"Request Deleted.", PrintType.SUCCESS)


def _request(ctx, uid):
    res = api.delete(ctx, f"{code.API_REQUEST}/{uid}")


# CLI ENV
@cli.command()
@click.option("--name", "-n", required=True, help="preset name.")
@pass_env
def preset(ctx, name):
    _preset(ctx, name)
    sprint(f"Preset `{name}` Deleted.", PrintType.SUCCESS)


def _preset(ctx, name):
    ctx.delete_presets(name)
