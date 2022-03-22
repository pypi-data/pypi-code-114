"""Lazy loaded command content for Clean."""
import subprocess

import importlib_resources


class LazyClean:  # pylint: disable=too-few-public-methods
    """Lazy loaded command content for Clean."""

    DEFAULT_CLEAN = {
        "files": ["node_modules/.uptodate", ".coverage"],
        "dirs": [
            "build",
            "build.eggs",
            "dist",
            "*.egg-info",
            "src/*.egg-info",
            ".coverage.*",
            ".pytest_cache",
        ],
        "file_names": ["*.py[co]"],
        "dir_names": ["__pycache__"],
        "empty_dirs": True,
    }
    DEEP_CLEAN = {"dirs": [".tox", "node_modules"]}

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """
        # Merge any project specific settings with our defaults
        config = args.project.config.get("tool.hdev.clean", {})
        to_clean = dict(self.DEFAULT_CLEAN)
        for key, value in to_clean.items():
            if isinstance(value, list):
                value.extend(config.get(key, []))
            else:
                to_clean[key] = config.get(key, value)

        self._clean(**to_clean, verbose=args.debug)

        if args.deep or args.all:
            self._clean(**self.DEEP_CLEAN, verbose=args.debug)

        if args.branches or args.all:
            self._run_script("clean_branches.sh")

    @classmethod
    def _clean(
        # pylint: disable=too-many-arguments
        cls,
        files=None,
        dirs=None,
        file_names=None,
        dir_names=None,
        verbose=False,
        empty_dirs=False,
    ):
        script_content = ";\n".join(
            list(cls._get_file_and_dir_command(files, dirs, verbose))
            + list(
                cls._get_file_and_dir_pattern_command(
                    file_names, dir_names, empty_dirs, verbose
                )
            )
        )

        if verbose:
            print(f"Clean script:\n\n{script_content}\n")

        subprocess.check_call(script_content, shell=True)

    @classmethod
    def _get_file_and_dir_command(cls, files, dirs, verbose):
        # Remove concrete files and dirs
        for options, items in (("--force", files), ("--recursive --force", dirs)):
            if verbose:
                options += " --verbose"

            if items:
                yield f"rm {options} {' '.join(items)}"

    @classmethod
    def _get_file_and_dir_pattern_command(
        cls, file_names, dir_names, empty_dirs, verbose
    ):
        # Remove file patterns
        if file_names:
            yield cls._find_command(
                "f", [f'-name "{item}"' for item in file_names], "-delete"
            )

        # Remove empty dirs or dir patterns
        if empty_dirs or dir_names:
            selectors = []
            if empty_dirs:
                selectors.append("-empty")

            if dir_names:
                selectors.extend([f'-name "{item}"' for item in dir_names])

            rm_command = (
                "-exec rm --recursive" + (" --verbose" if verbose else "") + " {} +"
            )

            yield cls._find_command("d", selectors, rm_command)

    @classmethod
    def _find_command(cls, item_type, selectors, command):
        selectors = " -or ".join(selectors)

        # Ensure we don't remove things based on patterns from the tox
        # directory as it can break libraries when we remove their compiled
        # files etc.
        find_excludes = "! -path './.tox/*'"

        return f"find . -type {item_type} {find_excludes} \\( {selectors} \\) {command}"

    _BIN_DIR = importlib_resources.files("hdev.resources.bin")

    @classmethod
    def _run_script(cls, script_name):
        with importlib_resources.as_file(cls._BIN_DIR / script_name) as script:
            subprocess.check_call([str(script)])
