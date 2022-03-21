import click
from datetime import datetime, timezone

from ocean import api, code, utils
from ocean.main import pass_env
from ocean.utils import sprint, PrintType


@click.group(cls=utils.AliasedGroup)
def cli():
    pass


# Workloads
@cli.command()
@pass_env
def instance(ctx):
    content = _instance(ctx, email=ctx.get_email())

    sprint(content.fstring.format(*content.header))
    for item in content.items:
        sprint(content.fstring.format(*item))


def _instance(ctx=None, body=None, email=None):
    if body is None:
        res = api.get(ctx, code.API_INSTANCE)
        body = utils.dict_to_namespace(res.json())

    content = utils.dict_to_namespace(
        {
            "fstring": "{:20} {:20} {:15} {:15} {:10}",
            "header": ["NAME", "STATUS", "TYPE", "VOLUME", "SSH PORT"],
            "items": [],
        }
    )

    for pod in body.pods:
        if email is not None and pod.annotations.email != email:
            continue

        content.items.append(
            [
                pod.name,
                pod.status,
                pod.labels.machineType.name,
                pod.volumes[0].persistentVolumeClaim.claimName,
                str(pod.nodePort),
            ]
        )

    return content


@cli.command()
@click.option("-d", "--detail", help="Show selected sub tasks detail")
@click.option(
    "-A",
    "--detail-all",
    is_flag=True,
    help="Show all sub tasks detail. `--detail` option will be ignored.",
)
@pass_env
def job(ctx, detail=None, detail_all=None):
    content = _job(ctx, detail, detail_all, email=ctx.get_email())
    sprint(content.fstring.format(*content.header))
    for item in content.items:
        sprint(content.fstring.format(*item[:-1]))
        if item[-1] != "":
            sprint(item[-1])


def _job(ctx=None, detail=None, detail_all=None, body=None, email=None):
    detail = detail.split(",") if detail else None

    # conditions
    print_detail = detail or detail_all
    print_simple = (detail is None) and (not detail_all)
    filter_job = lambda x: print_simple or detail_all or (x in detail)

    # api call
    if body is None:
        res = api.get(ctx, "/api/jobs/")
        body = utils.dict_to_namespace(res.json())

    content = utils.dict_to_namespace(
        {
            "fstring": "{:20} {:4} {:4} {:4} {:4} {:7} {:15} {:15} {:50} {:20}",
            "header": [
                "NAME",
                "WAIT",
                "RUN",
                "SUCC",
                "FAIL",
                "UNKNOWN",
                "TYPE",
                "VOLUME",
                "IMAGE",
                "COMMAND",
            ],
            "items": [],
        }
    )

    for jobInfo in body.jobsInfos:
        if email is not None and jobInfo.annotations.email != email:
            continue

        if not filter_job(jobInfo.name):
            continue

        pending, running, succeeded, failed, unknown = 0, 0, 0, 0, 0
        details = []
        for job in jobInfo.jobs:
            if len(job.jobPodInfos) > 0:
                status = job.jobPodInfos[0].status
                if status in ["Pending"]:
                    pending += 1
                elif status in ["Running", "ContainerCreating"]:
                    running += 1
                elif status == "Succeeded":
                    succeeded += 1
                else:
                    failed += 1
            else:
                unknown += 1

            if print_detail:
                start_time = utils.convert_time(job.startTime)
                complete_time = utils.convert_time(job.completionTime)
                delta = 0
                if status == "Running":
                    delta = (
                        datetime.now(timezone.utc).replace(microsecond=0) - start_time
                    )
                elif status == "Succeeded":
                    delta = complete_time - start_time

                start_time = utils.date_format(start_time)
                complete_time = utils.date_format(complete_time)

                details.append(
                    f"{job.name:20} {job.jobPodInfos[0].status:10} {start_time} ~ {complete_time} ({delta})"
                )

        content.items.append(
            (
                jobInfo.name,
                str(pending),
                str(running),
                str(succeeded),
                str(failed),
                str(unknown),
                jobInfo.labels.machineType.name,
                jobInfo.volumes[0].persistentVolumeClaim.claimName,
                jobInfo.image,
                jobInfo.command,
                "\n".join(details),
            )
        )

    return content


@cli.command()
@pass_env
def volume(ctx):
    content = _volume(ctx, email=ctx.get_email())

    sprint(content.fstring.format(*content.header))
    for item in content.items:
        sprint(content.fstring.format(*item))


def _volume(ctx=None, body=None, email=None):
    if body is None:
        res = api.get(ctx, "/api/volumes/")
        body = utils.dict_to_namespace(res.json())

    content = utils.dict_to_namespace(
        {
            "fstring": "{:20} {:10} {:10}",
            "header": ["NAME", "STATUS", "CAPACITY"],
            "items": [],
        }
    )

    for vol in body.volumes:
        if email is not None and vol.annotations.email != email:
            continue

        content.items.append([vol.name, vol.status, vol.capacity])

    return content


