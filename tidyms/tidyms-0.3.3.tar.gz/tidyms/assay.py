import pickle
from pathlib import Path
from typing import Optional, Tuple, List, Dict, Union, Callable
from .fileio import MSData
from .lcms import Roi
from .utils import is_notebook
from multiprocessing import Pool
from functools import partial
from time import time_ns
from tqdm import tqdm as cli_bar
from tqdm.notebook import tqdm as notebook_bar
import numpy as np
import pandas as pd

# TODO: testear y refactorear feature_correspondence. Agregar funcionalidad
#   para plotear ROI y features. Incluir funcionalidad para crear datacontainer.
#   agregar funcionalidad para almacenar ROI en disco.
#   la idea seria usar un parametro store_to_disk que se use para crear una
#   carpeta donde se almacenen las ROI.

# TODO: raise error messages if the functions are called in the wrong order
#   This could be done implementing a tag associated with each processing step
#   If the tag changes, the process should be done again. tag can be generated
#   from the hash of the parameters.

# TODO: add options to add new_samples

# TODO: add path variable to load existing assay data

class Assay:

    def __init__(
        self,
        path: Union[str, List[str], Path],
        sample_metadata: Optional[pd.DataFrame] = None,
        name: Optional[str] = None,
        ms_mode: str = "centroid",
        instrument: str = "qtof",
        separation: str = "uplc",
    ):
        # path for mzml files
        path_list = _get_path_list(path)
        name2path = {x.stem: x for x in path_list}
        self._name_to_path = name2path

        # sample metadata
        sample2code = dict(zip(name2path.keys(), range(len(name2path))))
        self._sample_to_code = sample2code
        self._sample_to_group = None
        self._sample_per_group = None
        self._group_factors = None
        self.sample_metadata = sample_metadata

        # assay name and assay storage dir
        self.name = name
        data_dir_name = "{}.tidyms-assay".format(self.name)
        self._data_path = Path(data_dir_name)
        self._roi_path = self._data_path.joinpath("roi")
        self._feature_path = self._data_path.joinpath("feature")
        if not self._data_path.is_dir():
            self._data_path.mkdir()
            self._roi_path.mkdir()
            self._feature_path.mkdir()
        else:
            check = self._feature_path.is_dir() and self._roi_path.is_dir()
            if not check:
                msg = "{} is not a valid assay path.".format(path)
                raise ValueError(msg)

        self.feature_table = None
        self._params = dict()
        ms_data_params = {
            "ms_mode": ms_mode,
            "instrument": instrument,
            "separation": separation
        }
        self._params["MSData"] = ms_data_params

    @property
    def sample_metadata(self) -> pd.DataFrame:
        return self._sample_metadata

    @sample_metadata.setter
    def sample_metadata(self, value: pd.DataFrame):
        # TODO: validate data
        if value is None:
            self._sample_to_group = {x: 0 for x in self._name_to_path}
            self._sample_per_group = {0: len(self._name_to_path)}
            self._group_factors = [0]
        elif "group_" in value:
            groups, groups_factors = pd.factorize(value.group_)
            counts = np.unique(groups, return_counts=True)
            self._sample_to_group = dict(zip(value.index, groups))
            self._sample_per_group = dict(zip(*counts))
            self._group_factors = groups_factors
        self._sample_metadata = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: Optional[str]):
        if value is None:
            value = "tidyms-assay-{}".format(time_ns())
        # TODO: check valid file names
        elif not value.isalnum():
            msg = "Value must be a alphanumeric string. Got '{}'".format(value)
            raise ValueError(msg)
        self._name = value

    def make_roi(self, **kwargs):
        """
        Builds regions of interest from raw data.

        ROIs are stored in the `roi` attribute. See the Notes for a detailed
        description of the algorithm used.

        Parameters
        ----------
        tolerance : positive number or None, default=None
            m/z tolerance to connect values across scans. If None, the value is
            set based on the value of ``self.instrument``. If
            ``self.instrument`` is ``"qtof"``, the tolerance is ``0.01``. If
            ``self.instrument`` is ``"orbitrap"``, the tolerance is ``0.005``
        max_missing : non-negative integer or None, default=None
            maximum number of consecutive missing values in a valid  ROI. If
            ``None``, the value is set to ``1``.
        min_length : positive integer or None, default=None
            The minimum length of a valid ROI. If, ``None``, the value is set
            based on ``self.separation``. If ``self.separation`` is ``"uplc"``,
            the value is set to ``10``. If ``self.separation`` is ``"hplc"``,
            the value is set to ``20``.
        min_intensity : non-negative number , default=0.0
            Minimum intensity in a valid ROI.
        pad: int or None, default=None
            Pad dummy values to the left and right of the ROI. This produces
            better peak picking results when searching low intensity peaks in a
            ROI. Using None set the value to ``2`` if ``self.separation`` is
            ``"uplc"`` or ``"hplc"``.
        multiple_match : {"closest", "reduce"}, default="reduce"
            How peaks are matched when there is more than one valid match. If
            ``"closest"`` is used, the closest peak is assigned as a match and
            the others are used to create new ROIs. If ``"reduce"`` is used,
            unique m/z and intensity values are generated using the reduce
            function in `mz_reduce` and `sp_reduce` respectively.
        mz_reduce : "mean" or Callable, default="mean"
            Function used to reduce m/z values. If ``"mean"`` is used, the mean
            value of all valid m/z is used. Any function that accepts numpy
            arrays and return numbers can be used. Used only when
            `multiple_match` is set to ``"reduce"``. See the following
            prototype:

            .. code-block:: python

                def mz_reduce(mz_match: np.ndarray) -> float:
                    pass

        sp_reduce : {"mean", "sum"} or Callable, default="sum"
            Function used to reduce intensity values. ``"mean"`` computes the
            mean intensity and ``"sum"`` computes the total intensity. Any
            function that accepts numpy arrays and return numbers can be used.
            Only used when `multiple_match` is set to ``"reduce"``. See the
            prototype shown on `mz_reduce`.
        targeted_mz : numpy.ndarray or None, default=None
            A list of m/z values to perform a targeted ROI creation. If this
            value is provided, only ROI with these m/z values will be created.
        ms_level : int, default=1
            ms level used to build the ROI.
        start : int, default=0
            Create ROI starting at this scan
        end : int or None, default=None
            Stop ROI creation at this scan. If None, stops after the last scan
            in the file.
        start_time : float, default=0.0
            Use scans starting at this acquisition time.
        end_time : float or None, default=None
            Stops when the acquisition time is higher than this value.
        min_snr : positive number, default=10.0
            Minimum signal-to-noise ratio of the peaks. Used only to convert
            profile data to centroid mode
        min_distance : positive number or None, default=None
            Minimum distance between consecutive peaks. If ``None``, the value
            is set to 0.01 if ``self.instrument`` is ``"qtof"`` or to 0.005 if
            ``self.instrument`` is ``"orbitrap"``. Used only to convert profile
            data to centroid mode.
        n_jobs: int, default=1
            Number of parallel process used to create ROI. If ``None``, use all
            available cores. If there are errors while using multiple cores in
            Jupyter Notebooks, the kernel will restart and no error message
            will be displayed.
        verbose : bool, default=True
            Display a message showing progress.

        Notes
        -----
        ROIs are built using the method described in [TR08]_ with slight
        modifications.

        A ROI is modelled as a combination of three arrays with the same size:
        m/z, intensity and time. ROIs are created and extended connecting
        m/z values across successive scans using the following method:

        1.  The m/z values in The first scan are used to initialize a list of
            ROI. If `targeted_mz` is used, the ROI are initialized using this
            list.
        2.  m/z values from the next scan extend the ROIs if they are closer
            than `tolerance` to the mean m/z of the ROI. Values that don't match
            any ROI are used to create new ROIs and are appended to the ROI
            list (only if `targeted_mz` is not used).
        3.  If more than one m/z value is within the tolerance threshold,
            m/z and intensity values are computed according to the
            `multiple_match` strategy.
        4.  If a ROI can't be extended with any m/z value from the new scan,
            it is extended using NaNs.
        5.  If the last `max_missing` values of a ROI are NaN, the ROI is
            flagged as finished. If the maximum intensity of a finished ROI
            is greater than `min_intensity` and the number of points is greater
            than `min_length`, then the ROI is flagged as valid. Otherwise, the
            ROI is discarded.
        6.  Repeat from step 2 until no more scans are available.

        Returns
        -------
        roi : list[Roi]
            A list with the detected regions of interest.

        Raises
        ------
        ValueError
            If the data is not in centroid mode.

        See Also
        --------
        lcms.Roi : Representation of a ROI.

        References
        ----------
        .. [TR08] Tautenhahn, R., Böttcher, C. & Neumann, S. Highly sensitive
            feature detection for high resolution LC/MS. BMC Bioinformatics 9,
            504 (2008). https://doi.org/10.1186/1471-2105-9-504

        """
        n_samples = len(self._name_to_path)
        try:
            verbose = kwargs.pop("verbose")
        except KeyError:
            verbose = True

        try:
            n_jobs = kwargs.pop("n_jobs")
        except KeyError:
            n_jobs = 1

        func = partial(
            _make_roi_worker,
            ms_data_params=self._params["MSData"],
            make_roi_params=kwargs,
            roi_path=self._roi_path
        )
        bar = _get_progress_bar()
        if n_jobs == 1:
            results = (func(x) for x in self._name_to_path.items())
            if verbose:
                results = bar(results, total=n_samples)
            tuple(results)
        else:
            with Pool(n_jobs) as pool:
                results = pool.imap(func, self._name_to_path.items())
                if verbose:
                    print("Creating ROI in {} samples.".format(n_samples))
                    results = bar(results, total=n_samples)
                tuple(results)
        self._params["make_roi"] = kwargs

    def load_roi(self, name: str) -> List[Roi]:
        file_path = self._roi_path.joinpath(name + ".pickle")
        with file_path.open("rb") as fin:
            roi = pickle.load(fin)
        return roi

    def load_feature(self, name: str) -> pd.DataFrame:
        file_path = self._feature_path.joinpath(name + ".pickle")
        with file_path.open("rb") as fin:
            df = pickle.load(fin)
        return df

    def detect_features(
        self,
        smoothing_strength: Optional[float] = 1.0,
        find_peaks_params: Optional[dict] = None,
        descriptors: Optional[dict] = None,
        filters: Optional[dict] = None,
        verbose: bool = True,
        n_jobs: Optional[int] = 1
    ):
        """
        Perform feature detection on LC-MS centroid samples.

        Parameters
        ----------
        smoothing_strength: positive number, optional
            Width of a gaussian window used to smooth the ROI. If None, no
            smoothing is applied.
        find_peaks_params : dict, optional
            parameters to pass to :py:func:`tidyms.peaks.detect_peaks`
        descriptors : dict, optional
            descriptors to pass to :py:func:`tidyms.peaks.get_peak_descriptors`
        filters : dict, optional
            filters to pass to :py:func:`tidyms.peaks.get_peak_descriptors`
        descriptors : dict, optional
            pass custom descriptors to :py:func:`tidyms.peaks.get_peak_descriptors`
        filters : dict, optional
            pass custom filters to :py:func:`tidyms.peaks.get_peak_descriptors`
        verbose: bool

        Returns
        -------
        feature_table: DataFrame
            A Pandas DataFrame where each row is a feature detected in a sample and
            each column is a feature descriptor. By default the following
            descriptors are computed:

            mz
                weighted average of the m/z in the peak region.
            mz std
                standard deviation of the m/z in the peak region.
            rt
                weighted average of the retention time in the peak region.
            width
                Chromatographic peak width.
            height
                Height of the chromatographic peak minus the baseline.
            area
                Area of the chromatographic peak. minus the baseline area.
            sample
                The sample name where the feature was detected.

            Also, two additional columns have information to search each feature
            in its correspondent Roi:

            roi_index :
                index in the list of ROI where the feature was detected.
            peak_index :
                index of the peaks attribute of each ROI associated to the feature.

        Notes
        -----
        Features are detected as follows:

        1.  Default parameters are set based on the values of the parameters
            `instrument` and `separation`.
        2.  Regions of interest (ROI) are detected in each sample. See the
            documentation of :py:meth:`tidyms.fileio.MSData.make_roi` for a detailed
            description of how ROI are created from raw data.
        3.  Features (chromatographic peaks) are detected on each ROI. See
            :py:meth:`tidyms.lcms.Chromatogram.find_peaks` for a detailed
            description of how peaks are detected and how descriptors are computed.

        """
        func = partial(
            _detect_features_worker,
            smoothing_strength=smoothing_strength,
            descriptors=descriptors,
            filters=filters,
            find_peaks_params=find_peaks_params
        )
        p_iter = (self._roi_path.joinpath(x + ".pickle") for x in self._name_to_path)
        bar = _get_progress_bar()
        n_samples = len(self._name_to_path)
        if n_jobs == 1:
            results = (func(x) for x in p_iter)
            if verbose:
                results = bar(results, total=n_samples)
            tuple(results)
        else:
            with Pool(n_jobs) as pool:
                results = pool.imap(func, p_iter)
                if verbose:
                    msg = "Searching features in {} samples.".format(n_samples)
                    print(msg)
                    results = bar(results, total=n_samples)
                tuple(results)

    def build_feature_table(self):
        # create feature table
        df_list = list()
        for name in self._name_to_path:
            df = self.load_feature(name)
            df["sample_"] = self._sample_to_code[name]
            group = self._sample_to_group.get(name)
            if group is None:
                df["group_"] = 0
            else:
                df["group_"] = group
            df_list.append(df)
        feature_table = pd.concat(df_list).reset_index(drop=True)
        feature_table["roi index"] = feature_table["roi index"].astype(int)
        feature_table["peak index"] = feature_table["peak index"].astype(int)
        feature_table["sample_"] = feature_table["sample_"].astype(int)
        feature_table["group_"] = feature_table["group_"].astype(int)
        save_path = self._data_path.joinpath("feature-table.pickle")
        feature_table.to_pickle(save_path)
        self.feature_table = feature_table


