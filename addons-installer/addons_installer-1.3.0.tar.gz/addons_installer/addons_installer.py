import abc
import logging
import subprocess
import sys
from os.path import exists as path_exists
from os.path import expanduser
from os.path import join as path_join
from typing import Dict, List, Optional, Set

if sys.version_info[0] == 2:  # Python 2

    class ABC(object):
        __meta_class__ = abc.ABCMeta
        __slots__ = ()

else:
    ABC = abc.ABC

_logger = logging.getLogger("install_addons")
_logger.setLevel(logging.INFO)
if not _logger.handlers:
    handler = logging.StreamHandler()
    _logger.addHandler(handler)


class AddonsRegistry(object):
    def __init__(self):
        # type: () -> AddonsRegistry
        self.addon_types = [LocalSubDirOdooAddons, GitSubDirOdooAddons, LocalOdooAddons, GitOdooAddons]

    def parse_env(self, env_vars=None):
        # type: (Dict[str, str]) -> Set[OdooAddonsDef]
        founded = {}
        if env_vars.get("ODOO_PATH"):
            if "ADDONS_LOCAL_SRC_ODOO_ADDONS" not in env_vars:
                env_vars["ADDONS_LOCAL_SRC_ODOO_ADDONS"] = path_join(env_vars["ODOO_PATH"], "addons")
            if "ADDONS_LOCAL_SRC_ODOO_ADDONS_ADDONS" not in env_vars:
                env_vars["ADDONS_LOCAL_SRC_ODOO_ADDONS_ADDONS"] = path_join(env_vars["ODOO_PATH"], "odoo", "addons")

        for k, v in env_vars.items():
            addons = self.parse_key(k)
            if addons:
                if addons.identifier not in founded or addons.prefix != GitOdooAddons._prefix:
                    founded[addons.identifier] = addons
        return {f.extract(env_vars) for f in founded.values()}

    def parse_key(self, env_key):
        # type: (str) -> Optional[AddonsSuffix]
        for addon_type in self.addon_types:
            addons = addon_type(env_key)
            if addons.is_valid():
                _logger.info("Found depends %s from %s", addons, env_key)
                return addons
        return None


