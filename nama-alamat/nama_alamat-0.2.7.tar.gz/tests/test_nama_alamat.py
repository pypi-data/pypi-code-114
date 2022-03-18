#!/usr/bin/env python

"""Tests for `nama_alamat` package."""

import pytest


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

    from nama_alamat.preprocessing import Preprocessing

    preprocessing_nama = Preprocessing(tipe='nama')
    preprocessing_alamat = Preprocessing(tipe='alamat')

    strings1 = 'IR SULAEMAN'
    strings2 = 'JALAN GARUDA IX BLOK C/3 RT 003 RW 002, JAKARTA UTARA, DKI JAKARTA 12110'
    strings3 = 'A L I'
    strings4 = 'DONI DONI'

    return (
        preprocessing_nama.preprocessing(strings1)
        + preprocessing_alamat.preprocessing(strings2)
        + preprocessing_nama.preprocessing(strings3)
        + preprocessing_nama.preprocessing(strings4)
    )


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    assert 'sulaeman' in response
    assert 'jakarta' in response
    del response
