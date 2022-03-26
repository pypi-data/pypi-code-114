"""
pydap client.

This module contains functions to access DAP servers. The most common use is to
open a dataset by its canonical URL, ie, without any DAP related extensions
like dds/das/dods/html. Here is an example:

    >>> from pydap.client import open_url
    >>> dataset = open_url("http://test.pydap.org/coads.nc")

This will return a `DatasetType` object, which is a container for lazy
evaluated objects. Data is downloaded automatically when arrays are sliced or
when sequences are iterated.

It is also possible to download data directly from a dods (binary) response.
This allows calling server-specific functions, like those supported by the
Ferret and the GrADS data servers:

    >>> from pydap.client import open_dods
    >>> dataset = open_dods(
    ...     "http://test.pydap.org/coads.nc.dods",
    ...     metadata=True)

Setting the `metadata` flag will also request the das response, populating the
dataset with the corresponding metadata.

If the dods response has already been downloaded, it is possible to open it as
if it were a remote dataset. Optionally, it is also possible to specify a das
response:

    >>> from pydap.client import open_file
    >>> dataset = open_file(
    ...     "/path/to/file.dods", "/path/to/file.das")  #doctest: +SKIP

Remote datasets opened with `open_url` can call server functions. pydap has a
lazy mechanism for function call, supporting any function. Eg, to call the
`geogrid` function on the server:

    >>> dataset = open_url(
    ...     'http://test.opendap.org/dap/data/nc/coads_climatology.nc')
    >>> new_dataset = dataset.functions.geogrid(dataset.SST, 10, 20, -10, 60)
    >>> print(new_dataset.SST.SST.shape) #doctest: +SKIP
    (12, 12, 21)

"""

import ast
import copy
import gzip
import logging
import operator
import re
from collections import Mapping, OrderedDict
from contextlib import closing
from functools import reduce
from io import BytesIO, open
from itertools import zip_longest
from urllib.parse import quote, unquote, urlsplit, urlunsplit

import numpy as np
import requests
from pkg_resources import iter_entry_points
from requests.exceptions import InvalidSchema, MissingSchema, Timeout
from webob import Request

logger = logging.getLogger("pydap")
logger.addHandler(logging.NullHandler())

BUFFER_SIZE = 2 ** 27
STRING = "|S128"
DEFAULT_TIMEOUT = 120  # 120 seconds = 2 minutes
# Typemap from lower case DAP2 types to
# numpy dtype string with specified endiannes.
# Here, the endianness is very important:
LOWER_DAP2_TO_NUMPY_PARSER_TYPEMAP = {
    "float64": ">d",
    "float32": ">f",
    "int16": ">h",
    "uint16": ">H",
    "int32": ">i",
    "uint32": ">I",
    "byte": "B",
    "string": STRING,
    "url": STRING,
    "int": ">i",
    "uint": ">I",
}
name_regexp = r'[\w%!~"\'\*-]+'

# DAP2 demands big-endian 32 bytes signed integers
# www.opendap.org/pdf/dap_2_data_model.pdf
# Before pydap 3.2.2, length was
# big-endian 32 bytes UNSIGNED integers:
# DAP2_ARRAY_LENGTH_NUMPY_TYPE = '>I'
# Since pydap 3.2.2, the length type is accurate:
DAP2_ARRAY_LENGTH_NUMPY_TYPE = ">i"

NUMPY_TO_DAP2_TYPEMAP = {
    "d": "Float64",
    "f": "Float32",
    "h": "Int16",
    "H": "UInt16",
    "i": "Int32",
    "l": "Int32",
    "q": "Int32",
    "I": "UInt32",
    "L": "UInt32",
    "Q": "UInt32",
    # DAP2 does not support signed bytes.
    # Its Byte type is unsigned and thus corresponds
    # to numpy's 'B'.
    # The consequence is that there is no natural way
    # in DAP2 to represent numpy's 'b' type.
    # Ideally, DAP2 would have a signed Byte type
    # and an unsigned UByte type and we would have the
    # following mapping: {'b': 'Byte', 'B': 'UByte'}
    # but this not how the protocol has been defined.
    # This means that numpy's 'b' must be mapped to Int16
    # and data must be upconverted in the DODS response.
    "b": "Int16",
    "B": "Byte",
    # There are no boolean types in DAP2. Upconvert to
    # Byte:
    "?": "Byte",
    "S": "String",
    # Map numpy's 'U' to String b/c
    # DAP2 does not explicitly support unicode.
    "U": "String",
}

DAP2_TO_NUMPY_RESPONSE_TYPEMAP = {
    "Float64": ">d",
    "Float32": ">f",
    # This is a weird aspect of the DAP2 specification.
    # For backward-compatibility, Int16 and UInt16 are
    # encoded as 32 bits integers in the response,
    # respectively:
    "Int16": ">i",
    "UInt16": ">I",
    "Int32": ">i",
    "UInt32": ">I",
    # DAP2 does not support signed bytes.
    # It's Byte type is unsigned and thus corresponds
    # to numpy 'B'.
    # The consequence is that there is no natural way
    # in DAP2 to represent numpy's 'b' type.
    # Ideally, DAP2 would have a signed Byte type
    # and a usigned UByte type and we would have the
    # following mapping: {'Byte': 'b', 'UByte': 'B'}
    # but this not how the protocol has been defined.
    # This means that DAP2 Byte is unsigned and must be
    # mapped to numpy's 'B' type, usigned byte.
    "Byte": "B",
    # Map String to numpy's string type 'S' b/c
    # DAP2 does not explicitly support unicode.
    "String": "S",
    "URL": "S",
    #
    # These two types are not DAP2 but it is useful
    # to include them for compatiblity with other
    # data sources:
    "Int": ">i",
    "UInt": ">I",
}

# Typemap from lower case DAP2 types to
# numpy dtype string with specified endiannes.
# Here, the endianness is very important:
LOWER_DAP2_TO_NUMPY_PARSER_TYPEMAP = {
    "float64": ">d",
    "float32": ">f",
    "int16": ">h",
    "uint16": ">H",
    "int32": ">i",
    "uint32": ">I",
    "byte": "B",
    "string": STRING,
    "url": STRING,
    "int": ">i",
    "uint": ">I",
}


