# -*- coding: utf-8 -*-

from dataclasses import asdict, dataclass, field, fields
from typing import Dict, List
from tuxmake.runtime import Runtime
from tuxbake.utils import (
    repo_init,
    git_init,
)
from pathlib import Path
import json
import subprocess
import os
import sys
import shlex


class Base:
    def as_dict(self):
        return asdict(self)

    def as_json(self):
        return json.dumps(self.as_dict())

    @classmethod
    def new(cls, **kwargs):
        fields_names = [f.name for f in fields(cls)]
        i_kwargs = {}
        v_kwargs = {}
        for k in kwargs:
            if k in fields_names:
                v_kwargs[k] = kwargs[k]
            else:
                i_kwargs[k] = kwargs[k]

        return cls(**v_kwargs, extra=i_kwargs)


@dataclass
class OEBuild(Base):
    src_dir: str
    build_dir: str
    envsetup: str
    target: str
    distro: str = None
    machine: str = None
    container: str = None
    environment: Dict = field(default_factory=dict)
    local_conf: List[str] = None
    bblayers_conf: List[str] = None
    sources: List[Dict] = None
    sstate_mirror: str = None
    dl_dir: str = None
    extra: Dict = None
    __logger__ = None
    repo: Dict = None
    git_trees: List = None
    local_manifest: str = None

    @dataclass
    class Repo:
        url: str
        branch: str
        manifest: str

    @dataclass
    class Git:
        url: str
        branch: str = None
        ref: str = None
        sha: str = None

    def __post_init__(self):
        self.runtime = None
        self.log_dir = self.src_dir
        if self.sources.get("repo"):
            self.repo = self.Repo(**self.sources.get("repo"))
        elif self.sources.get("git_trees"):
            self.git_trees = []
            for git_entry in self.sources.get("git_trees"):
                self.git_trees.append(self.Git(**git_entry))

    def validate(self):
        return

    def __prepare__(self):
        os.makedirs(self.src_dir, exist_ok=True)
        os.makedirs(self.log_dir, exist_ok=True)
        if self.sources.get("repo"):
            repo_init(self, self.src_dir, self.local_manifest)
        else:
            git_init(self, self.src_dir)

    def prepare(self):
        self.__prepare__()
        self.runtime = Runtime.get("docker")
        self.runtime.source_dir = Path(self.src_dir)
        self.runtime.basename = "build"
        self.runtime.set_image(f"docker.io/vishalbhoj/{self.container}")
        self.runtime.output_dir = Path(self.log_dir)
        if self.dl_dir:
            self.runtime.add_volume(self.dl_dir)
        environment = self.environment
        environment["MACHINE"] = self.machine
        environment["DISTRO"] = self.distro
        self.runtime.environment = environment

        self.runtime.prepare()
        with open(
            f"{os.path.abspath(self.src_dir)}/extra_local.conf", "w"
        ) as extra_local_conf:
            if self.dl_dir:
                extra_local_conf.write(f'DL_DIR = "{self.dl_dir}"\n')
            if self.sstate_mirror:
                extra_local_conf.write(f'SSTATE_MIRRORS ?= "{self.sstate_mirror}"\n')
                extra_local_conf.write(
                    'USER_CLASSES += "buildstats buildstats-summary"\n'
                )
            if self.local_conf:
                for line in self.local_conf:
                    extra_local_conf.write(f"{line}\n")

        if self.bblayers_conf:
            with open(
                f"{os.path.abspath(self.src_dir)}/bblayers.conf", "w"
            ) as bblayers_conf_file:
                for line in self.bblayers_conf:
                    bblayers_conf_file.write(f"{line}\n")
        return

    def do_build(self):
        cmd = [
            "bash",
            "-c",
            f"source {self.envsetup} {self.build_dir}; cat ../extra_local.conf >> conf/local.conf; cat ../bblayers.conf >> conf/bblayers.conf || true; echo 'Dumping local.conf..'; cat conf/local.conf; bitbake -e > bitbake-environment; bitbake {self.target}",
        ]
        if self.runtime.run_cmd(cmd):
            self.result = "pass"
        else:
            self.result = "fail"

    def do_cleanup(self):
        if self.runtime:
            self.runtime.cleanup()
