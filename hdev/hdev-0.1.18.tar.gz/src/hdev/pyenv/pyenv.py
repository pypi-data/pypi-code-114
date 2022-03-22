"""Wrappers around Pyenv functionality."""
import os
from functools import cached_property
from pathlib import Path
from subprocess import check_call, check_output

from hdev.pyenv.python_versions import PythonVersions


class Pyenv:
    """Wrappers around Pyenv functionality."""

    @classmethod
    def install(cls, version, verbose=False):
        """Install a particular version of Python.

        This will work fine if the version is already there.

        :param version: Version string or tuple of digits to install
        :param verbose: Give more feedback
        """
        version = cls._digits_to_version_string(version)

        install_command = ["pyenv", "install", "--skip-existing", version]
        if verbose:
            install_command += ["--verbose"]

        check_call(install_command)

    def installed_versions(self):
        """Get the Python versions which are already installed.

        :return: A PythonVersions object.
        """

        return PythonVersions.from_strings(
            path
            for path in os.listdir(self.root_dir)
            if (self.root_dir / path).is_dir()
        )

    @classmethod
    def rehash_binaries(cls):
        """Update indexes for any recently installed binary files."""

        check_call(["pyenv", "rehash"])

    @cached_property
    def root_dir(self):  # pylint: disable=no-self-use
        """Get the root directory in which Python versions are installed."""

        # Try the default location first, falling back to looking it up
        pyenv_root = Path(os.path.expanduser("~/.pyenv"))
        if not pyenv_root.exists():
            pyenv_root = Path(check_output(["pyenv", "root"]).decode("utf-8").strip())

        return pyenv_root / "versions"

    def ensure_tox(self, version, verbose=False):
        """Ensure that tox is available in a particular version of Python.

        :param version: Version string or tuple of digits to install tox in
        :param verbose: Give more feedback
        :return: True if tox was already installed
        """
        version = self._digits_to_version_string(version)

        bin_dir = self.root_dir / version / "bin"
        if (bin_dir / "tox").exists():
            return True

        pip_command = [
            (bin_dir / "pip"),
            "install",
            "--disable-pip-version-check",
            # Ensure we actually get one in this installation rather
            # than picking up an ambient install
            "--force",
            "tox",
        ]

        # The regular level of verbosity is verbose enough for us, actually
        # adding --verbose to pip gives _way_ too much output
        if not verbose:
            pip_command.append("--quiet")

        check_call(pip_command)

        self.rehash_binaries()

        return False

    @classmethod
    def _digits_to_version_string(cls, digits):
        if isinstance(digits, tuple):
            return PythonVersions.format_digits(digits, "plain")

        return digits
