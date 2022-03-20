"""
This subpackage contains CMake config/package files and functions that can be called from CMake.

Find Abies in cmake using this snippet:

    # Find Abies from a python installation if Abies_ROOT is not given.
    if (NOT Abies_ROOT)
        execute_process(
            COMMAND "${Python_EXECUTABLE}" -c
                    "import abies; print(abies.get_cmake_dir())"
            OUTPUT_VARIABLE _abies_cmake_dir
            OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
            message(${_abies_cmake_dir})
        list(APPEND CMAKE_PREFIX_PATH ${_abies_cmake_dir})
    else()
        # Root of source repository was supplied to CMake.
        list(APPEND CMAKE_PREFIX_PATH ${Abies_ROOT}/abies/cmake)
    endif()

    # Abies CMake package contains cmake functions to create libraries.
    find_package(Abies REQUIRED)


"""

from pathlib import Path


def get_cmake_dir() -> Path:
    """
    Return a path to the directory containing AbiesConfig.cmake.
    This directory needs to be appended to CMAKE_PREFIX_PATH.
    """
    return Path(__file__).parent


__all__ = [
    "get_cmake_dir",
]
