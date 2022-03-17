import os
import shutil

from unittest import TestCase

from property_price_register.utils import (
    download_zip,
    extract_zip
)


class UtilsTest(TestCase):

    def test_download(self):
        if os.path.exists('/tmp/test_download.zip'):
            shutil.rmtree('/tmp/test_download.zip')
        download_zip('/tmp/test_download.zip')
        self.assertTrue(os.path.exists('/tmp/test_download.zip'))

    def test_extract(self):
        if os.path.isdir('/tmp/test_extract'):
            shutil.rmtree('/tmp/test_extract')

        if os.path.exists('/tmp/test_download.zip'):
            os.remove('/tmp/test_download.zip')

        download_zip('/tmp/test_extract.zip')
        extract_zip('/tmp/test_extract.zip')
        self.assertTrue(os.path.isdir('/tmp/test_extract'))