def _get_path_list(path: Union[str, List[str], Path]) -> List[Path]:
    if isinstance(path, str):
        path = Path(path)

    if isinstance(path, list):
        path_list = [Path(x) for x in path]
        for p in path_list:
            # check if all files in the list exists
            if not p.is_file():
                msg = "{} doesn't exist".format(p)
                raise ValueError(msg)
    else:
        if path.is_dir():
            path_list = list(path.glob("*.mzML"))
        elif path.is_file():
            path_list = [path]
        else:
            msg = ("Path must be a string or Path object pointing to a "
                   "directory with mzML files or a list strings with the "
                   "absolute path to mzML")
            raise ValueError(msg)
    return path_list


def _load_roi(file_path: Path) -> List[Roi]:
    with file_path.open("rb") as fin:
        roi = pickle.load(fin)
    return roi


def _save_roi(file_path: Path, roi: List[Roi]):
    with file_path.open("wb") as fin:
        pickle.dump(roi, fin)


def _make_roi_worker(arg, ms_data_params, make_roi_params, roi_path: Path):
    sample_name, sample_path = arg
    ms_data = MSData(sample_path, **ms_data_params)
    roi = ms_data.make_roi(**make_roi_params)
    file_path = roi_path.joinpath(sample_name + ".pickle")
    _save_roi(file_path, roi)