class OdooAddonsDef(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def addons_path(self):
        raise NotImplementedError()

    def install_cmd(self):
        raise NotImplementedError()


class AddonsInstaller:
    @staticmethod
    def exec_cmd(cmd, force_log=True):
        if not cmd:
            return 0
        if force_log:
            _logger.info(" ".join(cmd))
        return AddonsInstaller.exit_if_error(subprocess.Popen(cmd).wait())

    @staticmethod
    def exit_if_error(error_no):
        if error_no:
            sys.exit(error_no)
        return error_no

    @staticmethod
    def install_py_requirements(path_depot):
        path_requirements = path_join(path_depot, "requirements.txt")
        if path_exists(path_requirements):
            AddonsInstaller.exec_cmd(
                [sys.executable, "-m", "pip", "install", "-q", "--no-input", "-r", path_requirements], True
            )
        else:
            _logger.debug("No requirements.txt founded in %s", path_requirements)

    @staticmethod
    def install_npm_package(path_depot):
        path_npm = path_join(path_depot, "package.json")
        if path_exists(path_npm):
            AddonsInstaller.exec_cmd(["npm", "install", "-g", path_npm], True)
        else:
            _logger.debug("No package.json founded in %s", path_npm)

    @staticmethod
    def install(addons):
        # type: (OdooAddonsDef) -> None
        _logger.info("install %s", addons)
        try:
            for cmd in addons.install_cmd():
                AddonsInstaller.exec_cmd(cmd, True)
            AddonsInstaller.install_py_requirements(addons.addons_path)
            AddonsInstaller.install_npm_package(addons.addons_path)
        except Exception as e:
            _logger.exception("Error", exc_info=e)
            sys.exit(1)


class KeySuffix(object):
    def __init__(self, addons, name, default=None, have_default=True):
        # type: (AddonsSuffix, str, str, bool) -> KeySuffix
        self.name = name
        self.prefix = addons.prefix
        self.base_key = addons.identifier
        self.default_value = default
        self.have_default = have_default

    def get_value(self, env_vars, with_default=True):
        return (
            env_vars.get(self.full_key, env_vars.get(self.default_key, with_default and self.default_value or None))
            or None
        )

    def get_key(self, *args):
        # type: (List[str]) -> str
        return "_".join([s for s in args if s]).upper()

    @property
    def full_key(self):
        return self.get_key(self.prefix, self.base_key, self.name)

    @property
    def default_key(self):  # type: ()-> Optional[str]
        return self.have_default and self.get_key(self.prefix, AddonsSuffix.ADDONS_DEFAULT, self.name) or None

    def __repr__(self):
        return "%s(%s, default=%s)" % (type(self).__name__, self.full_key, self.default_key)


class AddonsSuffix(ABC):
    ADDONS_DEFAULT = "DEFAULT"
    ADDONS_SUFFIX_EXCLUDE = "EXCLUDE"

    def __init__(self, prefix, base_key):
        # type: (str, str) -> AddonsSuffix
        super(AddonsSuffix, self).__init__()
        self.base_key = base_key
        self.prefix = prefix
        self._key_registry = {}
        self._values = {}
        self.NAME = self.create_key("", have_default=False)

    @property
    def identifier(self):
        return self.base_key.replace(self.prefix, "").strip("_")

    def extract(self, env_vars):
        # type: (Dict[str, str]) -> OdooAddonsDef
        raise NotImplementedError()

    def to_dict(self, env_vars):
        # type: (Dict[str, str]) -> Dict[KeySuffix, str]
        return {key: key.get_value(env_vars) for key_name, key in self._key_registry.items()}

    def get_suffix_keys(self):
        # type: () -> List[str]
        return list(self._key_registry.keys())

    def create_key(self, name, default=None, have_default=True):
        key = KeySuffix(addons=self, name=name, default=default, have_default=have_default)
        self._key_registry[name] = key
        return key

    def is_valid(self):
        return (
            self.base_key.startswith(self.prefix)
            and self.identifier != self.base_key
            and not any(self.base_key.endswith(suffix) for suffix in self.get_suffix_keys() if suffix)
            and not self.base_key.endswith(self.ADDONS_SUFFIX_EXCLUDE)
        )

    def __repr__(self):
        return "%s(%s)" % (type(self).__name__, self.base_key.replace(self.prefix + "_", ""))


class GitOdooAddons(AddonsSuffix):
    _prefix = "ADDONS_GIT"
    PROTOCLE_HTTPS = "https"
    PROTOCLE_SSH = "ssh"
    PROTOCLE_PUBLIC = "public"
    FORMAT_GIT_CLONE = {
        PROTOCLE_HTTPS: "https://%(login)s:%(password)s@%(server)s/%(git_path)s.git",
        PROTOCLE_SSH: "git@%(server)s:%(git_path)s.git",
        PROTOCLE_PUBLIC: "https://%(server)s/%(git_path)s.git",
    }

    def __init__(self, base_key):
        super(GitOdooAddons, self).__init__(GitOdooAddons._prefix, base_key)
        self.BRANCH = self.create_key("BRANCH", default="master")
        self.CLONE_PATH = self.create_key("CLONE_PATH")
        self.PULL_OPTIONS = self.create_key("PULL_OPTIONS", default="--depth=1 --quiet --single-branch")
        self.HTTPS_LOGIN = self.create_key("HTTPS_LOGIN", have_default=False)
        self.HTTPS_PASSWORD = self.create_key("HTTPS_PASSWORD", have_default=False)
        self.SSH_KEY = self.create_key("SSH_KEY", have_default=False)
        self.PROTOCOLE = self.create_key("PROTOCOLE", default=self.PROTOCLE_PUBLIC)
        self.SERVER = self.create_key("SERVER")

    class Result(OdooAddonsDef):
        def __init__(
            self,
            name,
            git_path,
            branch,
            clone_path,
            pull_options,
            https_login,
            https_password,
            ssh_key,
            protocole,
            server,
        ):
            super(GitOdooAddons.Result, self).__init__(name)
            self.git_path = git_path
            self.branch = branch
            if not clone_path:
                clone_path = path_join("/", "opt", "addons", git_path.lower())
            if not clone_path:
                clone_path = path_join(clone_path, git_path.lower())
            self.clone_path = expanduser(clone_path)
            self.pull_options = pull_options
            self.https_login = https_login
            self.https_password = https_password
            self.ssh_key = ssh_key
            self.protocole = protocole
            self.server = server
            self.format = GitOdooAddons.FORMAT_GIT_CLONE[protocole]

        def install_cmd(self):
            if path_exists(self.clone_path):
                _logger.info("Path %s not empty to clone %s", (self.clone_path, self))
                return
            clone_cmd = ["git", "clone"]
            if self.pull_options:
                clone_cmd.append(self.pull_options)
            if self.branch:
                clone_cmd.append("-b")
                clone_cmd.append(self.branch)
            clone_cmd.append(self.git_url)
            clone_cmd.append(self.clone_path)
            return [clone_cmd]

        @property
        def addons_path(self):
            return self.clone_path

        @property
        def git_url(self):
            return self.format % {
                "login": self.https_login,
                "password": self.https_password,
                "server": self.server,
                "git_path": self.git_path,
            }

    def extract(self, env_vars):
        # type: (Dict[str, str]) -> GitOdooAddons.Result
        res = self.to_dict(env_vars)
        # Remove de '/' at the end and the beginning of the name '/p1/p2' become 'p1/p2'
        if not res[self.SERVER]:
            raise ValueError(
                "Not git server is provided, key [%s] or [%s]" % (self.SERVER.full_key, self.SERVER.default_key)
            )

        if res[self.PROTOCOLE] not in self.FORMAT_GIT_CLONE.keys():
            raise ValueError(
                "The selected protocole %s is not supported, possible values are %s"
                % (res[self.PROTOCOLE], sorted(list(self.FORMAT_GIT_CLONE.keys())))
            )

        res[self.NAME] = res[self.NAME].strip("/")
        if self.PROTOCLE_SSH == res[self.PROTOCOLE]:
            raise ValueError("Protocole [%s] not supported for the moment" % self.PROTOCLE_SSH)
        else:
            res.pop(self.SSH_KEY, False)

        if (
            not self.PROTOCOLE.get_value(env_vars, with_default=False)
            and res[self.HTTPS_LOGIN]
            and res[self.HTTPS_PASSWORD]
        ):
            res[self.PROTOCOLE] = "https"

        if self.PROTOCLE_HTTPS == res[self.PROTOCOLE]:
            if not res[self.HTTPS_LOGIN] or not res[self.HTTPS_PASSWORD]:
                raise ValueError(
                    "Please add %s and %s var in your environment when you use [%s] has git protocole"
                    % (
                        self.HTTPS_LOGIN.full_key,
                        self.HTTPS_PASSWORD.full_key,
                        self.PROTOCLE_HTTPS,
                    )
                )
        else:
            res.pop(self.HTTPS_LOGIN, False)
            res.pop(self.HTTPS_PASSWORD, False)
        if self.CLONE_PATH.default_key in env_vars and self.CLONE_PATH.full_key not in env_vars:
            # If default key in env_vars but not dedicated key then we add identifier in lower case to the clone path
            res[self.CLONE_PATH] = path_join(res[self.CLONE_PATH], self.identifier.lower())
        return GitOdooAddons.Result(
            name=self.identifier,
            git_path=res[self.NAME],
            branch=res[self.BRANCH],
            clone_path=res[self.CLONE_PATH],
            pull_options=res[self.PULL_OPTIONS],
            https_login=res.get(self.HTTPS_LOGIN),
            https_password=res.get(self.HTTPS_PASSWORD),
            ssh_key=res.get(self.SSH_KEY),
            protocole=res[self.PROTOCOLE],
            server=res[self.SERVER],
        )


class LocalOdooAddons(AddonsSuffix):
    _prefix = "ADDONS_LOCAL"

    def __init__(self, base_key):
        super(LocalOdooAddons, self).__init__("ADDONS_LOCAL", base_key)
        self.BASE_PATH = self.create_key("BASE_PATH", default="/")

    def extract(self, env_vars):  # type: (Dict[str, str]) -> LocalOdooAddons.Result
        res = self.to_dict(env_vars)
        return LocalOdooAddons.Result(
            name=self.NAME.full_key,
            full_path=path_join(res[self.BASE_PATH], res[self.NAME]),
        )

    class Result(OdooAddonsDef):
        def install_cmd(self):
            return []

        @property
        def addons_path(self):
            return self.full_path

        def __init__(self, name, full_path):
            super(LocalOdooAddons.Result, self).__init__(name)
            self.name = name
            self.full_path = full_path


class ABCSubDirAddons(AddonsSuffix, ABC):
    _identifier = None

    def __init__(self, base_key):
        of_ref = base_key.split("_OF_")[-1]
        super(ABCSubDirAddons, self).__init__(self._identifier, base_key)
        self.parent_addons = None
        if of_ref and self.is_valid():
            tmp = self.get_parent("")
            key_git = tmp.prefix + "_" + of_ref
            self.parent_addons = self.get_parent(key_git)
            assert self.parent_addons.is_valid(), "The key %s is not a Addons valid key" % key_git

    def get_parent(self, key):
        raise NotImplementedError

    def extract(self, env_vars):  # type: (Dict[str, str]) -> LocalOdooAddons
        raise NotImplementedError


class GitSubDirOdooAddons(ABCSubDirAddons):
    _identifier = "ADDONS_SUBDIR_GIT"

    def get_parent(self, key):
        return GitOdooAddons(key)

    def extract(self, env_vars):  # type: (Dict[str, str]) -> LocalOdooAddons.Result
        res = self.to_dict(env_vars)
        git_res = self.parent_addons.to_dict(env_vars)
        return LocalOdooAddons.Result(
            name=self.NAME.full_key,
            full_path=path_join(git_res[self.parent_addons.CLONE_PATH], res[self.NAME]),
        )


class LocalSubDirOdooAddons(ABCSubDirAddons):
    _identifier = "ADDONS_SUBDIR_LOCAL"

    def get_parent(self, key):
        return LocalOdooAddons(key)

    def extract(self, env_vars):  # type: (Dict[str, str]) -> LocalOdooAddons.Result
        res = self.to_dict(env_vars)
        return LocalOdooAddons.Result(
            name=self.NAME.full_key,
            full_path=path_join(res[self.BASE_PATH], res[self.NAME]),
        )
