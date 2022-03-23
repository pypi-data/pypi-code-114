#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --
# ansible-roles-ctl, manage installation and upgrade of Ansible roles
# Copyright (C) 2016-2020  Marc Dequènes (Duck)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ++
# You can find the code here: https://gitlab.com/osas/ansible-roles-ctl

VERSION = "2.0.0"


# PYTHON_ARGCOMPLETE_OK
import argcomplete, argparse
from argcomplete.completers import ChoicesCompleter, SuppressCompleter
import yaml
import os.path
import re
import shutil
import time
import ansible.constants as C
import git
from git import Commit, Reference
from git.repo import Repo
from git.exc import GitCommandError, BadName
from pkg_resources import parse_version
from pathlib import Path
import abc
from typing import Dict, Iterator, List, Optional, Union


# GitPython path parameter was broken
if parse_version(git.__version__) >= parse_version("3.1.10"):
    # used to ignore leftover from Galaxy installation
    GITPYTHON_DIRTY_PATHSPEC = ":!meta/.galaxy_install_info"
else:
    GITPYTHON_DIRTY_PATHSPEC = None


class AnsibleRolesCtlException(Exception):
    """AnsibleRolesCtl exceptions"""


class InvalidAnsibleReq(AnsibleRolesCtlException):
    """Ansible requirement is in an unusable state"""


class NotForUsAnsibleReq(AnsibleRolesCtlException):
    """Ansible requirement cannot be managed"""


class NonExistingAnsibleReqTarget(AnsibleRolesCtlException):
    """Ansible requirement is setup to target a non-existing tag or branch"""


class ReqOffAnsibleReq(AnsibleRolesCtlException):
    """Ansible requirement does not follow the defined tag or branch"""