def _get_progress_bar():
    if is_notebook():
        progress_bar = notebook_bar
    else:
        progress_bar = cli_bar
    return progress_bar


def _detect_features_worker(
        file_path: Path,
        smoothing_strength: Optional[float] = 1.0,
        descriptors: Optional[dict] = None,
        filters: Optional[dict] = None,
        find_peaks_params: Optional[dict] = None
) -> pd.DataFrame:
    """
    Builds a DataFrame with feature descriptors. Aux function for
    detect_features.

    Returns
    -------
    DataFrame

    """
    roi_index_list = list()
    peak_index_list = list()
    mz_mean_list = list()
    mz_std_list = list()
    descriptors_list = list()
    roi = _load_roi(file_path)

    for roi_index, k_roi in enumerate(roi):
        k_roi.fill_nan()
        try:
            k_params = k_roi.find_peaks(smoothing_strength=smoothing_strength,
                                        descriptors=descriptors,
                                        filters=filters,
                                        find_peaks_params=find_peaks_params)
        except:
            print(str(file_path))
            print(roi_index)
            raise ValueError

        n_features = len(k_params)
        descriptors_list.extend(k_params)
        k_mz_mean, k_mz_std = k_roi.get_peaks_mz()
        roi_index_list.append([roi_index] * n_features)
        peak_index_list.append(range(n_features))
        mz_mean_list.append(k_mz_mean)
        mz_std_list.append(k_mz_std)
    _save_roi(file_path, roi)

    roi_index_list = np.hstack(roi_index_list)
    peak_index_list = np.hstack(peak_index_list)
    mz_mean_list = np.hstack(mz_mean_list)
    mz_std_list = np.hstack(mz_std_list)

    ft_table = pd.DataFrame(data=descriptors_list)
    ft_table = ft_table.rename(columns={"loc": "rt"})
    ft_table["mz"] = mz_mean_list
    ft_table["mz std"] = mz_std_list
    ft_table["roi index"] = roi_index_list
    ft_table["peak index"] = peak_index_list
    ft_table = ft_table.dropna(axis=0)
    ft_table["roi index"] = ft_table["roi index"].astype(int)
    ft_table["peak index"] = ft_table["peak index"].astype(int)
    # TODO: save features into a file
    # save dataframe into a file
    data_path = file_path.parent.parent
    df_path = data_path.joinpath("feature", file_path.stem + ".pickle")
    ft_table.to_pickle(df_path)
    return ft_table
