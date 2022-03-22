"""Sub-command of `hdev` to install Python versions."""
from hdev.command.sub_command import SubCommand


class InstallPython(SubCommand):
    """Sub-command of `hdev` to install Python versions."""

    name = "install-python"
    help = "Install the versions of python listed in the `.python-version` file."

    @classmethod
    def __call__(cls, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """
        # pylint: disable=import-outside-toplevel
        from hdev.pyenv.pyenv import Pyenv
        from hdev.pyenv.version_file import PyenvVersionFile

        if cls._running_inside_ci():
            print("Python install disabled as we are running in CI")
            return

        report = print if args.debug else lambda message: None
        version_file = PyenvVersionFile(args.project.root_dir / ".python-version")
        pyenv = Pyenv()

        # It's twice as fast to check which versions are installed as it is to
        # try to blind install one. There are other savings too as we don't
        # need to determine the root directory
        installed_versions = pyenv.installed_versions()

        for version in version_file.versions():
            if version in installed_versions:
                report(f"Skipping Python {version} as it's already installed")
            else:
                report(f"Installing Python {version}...")
                pyenv.install(version, verbose=args.debug)

            if pyenv.ensure_tox(version, verbose=args.debug):
                report("Tox already installed")
            else:
                report("Installed tox")

    @classmethod
    def _running_inside_ci(cls):
        """Check if we are running inside a CI environment."""

        # pylint: disable=import-outside-toplevel
        import os

        for env_var in ("GITHUB_ACTIONS", "TRAVIS"):
            if os.environ.get(env_var) == "true":
                return True

        return "JENKINS_URL" in os.environ and os.environ["JENKINS_URL"]