class AnsibleReq(abc.ABC):

    req_type = ''

    name: str
    src: str
    scm: str
    version: str
    repo: Optional[Repo]

    def __init__(self, req_info):
        self.name = req_info['name']

        self.repo = None
        if self.isInstalled():
            try:
                self.repo = Repo(self.path)
            except Exception as e:
                pass

        # if no version specified, then HEAD is considered default
        self.version = req_info.get('version', 'HEAD')

    @property
    def type(self) -> str:
        return self.__class__.req_type

    @property
    @abc.abstractmethod
    def path(self) -> str:
        pass

    def isInstalled(self) -> bool:
        return os.path.exists(self.path)

    def localBranch(self) -> Optional[Reference]:
        assert self.repo
        if self.repo.head.is_detached:
            return None

        return self.repo.head.reference

    def localVersion(self) -> Optional[Commit]:
        assert self.repo
        try:
            return self.versionTags()[self.repo.head.commit]
        except:
            return None

    def remoteBranch(self) -> Optional[Reference]:
        assert self.repo
        if self.repo.head.is_detached:
            return None

        # used configured tracking branch if exist
        branch = self.localBranch().tracking_branch()
        if branch:
            return branch

        # or try a matching branch name in 'origin' remote
        if self.localBranch().name in self.repo.remotes.origin.refs:
            ref = self.repo.remotes.origin.refs[self.localBranch().name]
            self.localBranch().set_tracking_branch(ref)
            print(
                f"{self.type} '{self.name}' lacked tracking branch configuration, fixed"
            )
            return ref

        return None

    def isTargetingVersionTag(self) -> bool:
        if self.version in self.repo.tags:
            return True
        else:
            return False

    def testValid(self) -> None:
        if not self.src:
            raise NotForUsAnsibleReq()
        if self.scm and self.scm != "git":
            raise InvalidAnsibleReq("using an unsupported SCM")
        if not (self.scm or re.search("https?://", self.src)):
            raise InvalidAnsibleReq(f"{self.src} from Ansible Galaxy")

        # if role is not installed yet, then skip following tests
        if not self.isInstalled():
            return

        if not self.repo:
            raise InvalidAnsibleReq("not a valid SCM directory")
        if self.repo.bare:
            raise InvalidAnsibleReq("bare repository")
        if self.localBranch() is not None and self.remoteBranch() is None:
            raise InvalidAnsibleReq(
                f"on a local branch '{self.localBranch().name}' (no corresponding remote branch)"
            )

        return

    @property
    def version_commit(self):
        assert self.version

        try:
            return self.repo.commit(self.version)
        except (ValueError, BadName):
            raise NonExistingAnsibleReqTarget(
                f"targeting an unexisting branch/version ({self.version})"
            )

    def testRequirements(self) -> None:
        assert self.repo
        if self.isTargetingVersionTag():
            if self.repo.head.commit != self.version_commit:
                version = self.localVersion()
                if version:
                    raise ReqOffAnsibleReq(
                        f"on version '{version}' but not the requirements (version '{self.version}')"
                    )
                elif self.localBranch() is not None:
                    raise ReqOffAnsibleReq(
                        f"on branch '{self.localBranch().name}' but not the requirements (version '{self.version}')"
                    )
                else:
                    raise ReqOffAnsibleReq(
                        f"on a detached commit but not the requirements (version '{self.version}')"
                    )

        elif self.localBranch() is None:
            version = self.localVersion()
            if version:
                raise ReqOffAnsibleReq(
                    f"on version '{version}' but not the requirements (branch '{self.version}')"
                )
            else:
                raise ReqOffAnsibleReq(
                    f"on a detached commit but not the requirements (branch '{self.version}')"
                )

        elif self.localBranch().commit != self.version_commit:
            raise ReqOffAnsibleReq(
                f"on branch '{self.localBranch().name}' but not the requirements (branch '{self.version}')"
            )

    def fetchUpdates(self) -> None:
        assert self.repo
        self.repo.remotes.origin.fetch()

    def commitsAhead(self) -> Union[List[Commit], Iterator[Commit]]:
        assert self.repo
        if self.repo.head.is_detached:
            return []

        if self.remoteBranch().is_valid():
            return Commit.iter_items(self.repo, f"{self.remoteBranch()}..HEAD")
        else:
            return Commit.iter_items(self.repo, "HEAD")

    def commitsBehind(self) -> Union[List[Commit], Iterator[Commit]]:
        assert self.repo
        if self.repo.head.is_detached:
            return []

        if self.remoteBranch().is_valid():
            return Commit.iter_items(self.repo, f"HEAD..{self.remoteBranch()}")
        else:
            return []

    def versionTags(self) -> Dict[Commit, str]:
        assert self.repo
        list = {}
        for t in self.repo.tags:
            list[t.commit] = t.name
        return list

    def newVersions(self) -> List[str]:
        if self.localBranch() is not None:
            all_tags = self.versionTags()

            new_versions = []
            for commit in self.commitsBehind():
                if commit in all_tags:
                    new_versions.append(all_tags[commit])
            return sorted(new_versions)

        version = self.localVersion()
        if version:
            return sorted([x for x in self.versionTags().values() if x > version])

        return []

    def hasRemoteBranch(self, branch) -> bool:
        assert self.repo
        try:
            self.repo.remotes.origin.refs[branch]
            return True
        except Exception as e:
            return False

    def trackRemoteBranch(self, branch) -> None:
        assert self.repo
        if branch not in self.repo.refs:
            self.repo.create_head(branch, self.repo.remotes.origin.refs[branch])
        self.repo.heads[branch].set_tracking_branch(
            self.repo.remotes.origin.refs[branch]
        )
        self.repo.heads[branch].checkout()

    def uninstall(self) -> None:
        if not self.isInstalled():
            return

        shutil.rmtree(self.path)

    def install(self) -> bool:
        if self.isInstalled():
            return False

        self.repo = Repo.clone_from(self.src, self.path)

        # newly created empty repository
        if not self.repo.remotes.origin.refs:
            return True

        if self.isTargetingVersionTag():
            if self.version in self.repo.tags:
                self.repo.head.reference = self.version
                self.repo.head.reset(index=True, working_tree=True)
            else:
                self.uninstall()
                raise NonExistingAnsibleReqTarget(
                    f"setup to target version '{self.version}', but it does not exist"
                )

        else:
            if self.hasRemoteBranch(self.version):
                self.trackRemoteBranch(self.version)
            else:
                self.uninstall()
                raise NonExistingAnsibleReqTarget(
                    f"setup to follow branch '{self.version}', but it does not exist"
                )

        return True

    def update(self, new_target_version=None) -> bool:
        if not self.isInstalled():
            raise InvalidAnsibleReq("not yet installed")

        assert self.repo
        if self.repo.is_dirty(untracked_files=True, path=GITPYTHON_DIRTY_PATHSPEC):
            raise InvalidAnsibleReq(
                "has local changes (please commit, stash or cleanup)"
            )

        self.fetchUpdates()
        try:
            self.fetchUpdates()
        except GitCommandError as e:
            raise InvalidAnsibleReq(f"has problems fetching updates: {e}")

        new_target_tag = None
        if new_target_version:
            new_target_tag = new_target_version
        elif self.isTargetingVersionTag():
            new_target_tag = self.version

        if new_target_tag:
            if new_target_tag not in self.repo.tags:
                raise NonExistingAnsibleReqTarget(
                    f"cannot be upgraded to nonexisting version '{new_target_tag}'"
                )
            # already at target
            if self.repo.head.is_detached and self.repo.tags[new_target_tag].commit == self.repo.head.commit:
                return False

            self.repo.head.reference = new_target_tag
            self.repo.head.reset(index=True, working_tree=True)
            self.version = new_target_tag

        else:
            updated = False

            # if not on the right branch, then switch
            if self.repo.head.is_detached or self.localBranch().name != self.version:
                if self.hasRemoteBranch(self.version):
                    self.trackRemoteBranch(self.version)
                else:
                    raise NonExistingAnsibleReqTarget(
                        f"cannot be upgraded to nonexisting branch '{self.version}'"
                    )
                updated = True

            la = list(self.commitsAhead())
            lb = list(self.commitsBehind())

            if la and lb:
                raise NonExistingAnsibleReqTarget("has diverged from origin")

            if la:
                raise NonExistingAnsibleReqTarget("is ahead origin")

            # already at target
            if not lb:
                return updated

            self.repo.remotes.origin.pull()

        return True