def convert_stream_to_list(stream, parser_dtype, shape, id):
    out = []
    response_dtype = DAP2_response_dtypemap(parser_dtype)
    if shape:
        n = np.frombuffer(stream.read(4), DAP2_ARRAY_LENGTH_NUMPY_TYPE)[0]
        count = response_dtype.itemsize * n
        if response_dtype.char in "S":
            # Consider on 'S' and not 'SU' because
            # response_dtype.char should never be
            data = []
            for _ in range(n):
                k = np.frombuffer(stream.read(4), DAP2_ARRAY_LENGTH_NUMPY_TYPE)[0]
                data.append(stream.read(k))
                stream.read(-k % 4)
            out.append(
                np.array([text_type(x.decode("ascii")) for x in data], "S").reshape(
                    shape
                )
            )
        else:
            stream.read(4)  # read additional length
            try:
                out.append(
                    np.frombuffer(stream.read(count), response_dtype)
                    .astype(parser_dtype)
                    .reshape(shape)
                )
            except ValueError as e:
                if str(e) == "total size of new array must be unchanged":
                    # server-side failure.
                    # it is expected that the user should be mindful of this:
                    raise RuntimeError(
                        (
                            "variable {0} could not be properly "
                            "retrieved. To avoid this "
                            "error consider using open_url(..., "
                            "output_grid=False)."
                        ).format(quote(id))
                    )
                else:
                    raise
            if response_dtype.char == "B":
                # Unsigned Byte type is packed to multiples of 4 bytes:
                stream.read(-n % 4)

    # special types: strings and bytes
    elif response_dtype.char in "S":
        # Consider on 'S' and not 'SU' because
        # response_dtype.char should never be
        # 'U'
        k = np.frombuffer(stream.read(4), DAP2_ARRAY_LENGTH_NUMPY_TYPE)[0]
        out.append(text_type(stream.read(k).decode("ascii")))
        stream.read(-k % 4)
    # usual data
    else:
        out.append(
            np.frombuffer(stream.read(response_dtype.itemsize), response_dtype).astype(
                parser_dtype
            )[0]
        )
        if response_dtype.char == "B":
            # Unsigned Byte type is packed to multiples of 4 bytes:
            stream.read(3)
    return out


def DAP2_response_dtypemap(dtype):
    """
    This function takes a numpy dtype object
    and returns a dtype object that is compatible with
    the DAP2 specification.
    """
    dtype_str = DAP2_TO_NUMPY_RESPONSE_TYPEMAP[NUMPY_TO_DAP2_TYPEMAP[dtype.char]]
    return np.dtype(dtype_str)


def unpack_children(stream, template):
    """Unpack children from a structure, returning their data."""
    cols = list(template.children()) or [template]

    out = []
    for col in cols:
        # sequences and other structures
        if isinstance(col, SequenceType):
            out.append(IterData(list(unpack_sequence(stream, col)), col))
        elif isinstance(col, StructureType):
            out.append(tuple(unpack_children(stream, col)))

        # unpack arrays
        else:
            out.extend(convert_stream_to_list(stream, col.dtype, col.shape, col.id))
    return out


class BytesReader(object):

    """Class to allow reading a `bytes` object."""

    def __init__(self, data):
        self.data = data

    def read(self, n):
        """Read and return `n` bytes."""
        out = self.data[:n]
        self.data = self.data[n:]
        return out


def safe_dds_and_data(r, user_charset):
    if r.content_encoding == "gzip":
        raw = gzip.GzipFile(fileobj=BytesIO(r.body)).read()
    else:
        raw = r.body
    dds, data = raw.split(b"\nData:\n", 1)
    return dds.decode(get_charset(r, user_charset)), data


def hyperslab(slice_):
    """Return a DAP representation of a multidimensional slice."""
    if not isinstance(slice_, tuple):
        slice_ = [slice_]
    else:
        slice_ = list(slice_)

    while slice_ and slice_[-1] == slice(None):
        slice_.pop(-1)

    return "".join(
        "[%s:%s:%s]" % (s.start or 0, s.step or 1, (s.stop or MAXSIZE) - 1)
        for s in slice_
    )


def fix_slice(slice_, shape):
    """Return a normalized slice.

    This function returns a slice so that it has the same length of `shape`,
    and no negative indexes, if possible.

    This is based on this document:

        http://docs.scipy.org/doc/numpy/reference/arrays.indexing.html

    """
    # convert `slice_` to a tuple
    if not isinstance(slice_, tuple):
        slice_ = (slice_,)

    # expand Ellipsis and make `slice_` at least as long as `shape`
    expand = len(shape) - len(slice_)
    out = []
    for s in slice_:
        if s is Ellipsis:
            out.extend((slice(None),) * (expand + 1))
            expand = 0
        else:
            out.append(s)
    slice_ = tuple(out) + (slice(None),) * expand

    out = []
    for s, n in zip(slice_, shape):
        if isinstance(s, int):
            if s < 0:
                s += n
            out.append(s)
        else:
            k = s.step or 1

            i = s.start
            if i is None:
                i = 0
            elif i < 0:
                i += n

            j = s.stop
            if j is None or j > n:
                j = n
            elif j < 0:
                j += n

            out.append(slice(i, j, k))

    return tuple(out)


def combine_slices(slice1, slice2):
    """Return two tuples of slices combined sequentially.

    These two should be equal:

        x[ combine_slices(s1, s2) ] == x[s1][s2]

    """
    out = []
    for exp1, exp2 in zip_longest(slice1, slice2, fillvalue=slice(None)):
        if isinstance(exp1, int):
            exp1 = slice(exp1, exp1 + 1)
        if isinstance(exp2, int):
            exp2 = slice(exp2, exp2 + 1)

        start = (exp1.start or 0) + (exp2.start or 0)
        step = (exp1.step or 1) * (exp2.step or 1)

        if exp1.stop is None and exp2.stop is None:
            stop = None
        elif exp1.stop is None:
            stop = (exp1.start or 0) + exp2.stop
        elif exp2.stop is None:
            stop = exp1.stop
        else:
            stop = min(exp1.stop, (exp1.start or 0) + exp2.stop)

        out.append(slice(start, stop, step))
    return tuple(out)


def parse_ce(query_string):
    """Extract the projection and selection from the QUERY_STRING.

        >>> parse_ce('a,b[0:2:9],c&a>1&b<2')  # doctest: +NORMALIZE_WHITESPACE
        ([[('a', ())], [('b', (slice(0, 10, 2),))], [('c', ())]],
                ['a>1', 'b<2'])
        >>> parse_ce('a>1&b<2')
        ([], ['a>1', 'b<2'])

    This function can also handle function calls in the URL, according to the
    DAP specification:

        >>> ce = 'time&bounds(0,360,-90,90,0,500,00Z01JAN1970,00Z04JAN1970)'
        >>> print(parse_ce(ce))  # doctest: +NORMALIZE_WHITESPACE
        ([[('time', ())]],
                ['bounds(0,360,-90,90,0,500,00Z01JAN1970,00Z04JAN1970)'])

        >>> ce = 'time,bounds(0,360,-90,90,0,500,00Z01JAN1970,00Z04JAN1970)'
        >>> print(parse_ce(ce))  # doctest: +NORMALIZE_WHITESPACE
        ([[('time', ())],
            'bounds(0,360,-90,90,0,500,00Z01JAN1970,00Z04JAN1970)'], [])
        >>> parse_ce('mean(g,0)')
        (['mean(g,0)'], [])
        >>> parse_ce('mean(mean(g.a,1),0)')
        (['mean(mean(g.a,1),0)'], [])

    Returns a tuple with the projection and the selection.

    """
    tokens = [token for token in unquote(query_string).split("&") if token]
    if not tokens:
        projection = []
        selection = []
    elif re.search("<=|>=|!=|=~|>|<|=", tokens[0]):
        projection = []
        selection = tokens
    else:
        projection = parse_projection(tokens[0])
        selection = tokens[1:]

    return projection, selection


