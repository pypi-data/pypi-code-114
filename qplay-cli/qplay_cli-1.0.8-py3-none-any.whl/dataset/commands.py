from qplay_cli.dataset.volume import Volume
import click

@click.group()
def dataset():
    pass

@dataset.command()
def list_xvd_disks():
    vol = Volume()
    print(vol.list_xvd_disks())

@dataset.command()
@click.option('--nvme_device', default=None)
def list_nvme_volumes(nvme_device):
    vol = Volume()
    print(vol.list_nvme_volumes(nvme_device))

@dataset.command()
@click.option('--dataset_type', default=None)
def mount_dataset(dataset_type):
    vol = Volume()
    vol.mount_dataset(dataset_type)

@dataset.command()
def unmount_datasets():
    vol = Volume()
    vol.unmount_datasets()