# Resources
@cli.command()
@pass_env
def image(ctx):
    content = _image(ctx)

    sprint(content.fstring.format(*content.header))
    for item in content.items:
        sprint(content.fstring.format(*item))


def _image(ctx, email=None):
    content = utils.dict_to_namespace(
        {
            "fstring": "{:11} {:10} {:80} {}",
            "header": ["TYPE", "STATUS", "IMAGE", "LABLES"],
            "items": [],
        }
    )

    # public, user images
    res = api.get(ctx, "/api/images/")
    body = utils.dict_to_namespace(res.json())

    images_list = body.public + body.user

    # snapshot
    res = api.get(ctx, "/api/instances")

    for uid in map(lambda x: x["podUid"], res.json()["pods"]):
        res = api.get(ctx, f"/api/images/commit/{uid}")
        body = res.json()

        images_list += utils.dict_to_namespace(body["workHistory"][uid]["images"])

    # insert
    for img in images_list:
        if email is not None and img.annotations.email != email:
            continue
        content.items.append(
            [img.imageType, img.imageStatus, img.imageName, ",".join(img.imageLabels)]
        )

    return content


@cli.command()
@pass_env
def quota(ctx):
    content = _quota(ctx)

    sprint(content.fstring.format(*content.header))
    for item in content.items:
        sprint(content.fstring.format(*item))


def _quota(ctx=None, body=None):
    if body is None:
        res = api.get(ctx, code.API_USERS_RESOURCES)
        body = utils.dict_to_namespace(res.json())

    content = utils.dict_to_namespace(
        {
            "fstring": "{:20} {:10} {:100}",
            "header": ["MACHINETYPE", "QUOTA", "SPEC"],
            "items": [],
        }
    )

    for mt in body.machineTypes:
        content.items.append(
            [
                mt.name,
                f"{mt.quotaUsedIn}/{mt.quota}",
                f"CPU {mt.cpus:2}, MEM {mt.memory:3} Gi, GPU {mt.gpus:1} x {mt.gpuType}",
            ]
        )

    return content


@cli.command()
@pass_env
def request(ctx):
    content = _request(ctx, email=ctx.get_email())

    sprint(content.fstring.format(*content.header))
    for item in content.items:
        sprint(content.fstring.format(*item))


def _request(ctx, body=None, email=None):
    if body is None:
        res = api.get(ctx, code.API_REQUEST)
        body = utils.dict_to_namespace(res.json())

    content = utils.dict_to_namespace(
        {
            "fstring": "{:10} {:20} {:10} {:12} {:12} {:50}",
            "header": [
                "STATUS",
                "MACHINETYPE",
                "QUOTA",
                "START",
                "END",
                "REJECTED REASON",
            ],
            "items": [],
        }
    )

    for req in body:
        if email is not None and req.user.email != email:
            continue
        content.items.append(
            [
                req.status,
                req.machineType.name,
                str(req.quota),
                req.startDate[:10],
                req.endDate[:10],
                f"{req.rejectedReason}",
                req.id,
            ]
        )

    return content


@cli.command()
@pass_env
def machine_type(ctx):
    content = _machine_type(ctx)

    sprint(content.fstring.format(*content.header))
    for item in content.items:
        sprint(content.fstring.format(*item))


def _machine_type(ctx):
    res = api.get(ctx, "/api/machinetypes/")

    body = utils.dict_to_namespace(res.json())

    content = utils.dict_to_namespace(
        {"fstring": "{:20} {:100}", "header": ["NAME", "SPEC"], "items": []}
    )

    for mt in body:
        content.items.append(
            [
                mt.name,
                f"CPU {mt.cpus:4}, MEM {mt.memory:5} Gi, GPU {mt.gpus:1} x {mt.gpuType}",
                mt.id,
            ]
        )
    return content


# CLI ENV
@cli.command()
@pass_env
def preset(ctx):
    _preset(ctx)


def _preset(ctx, show_id=False):
    fstring = "{:20} {:15} {:10} {:40}"
    fstring = "{id:5} " + fstring if show_id else fstring

    sprint(fstring.format("NAME", "TYPE", "VOLUME", "IMAGE", id="ID"))
    for preset in utils.dict_to_namespace(ctx.get_presets()):
        default_txt = " (default)" if preset.default else ""
        sprint(
            fstring.format(
                preset.name + default_txt,
                preset.machineType,
                preset.volume,
                f"{preset.image} ({preset.imageType})",
            )
        )