class BaseProxy(object):

    """A proxy for remote base types.

    This class behaves like a Numpy array, proxying the data from a base type
    on a remote dataset.

    """

    def __init__(
        self,
        baseurl,
        id,
        dtype,
        shape,
        slice_=None,
        application=None,
        session=None,
        timeout=DEFAULT_TIMEOUT,
        verify=True,
        user_charset="ascii",
    ):
        self.baseurl = baseurl
        self.id = id
        self.dtype = dtype
        self.shape = shape
        self.slice = slice_ or tuple(slice(None) for s in self.shape)
        self.application = application
        self.session = session
        self.timeout = timeout
        self.verify = verify
        self.user_charset = user_charset

    def __repr__(self):
        return "BaseProxy(%s)" % ", ".join(
            map(repr, [self.baseurl, self.id, self.dtype, self.shape, self.slice])
        )

    def __getitem__(self, index):
        # build download url
        index = combine_slices(self.slice, fix_slice(index, self.shape))
        scheme, netloc, path, query, fragment = urlsplit(self.baseurl)
        url = urlunsplit(
            (
                scheme,
                netloc,
                path + ".dods",
                quote(self.id) + hyperslab(index) + "&" + query,
                fragment,
            )
        ).rstrip("&")

        # download and unpack data
        logger.info("Fetching URL: %s" % url)
        r = GET(
            url,
            self.application,
            self.session,
            timeout=self.timeout,
            verify=self.verify,
        )
        raise_for_status(r)
        dds, data = safe_dds_and_data(r, self.user_charset)

        # Parse received dataset:
        dataset = build_dataset(dds)
        dataset.data = unpack_data(BytesReader(data), dataset)
        return dataset[self.id].data

    def __len__(self):
        return self.shape[0]

    def __iter__(self):
        return iter(self[:])

    # Comparisons return a boolean array
    def __eq__(self, other):
        return self[:] == other

    def __ne__(self, other):
        return self[:] != other

    def __ge__(self, other):
        return self[:] >= other

    def __le__(self, other):
        return self[:] <= other

    def __gt__(self, other):
        return self[:] > other

    def __lt__(self, other):
        return self[:] < other


class DapType(object):

    """The common Opendap type.

    This is a base class, defining common methods and attributes for all other
    classes in the data model.

    """

    def __init__(self, name="nameless", attributes=None, **kwargs):
        self.name = quote(name)
        self.attributes = attributes or {}
        self.attributes.update(kwargs)

        # Set the id to the name.
        self._id = self.name

    def __repr__(self):
        return "DapType(%s)" % ", ".join(map(repr, [self.name, self.attributes]))

    # The id.
    def _set_id(self, id):
        self._id = id

        # Update children id.
        for child in self.children():
            child.id = "%s.%s" % (id, child.name)

    def _get_id(self):
        return self._id

    id = property(_get_id, _set_id)

    def __getattr__(self, attr):
        """Attribute shortcut.

        Data classes have their attributes stored in the `attributes`
        attribute, a dictionary. For convenience, access to attributes can be
        shortcut by accessing the attributes directly::

            >>> var = DapType('var')
            >>> var.attributes['foo'] = 'bar'
            >>> var.foo
            'bar'

        This will return the value stored under `attributes`.

        """
        try:
            return self.attributes[attr]
        except (KeyError, TypeError):
            raise AttributeError(
                "'%s' object has no attribute '%s'" % (type(self), attr)
            )

    def children(self):
        """Return iterator over children."""
        return ()


class StructureType(DapType, Mapping):
    """A dict-like object holding other variables."""

    def __init__(self, name="nameless", attributes=None, **kwargs):
        super(StructureType, self).__init__(name, attributes, **kwargs)

        # allow some keys to be hidden:
        self._visible_keys = []
        self._dict = OrderedDict()

    def __repr__(self):
        return "<%s with children %s>" % (
            type(self).__name__,
            ", ".join(map(repr, self._visible_keys)),
        )

    def __getattr__(self, attr):
        """Lazy shortcut return children."""
        try:
            return self[attr]
        except Exception:
            return DapType.__getattr__(self, attr)

    def __contains__(self, key):
        return key in self._visible_keys

    # __iter__, __getitem__, __len__ are required for Mapping
    # From these, keys, items, values, get, __eq__,
    # and __ne__ are obtained.
    def __iter__(self):
        for key in self._dict.keys():
            if key in self._visible_keys:
                yield key

    def _all_keys(self):
        # used in ..handlers.lib
        return iter(self._dict.keys())

    def _getitem_string(self, key):
        """Assume that key is a string type"""
        try:
            return self._dict[quote(key)]
        except KeyError:
            splitted = key.split(".")
            if len(splitted) > 1:
                try:
                    return self[splitted[0]][".".join(splitted[1:])]
                except (KeyError, IndexError):
                    return self[".".join(splitted[1:])]
            else:
                raise

    def _getitem_string_tuple(self, key):
        """Assume that key is a tuple of strings"""
        out = type(self)(self.name, data=self.data, attributes=self.attributes.copy())
        for name in key:
            out[name] = copy.copy(self._getitem_string(name))
        return out

    def __getitem__(self, key):
        if isinstance(key, str):
            return self._getitem_string(key)
        elif isinstance(key, tuple) and all(isinstance(name, str) for name in key):
            out = copy.copy(self)
            out._visible_keys = list(key)
            return out
        else:
            raise KeyError(key)

    def __len__(self):
        return len(self._visible_keys)

    def children(self):
        # children method always yields an
        # iterator on visible children:
        for key in self._visible_keys:
            yield self[key]

    def __setitem__(self, key, item):
        key = quote(key)
        if key != item.name:
            raise KeyError(
                'Key "%s" is different from variable name "%s"!' % (key, item.name)
            )

        if key in self:
            del self[key]
        self._dict[key] = item
        # By default added keys are visible:
        self._visible_keys.append(key)

        # Set item id.
        item.id = "%s.%s" % (self.id, item.name)

    def __delitem__(self, key):
        del self._dict[key]
        try:
            self._visible_keys.remove(key)
        except ValueError:
            pass

    def _get_data(self):
        return [var.data for var in self.children()]

    def _set_data(self, data):
        for col, var in zip(data, self.children()):
            var.data = col

    data = property(_get_data, _set_data)

    def __shallowcopy__(self):
        out = type(self)(self.name, self.attributes.copy())
        out.id = self.id
        return out

    def __copy__(self):
        """Return a lightweight copy of the Structure.

        The method will return a new Structure with cloned children, but any
        data object are not copied.

        """
        out = self.__shallowcopy__()

        # Clone all children too.
        for child in self._dict.values():
            out[child.name] = copy.copy(child)
        return out


