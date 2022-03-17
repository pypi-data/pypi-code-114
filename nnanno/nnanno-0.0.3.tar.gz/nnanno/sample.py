# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_sample.ipynb (unless otherwise specified).

__all__ = ['get_json_url', 'load_json', 'count_json_iter', 'get_year_size', 'get_year_sizes', 'get_all_year_sizes',
           'sample_stream', 'calc_frac_size', 'calc_year_from_total', 'reduce_df_memory', 'nnSampler', 'sample_year',
           'create_sample', 'download_sample']

# Cell
from .core import *

# Cell
# TODO tidy imports
# sys
import io
import shutil
import pkg_resources
from pathlib import Path
from datetime import datetime

# other
from tqdm.auto import trange, tqdm
import requests
import ijson
import functools
import math
from cytoolz import dicttoolz, itertoolz
import random
import json
from PIL import Image

import concurrent.futures
import numpy as np
import itertools
from pandas import json_normalize
import pandas as pd
from functools import partial
import numpy as np
from fastcore.foundation import patch_to

# Cell

import PIL
from typing import (
    Any,
    Optional,
    Union,
    Dict,
    List,
    Tuple,
    Set,
    Iterable,
)

# Cell
def get_json_url(year: Union[str, int], kind: str = "photos") -> str:
    """Returns url for the json data from news-navigator for given `year` and `kind`"""
    return f"https://news-navigator.labs.loc.gov/prepackaged/{year}_{kind}.json"

# Cell
def load_json(url: str) -> Dict[str, Any]:
    """Returns json loaded from `url`"""
    with requests.get(url, timeout=2) as r:
        r.raise_for_status()
        return json.loads(r.content)

# Cell
@functools.lru_cache(256)
def count_json_iter(url: str, session=None) -> int:
    """Returns count of objects in url json file using an iterator to avoid loading json into memory"""
    if not session:
        session = create_cached_session()
    with session.get(url, timeout=60) as r:
        r.raise_for_status()
        if r:
            objects = ijson.items(r.content, "item")
            count = itertoolz.count(iter(objects))
        else:
            count = np.nan
    return count

# Cell
@functools.lru_cache(256)
def get_year_size(year: Union[int, str], kind: str) -> dict:
    """returns size of a json dataset for a given year and kind
    results are cached
    Parameters
    ----------
    year : Union[int,str]
        year from newspaper navigator
    kind : str
        {'ads', 'photos', 'maps', 'illustrations', 'comics', 'cartoons', 'headlines'}
    Returns
    -------
    size :dict
        returns a dict with year as a key and size as value
    """
    session = None
    dset_size = {}
    url = get_json_url(year, kind)
    if kind == "ads" and int(year) >= 1870 or (kind == "headlines"):
        session = create_session()
    dset_size[str(year)] = count_json_iter(url, session)
    return dset_size

# Cell
@functools.lru_cache(512)
def get_year_sizes(kind: str, start: int = 1850, end: int = 1950, step: int = 5):
    """
    Returns the sizes for json data files for `kind` between year `start` and `end`
    with step size 'step'

    Parameters:
    kind (str): kind of image from news-navigator:
    {'ads', 'photos', 'maps', 'illustrations', 'comics', 'cartoons', 'headlines'}

    Returns:
    Pandas.DataFrame: holding data from input json url
    """
    futures = []
    years = range(start, end + 1, step)
    max_workers = get_max_workers(years)
    with tqdm(total=len(years)) as progress:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            for year in years:
                future = executor.submit(get_year_size, year, kind)
                future.add_done_callback(lambda p: progress.update())
                futures.append(future)
        results = [future.result() for future in futures]
        dset_size = {k: v for d in results for k, v in d.items()}
    return pd.DataFrame.from_dict(dset_size, orient="index", columns=[f"{kind}_count"])

# Cell
def get_all_year_sizes(
    start: int = 1850, end: int = 1950, step: int = 1, save: bool = True
):
    """
    Returns a dataframe with number of counts from year `start` to `end`
    """
    kinds = [
        "ads",
        "photos",
        "maps",
        "illustrations",
        "comics",
        "cartoons",
        "headlines",
    ]
    dfs = []
    for kind in tqdm(kinds):
        df = get_year_sizes(kind, start=start, end=end, step=step)
        dfs.append(df)
    df = pd.concat(dfs, axis=1)
    df["total"] = df.sum(axis=1)
    if save:
        df.to_csv("all_year_sizes.csv")
    return df

# Cell
def sample_stream(stream, k: int):
    """
    Return a random sample of k elements drawn without replacement from stream.
    Designed to be used when the elements of stream cannot easily fit into memory.
    """
    r = np.array(list(itertools.islice(stream, k)))
    for t, x in enumerate(stream, k + 1):
        i = np.random.randint(1, t + 1)
        if i <= k:
            r[i - 1] = x
    return r

# Cell
@functools.lru_cache(1024)
def calc_frac_size(url, frac, session=None):
    "returns fraction size from a json stream"
    return round(count_json_iter(url, session) * frac)

# Cell
def calc_year_from_total(total, start, end, step):
    "Calculate size of a year sample based on a total sample size"
    return max(1, round(total / (((end - start) + 1) / step)))

# Cell
def reduce_df_memory(df):
    return df.astype(
        {
            "score": "float64",
            "page_seq_num": "int32",
            "batch": "category",
            "box": "object",
            "lccn": "category",
            "page_url": "category",
            "name": "category",
            "publisher": "category",
            "place_of_publication": "category",
            "edition_seq_num": "category",
        }
    )

