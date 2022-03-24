"""Test custom fixtures."""


from pathlib import Path

import h5py
import pytest

from ptvpy import io


class Test_fresh_project:
    def test_content(self, fresh_project):
        assert Path.cwd() == fresh_project

        # Check for expected files and names
        files = list(Path(".").glob("**/*"))
        assert len(files) == 21  # 20 frames + profile
        assert "ptvpy.toml" in (f.name for f in files)
        for i in range(20):
            assert f"image_{i:0>2}.tiff" in (f.name for f in files)

        # Hash actual image content
        arrays = io.FrameLoader("image_*.tiff").lazy_frame_sequence()
        digest = io.hash_arrays(arrays)
        assert digest == "35a45d22f5a9e3056c42e8eb7afd798270c16473", (
            "Unknown hash for image content by the fresh_project fixture. This might "
            "be due to an intended change or a change in the runtime environment. "
            "Please verify the output manually and why it changed before updating the "
            "hashes in this test!"
        )

    @pytest.mark.parametrize("run_count", [1, 2])
    def test_scope(self, fresh_project, run_count):
        file = Path("ptvpy.toml")
        assert file.is_file(), (
            "fixture output might not be independent between test functions if this"
            "tests fails for the second run only"
        )
        file.unlink()
        assert not file.is_file()


class Test_full_project:
    def test_full_project(self, full_project):
        assert Path.cwd() == full_project
        files = list(Path(".").glob("**/*"))

        assert "ptvpy.h5" in (f.name for f in files)
        assert len(files) == 22  # 20 frames + profile + storage

        with h5py.File("./ptvpy.h5", mode="r") as file:
            assert len(file["particles"]) > 0
            assert "background" in file

        # TODO Somehow the checksum for the "ptvpy.h5" file changes between runs. Why?

    @pytest.mark.parametrize("run_count", [1, 2])
    def test_scope(self, full_project, run_count):
        file = Path("ptvpy.h5")
        assert file.is_file(), (
            "fixture output might not be independent between test functions if this"
            "tests fails for the second run only"
        )
        file.unlink()
        assert not file.is_file()