class SequenceType(StructureType):

    """A container that stores data in a Numpy array.

    Here's a standard dataset for testing sequential data:

        >>> import numpy as np
        >>> data = np.array([
        ... (10, 15.2, 'Diamond_St'),
        ... (11, 13.1, 'Blacktail_Loop'),
        ... (12, 13.3, 'Platinum_St'),
        ... (13, 12.1, 'Kodiak_Trail')],
        ... dtype=np.dtype([
        ... ('index', np.int32), ('temperature', np.float32),
        ... ('site', np.dtype('|S14'))]))
        ...
        >>> seq = SequenceType('example')
        >>> seq['index'] = BaseType('index')
        >>> seq['temperature'] = BaseType('temperature')
        >>> seq['site'] = BaseType('site')
        >>> seq.data = data

    Iteraring over the sequence returns data:

        >>> for line in seq.iterdata():
        ...     print(line)
        (10, 15.2, 'Diamond_St')
        (11, 13.1, 'Blacktail_Loop')
        (12, 13.3, 'Platinum_St')
        (13, 12.1, 'Kodiak_Trail')

    The order of the variables can be changed:

        >>> for line in seq['temperature', 'site', 'index'].iterdata():
        ...     print(line)
        (15.2, 'Diamond_St', 10)
        (13.1, 'Blacktail_Loop', 11)
        (13.3, 'Platinum_St', 12)
        (12.1, 'Kodiak_Trail', 13)

    We can iterate over children:

        >>> for line in seq['temperature'].iterdata():
        ...     print(line)
        15.2
        13.1
        13.3
        12.1

    We can filter the data:

        >>> for line in seq[ seq.index > 10 ].iterdata():
        ...     print(line)
        (11, 13.1, 'Blacktail_Loop')
        (12, 13.3, 'Platinum_St')
        (13, 12.1, 'Kodiak_Trail')

        >>> for line in seq[ seq.index > 10 ]['site'].iterdata():
        ...     print(line)
        Blacktail_Loop
        Platinum_St
        Kodiak_Trail

        >>> for line in (seq['site', 'temperature'][seq.index > 10]
        ...              .iterdata()):
        ...     print(line)
        ('Blacktail_Loop', 13.1)
        ('Platinum_St', 13.3)
        ('Kodiak_Trail', 12.1)

    Or slice it:

        >>> for line in seq[::2].iterdata():
        ...     print(line)
        (10, 15.2, 'Diamond_St')
        (12, 13.3, 'Platinum_St')

        >>> for line in seq[ seq.index > 10 ][::2]['site'].iterdata():
        ...     print(line)
        Blacktail_Loop
        Kodiak_Trail

        >>> for line in seq[ seq.index > 10 ]['site'][::2]:
        ...     print(line)
        Blacktail_Loop
        Kodiak_Trail

    """

    def __init__(self, name="nameless", data=None, attributes=None, **kwargs):
        super(SequenceType, self).__init__(name, attributes, **kwargs)
        self._data = data

    def _set_data(self, data):
        self._data = data
        for child in self.children():
            tokens = child.id[len(self.id) + 1 :].split(".")
            child.data = reduce(operator.getitem, [data] + tokens)

    def _get_data(self):
        return self._data

    data = property(_get_data, _set_data)

    def iterdata(self):
        for line in self.data:
            yield tuple(map(decode_np_strings, line))

    def __iter__(self):
        # This method should be removed in pydap 3.4
        warnings.warn(
            "Starting with pydap 3.4 "
            "``for val in sequence: ...`` "
            "will give children names. "
            "To iterate over data the construct "
            "``for val in sequence.iterdata(): ...``"
            "is available now and will be supported in the"
            "future to iterate over data.",
            PendingDeprecationWarning,
        )
        return self.iterdata()

    def __len__(self):
        # This method should be removed in pydap 3.4
        warnings.warn(
            "Starting with pydap 3.4, "
            "``len(sequence)`` will give "
            "the number of children and not the "
            "length of the data.",
            PendingDeprecationWarning,
        )
        return len(self.data)

    def items(self):
        # This method should be removed in pydap 3.4
        for key in self._visible_keys:
            yield (key, self[key])

    def values(self):
        # This method should be removed in pydap 3.4
        for key in self._visible_keys:
            yield self[key]

    def keys(self):
        # This method should be removed in pydap 3.4
        return iter(self._visible_keys)

    def __contains__(self, key):
        # This method should be removed in pydap 3.4
        return key in self._visible_keys

    def __getitem__(self, key):
        # If key is a string, return child with the corresponding data.
        if isinstance(key, string_types):
            return self._getitem_string(key)

        # If it's a tuple, return a new `SequenceType` with selected children.
        elif isinstance(key, tuple):
            out = self._getitem_string_tuple(key)
            # copy.copy() is necessary here because a view will be returned in
            # the future:
            out.data = copy.copy(self.data[list(key)])
            return out

        # Else return a new `SequenceType` with the data sliced.
        else:
            out = copy.copy(self)
            out.data = self.data[key]
            return out

    def __shallowcopy__(self):
        out = type(self)(self.name, self.data, self.attributes.copy())
        out.id = self.id
        return out


class GridType(StructureType):

    """A Grid container.

    The Grid is a Structure with an array and the corresponding axes.

    """

    def __init__(self, name="nameless", attributes=None, **kwargs):
        super(GridType, self).__init__(name, attributes, **kwargs)
        self._output_grid = True

    def __repr__(self):
        return "<%s with array %s and maps %s>" % (
            type(self).__name__,
            repr(list(self.keys())[0]),
            ", ".join(map(repr, list(self.keys())[1:])),
        )

    def __getitem__(self, key):
        # Return a child.
        if isinstance(key, str):
            return self._getitem_string(key)

        # Return a new `GridType` with part of the data.
        elif isinstance(key, tuple) and all(isinstance(name, str) for name in key):
            out = self._getitem_string_tuple(key)
            for var in out.children():
                var.data = self[var.name].data
            return out
        else:
            if not self.output_grid:
                return self.array[key]

            if not isinstance(key, tuple):
                key = (key,)

            out = copy.copy(self)
            for var, slice_ in zip(out.children(), [key] + list(key)):
                var.data = self[var.name].data[slice_]
            return out

    @property
    def dtype(self):
        """Return the first children dtype."""
        return self.array.dtype

    @property
    def shape(self):
        """Return the first children shape."""
        return self.array.shape

    @property
    def ndim(self):
        return len(self.shape)

    @property
    def size(self):
        return int(np.prod(self.shape))

    @property
    def output_grid(self):
        return self._output_grid

    def set_output_grid(self, key):
        self._output_grid = bool(key)

    @property
    def array(self):
        """Return the first children."""
        return self[list(self.keys())[0]]

    def __array__(self):
        return self.array.data

    @property
    def maps(self):
        """Return the axes in an ordered dict."""
        return OrderedDict([(k, self[k]) for k in self.keys()][1:])

    @property
    def dimensions(self):
        """Return the name of the axes."""
        return tuple(list(self.keys())[1:])


def get_charset(r, user_charset):
    charset = r.charset
    if not charset:
        charset = user_charset
    return charset


def safe_charset_text(r, user_charset):
    if r.content_encoding == "gzip":
        return (
            gzip.GzipFile(fileobj=BytesIO(r.body))
            .read()
            .decode(get_charset(r, user_charset))
        )
    else:
        r.charset = get_charset(r, user_charset)
        return r.text


def get_response(req, application, verify=True):
    """
    If verify=False, use the ssl library to temporarily disable
    ssl verification.
    """
    if verify:
        resp = req.get_response(application)
    else:
        # Here, we use monkeypatching. Webob does not provide a way
        # to bypass SSL verification.
        # This approach is never ideal but it appears to be the only option
        # here.
        # This only works in python 2.7 and >=3.5. Python 3.4
        # does not require it because by default contexts are not
        # verified.
        try:
            _create_default_https_ctx = ssl._create_default_https_context
            _create_unverified_ctx = ssl._create_unverified_context
            ssl._create_default_https_context = _create_unverified_ctx
        except AttributeError:
            _create_default_https_ctx = None

        try:
            resp = req.get_response(application)
        finally:
            if _create_default_https_ctx is not None:
                # Restore verified context
                ssl._create_default_https_context = _create_default_https_ctx
    return resp


