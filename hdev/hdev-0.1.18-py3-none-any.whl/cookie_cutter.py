"""A script for re-applying a cookiecutter template over a project."""
import fnmatch
import os
import os.path
import shutil
from distutils.dir_util import mkpath
from tempfile import mkdtemp

from cookiecutter.main import cookiecutter


class CookieCutter:
    """A collection of cookie cutter related functions."""

    @classmethod
    def replay(cls, project_dir, config):
        """Replay a project based on the config provided.

        :param project_dir: The target directory
        :param config: The config to apply
        :return: The name of the project created

        :raise ValueError: If cookiecutter replaying would change the
            name of the project (the name of the project created by replaying
            the cookiecutter project template is different from the currently
            existing name of the project)
        """
        project_dir = os.path.abspath(project_dir)
        disable_replay = config.get("options", {}).get("disable_replay")

        temp_dir = mkdtemp()

        try:  # pylint:disable=too-many-try-statements
            project_name = cls.render_template(temp_dir, config)
            current_name = os.path.basename(project_dir)

            if project_name != current_name:
                raise ValueError(
                    "The project created does not match the project directory: "
                    f"Created {project_name}, existing {current_name}"
                )

            cls._copy_tree(
                os.path.join(temp_dir, project_name),
                project_dir,
                skip_patterns=disable_replay,
            )

            return project_name

        finally:
            shutil.rmtree(temp_dir)

    @classmethod
    def _matches_pattern(cls, filename, skip_patterns):
        """Check if the filename matches any of the patterns in skip_patterns.

        These patterns are bash style globs like 'thing/*.txt'
        """
        for pattern in skip_patterns:
            if fnmatch.fnmatch(filename, pattern):
                print(f"Skipping: '{filename}' as it matched pattern '{pattern}'")
                return True

        return False

    @classmethod
    def _copy_tree(cls, source_dir, target_dir, skip_patterns=None):
        """Copy a directory over another one.

        Optionally skipping files which match the specified glob style patterns
        like 'thing/*.txt'
        """
        if not skip_patterns:
            skip_patterns = []

        for parent_dir, _, filenames in os.walk(source_dir):
            for filename in filenames:
                rel_path = os.path.relpath(
                    os.path.join(parent_dir, filename), source_dir
                )

                target = os.path.join(target_dir, rel_path)

                if cls._matches_pattern(rel_path, skip_patterns):
                    if os.path.exists(target):
                        continue

                    print("... target doesn't exist: Skipping the skip!")

                source = os.path.join(source_dir, rel_path)

                mkpath(os.path.dirname(target))
                shutil.copy(source, target)

    @classmethod
    def render_template(cls, project_dir, config):
        """Create a project based on the config provided.

        :param project_dir: The target directory
        :param config: The config to apply
        :return: The name of the project created
        """

        template = cls.get_template_from_config(config)

        cookiecutter(
            template=template,
            no_input=True,
            extra_context=config,
            output_dir=project_dir,
        )

        items = os.listdir(project_dir)
        assert len(items) == 1, "There is a unique file in the output dir"
        return items[0]

    @classmethod
    def get_template_from_config(cls, config):
        """Read the template from a config file."""

        # The location of this value in the config object is decided by
        # cookiecutter, and is undocumented. This function is intended to
        # insulate callers outside of this package from having to know where
        # to look for this.
        return config["_template"]
