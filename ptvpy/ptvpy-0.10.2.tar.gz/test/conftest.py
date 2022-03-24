"""Fixtures and tools to test the CLI."""


import os
import shutil
import tempfile
from pathlib import Path
from datetime import datetime

import pytest
import tifffile
import trackpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from click.testing import CliRunner

from ptvpy import generate, process, io, _profile, _cli_root


# Enable debug mode for PtvPy to show all warnings
os.environ["PTVPY_DEBUG"] = "1"


# Ensure that trackpy doesn't log messages
trackpy.quiet()


# TODO Use autodirective to switch CWD in doctests?
#  https://stackoverflow.com/a/46991331/8483989


@pytest.fixture(scope="function", autouse=True)
def handle_matplotlib(monkeypatch):
    """Ensure that plots don't block.

    Is automatically applied to all tests in this directory.
    """
    running_in_ci = bool(os.environ.get("CI"))
    if running_in_ci:
        monkeypatch.setattr(plt, "show", lambda: None)
        yield
    else:
        plt.ion()
        yield
        plt.ioff()


@pytest.fixture(scope="function", autouse=True)
def automatically_close_plots():
    """Closes all open matplotlib figures when a test function exits.

    Is automatically applied to all tests in this directory.
    """
    yield
    plt.close("all")


@pytest.fixture(scope="session")
def _temporary_directory():
    """Provide session specific directory for the project fixtures.

    Is deleted when the session terminates.

    See Also
    --------
    _fresh_project, _full_project
    """
    tmp_dir = Path(tempfile.mkdtemp())
    try:
        yield tmp_dir
    finally:
        shutil.rmtree(tmp_dir)


@pytest.fixture(scope="session")
def _fresh_project(_temporary_directory):
    """Provides a session-specific test project directory without processing results.

    Parameters
    ----------
    _temporary_directory : Path
        Path to a session specific temporary directory.

    Returns
    -------
    static_fresh_project : Path
        Path to a session specific test project directory.
    """
    seed = 42
    static_dir = _temporary_directory / "fresh_project"
    static_dir.mkdir()

    particles = generate.describe_lines(
        frame_count=20,
        particle_count=20,
        x_max=200,
        y_max=200,
        x_vel=1,
        y_vel=0,
        seed=seed,
    )
    generate.add_properties(particles, seed=seed, inplace=True)
    frames = generate.render_frames(particles, background=np.zeros((200, 200)))
    path_template = "image_{:0>2}.tiff"
    for i, frame in enumerate(frames):
        # Ensure that allowed value range of storage format is not exceeded
        frame = frame.round().clip(0, 255).astype(np.uint8)
        tifffile.imwrite(
            static_dir / path_template.format(i),
            frame,
            # TIFF format stores a timestamp, to make the hash consistent we
            # need to enforce the date
            datetime=datetime(2019, 10, 24),
        )
    # Create matching profile file
    _profile.create_profile_file(
        static_dir / _profile.DEFAULT_PROFILE_NAME, data_files="image_*.tiff"
    )

    return static_dir


@pytest.fixture(scope="function")
def fresh_project(tmp_path, _fresh_project):
    """Provides a test project directory without processing results.

    Parameters
    ----------
    tmp_path : Path
        Path to a function specific temporary directory.
    _fresh_project : Path
        Path to a session specific test project directory.

    Returns
    -------
    fresh_project : Path
        Path to the new function specific test project directory.
    """
    tmp_path.rmdir()  # copytree expects to create target dir
    shutil.copytree(_fresh_project, tmp_path)
    os.chdir(tmp_path)
    return tmp_path


@pytest.fixture(scope="session")
def _full_project(_fresh_project, _temporary_directory):
    """Provides a session-specific test project directory with processing results.

    Parameters
    ----------
    _fresh_project : Path
        Path to a session specific test project directory.
    _temporary_directory : Path
        Path to a session specific temporary directory.

    Returns
    -------
    static_fresh_project : Path
        Path to a session specific test project directory.
    """
    static_dir = _temporary_directory / "full_project"
    assert not static_dir.exists()

    shutil.copytree(_fresh_project, static_dir)

    # Change to new directory and autodetect
    os.chdir(static_dir)
    profile = _profile.Profile(static_dir / _profile.DEFAULT_PROFILE_NAME)

    # Lazy-load Frames
    loader = io.FrameLoader(
        pattern=profile["general.data_files"],
        slice_=slice(*profile["general.subset"][["start", "stop", "step"]]),
    )
    storage_file = profile["general.storage_file"]
    if profile["step_locate.remove_background"]:
        loader.remove_background(storage_file)
    frames = loader.lazy_frame_sequence()

    # Locate particles
    particles = []
    for i, frame in enumerate(frames):
        result = trackpy.locate(frame, **profile["step_locate.trackpy_locate"])
        result["frame"] = i
        particles.append(result)
    particles = pd.concat(particles, ignore_index=True)

    # Link particles
    particles = trackpy.link(particles, **profile["step_link.trackpy_link"])
    particles = trackpy.filter_stubs(
        particles, **profile["step_link.trackpy_filter_stubs"]
    )
    particles.reset_index(drop=True, inplace=True)

    # Calculate velocities
    particles = process.particle_velocity(
        particles, step=profile["step_diff.diff_step"]
    )

    # Store the content
    with io.Storage(static_dir / Path(storage_file).name, "a") as file:
        file.save_df("particles", particles)

    return static_dir


@pytest.fixture(scope="function")
def full_project(tmp_path, _full_project):
    """Provides a project directory with processing results.

    Parameters
    ----------
    tmp_path : Path
        Path to a function specific temporary directory.
    _full_project : Path
        Path to a session specific test project directory.

    Returns
    -------
    static_fresh_project : Path
        Path to the new function specific test project directory.
    """
    tmp_path.rmdir()  # copytree expects to create target dir
    shutil.copytree(_full_project, tmp_path)
    os.chdir(tmp_path)
    return tmp_path


@pytest.fixture(scope="session")
def runner():
    """Session specific runner to execute PtvPy's console commands.

    Returns
    -------
    runner : callable
        Signature is the same as :func:`click.testing.CliRunner.invoke` without
        the first argument `cli`.
    """
    # TODO Currently, it's not possible to check if PtvPy writes to stderr.
    #  This is because Exceptions are only displayed in stderr after the
    #  command has run in the wrapping _cli_root.main method.
    runner = CliRunner(mix_stderr=False)

    def run(*args, **kwargs):
        kwargs.setdefault("catch_exceptions", False)
        return runner.invoke(_cli_root.root_group, *args, **kwargs)

    return run