def create_request_from_session(url, session, timeout=DEFAULT_TIMEOUT, verify=True):
    try:
        # Use session to follow redirects:
        with closing(
            session.head(url, allow_redirects=True, timeout=timeout, verify=verify)
        ) as head:
            req = Request.blank(head.url)
            req.environ["webob.client.timeout"] = timeout

            # Get cookies from head:
            cookies_dict = head.cookies.get_dict()

            # Set request cookies to the head cookies:
            req.headers["Cookie"] = ",".join(
                name + "=" + cookies_dict[name] for name in cookies_dict
            )
            # Set the headers to the session headers:
            for item in head.request.headers:
                req.headers[item] = head.request.headers[item]
            return req
    except (MissingSchema, InvalidSchema):
        # Missing schema can occur in tests when the url
        # is not pointing to any resource. Simply pass.
        req = Request.blank(url)
        req.environ["webob.client.timeout"] = timeout
        return req
    except Timeout:
        raise HTTPError("Timeout")


def create_request(url, session=None, timeout=DEFAULT_TIMEOUT, verify=True):
    if session is not None:
        # If session is set and cookies were loaded using pydap.cas.get_cookies
        # using the check_url option, then we can legitimately expect that
        # the connection will go through seamlessly. However, there might be
        # redirects that might want to modify the cookies. Webob is not
        # really up to the task here. The approach used here is to
        # piggy back on the requests library and use it to fetch the
        # head of the requested url. Requests will follow redirects and
        # adjust the cookies as needed. We can then use the final url and
        # the final cookies to set up a webob Request object that will
        # be guaranteed to have all the needed credentials:
        return create_request_from_session(url, session, timeout=timeout, verify=verify)
    else:
        # If a session object was not passed, we simply pass a new
        # requests.Session() object. The requests library allows the
        # handling of redirects that are not naturally handled by Webob.
        return create_request_from_session(
            url, requests.Session(), timeout=timeout, verify=verify
        )


def follow_redirect(
    url, application=None, session=None, timeout=DEFAULT_TIMEOUT, verify=True
):
    """
    This function essentially performs the following command:
    >>> Request.blank(url).get_response(application)  # doctest: +SKIP

    It however makes sure that the request possesses the same cookies and
    headers as the passed session.
    """

    req = create_request(url, session=session, timeout=timeout, verify=verify)
    return get_response(req, application, verify=verify)


def load_from_entry_point_relative(r, package):
    try:
        loaded = getattr(
            __import__(
                r.module_name.replace(package + ".", "", 1),
                globals(),
                None,
                [r.attrs[0]],
                1,
            ),
            r.attrs[0],
        )
        return r.name, loaded
    except ImportError:
        # This is only used in handlers testing:
        return r.name, r.load()


def walk(var, type=object):
    """Yield all variables of a given type from a dataset.

    The iterator returns also the parent variable.

    """
    if isinstance(var, type):
        yield var
    for child in var.children():
        for var in walk(child, type):
            yield var


def add_attributes(dataset, attributes):
    """Add attributes from a parsed DAS to a dataset.

    Returns the dataset with added attributes.

    """
    dataset.attributes["NC_GLOBAL"] = attributes.get("NC_GLOBAL", {})
    dataset.attributes["DODS_EXTRA"] = attributes.get("DODS_EXTRA", {})

    for var in list(walk(dataset))[::-1]:
        # attributes can be flat, eg, "foo.bar" : {...}
        if var.id in attributes:
            var.attributes.update(attributes.pop(var.id))

        # or nested, eg, "foo" : { "bar" : {...} }
        try:
            nested = reduce(operator.getitem, [attributes] + var.id.split(".")[:-1])
            k = var.id.split(".")[-1]
            value = nested.pop(k)
        except KeyError:
            pass
        else:
            try:
                var.attributes.update(value)
            except (TypeError, ValueError):
                # This attribute should be given to the parent.
                # Keep around:
                nested.update({k: value})

    # add attributes that don't belong to any child
    for k, v in attributes.items():
        dataset.attributes[k] = v

    return dataset


def load_responses():
    """Load all available responses from the system, returning a dictionary."""
    # Relative import of responses:
    package = "pydap"
    entry_points = "pydap.response"
    base_dict = dict(
        load_from_entry_point_relative(r, package)
        for r in iter_entry_points(entry_points)
        if r.module_name.startswith(package)
    )
    opts_dict = dict(
        (r.name, r.load())
        for r in iter_entry_points(entry_points)
        if not r.module_name.startswith(package)
    )
    base_dict.update(opts_dict)
    return base_dict


class BaseHandler(object):

    """Base class for pydap handlers.

    Handlers are WSGI applications that parse the client request and build the
    corresponding dataset. The dataset is passed to proper Response (DDS, DAS,
    etc.)

    """

    # load all available responses
    responses = load_responses()

    def __init__(self, dataset=None, gzip=False):
        self.dataset = dataset
        self.additional_headers = []
        self._gzip = gzip

    def __call__(self, environ, start_response):
        req = Request(environ)
        path, response = req.path.rsplit(".", 1)
        if response == "das":
            req.query_string = ""
        projection, selection = parse_ce(req.query_string)
        buffer_size = environ.get("pydap.buffer_size", BUFFER_SIZE)

        try:
            # build the dataset and pass it to the proper response, returning a
            # WSGI app
            dataset = self.parse(projection, selection, buffer_size)
            app = self.responses[response](dataset)
            app.close = self.close

            # now build a Response and set additional headers
            res = req.get_response(app)
            for key, value in self.additional_headers:
                res.headers.add(key, value)

            # CORS for Javascript requests
            if response in CORS_RESPONSES:
                res.headers.add("Access-Control-Allow-Origin", "*")
                res.headers.add(
                    "Access-Control-Allow-Headers",
                    "Origin, X-Requested-With, Content-Type",
                )

            if self._gzip:
                res.encode_content()
            return res(environ, start_response)
        except Exception:
            # should the exception be catched?
            if environ.get("x-wsgiorg.throw_errors"):
                raise
            else:
                res = ErrorResponse(info=sys.exc_info())
                return res(environ, start_response)

    def parse(self, projection, selection, buffer_size=BUFFER_SIZE):
        """Parse the constraint expression, returning a new dataset."""
        if self.dataset is None:
            raise NotImplementedError(
                "Subclasses must define a ``dataset`` attribute pointing to a"
                "``DatasetType`` object."
            )

        # make a copy of the dataset, so we can filter sequences inplace
        dataset = copy.copy(self.dataset)

        # apply the selection to the dataset, inplace
        apply_selection(selection, dataset)

        # wrap data in Arrayterator, to optimize projection/selection
        dataset = wrap_arrayterator(dataset, buffer_size)

        # fix projection
        if projection:
            projection = fix_shorthand(projection, dataset)
        else:
            projection = [[(key, ())] for key in dataset.keys()]
        dataset = apply_projection(projection, dataset)

        return dataset

    def close(self):
        """Optional method for closing the dataset."""
        pass


