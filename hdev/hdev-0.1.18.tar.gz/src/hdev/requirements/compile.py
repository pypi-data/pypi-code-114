from hdev.requirements.requirements_file import RequirementsFile
from hdev.tox_cmd import run_tox


def compile_unpinned(unpinned_file, specific_package=None):
    """Compile an unpinned file, optionally specifying a single package.

    :param unpinned_file: The requirements file to compile
    :param specific_package: A package definition like `package` to upgrade or
        `package>=1.2` to specify a version requirement
    :return: A pathlib Path object for the pinned version created

    :raises FileNotFoundError: If the specified file is missing
    """

    unpinned_file = RequirementsFile(unpinned_file).unpinned_file
    if not unpinned_file.exists():
        raise FileNotFoundError(unpinned_file)

    if unpinned_file.settings().get("touch", True):
        # Looks like the environment we are going to build in relies on a
        # requirements file existing, so we'll ensure it does
        unpinned_file.tox_env_requirements_file.touch()

    command = f"pip-compile {unpinned_file}"
    if specific_package:
        command += f' --upgrade-package "{specific_package}"'

    run_tox(unpinned_file.tox_env, command, env_vars={"EXTRA_DEPS": "pip-tools"})

    return unpinned_file.pinned_file
