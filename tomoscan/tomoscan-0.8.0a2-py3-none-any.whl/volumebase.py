# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2022 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/
"""module to define base class for a volume"""


__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "27/01/2022"


import numpy
from tomoscan.identifier import VolumeIdentifier
from tomoscan.tomoobject import TomoObject
from tomoscan.scanbase import TomoScanBase
from typing import Optional, Union
from silx.io.url import DataUrl


class VolumeBase(TomoObject):
    """
    context: we aim at having a common way of saving and loading volumes through the tomotools suite.
    The goal is to aim handling of volumes when creating them or doing some operations with those like stitching...

    :param DataUlr url: url of the volume. Could be path to a master file if we can provide one per each volume. Otherwise could be a pattern of edf files or tiff file with a data range
    :param Optional[TomoScanBase] source_scan: potential instance of TomoScanBase in order to get extra information. This could be saved in the volume file to (external link)
    :param Optional[nump.ndarray] data: volume data. Expected to be 3D
    :param Optional[dict] metadata: metadata associated to the volume. Must be a dict of serializable object
    :param Optional[DataUrl] data_url: url to save the data. If provided url must not be provided. If an object is constructed from data and metadta url then no rule to create a VolumeIdentifier can be created and call to et_identifier will raise an error.
    :param Optional[DataUrl] metadata_url: url to save the metadata. If provided url must not be provided. If an object is constructed from data and metadta url then no rule to create a VolumeIdentifier can be created and call to et_identifier will raise an error.
    :param bool overwrite: when save the data if encounter a ressource already existing overwrite it (if True) or not.
    :param str overwrite: when save the data if encounter a ressource already existing overwrite it (if True) or not.

    :raises TypeError:
    :raises ValueError: * if data is a numpy array and not 3D.
    :raises OSError:
    """

    EXTENSION = None

    def __init__(
        self,
        url: Optional[DataUrl] = None,
        data: Optional[numpy.ndarray] = None,
        source_scan: Optional[TomoScanBase] = None,
        metadata: Optional[dict] = None,
        data_url: Optional[DataUrl] = None,
        metadata_url: Optional[DataUrl] = None,
        overwrite: bool = False,
    ) -> None:
        super().__init__()
        if url is not None and (data_url is not None or metadata_url is not None):
            raise ValueError(
                "Either url or (data_url and / or metadata_url) can be provided not both"
            )

        # warning on source_scan: should be defined before the url because deduce_data_and_metadata_urls might need it
        # Then as source scan can imply several modification of url... we can only define it during construction and this
        # must not involve with object life
        if not isinstance(source_scan, (TomoScanBase, type(None))):
            raise TypeError(
                f"source scan is expected to be None or an instance of TomoScanBase. Not {type(source_scan)}"
            )
        self.__source_scan = source_scan

        self.overwrite = overwrite
        self.url = url
        self.metadata = metadata
        self.data = data

        if url is None:
            self._data_url = data_url
            self._metadata_url = metadata_url
        else:
            # otherwise have be setted when url has been set from call to deduce_data_and_metadata_urls
            pass

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url: Optional[DataUrl]) -> None:
        if url is not None and not isinstance(url, DataUrl):
            raise TypeError
        self._url = url
        self._data_url, self._metadata_url = self.deduce_data_and_metadata_urls(url)

    def deduce_data_and_metadata_urls(self, url: Optional[DataUrl]) -> tuple:
        """
        compute data and metadata urls from 'parent url'
        :return: data_url: Optional[DataUrl], metadata_url: Optional[DataUrl]
        """
        raise NotImplementedError("Base class")

    @property
    def data_url(self):
        return self._data_url

    @property
    def metadata_url(self):
        return self._metadata_url

    @property
    def data(self) -> Optional[numpy.ndarray]:
        return self._data

    @data.setter
    def data(self, data):
        if not isinstance(data, (numpy.ndarray, type(None))):
            raise TypeError(
                f"data is expected to be None or a numpy array not {type(data)}"
            )
        if isinstance(data, numpy.ndarray) and data.ndim != 3:
            raise ValueError(f"data is expected to be 3D and not {data.ndim}D.")
        self._data = data

    @property
    def metadata(self) -> Optional[dict]:
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Optional[dict]):
        if not isinstance(metadata, (dict, type(None))):
            raise TypeError(
                f"metadata is expected to be None or a dict not {type(metadata)}"
            )
        self._metadata = metadata

    def clear_cache(self):
        """remove object stored in data and medatada"""
        self.data = None
        self.metadata = None

    # generic function requested
    @property
    def source_scan(self) -> Optional[TomoScanBase]:
        return self.__source_scan

    @property
    def overwrite(self) -> bool:
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite: bool) -> None:
        if not isinstance(overwrite, bool):
            raise TypeError
        self._overwrite = overwrite

    # function to be loaded to an url
    @staticmethod
    def from_identifier(identifier: Union[str, VolumeIdentifier]):
        """Return the Dataset from a identifier"""
        raise NotImplementedError("Base class")

    def get_identifier(self) -> VolumeIdentifier:
        """dataset unique identifier. Can be for example a hdf5 and
        en entry from which the dataset can be rebuild"""
        raise NotImplementedError("Base class")

    # utils required for operations like stitching
    @property
    def position(self) -> tuple:
        raise NotImplementedError("Base class")

    @position.setter
    def position(self, position) -> tuple:
        raise NotImplementedError("Base class")

    @property
    def pixel_size(self):
        raise NotImplementedError("Base class")

    @pixel_size.setter
    def pixel_size(self, pixel_size):
        raise NotImplementedError("Base class")

    @property
    def shape(self):
        raise NotImplementedError("Base class")

    @property
    def dims_in_cm(self):
        raise NotImplementedError("Base class")

    def volume(self) -> numpy.array:
        raise NotImplementedError("Base class")

    def get_slice(self, slice_idx) -> numpy.array:
        # is it needed ?
        raise NotImplementedError("Base class")

    # load / save stuff

    @property
    def extension(self) -> str:
        return self.EXTENSION

    def load(self):
        self.load_metadata(store=True)
        # always load metadata first because we might expect to get some information from
        # it in order to load data next
        self.load_data(store=True)

    def save(self, url: Optional[DataUrl] = None):
        if url is not None:
            data_url, metadata_url = self.deduce_data_and_metadata_urls(url=url)
        else:
            data_url = self.data_url
            metadata_url = self.metadata_url
        self.save_data(data_url)
        if self.metadata is not None:
            # a volume is not force to have metadata to save. But calling save_metadata direclty might raise an error
            # if no metadata found
            self.save_metadata(metadata_url)

    def save_data(self, url: Optional[DataUrl] = None) -> None:
        """
        save data to the provided url or existing one if none is provided
        """
        raise NotImplementedError("Base class")

    def save_metadata(self, url: Optional[DataUrl] = None) -> None:
        """
        save metadata to the provided url or existing one if none is provided
        """
        raise NotImplementedError("Base class")

    def load_data(
        self, url: Optional[DataUrl] = None, store: bool = True
    ) -> numpy.ndarray:
        raise NotImplementedError("Base class")

    def load_metadata(self, url: Optional[DataUrl] = None, store: bool = True) -> dict:
        raise NotImplementedError("Base class")

    def check_can_provide_identifier(self):
        if self.url is None:
            raise ValueError(
                "Unable to provide an identifier. No url has been provided"
            )