class DapType(object):

    """The common Opendap type.

    This is a base class, defining common methods and attributes for all other
    classes in the data model.

    """

    def __init__(self, name="nameless", attributes=None, **kwargs):
        self.name = quote(name)
        self.attributes = attributes or {}
        self.attributes.update(kwargs)

        # Set the id to the name.
        self._id = self.name

    def __repr__(self):
        return "DapType(%s)" % ", ".join(map(repr, [self.name, self.attributes]))

    # The id.
    def _set_id(self, id):
        self._id = id

        # Update children id.
        for child in self.children():
            child.id = "%s.%s" % (id, child.name)

    def _get_id(self):
        return self._id

    id = property(_get_id, _set_id)

    def __getattr__(self, attr):
        """Attribute shortcut.

        Data classes have their attributes stored in the `attributes`
        attribute, a dictionary. For convenience, access to attributes can be
        shortcut by accessing the attributes directly::

            >>> var = DapType('var')
            >>> var.attributes['foo'] = 'bar'
            >>> var.foo
            'bar'

        This will return the value stored under `attributes`.

        """
        try:
            return self.attributes[attr]
        except (KeyError, TypeError):
            raise AttributeError(
                "'%s' object has no attribute '%s'" % (type(self), attr)
            )

    def children(self):
        """Return iterator over children."""
        return ()


class DatasetType(StructureType):

    """A root Dataset.

    The Dataset is a Structure, but it names does not compose the id hierarchy:

        >>> dataset = DatasetType("A")
        >>> dataset["B"] = BaseType("B")
        >>> dataset["B"].id
        'B'

    """

    def __setitem__(self, key, item):
        StructureType.__setitem__(self, key, item)

        # The dataset name does not goes into the children ids.
        item.id = item.name

    def _set_id(self, id):
        """The dataset name is not included in the children ids."""
        self._id = id

        for child in self.children():
            child.id = child.name

    def to_netcdf(self, *args, **kwargs):
        try:
            from .apis.netcdf4 import NetCDF

            return NetCDF(self, *args, **kwargs)
        except ImportError:
            raise NotImplementedError(".to_netcdf requires the netCDF4 " "package.")


def DAP2_parser_typemap(type_string):
    """
    This function takes a numpy dtype object
    and returns a dtype object that is compatible with
    the DAP2 specification.
    """
    dtype_str = LOWER_DAP2_TO_NUMPY_PARSER_TYPEMAP[type_string.lower()]
    return np.dtype(dtype_str)


class SimpleParser(object):

    """A very simple parser."""

    def __init__(self, input, flags=0):
        self.buffer = input
        self.flags = flags

    def peek(self, regexp):
        """Check if a token is present and return it."""
        p = re.compile(regexp, self.flags)
        m = p.match(self.buffer)
        if m:
            token = m.group()
        else:
            token = ""
        return token

    def consume(self, regexp):
        """Consume a token from the buffer and return it."""
        p = re.compile(regexp, self.flags)
        m = p.match(self.buffer)
        if m:
            token = m.group()
            self.buffer = self.buffer[len(token) :]
        else:
            raise Exception("Unable to parse token: %s" % self.buffer[:10])
        return token


class DASParser(SimpleParser):

    """A parser for the Dataset Attribute Structure response."""

    def __init__(self, das):
        super(DASParser, self).__init__(das, re.IGNORECASE | re.VERBOSE | re.DOTALL)

    def consume(self, regexp):
        """Return a token from the buffer.

        Not that it will Ignore white space when consuming tokens.

        """
        token = super(DASParser, self).consume(regexp)
        self.buffer = self.buffer.lstrip()
        return token

    def parse(self):
        """Start the parsing, returning a nested dictionary of attributes."""
        out = {}
        self.consume("attributes")
        self.container(out)
        return out

    def container(self, target):
        """Collect the attributes for a DAP variable."""
        self.consume("{")
        while not self.peek("}"):
            if self.peek(r"[^\s]+\s+{"):
                name = self.consume(r"[^\s]+")
                target[name] = {}
                self.container(target[name])
            else:
                name, values = self.attribute()
                target[name] = values
        self.consume("}")

    def attribute(self):
        """Parse attributes.

        The function will parse attributes from the DAS, converting them to the
        corresponding Python object. Returns the name of the attribute and the
        attribute(s).

        """
        type = self.consume(r"[^\s]+")
        name = self.consume(r"[^\s]+")

        values = []
        while not self.peek(";"):
            value = self.consume(
                r"""
                    ""          # empty attribute
                    |           # or
                    ".*?[^\\]"  # from quote up to an unquoted quote
                    |           # or
                    [^;,]+      # up to semicolon or comma
                """
            )

            if type.lower() in ["string", "url"]:
                value = str(value).strip('"')
            elif value.lower() in ["nan", "nan.", "-nan"]:
                value = float("nan")
            elif value.lower() in ["inf", "inf."]:
                value = float("inf")
            elif value.lower() in ["-inf", "-inf."]:
                value = float("-inf")
            else:
                value = ast.literal_eval(value)

            values.append(value)
            if self.peek(","):
                self.consume(",")

        self.consume(";")

        if len(values) == 1:
            values = values[0]

        return name, values


class DummyData(object):
    def __init__(self, dtype, shape):
        self.dtype = dtype
        self.shape = shape


class BaseType(DapType):

    """A thin wrapper over Numpy arrays."""

    def __init__(
        self, name="nameless", data=None, dimensions=None, attributes=None, **kwargs
    ):
        super(BaseType, self).__init__(name, attributes, **kwargs)
        self.data = data
        self.dimensions = dimensions or ()

        # these are set when not data is present (eg, when parsing a DDS)
        self._dtype = None
        self._shape = ()

    def __repr__(self):
        return "<%s with data %s>" % (type(self).__name__, repr(self.data))

    @property
    def dtype(self):
        """Property that returns the data dtype."""
        return self.data.dtype

    @property
    def shape(self):
        """Property that returns the data shape."""
        return self.data.shape

    def reshape(self, *args):
        """Method that reshapes the data:"""
        self.data = self.data.reshape(*args)
        return self

    @property
    def ndim(self):
        return len(self.shape)

    @property
    def size(self):
        return int(np.prod(self.shape))

    def __copy__(self):
        """A lightweight copy of the variable.

        This will return a new object, with a copy of the attributes,
        dimensions, same name, and a view of the data.

        """
        out = type(self)(
            self.name, self.data, self.dimensions[:], self.attributes.copy()
        )
        out.id = self.id
        return out

    # Comparisons are passed to the data.
    def __eq__(self, other):
        return self.data == other

    def __ne__(self, other):
        return self.data != other

    def __ge__(self, other):
        return self.data >= other

    def __le__(self, other):
        return self.data <= other

    def __gt__(self, other):
        return self.data > other

    def __lt__(self, other):
        return self.data < other

    # Implement the sequence and iter protocols.
    def __getitem__(self, index):
        out = copy.copy(self)
        out.data = self._get_data_index(index)
        return out

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        if self._is_string_dtype:
            for item in self.data:
                yield np.vectorize(decode_np_strings)(item)
        else:
            for item in self.data:
                yield item

    @property
    def _is_string_dtype(self):
        return hasattr(self._data, "dtype") and self._data.dtype.char == "S"

    def iterdata(self):
        """This method was added to mimic new SequenceType method."""
        return iter(self)

    def __array__(self):
        return self._get_data_index()

    def _get_data_index(self, index=Ellipsis):
        if self._is_string_dtype and isinstance(self._data, np.ndarray):
            return np.vectorize(decode_np_strings)(self._data[index])
        else:
            return self._data[index]

    def _get_data(self):
        return self._data

    def _set_data(self, data):
        self._data = data
        if np.isscalar(data):
            # Convert scalar data to
            # numpy scalar, otherwise
            # ``.dtype`` and ``.shape``
            # methods will fail.
            self._data = np.array(data)

    data = property(_get_data, _set_data)


