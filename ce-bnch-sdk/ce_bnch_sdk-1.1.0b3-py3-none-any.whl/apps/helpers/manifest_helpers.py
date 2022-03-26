from io import BytesIO
from pathlib import Path
from typing import Any, Dict

from benchling_api_client.v2.alpha.models.benchling_app_manifest import BenchlingAppManifest
import yaml


def manifest_to_bytes(manifest: BenchlingAppManifest, encoding: str = "utf-8") -> BytesIO:
    """Write a modeled Benchling App manifest to BytesIO of YAML."""
    manifest_dict = manifest.to_dict()
    yaml_format = yaml.safe_dump(manifest_dict, encoding=encoding, allow_unicode=True, sort_keys=False)
    return BytesIO(yaml_format)


def manifest_from_bytes(manifest: BytesIO) -> BenchlingAppManifest:
    """Read a modeled Benchling App manifest from BytesIO."""
    yaml_format = yaml.safe_load(manifest)
    _update_manifest_for_parsing(yaml_format)
    return BenchlingAppManifest.from_dict(yaml_format)


def manifest_from_file(file_path: Path) -> BenchlingAppManifest:
    """Read a modeled Benchling App manifest from a file."""
    with open(file_path, "rb") as file:
        return manifest_from_bytes(BytesIO(file.read()))


def _update_manifest_for_parsing(manifest: Dict[str, Any]) -> None:
    """
    Update a manifest to allow flexible parsing.

    Mutates the provided dict / mapping to be parsed by OpenAPI models as a side effect.
    The OpenAPI generated Enum will fail on `manifestVersion: 1` but work on `manifestVersion: '1'`
    because the enum wants a string type. Convert it here so it just works for developers.
    """
    manifest["manifestVersion"] = str(manifest["manifestVersion"])
