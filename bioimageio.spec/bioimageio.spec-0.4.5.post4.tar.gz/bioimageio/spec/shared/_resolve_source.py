import json
import os
import pathlib
import re
import shutil
import typing
import warnings
import zipfile
from functools import singledispatch
from io import BytesIO, StringIO
from tempfile import TemporaryDirectory
from urllib.request import url2pathname, urlopen

from marshmallow import ValidationError

from . import fields, raw_nodes
from .common import (
    BIOIMAGEIO_CACHE_PATH,
    BIOIMAGEIO_COLLECTION_URL,
    BIOIMAGEIO_USE_CACHE,
    BIOIMAGEIO_SITE_CONFIG_URL,
    DOI_REGEX,
    no_cache_tmp_list,
    RDF_NAMES,
    tqdm,
    yaml,
)


def _is_path(s: typing.Any) -> bool:
    if not isinstance(s, (str, os.PathLike)):
        return False

    try:
        return pathlib.Path(s).exists()
    except OSError:
        return False


def resolve_rdf_source(
    source: typing.Union[dict, os.PathLike, typing.IO, str, bytes, raw_nodes.URI]
) -> typing.Tuple[dict, str, typing.Union[pathlib.Path, raw_nodes.URI, bytes]]:
    # reduce possible source types
    if isinstance(source, (BytesIO, StringIO)):
        source = source.read()
    elif isinstance(source, os.PathLike):
        source = pathlib.Path(source)
    elif isinstance(source, raw_nodes.URI):
        source = str(source)

    assert isinstance(source, (dict, pathlib.Path, str, bytes)), type(source)

    if isinstance(source, pathlib.Path):
        source_name = str(source)
        root: typing.Union[pathlib.Path, raw_nodes.URI, bytes] = source.parent
    elif isinstance(source, dict):
        source_name = f"{{name: {source.get('name', '<unknown>')}, ...}}"
        root = pathlib.Path()
    elif isinstance(source, (str, bytes)):
        source_name = str(source[:120]) + "..."
        # string might be path or yaml string; for yaml string (or bytes) set root to cwd

        if _is_path(source):
            assert isinstance(source, (str, os.PathLike))
            root = pathlib.Path(source).parent
        else:
            root = pathlib.Path()
    else:
        raise TypeError(source)

    if isinstance(source, str):
        # source might be bioimageio id, doi, url or file path -> resolve to pathlib.Path

        bioimageio_rdf_source: typing.Optional[str] = (BIOIMAGEIO_COLLECTION_ENTRIES or {}).get(source, (None, None))[1]

        if bioimageio_rdf_source is not None:
            # source is bioimageio id
            source = bioimageio_rdf_source
        elif re.fullmatch(DOI_REGEX, source):  # turn doi into url
            import requests  # not available in pyodide

            zenodo_prefix = "10.5281/zenodo."
            zenodo_record_api = "https://zenodo.org/api/records"
            zenodo_sandbox_prefix = "10.5072/zenodo."
            zenodo_sandbox_record_api = "https://sandbox.zenodo.org/api/records"
            is_zenodo_doi = False
            if source.startswith(zenodo_prefix):
                is_zenodo_doi = True
            elif source.startswith(zenodo_sandbox_prefix):
                # zenodo sandbox doi (which is not a valid doi)
                zenodo_prefix = zenodo_sandbox_prefix
                zenodo_record_api = zenodo_sandbox_record_api
                is_zenodo_doi = True

            if is_zenodo_doi:
                # source is a doi pointing to a zenodo record;
                # we'll expect an rdf.yaml file in that record and use it as source...
                record_id = source[len(zenodo_prefix) :]
                s_count = record_id.count("/")
                if s_count:
                    # record_id/record_version_id
                    if s_count != 1:
                        warnings.warn(
                            f"Unexpected Zenodo record ids: {record_id}. "
                            f"Expected <concept id> or <concept id>/<version id>."
                        )

                    record_id = record_id.split("/")[-1]

                response = requests.get(f"{zenodo_record_api}/{record_id}")
                if not response.ok:
                    raise RuntimeError(response.status_code)

                zenodo_record = response.json()
                for rdf_name in RDF_NAMES:
                    for f in zenodo_record["files"]:
                        if f["key"] == rdf_name:
                            source = f["links"]["self"]
                            break
                    else:
                        continue

                    break
                else:
                    raise ValidationError(f"No RDF found; looked for {RDF_NAMES}")

            else:
                # resolve doi
                # todo: make sure the resolved url points to a rdf.yaml or a zipped package
                response = urlopen(f"https://doi.org/{source}?type=URL")
                source = response.url
                assert isinstance(source, str)
                if not (source.endswith(".yaml") or source.endswith(".zip")):
                    raise NotImplementedError(
                        f"Resolved doi {source_name} to {source}, but don't know where to find 'rdf.yaml' "
                        f"or a packaged resource zip file."
                    )

        assert isinstance(source, str)
        if source.startswith("http"):
            root = raw_nodes.URI(uri_string=source)
            source = _download_url(root)

        if _is_path(source):
            source = pathlib.Path(source)

    if isinstance(source, (pathlib.Path, str, bytes)):
        # source is either:
        #   - a file path (to a yaml or a packaged zip)
        #   - a yaml string,
        #   - or yaml file or zip package content as bytes

        if yaml is None:
            raise RuntimeError(f"Cannot read RDF from {source_name} without ruamel.yaml dependency!")

        if isinstance(source, bytes):
            potential_package: typing.Union[pathlib.Path, typing.IO, str] = BytesIO(source)
            potential_package.seek(0)  # type: ignore
        else:
            potential_package = source

        if zipfile.is_zipfile(potential_package):
            with zipfile.ZipFile(potential_package) as zf:
                for rdf_name in RDF_NAMES:
                    if rdf_name in zf.namelist():
                        break
                else:
                    raise ValueError(f"Missing 'rdf.yaml' in package {source_name}")

                assert isinstance(source, (pathlib.Path, bytes))
                root = source
                source = BytesIO(zf.read(rdf_name))

        source = yaml.load(source)

    assert isinstance(source, dict), source
    return source, source_name, root