class DDSParser(SimpleParser):

    """A parser for the DDS."""

    def __init__(self, dds):
        super(DDSParser, self).__init__(dds, re.IGNORECASE)
        self.dds = dds

    def consume(self, regexp):
        """Consume and return a token."""
        token = super(DDSParser, self).consume(regexp)
        self.buffer = self.buffer.lstrip()
        return token

    def parse(self):
        """Parse the DAS, returning a dataset."""
        dataset = DatasetType("nameless")

        self.consume("dataset")
        self.consume("{")
        while not self.peek("}"):
            var = self.declaration()
            dataset[var.name] = var
        self.consume("}")

        dataset.name = quote(self.consume("[^;]+"))
        dataset._set_id(dataset.name)
        self.consume(";")

        return dataset

    def declaration(self):
        """Parse and return a declaration."""
        token = self.peek(r"\w+").lower()

        map = {
            "grid": self.grid,
            "sequence": self.sequence,
            "structure": self.structure,
        }
        method = map.get(token, self.base)
        return method()

    def base(self):
        """Parse a base variable, returning a ``BaseType``."""
        data_type_string = self.consume(r"\w+")

        parser_dtype = DAP2_parser_typemap(data_type_string)
        name = quote(self.consume(r"[^;\[]+"))

        shape, dimensions = self.dimensions()
        self.consume(r";")

        data = DummyData(parser_dtype, shape)
        var = BaseType(name, data, dimensions=dimensions)

        return var

    def dimensions(self):
        """Parse variable dimensions, returning tuples of dimensions/names."""
        shape = []
        names = []
        while not self.peek(";"):
            self.consume(r"\[")
            token = self.consume(name_regexp)
            if self.peek("="):
                names.append(token)
                self.consume("=")
                token = self.consume(r"\d+")
            shape.append(int(token))
            self.consume(r"\]")
        return tuple(shape), tuple(names)

    def sequence(self):
        """Parse a DAS sequence, returning a ``SequenceType``."""
        sequence = SequenceType("nameless")
        self.consume("sequence")
        self.consume("{")

        while not self.peek("}"):
            var = self.declaration()
            sequence[var.name] = var
        self.consume("}")

        sequence.name = quote(self.consume("[^;]+"))
        self.consume(";")
        return sequence

    def structure(self):
        """Parse a DAP structure, returning a ``StructureType``."""
        structure = StructureType("nameless")
        self.consume("structure")
        self.consume("{")

        while not self.peek("}"):
            var = self.declaration()
            structure[var.name] = var
        self.consume("}")

        structure.name = quote(self.consume("[^;]+"))
        self.consume(";")

        return structure

    def grid(self):
        """Parse a DAP grid, returning a ``GridType``."""
        grid = GridType("nameless")
        self.consume("grid")
        self.consume("{")

        self.consume("array")
        self.consume(":")
        array = self.base()
        grid[array.name] = array

        self.consume("maps")
        self.consume(":")
        while not self.peek("}"):
            var = self.base()
            grid[var.name] = var
        self.consume("}")

        grid.name = quote(self.consume("[^;]+"))
        self.consume(";")

        return grid


def build_dataset(dds):
    """Return a dataset object from a DDS representation."""
    return DDSParser(dds).parse()


def parse_das(das):
    """Parse the DAS, returning nested dictionaries."""
    return DASParser(das).parse()


def raise_for_status(response):
    # Raise error if status is above 300:
    if response.status_code >= 400:
        raise HTTPError(
            detail=response.status + "\n" + response.text,
            headers=response.headers,
            comment=response.body,
        )
    elif response.status_code >= 300:
        try:
            text = response.text
        except AttributeError:
            # With this status_code, response.text could
            # be ill-defined. If the redirect does not set
            # an encoding (i.e. response.charset is None).
            # Set the text to empty string:
            text = ""
        raise HTTPError(
            detail=(
                response.status
                + "\n"
                + text
                + "\n"
                + "This is redirect error. These should not usually raise "
                + "an error in pydap beacuse redirects are handled "
                + "implicitly. If it failed it is likely due to a "
                + "circular redirect."
            ),
            headers=response.headers,
            comment=response.body,
        )


def GET(url, application=None, session=None, timeout=DEFAULT_TIMEOUT, verify=True):
    """Open a remote URL returning a webob.response.Response object

    Optional parameters:
    session: a requests.Session() object (potentially) containing
             authentication cookies.

    Optionally open a URL to a local WSGI application
    """
    if application:
        _, _, path, query, fragment = urlsplit(url)
        url = urlunsplit(("", "", path, query, fragment))

    response = follow_redirect(
        url, application=application, session=session, timeout=timeout, verify=verify
    )
    # Decode request response (i.e. gzip)
    response.decode_content()
    return response


class DapType(object):

    """The common Opendap type.

    This is a base class, defining common methods and attributes for all other
    classes in the data model.

    """

    def __init__(self, name="nameless", attributes=None, **kwargs):
        self.name = quote(name)
        self.attributes = attributes or {}
        self.attributes.update(kwargs)

        # Set the id to the name.
        self._id = self.name

    def __repr__(self):
        return "DapType(%s)" % ", ".join(map(repr, [self.name, self.attributes]))

    # The id.
    def _set_id(self, id):
        self._id = id

        # Update children id.
        for child in self.children():
            child.id = "%s.%s" % (id, child.name)

    def _get_id(self):
        return self._id

    id = property(_get_id, _set_id)

    def __getattr__(self, attr):
        """Attribute shortcut.

        Data classes have their attributes stored in the `attributes`
        attribute, a dictionary. For convenience, access to attributes can be
        shortcut by accessing the attributes directly::

            >>> var = DapType('var')
            >>> var.attributes['foo'] = 'bar'
            >>> var.foo
            'bar'

        This will return the value stored under `attributes`.

        """
        try:
            return self.attributes[attr]
        except (KeyError, TypeError):
            raise AttributeError(
                "'%s' object has no attribute '%s'" % (type(self), attr)
            )

    def children(self):
        """Return iterator over children."""
        return ()


def encode(obj):
    """Return an object encoded to its DAP representation."""
    # fix for Python 3.5, where strings are being encoded as numbers
    if isinstance(obj, str) or isinstance(obj, np.ndarray) and obj.dtype.char in "SU":
        return '"{0}"'.format(obj)

    try:
        return "%.6g" % obj
    except Exception:
        return '"{0}"'.format(obj)