class AnsibleRole(AnsibleReq):

    req_type = 'role'

    def __init__(self, req_info):
        self.src = req_info.get('src', None)
        self.scm = req_info.get('scm', None)
        if not self.scm:
            url_with_scm = self.src.split('+')
            if len(url_with_scm) == 2:
                self.scm = url_with_scm[0]
                self.src = url_with_scm[1]

        super().__init__(req_info)

    @property
    def path(self):
        return Path(C.DEFAULT_ROLES_PATH[0], self.name)

class AnsibleCollection(AnsibleReq):

    req_type = 'collection'

    def __init__(self, req_info):
        self.src = req_info.get('source', None)
        self.scm = req_info.get('type', None)

        super().__init__(req_info)

    @property
    def path(self):
        path_parts = list(Path(C.COLLECTIONS_PATHS[0]).parts)
        if path_parts[-1] != "ansible_collections":
            path_parts.append("ansible_collections")
        # dots defines the namespace and each component is mapped as a subdirectory
        name_parts = self.name.split('.')
        return Path(*path_parts, *name_parts)


# errors deferred for completion, returning None instead
def load_reqs_info() -> Optional[Dict[str, AnsibleReq]]:
    try:
        stream = open("requirements.yml", "r")
    except Exception as e:
        print(f"Unable to open requirements file: {e}")
        return None

    try:
        requirements = yaml.safe_load(stream)
    except Exception as e:
        print(f"Unable to load data from the requirements file: {e}")
        return None

    if requirements is None:
        print("Requirements file is empty")
        return None

    # format v1
    if isinstance(requirements, list):
        req_roles = requirements
        req_collections = []
    # format v2
    else:
        req_roles = requirements.get('roles', [])
        req_collections = requirements.get('collections', [])

    reqs = {}

    def build_reqs(req_list, req_class):
        for req_info in req_list:
            if 'name' in req_info:
                reqs[req_info["name"]] = req_class(req_info)
            else:
                print("Requirement without name detected")

    build_reqs(req_roles, AnsibleRole)
    build_reqs(req_collections, AnsibleCollection)

    return reqs


