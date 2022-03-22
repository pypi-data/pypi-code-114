import argparse
import os
import sys
import requests
import subprocess
import git
import re
from uesm.uepath import UEPath

token = os.getenv("GITLAB_PRIVATE_TOKEN")

_gitlab_url = "https://technoarcheologist.iceseed.com"
_endpoint_projects = "{URL}/api/v4/groups/{GROUP}/projects/"

UnrealVersion = "5.0"
RepoNameSpace = "{_gitlab_url}/unreal-samples/".format(_gitlab_url=_gitlab_url)

paths = UEPath(UnrealVersion)


def get_request(url, page_number=1):
    openurl = url + "?page={page_number}".format(page_number=page_number)
    response = requests.get(openurl, headers={'PRIVATE-TOKEN': token})
    json_data = response.json()
    if response.headers["x-next-page"]:
        next_page = int(response.headers["x-next-page"])
        if page_number < next_page:
            resp2 = get_request(url, page_number + 1)
            json_data.extend(resp2)
    return json_data


def parse_args(args):
    parser = argparse.ArgumentParser(description='Arguments for script.')
    parser.add_argument('-v', '--version', type=str, default="5.0")
    return parser.parse_args(args)


def main(argv=None):
    global UnrealVersion
    global paths
    """The main entry point to coverage.py.
    This is installed as the script entry point.
    """

    args = parse_args(sys.argv[1:])

    if re.search('pytest', sys.argv[0]):
        args = parse_args([])

    if args.version is not None:
        UnrealVersion = args.version

    paths = UEPath(UnrealVersion)

    engine_binaries_path, engine_samples_path = paths.engine_binaries_path, paths.engine_samples_path

    # Use a breakpoint in the code line below to debug your script.
    print(f'Processing Samples for Unreal Engine {UnrealVersion}')  # Press ⌘F8 to toggle the breakpoint.
    os.chdir(engine_binaries_path)

    r = get_request(_endpoint_projects.format(URL=_gitlab_url, GROUP=10))
    data_json = r

    for p in data_json:
        res, response_file = update_sample(engine_samples_path, p)

        update_paths(response_file)

        subprocess.call(["./UnrealPak",
                         "../../../FeaturePacks/{res}.upack".format(res=res),
                         "-Create=../../../Samples/{res}/responsefile.txt".format(res=res)],
                        cwd=engine_binaries_path)


def update_paths(response_file):
    global paths
    with open(response_file, 'r') as file:
        data = file.read()
        data = paths.fix_paths(data)
    with open(response_file, 'w') as file:
        file.write(data)


def update_sample(engine_samples_path, sample):
    repo_path, res, sample_path, response_file = get_repo_paths(engine_samples_path, sample)
    if os.path.isdir(sample_path):
        print("Repo already exists, updating")
        repo = git.Repo(sample_path)
        repo.git.pull()
    else:
        repo = git.Repo.clone_from(repo_path, sample_path)
    return res, response_file


def get_repo_paths(engine_samples_path, sample):
    print("Processing {sample}".format(sample=sample['name']))
    init, *temp = sample['name'].split('-')
    res = ''.join([init.title(), *map(str.title, temp)])
    sample_path = os.path.join(engine_samples_path, res)
    repo_path = os.path.join(RepoNameSpace, sample['name'])
    response_file = os.path.join(sample_path, "responsefile.txt")
    return repo_path, res, sample_path, response_file
