import os
import subprocess
from tuxbake.exceptions import TuxbakeRunCmdError


def repo_init(oebuild, src_dir, local_manifest=None):
    cmd = f"repo init -u {oebuild.repo.url} -b {oebuild.repo.branch} -m {oebuild.repo.manifest}".split()
    run_cmd(cmd, src_dir, fail_ok=False)
    if local_manifest:
        cmd = f"cp {local_manifest} .repo/manifests/{oebuild.repo.manifest}".split()
        run_cmd(cmd, src_dir, fail_ok=False)
    cmd = "repo sync -j16".split()
    run_cmd(cmd, src_dir, fail_ok=False)
    cmd = "repo manifest -r -o pinned-manifest.xml".split()
    run_cmd(cmd, src_dir, fail_ok=False)


def git_init(oebuild, src_dir):
    for git_object in oebuild.git_trees:
        url = git_object.url
        branch = git_object.branch
        ref = git_object.ref
        sha = git_object.sha
        basename = os.path.splitext(os.path.basename(url))[0]
        if branch:
            cmd = f"git clone {url} -b {branch}".split()
        else:
            cmd = f"git clone {url}".split()
        run_cmd(cmd, src_dir, fail_ok=False)
        if ref:
            cmd = f"git fetch origin {ref}:{ref}".split()
            run_cmd(cmd, f"{src_dir}/{basename}", fail_ok=False)
            cmd = f"git checkout {ref}".split()
            run_cmd(cmd, f"{src_dir}/{basename}", fail_ok=False)
        if sha:
            cmd = f"git checkout {sha}".split()
            run_cmd(cmd, f"{src_dir}/{basename}", fail_ok=False)


def run_cmd(cmd, src_dir, env=None, fail_ok=True):
    process = subprocess.Popen(cmd, cwd=src_dir, env=env)
    process.communicate()
    if not fail_ok and process.returncode != 0:
        raise TuxbakeRunCmdError(f"Failed to run: {' '.join(cmd)}")