def load_reqs(args, reqs_info_list, selected_reqs) -> Dict[str, AnsibleReq]:
    req_list = {}
    for req_name, req in reqs_info_list.items():
        if selected_reqs and req_name not in selected_reqs:
            continue

        try:
            req.testValid()
        except NotForUsAnsibleReq:
            if not args.quiet:
                print(f"req '{req.name}' is managed via galaxy")
            continue
        except InvalidAnsibleReq as e:
            if not args.quiet:
                print(f"req '{req.name}' is invalid: {e}")
            continue

        req_list[req.name] = req

    return req_list


def display_changelog(commit, new_versions) -> None:
    try:
        changelog = commit.tree["CHANGELOG.yml"]
    except Exception:
        print("  no changelog file ('CHANGELOG.yml') could be found")
        return

    try:
        changelog_entries = yaml.safe_load(changelog.data_stream)
    except Exception as e:
        print(f"  changelog file ('CHANGELOG.yml') could not be parsed: {e}")
        return

    print("  changelog:")
    for version in sorted(new_versions):
        if version in changelog_entries:
            print(f"    {version}:")
            for entry in changelog_entries[version]:
                print(f"      - {entry}")
        else:
            print(f"    {version}: changelog entry is missing for this version")


def action_status(dep_list, selected_reqs, args) -> int:
    ret_ok = True

    for req_name in sorted(dep_list.keys()):
        if selected_reqs and req_name not in selected_reqs:
            continue

        req = dep_list[req_name]

        if not req.isInstalled():
            ret_ok = False
            print(f"{req.type} '{req.name}' is not installed")
            continue

        if req.repo.remotes.origin.url != req.src:
            print(
                f"{req.type} '{req.name}' is installed but does not track the expected origin (current: {req.repo.remotes.origin.url}, expected: {req.src})"
            )
            continue

        try:
            req.fetchUpdates()
        except GitCommandError as e:
            ret_ok = False
            print(f"{req.type} '{req.name}' has problems fetching updates: {e}")
            continue

        warning_msg = False
        target = "version" if req.isTargetingVersionTag() else "branch"
        msg = f"{req.type} '{req.name}' is properly installed, targeting {target} '{req.version}'"

        try:
            req.testRequirements()
        except Exception as e:
            warning_msg = True
            ret_ok = False
            msg += f"\n  is off target: {e}"

        if req.localBranch() is not None and req.remoteBranch().is_valid():
            if req.localBranch().commit == req.remoteBranch().commit:
                msg += "\n  is up-to-date with origin"

            else:
                warning_msg = True
                ret_ok = False
                la = list(req.commitsAhead())
                lb = list(req.commitsBehind())
                if la and lb:
                    msg += "\n  has diverged from origin"
                elif la:
                    msg += f"\n  is {len(la)} commits ahead origin"
                    if args.changelog:
                        for commit in la:
                            ts = time.strftime(
                                "%Y-%m-%d %H:%M %Z",
                                time.gmtime(commit.committed_date),
                            )
                            msg += f"\n    {ts}:  {commit.summary}"
                elif lb:
                    msg += f"\n  is {len(lb)} commits behind origin:"
                    if args.changelog:
                        for commit in lb:
                            ts = time.strftime(
                                "%Y-%m-%d %H:%M %Z",
                                time.gmtime(commit.committed_date),
                            )
                            msg += f"\n    {ts}:  {commit.summary}"

                new_versions = req.newVersions()
                if new_versions:
                    warning_msg = True
                    ver_list = ", ".join(new_versions)
                    msg += f"\n  has new version(s) available: {ver_list}"
                    if args.changelog:
                        commit = req.repo.tags[new_versions[-1]]
                        display_changelog(commit, new_versions)

        if req.localBranch() is not None and not req.remoteBranch().is_valid():
            la = list(req.commitsAhead())
            if la:
                warning_msg = True
                msg += f"\n  is {len(la)} commits ahead (empty) origin"
                if args.changelog:
                    for commit in la:
                        ts = time.strftime(
                            "%Y-%m-%d %H:%M %Z", time.gmtime(commit.committed_date)
                        )
                        msg += f"\n    {ts}:  {commit.summary}"

        if req.repo.is_dirty(untracked_files=True, path=GITPYTHON_DIRTY_PATHSPEC):
            warning_msg = True
            msg += (
                "\n  contains local changes (please commit, stash or cleanup)"
            )

        if selected_reqs or warning_msg or not args.quiet:
            print(msg)

    return 0 if ret_ok else -1


