import tarfile
import tempfile
import zipfile
from pathlib import Path

# import optional hooks as-is from setuptools
# don't mind the "unused import" warnings
from setuptools.build_meta import build_sdist as setuptools_build_sdist
from setuptools.build_meta import build_wheel as setuptools_build_wheel
from setuptools.build_meta import get_requires_for_build_sdist  # noqa: F401
from setuptools.build_meta import get_requires_for_build_wheel  # noqa: F401
from setuptools.build_meta import prepare_metadata_for_build_wheel  # noqa: F401


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    wheel_basename = setuptools_build_wheel(
        wheel_directory,
        config_settings=config_settings,
        metadata_directory=metadata_directory,
    )

    # wheel_path = Path(wheel_directory) / wheel_basename

    # with tempfile.TemporaryDirectory() as tmpdir:
    #     tmpdir = Path(tmpdir)

    #     with zipfile.ZipFile(wheel_path) as w:
    #         w.extractall(tmpdir)

    #     # shutil.make_archive(wheel_path, "zip", tmpdir)
    #     with zipfile.ZipFile(wheel_path, "w") as zf:
    #         for p in tmpdir.rglob("*"):
    #             zf.write(p, p.relative_to(tmpdir))

    return wheel_basename


def build_sdist(sdist_directory, config_settings=None):
    # build sdist with setuptools
    tar_basename = setuptools_build_sdist(sdist_directory, config_settings)

    # Unpack sdist and replace the original .py with obfuscated ones
    tar_path = Path(sdist_directory) / tar_basename

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        with tarfile.open(tar_path) as tar:
            tar.extractall(tmpdir)

        with tarfile.open(tar_path, "w:gz") as tar:
            tar.add(tmpdir, arcname=".")

    return tar_basename