def resolve_rdf_source_and_type(
    source: typing.Union[os.PathLike, str, dict, raw_nodes.URI]
) -> typing.Tuple[dict, str, typing.Union[pathlib.Path, raw_nodes.URI, bytes], str]:
    data, source_name, root = resolve_rdf_source(source)

    type_ = data.get("type", "rdf")
    if type_ not in ("rdf", "model", "collection"):
        type_ = "rdf"
    return data, source_name, root, type_


@singledispatch  # todo: fix type annotations
def resolve_source(source, root_path: os.PathLike = pathlib.Path(), output=None):
    raise TypeError(type(source))


@resolve_source.register
def _resolve_source_uri_node(
    source: raw_nodes.URI, root_path: os.PathLike = pathlib.Path(), output: typing.Optional[os.PathLike] = None
) -> pathlib.Path:
    path_or_remote_uri = resolve_local_source(source, root_path, output)
    if isinstance(path_or_remote_uri, raw_nodes.URI):
        local_path = _download_url(path_or_remote_uri, output)
    elif isinstance(path_or_remote_uri, pathlib.Path):
        local_path = path_or_remote_uri
    else:
        raise TypeError(path_or_remote_uri)

    return local_path


@resolve_source.register
def _resolve_source_str(
    source: str, root_path: os.PathLike = pathlib.Path(), output: typing.Optional[os.PathLike] = None
) -> pathlib.Path:
    return resolve_source(fields.Union([fields.URI(), fields.Path()]).deserialize(source), root_path, output)


@resolve_source.register
def _resolve_source_path(
    source: pathlib.Path, root_path: os.PathLike = pathlib.Path(), output: typing.Optional[os.PathLike] = None
) -> pathlib.Path:
    if not source.is_absolute():
        source = pathlib.Path(root_path).absolute() / source

    if output is None:
        return source
    else:
        try:
            shutil.copyfile(source, output)
        except shutil.SameFileError:  # source and output are identical
            pass
        return pathlib.Path(output)