def action_install(dep_list, selected_reqs, args) -> int:
    ret_ok = True

    for req_name in sorted(dep_list.keys()):
        if selected_reqs and req_name not in selected_reqs:
            continue

        req = dep_list[req_name]

        try:
            if req.install():
                print(f"{req.type} '{req.name}' has been installed")
                if not req.repo.remotes.origin.refs:
                    print("  is an empty repository")
            else:
                if not args.quiet:
                    print(f"{req.type} '{req.name}' is already installed")
        except Exception as e:
            print(f"{req.type} '{req.name}' installation failed: {e}")
            ret_ok = False

    return 0 if ret_ok else -1


def action_update(dep_list, selected_reqs, args):
    ret_ok = True

    for req_name in sorted(dep_list.keys()):
        if selected_reqs and req_name not in selected_reqs:
            continue

        req = dep_list[req_name]

        try:
            if req.update():
                print(f"{req.type} '{req.name}' has been updated")
            else:
                if not args.quiet:
                    print(f"{req.type} '{req.name}' is already updated to target")
        except Exception as e:
            print(f"{req.type} '{req.name}' update failed: {e}")
            ret_ok = False

    return 0 if ret_ok else -1


if __name__ == "__main__":
    reqs_info_list = load_reqs_info()

    if reqs_info_list:
        reqs_names = list(reqs_info_list.keys())
    else:
        reqs_names = []
    # work around https://bugs.python.org/issue27227
    #             https://bugs.python.org/issue9625
    # by adding the empty list to the list of choices
    reqs_names.append([])

    # declare available subcommands and options
    parser = argparse.ArgumentParser(description="Manage roles installation")
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {VERSION}"
    )
    parser.add_argument(
        "--quiet", "-q", action="store_true", help="less verbose display"
    )
    subparsers = parser.add_subparsers(help="sub-command help")
    parser_status = subparsers.add_parser(
        "status", help="inform about roles/collections installation status"
    )
    parser_status.set_defaults(func=action_status)
    parser_status.add_argument(
        "--changelog",
        "-c",
        action="store_true",
        help="display changelog entries for new versions",
    )
    parser_status.add_argument(
        'reqs',
        metavar="roles/collections",
        nargs="*",
        choices=reqs_names,
        help="limit command to a list of roles/collections",
    )
    parser_install = subparsers.add_parser("install", help="install roles/collections")
    parser_install.set_defaults(func=action_install)
    parser_install.add_argument(
        'reqs',
        metavar="roles/collections",
        nargs="*",
        choices=reqs_names,
        help="limit command to a list of roles/collections",
    )
    parser_update = subparsers.add_parser("update", help="update roles/collections")
    parser_update.set_defaults(func=action_update)
    parser_update.add_argument(
        'reqs',
        metavar="roles/collections",
        nargs="*",
        choices=reqs_names,
        help='limit command to a list of roles/collections',
    )

    # Completion
    argcomplete.autocomplete(parser)

    # deferred for completion
    if not reqs_info_list:
        exit(-1)

    # let's parse
    args = parser.parse_args()

    # load user config
    dep_list = load_reqs(args, reqs_info_list, args.reqs)

    # action!
    if hasattr(args, "func"):
        exit(args.func(dep_list, args.reqs, args))
    else:
        parser.print_help()