# Cell
class nnSampler:
    """Sampler for creating samples from Newspaper Navigator data"""

    population = pd.read_csv(
        pkg_resources.resource_stream("nnanno", "data/all_year_counts.csv"), index_col=0
    )

    def __repr__(self):
        return f"{self.__class__.__name__}"

# Cell
def sample_year(kind: str, sample_size: Union[int, float], year: int) -> np.array:
    """samples `sample_size` for `year` and `kind`"""
    url = get_json_url(year, kind)
    if kind == "ads" and int(year) >= 1870 or (kind == "headlines"):
        session = create_session()
    else:
        session = create_cached_session()
    if type(sample_size) is float:
        sample_size = max(1, calc_frac_size(url, sample_size, session))
        if kind == "ads" and int(year) >= 1870 or (kind == "headlines"):
            session = create_session()
        else:
            session = create_cached_session()
    with session.get(get_json_url(year, kind)) as r:
        if r:
            try:
                data = ijson.items(r.content, "item")
                sample_data = sample_stream(iter(data), sample_size)
            except requests.exceptions.RequestException as e:
                sample_data = np.nan
        return sample_data

# Cell
@patch_to(nnSampler)
def create_sample(
    self,
    sample_size: Union[int, float],
    kind: str = "photos",
    start_year: int = 1850,
    end_year: int = 1950,
    step: int = 5,
    year_sample=True,
    save: bool = False,
    reduce_memory=True,
):
    """
    Creates a sample of Newspaper Navigator data for a given set of years and a kind

    Parameters:
    sample_size: int, float
        `sample size` can either be a fixed number or a fraction of the total dataset size
    kind (str): kind of image from news-navigator:
    {'ads', 'photos', 'maps', 'illustrations', 'comics', 'cartoons', 'headlines'}
    start_year (int): year to begin sample from
    end_year (int): year to end sample on
    step: step size between years being sampled
    year_sample (bool): whether to sample by year or total dataset size
    save (bool): whether to save the sample to a `json` file
    redue_memory (bool): use pandas dtypes to reduce memory foot print of sample DataFrame

    Returns:
    Pandas.DataFrame: holding data from input json url
    """

    if not year_sample:
        if type(sample_size) != int:
            raise ValueError(
                f"""type{sample_size} is not an int. Fractions are only supported
                            for sampling by year"""
            )
        sample_size = calc_year_from_total(sample_size, start_year, end_year, step)
    futures = []
    years = range(start_year, end_year + 1, step)
    _year_sample = partial(sample_year, kind, sample_size)
    with tqdm(total=len(years)) as progress:
        workers = get_max_workers(years)
        with concurrent.futures.ThreadPoolExecutor(1) as executor:
            for year in years:
                future = executor.submit(_year_sample, year)
                future.add_done_callback(lambda p: progress.update())
                futures.append(future)
    results = [future.result() for future in futures]
    df = pd.DataFrame.from_dict(list(itertoolz.concat(results)))

    if reduce_memory:
        df = reduce_df_memory(df)
    if save:
        df.to_json(f"{kind}_{start_year}_{end_year}_sample.json")
    self.sample = df
    return df

# Cell
@patch_to(nnSampler)
def download_sample(
    self,
    out_dir: str,
    json_name: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    original: bool = True,
    pct: Optional[int] = None,
    size: Optional[tuple] = None,
    preserve_asp_ratio: bool = True,
) -> Union[None]:
    """Download images associated with a sample
    The majority of paramters relate to the options available in a IIIF image request
    see `https://iiif.io/api/image/3.0/#4-image-requests` for further information

    Parameters
    ----------
    out_dir
        The save directory for the images
    json_name

    df
        optional DataFrame containing a sample
    original
        if `True` will download orginal size images via IIIF
    pct
        optional value which scales the size of images requested by `pct`
    size
        a tuple representing `width` by `height`, will be passed to IIIF request
    preserve_asp_ratio
        whether to ask the IIIF request to preserve aspect ratio of image or not

    Returns
    -------
    None
    """

    if df is not None:
        self.download_df = df.copy(deep=True)
    else:
        try:
            self.download_df = self.sample.copy(deep=True)
        except AttributeError as E:
            print(
                "You need to create a sample before downloading, or pass in a previously created "
            )
    self.download_df["iiif_url"] = self.download_df.apply(
        lambda x: iiif_df_apply(
            x,
            original=original,
            pct=pct,
            size=size,
            preserve_asp_ratio=preserve_asp_ratio,
        ),
        axis=1,
    )
    self.download_df["download_image_path"] = self.download_df["filepath"].str.replace(
        "/", "_"
    )

    if not Path(out_dir).exists():
        Path(out_dir).mkdir(parents=True)
    _download_image = lambda x: download_image(
        x.iiif_url, x.download_image_path, out_dir
    )
    with tqdm(total=len(self.download_df)) as progress:
        workers = get_max_workers(self.download_df)
        with concurrent.futures.ThreadPoolExecutor(workers) as executor:
            futures = []
            for tuple_row in self.download_df.itertuples():
                future = executor.submit(_download_image, tuple_row)
                future.add_done_callback(lambda p: progress.update())
                futures.append(future)
            del futures
    if json_name is None:
        today = datetime.today()
        time_stamp = today.strftime("%Y_%d_%m_%H_%M")
        json_name = f"{time_stamp}_{len(self.download_df)}_sample"
    self.download_df.to_json(f"{out_dir}/{json_name}.json")