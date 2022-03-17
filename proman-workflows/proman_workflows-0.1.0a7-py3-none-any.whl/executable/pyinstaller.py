# -*- coding: utf-8 -*-
"""Manage all-in-one executable builds with PyInstaller."""

from typing import TYPE_CHECKING, Optional

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context


@task
def build(ctx, kind=None):  # type: (Context, Optional[bool]) -> None
    """Build wheel package."""
    args = ['--no-interaction']
    if kind:
        args.append(f"--format={kind}")
    ctx.run(f"poetry build {' '.join(args)}")


# [-h] [-v] [-D] [-F] [--specpath DIR] [-n NAME]
# [--add-data <SRC;DEST or SRC:DEST>]
# [--add-binary <SRC;DEST or SRC:DEST>] [-p DIR]
# [--hidden-import MODULENAME]
# [--collect-submodules MODULENAME]
# [--collect-data MODULENAME] [--collect-binaries MODULENAME]
# [--collect-all MODULENAME] [--copy-metadata PACKAGENAME]
# [--recursive-copy-metadata PACKAGENAME]
# [--additional-hooks-dir HOOKSPATH]
# [--runtime-hook RUNTIME_HOOKS] [--exclude-module EXCLUDES]
# [--key KEY] [--splash IMAGE_FILE]
# [-d {all,imports,bootloader,noarchive}] [-s] [--noupx]
# [--upx-exclude FILE] [-c] [-w]
# [-i <FILE.ico or FILE.exe,ID or FILE.icns or "NONE">]
# [--disable-windowed-traceback] [--version-file FILE]
# [-m <FILE or XML>] [-r RESOURCE] [--uac-admin]
# [--uac-uiaccess] [--win-private-assemblies]
# [--win-no-prefer-redirects]
# [--osx-bundle-identifier BUNDLE_IDENTIFIER]
# [--target-architecture ARCH] [--codesign-identity IDENTITY]
# [--osx-entitlements-file FILENAME] [--runtime-tmpdir PATH]
# [--bootloader-ignore-signals] [--distpath DIR]
# [--workpath WORKPATH] [-y] [--upx-dir UPX_DIR] [-a]
# [--clean] [--log-level LEVEL]
# scriptname [scriptname ...]


namespace: Collection = Collection(build)
