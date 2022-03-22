# standard imports
import base64
import logging
import os
import sys
import urllib.request
import json

from cic_types.ext.metadata import MetadataRequestsHandler, MetadataPointer

logg = logging.getLogger(__name__)


class OutputWriter:
    def __init__(self, *args, **kwargs):
        pass

    def write(self, k, v):
        raise NotImplementedError()


class StdoutWriter(OutputWriter):
    def write(self, k, v):
        sys.stdout.write(f"{k}\t{v}\n")


class KVWriter(OutputWriter):
    def __init__(self, path=None, *args, **kwargs):
        try:
            os.stat(path)
        except FileNotFoundError:
            os.makedirs(path)
        self.path = path

    def write(self, k, v):
        fp = os.path.join(self.path, str(k))
        logg.debug(f"path write {fp} {str(v)}")
        f = open(fp, "wb")
        f.write(v)
        f.close()


class HTTPWriter(OutputWriter):
    def __init__(self, path=None, *args, **kwargs):
        super(HTTPWriter, self).__init__(*args, **kwargs)
        self.path = path

    def write(self, k, v):
        path = self.path
        if k is not None:
            path = os.path.join(path, k)
        logg.debug(f"http writer post {path} \n key: {k}, value: {v}")
        rq = urllib.request.Request(path, method="POST", data=v)
        r = urllib.request.urlopen(rq)
        logg.info(f"http writer submitted at {r.read()}")


class KeyedWriter(OutputWriter):
    def __init__(self, writer_keyed, writer_immutable):
        self.writer_keyed = writer_keyed
        self.writer_immutable = writer_immutable

    def write(self, k, v):
        logg.debug(f"writing keywriter key: {k} value: {v}")
        if isinstance(v, str):
            v = v.encode("utf-8")
        if self.writer_keyed is not None:
            self.writer_keyed.write(k, v)
        if self.writer_immutable is not None:
            self.writer_immutable.write(None, v)


class KeyedWriterFactory:
    def __init__(
        self, key_writer_constructor, immutable_writer_constructor, *args, **kwargs
    ):
        self.key_writer_constructor = key_writer_constructor
        self.immutable_writer_constructor = immutable_writer_constructor
        self.x = {}
        for k, v in kwargs.items():
            logg.debug(f"adding key {k} t keyed writer factory")
            self.x[k] = v

    def new(self, path=None, *args, **kwargs):
        writer_keyed = None
        writer_immutable = None
        if self.key_writer_constructor is not None:
            writer_keyed = self.key_writer_constructor(path, **self.x)
        if self.immutable_writer_constructor is not None:
            writer_immutable = self.immutable_writer_constructor(path, **self.x)
        return KeyedWriter(writer_keyed, writer_immutable)


class MetadataWriter(OutputWriter):
    """Custom writer for publishing data under immutable content-addressed pointers in the cic-meta storage backend.

    Data that is not utf-8 will be converted to base64 before publishing.

    Implements cic.writers.OutputWriter
    """

    def write(self, k, v):
        rq = MetadataRequestsHandler(MetadataPointer.NONE, bytes.fromhex(k))
        try:
            v = v.decode("utf-8")
            v = json.loads(v)
            logg.debug(f"metadatawriter bindecode {k} {v}")
        except UnicodeDecodeError:
            v = base64.b64encode(v).decode("utf-8")
            v = json.loads(json.dumps(v, separators=(",", ":")))
            logg.debug(f"metadatawriter b64encode {k} {v}")
        r = rq.create(v)
        logg.info(f"metadata submitted at {k}")
        return r