def unpack_data(xdr_stream, dataset):
    """Unpack a string of encoded data, returning data as lists."""
    return unpack_children(xdr_stream, dataset)


class StreamReader(object):

    """Class to allow reading a `urllib3.HTTPResponse`."""

    def __init__(self, stream):
        self.stream = stream
        self.buf = bytearray()

    def read(self, n):
        """Read and return `n` bytes."""
        while len(self.buf) < n:
            bytes_read = next(self.stream)
            self.buf.extend(bytes_read)

        out = bytes(self.buf[:n])
        self.buf = self.buf[n:]
        return out


class DAPHandler(BaseHandler):

    """Build a dataset from a DAP base URL."""

    def __init__(
        self,
        url,
        application=None,
        session=None,
        output_grid=True,
        timeout=DEFAULT_TIMEOUT,
        verify=True,
        user_charset="ascii",
    ):
        # download DDS/DAS
        scheme, netloc, path, query, fragment = urlsplit(url)

        ddsurl = urlunsplit((scheme, netloc, path + ".dds", query, fragment))
        r = GET(ddsurl, application, session, timeout=timeout, verify=verify)
        raise_for_status(r)
        try:
            dds = safe_charset_text(r, user_charset)
        except AttributeError:
            dds = safe_charset_text(r, None)

        dasurl = urlunsplit((scheme, netloc, path + ".das", query, fragment))
        r = GET(dasurl, application, session, timeout=timeout, verify=verify)
        raise_for_status(r)
        try:
            das = safe_charset_text(r, user_charset)
        except AttributeError:
            das = safe_charset_text(r, None)

        # build the dataset from the DDS and add attributes from the DAS
        self.dataset = build_dataset(dds)
        add_attributes(self.dataset, parse_das(das))

        # remove any projection from the url, leaving selections
        projection, selection = parse_ce(query)
        url = urlunsplit((scheme, netloc, path, "&".join(selection), fragment))

        # now add data proxies
        for var in walk(self.dataset, BaseType):
            var.data = BaseProxy(
                url,
                var.id,
                var.dtype,
                var.shape,
                application=application,
                session=session,
            )
        for var in walk(self.dataset, SequenceType):
            template = copy.copy(var)
            var.data = SequenceProxy(
                url, template, application=application, session=session
            )

        # apply projections
        for var in projection:
            target = self.dataset
            while var:
                token, index = var.pop(0)
                target = target[token]
                if isinstance(target, BaseType):
                    target.data.slice = fix_slice(index, target.shape)
                elif isinstance(target, GridType):
                    index = fix_slice(index, target.array.shape)
                    target.array.data.slice = index
                    for s, child in zip(index, target.maps):
                        target[child].data.slice = (s,)
                elif isinstance(target, SequenceType):
                    target.data.slice = index

        # retrieve only main variable for grid types:
        for var in walk(self.dataset, GridType):
            var.set_output_grid(output_grid)


def open_url(
    url,
    application=None,
    session=None,
    output_grid=True,
    timeout=DEFAULT_TIMEOUT,
    verify=True,
    user_charset="ascii",
):
    """
    Open a remote URL, returning a dataset.

    set output_grid to False to retrieve only main arrays and
    never retrieve coordinate axes.
    """
    dataset = DAPHandler(
        url,
        application,
        session,
        output_grid,
        timeout=timeout,
        verify=verify,
        user_charset=user_charset,
    ).dataset

    # attach server-side functions
    dataset.functions = Functions(url, application, session, timeout=timeout)

    return dataset


def open_file(dods, das=None):
    """Open a file downloaded from a `.dods` response, returning a dataset.

    Optionally, read also the `.das` response to assign attributes to the
    dataset.

    """
    dds = ""
    # This file contains both ascii _and_ binary data
    # Let's handle them separately in sequence
    # Without ignoring errors, the IO library will
    # actually read past the ascii part of the
    # file (despite our break from iteration) and
    # will error out on the binary data
    with open(
        dods, "rt", buffering=1, encoding="ascii", newline="\n", errors="ignore"
    ) as f:
        for line in f:
            if line.strip() == "Data:":
                break
            dds += line
    dataset = build_dataset(dds)
    pos = len(dds) + len("Data:\n")

    with open(dods, "rb") as f:
        f.seek(pos)
        dataset.data = unpack_data(f, dataset)

    if das is not None:
        with open(das) as f:
            add_attributes(dataset, parse_das(f.read()))

    return dataset


def open_dods(
    url,
    metadata=False,
    application=None,
    session=None,
    timeout=DEFAULT_TIMEOUT,
    verify=True,
):
    """Open a `.dods` response directly, returning a dataset."""
    r = GET(url, application, session, timeout=timeout)
    raise_for_status(r)

    dds, data = r.body.split(b"\nData:\n", 1)
    dds = dds.decode(r.content_encoding or "ascii")
    dataset = build_dataset(dds)
    stream = StreamReader(BytesIO(data))
    dataset.data = unpack_data(stream, dataset)

    if metadata:
        scheme, netloc, path, query, fragment = urlsplit(url)
        dasurl = urlunsplit((scheme, netloc, path[:-4] + "das", query, fragment))
        r = GET(dasurl, application, session, timeout=timeout, verify=verify)
        raise_for_status(r)
        das = r.text
        add_attributes(dataset, parse_das(das))

    return dataset


class Functions(object):

    """Proxy for server-side functions."""

    def __init__(
        self, baseurl, application=None, session=None, timeout=DEFAULT_TIMEOUT
    ):
        self.baseurl = baseurl
        self.application = application
        self.session = session
        self.timeout = timeout

    def __getattr__(self, attr):
        return ServerFunction(
            self.baseurl, attr, self.application, self.session, timeout=self.timeout
        )


class ServerFunction(object):

    """A proxy for a server-side function.

    Instead of returning datasets, the function will return a proxy object,
    allowing nested requests to be performed on the server.

    """

    def __init__(
        self, baseurl, name, application=None, session=None, timeout=DEFAULT_TIMEOUT
    ):
        self.baseurl = baseurl
        self.name = name
        self.application = application
        self.session = session
        self.timeout = timeout

    def __call__(self, *args):
        params = []
        for arg in args:
            if isinstance(arg, (DapType, ServerFunctionResult)):
                params.append(arg.id)
            else:
                params.append(encode(arg))
        id_ = self.name + "(" + ",".join(params) + ")"
        return ServerFunctionResult(
            self.baseurl, id_, self.application, self.session, timeout=self.timeout
        )


class ServerFunctionResult(object):

    """A proxy for the result from a server-side function call."""

    def __init__(
        self, baseurl, id_, application=None, session=None, timeout=DEFAULT_TIMEOUT
    ):
        self.id = id_
        self.dataset = None
        self.application = application
        self.session = session
        self.timeout = timeout

        scheme, netloc, path, query, fragment = urlsplit(baseurl)
        self.url = urlunsplit((scheme, netloc, path + ".dods", id_, None))

    def __getitem__(self, key):
        if self.dataset is None:
            self.dataset = open_dods(
                self.url, True, self.application, self.session, self.timeout
            )
        return self.dataset[key]

    def __getattr__(self, name):
        return self[name]