@resolve_source.register
def _resolve_source_resolved_importable_path(
    source: raw_nodes.ResolvedImportableSourceFile,
    root_path: os.PathLike = pathlib.Path(),
    output: typing.Optional[os.PathLike] = None,
) -> raw_nodes.ResolvedImportableSourceFile:
    return raw_nodes.ResolvedImportableSourceFile(
        callable_name=source.callable_name, source_file=resolve_source(source.source_file, root_path, output)
    )


@resolve_source.register
def _resolve_source_importable_path(
    source: raw_nodes.ImportableSourceFile,
    root_path: os.PathLike = pathlib.Path(),
    output: typing.Optional[os.PathLike] = None,
) -> raw_nodes.ResolvedImportableSourceFile:
    return raw_nodes.ResolvedImportableSourceFile(
        callable_name=source.callable_name, source_file=resolve_source(source.source_file, root_path, output)
    )


@resolve_source.register
def _resolve_source_list(
    source: list,
    root_path: os.PathLike = pathlib.Path(),
    output: typing.Optional[typing.Sequence[typing.Optional[os.PathLike]]] = None,
) -> typing.List[pathlib.Path]:
    assert output is None or len(output) == len(source)
    return [resolve_source(el, root_path, out) for el, out in zip(source, output or [None] * len(source))]


def resolve_local_sources(
    sources: typing.Sequence[typing.Union[str, os.PathLike, raw_nodes.URI]],
    root_path: os.PathLike,
    outputs: typing.Optional[typing.Sequence[typing.Optional[os.PathLike]]] = None,
) -> typing.List[typing.Union[pathlib.Path, raw_nodes.URI]]:
    if outputs is None:
        outputs = [None] * len(sources)

    assert outputs is not None
    assert len(outputs) == len(sources)
    return [resolve_local_source(src, root_path, out) for src, out in zip(sources, outputs)]


def resolve_local_source(
    source: typing.Union[str, os.PathLike, raw_nodes.URI],
    root_path: os.PathLike,
    output: typing.Optional[os.PathLike] = None,
) -> typing.Union[pathlib.Path, raw_nodes.URI]:
    if isinstance(source, os.PathLike) or isinstance(source, str):
        try:  # source as path from cwd
            is_path_cwd = pathlib.Path(source).exists()
        except OSError:
            is_path_cwd = False

        try:  # source as relative path from root_path
            path_from_root = pathlib.Path(root_path) / source
            is_path_rp = (path_from_root).exists()
        except OSError:
            is_path_rp = False
        else:
            if not is_path_cwd and is_path_rp:
                source = path_from_root

        if is_path_cwd or is_path_rp:
            source = pathlib.Path(source)
            if output is None:
                return source
            else:
                try:
                    shutil.copyfile(source, output)
                except shutil.SameFileError:
                    pass
                return pathlib.Path(output)

        elif isinstance(source, os.PathLike):
            raise FileNotFoundError(f"Could neither find {source} nor {pathlib.Path(root_path) / source}")

    if isinstance(source, str):
        uri = fields.URI().deserialize(source)
    else:
        uri = source

    assert isinstance(uri, raw_nodes.URI), uri
    if uri.scheme == "file":
        local_path_or_remote_uri: typing.Union[pathlib.Path, raw_nodes.URI] = pathlib.Path(url2pathname(uri.path))
    elif uri.scheme in ("https", "https"):
        local_path_or_remote_uri = uri
    else:
        raise ValueError(f"Unknown uri scheme {uri.scheme}")

    return local_path_or_remote_uri


def source_available(source: typing.Union[pathlib.Path, raw_nodes.URI], root_path: pathlib.Path) -> bool:
    import requests  # not available in pyodide

    local_path_or_remote_uri = resolve_local_source(source, root_path)
    if isinstance(local_path_or_remote_uri, raw_nodes.URI):
        response = requests.head(str(local_path_or_remote_uri))
        available = response.status_code == 200
    elif isinstance(local_path_or_remote_uri, pathlib.Path):
        available = local_path_or_remote_uri.exists()
    else:
        raise TypeError(local_path_or_remote_uri)

    return available


