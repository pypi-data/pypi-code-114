#
# Copyright (C) 2020 IHS Markit.
# All Rights Reserved
#
import multiprocessing
from typing import List, Optional
from concurrent.futures.thread import ThreadPoolExecutor
from urllib.parse import urljoin
import humps  # noqa: I900

from dli.models.file_model import FileModel

from platform_services_lib.lib.context.urls import consumption_urls
from platform_services_lib.lib.aspects.decorators import analytics_decorator, logging_decorator, log_public_functions_calls_using
from platform_services_lib.lib.services.dlc_attributes_dict import AttributesDict

THREADS = multiprocessing.cpu_count()


class InstanceModel(AttributesDict):

    def __init__(self, **kwargs):
        # Ignore the datafile's files
        kwargs.pop('files', [])
        super().__init__(**kwargs)

    def files(self) -> List[FileModel]:
        """
        :return: list of file models for files in the instance.
        """
        url = urljoin(
            self._client._environment.consumption,
            consumption_urls.consumption_manifest.format(
                id=self.datafile_id
            )
        )

        response = self._client.session.get(url)
        return [
            self._client._File(
                datafile_id=self.datafile_id,
                **d['attributes']
            )
            for d in response.json()['data']
        ]

    @classmethod
    def _from_v1_entity(cls, entity, page_size=None):
        properties = humps.decamelize(entity['properties'])
        return cls(**properties)

    def download(self, to: Optional[str]='./', flatten: Optional[bool]=False) -> List[str]:
        """
        Download the files for the instance, then return a list of the file
        paths that were written.

        :param str to: The path on the system, where the files
            should be saved. must be a directory, if doesn't exist, will be
            created.

        :param bool flatten: The flatten parameter default behaviour
            (flatten=False) will allow the user to specify that they would
            like to keep the underlying folder structure when writing the
            downloaded files to disk.
            When “flatten” is set to True the
            folder structure and download all data to the specified path in
            and retains only the original file name. This is not useful if the
            file names are identical for multiple files.

        :return: List of paths to the downloaded files.

        :example:

            Downloading without flatten:

            .. code-block:: python

                >>> dataset = client.datasets.get(dataset_short_code='ExampleDatasetShortCode', organisation_short_code='IHSMarkit')
                >>> dataset.instances.latest().download('./local/path/')
                [
                  'as_of_date=2019-09-10/type=full/StormEvents_details-ftp_v1.0_d1950_c20170120.csv.gz',
                  'as_of_date=2019-09-11/type=full/StormEvents_details-ftp_v1.0_d1951_c20160223.csv.gz'
                ]


        :example:

            When flatten = True, we remove the s3 structure. Example:

            Example output for new behaviour:

            .. code-block:: python

                >>> dataset.instances.latest().download('./local/path/', flatten=True)
                [
                  'StormEvents_details-ftp_v1.0_d1950_c20170120.csv.gz',
                  'StormEvents_details-ftp_v1.0_d1951_c20160223.csv.gz'
                ]


        """
        files = self.files()

        def _download(file_: FileModel):
            return file_.download(to=to, flatten=flatten)

        threads = min(THREADS, max(1, len(files)))
        with ThreadPoolExecutor(max_workers=threads) as executor:
            return list(executor.map(_download, files))

    def __str__(self):
        return f"\nINSTANCE {self.datafile_id} (size: {self.total_size/1048576 :.2f} Mb)"




log_public_functions_calls_using(
    [analytics_decorator, logging_decorator],
    class_fields_to_log=['datafile_id']
)(InstanceModel)