def _download_url(uri: raw_nodes.URI, output: typing.Optional[os.PathLike] = None) -> pathlib.Path:
    if output is not None:
        local_path = pathlib.Path(output)
    elif BIOIMAGEIO_USE_CACHE:
        # todo: proper caching
        local_path = BIOIMAGEIO_CACHE_PATH / uri.scheme / uri.authority / uri.path.strip("/") / uri.query
    else:
        tmp_dir = TemporaryDirectory()
        no_cache_tmp_list.append(tmp_dir)  # keep temporary file until process ends
        local_path = pathlib.Path(tmp_dir.name) / "file"

    if local_path.exists():
        warnings.warn(f"found cached {local_path}. Skipping download of {uri}.")
    else:
        local_path.parent.mkdir(parents=True, exist_ok=True)

        import requests  # not available in pyodide

        try:
            # download with tqdm adapted from:
            # https://github.com/shaypal5/tqdl/blob/189f7fd07f265d29af796bee28e0893e1396d237/tqdl/core.py
            # Streaming, so we can iterate over the response.
            r = requests.get(str(uri), stream=True)
            # Total size in bytes.
            total_size = int(r.headers.get("content-length", 0))
            block_size = 1024  # 1 Kibibyte
            t = tqdm(total=total_size, unit="iB", unit_scale=True, desc=uri.path.split("/")[-1])
            tmp_path = local_path.with_suffix(f"{local_path.suffix}.part")
            with tmp_path.open("wb") as f:
                for data in r.iter_content(block_size):
                    t.update(len(data))
                    f.write(data)

            t.close()
            if total_size != 0 and hasattr(t, "n") and t.n != total_size:
                # todo: check more carefully and raise on real issue
                warnings.warn(f"Download ({t.n}) does not have expected size ({total_size}).")

            shutil.move(f.name, str(local_path))
        except Exception as e:
            raise RuntimeError(f"Failed to download {uri} ({e})")

    return local_path


T = typing.TypeVar("T")


def _resolve_json_from_url(
    url: str,
    expected_type: typing.Union[typing.Type[dict], typing.Type[T]] = dict,
    warning_msg: str = "Failed to fetch {url}: {error}",
) -> typing.Tuple[typing.Optional[T], typing.Optional[str]]:
    try:
        p = resolve_source(url)
        with p.open() as f:
            data = json.load(f)

        assert isinstance(data, expected_type)
    except Exception as e:
        data = None
        error: typing.Optional[str] = str(e)
        if warning_msg:
            warnings.warn(warning_msg.format(url=url, error=error))
    else:
        error = None

    return data, error


BIOIMAGEIO_SITE_CONFIG, BIOIMAGEIO_SITE_CONFIG_ERROR = _resolve_json_from_url(BIOIMAGEIO_SITE_CONFIG_URL)
BIOIMAGEIO_COLLECTION, BIOIMAGEIO_COLLECTION_ERROR = _resolve_json_from_url(BIOIMAGEIO_COLLECTION_URL)
if BIOIMAGEIO_COLLECTION is None:
    BIOIMAGEIO_COLLECTION_ENTRIES: typing.Optional[typing.Dict[str, typing.Tuple[str, str]]] = None
else:
    BIOIMAGEIO_COLLECTION_ENTRIES = {
        cr["id"]: (cr["type"], cr["rdf_source"])
        for cr in BIOIMAGEIO_COLLECTION.get("collection", [])
        if "id" in cr and "rdf_source" in cr and "type" in cr
    }
    # add resource versions explicitly
    BIOIMAGEIO_COLLECTION_ENTRIES.update(
        {
            f"{cr['id']}/{cv}": (
                cr["type"],
                cr["rdf_source"].replace(
                    f"/{cr['versions'][0]}", f"/{cv}"
                ),  # todo: improve this replace-version-monkeypatch
            )
            for cr in BIOIMAGEIO_COLLECTION.get("collection", [])
            for cv in cr.get("versions", [])
            if "id" in cr and "rdf_source" in cr and "type" in cr
        }
    )
