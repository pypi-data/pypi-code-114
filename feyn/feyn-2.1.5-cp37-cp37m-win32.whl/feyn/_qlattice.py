"""Classes and functions to interact with a remote QLattice."""
import os
from collections import Counter
from warnings import warn
from typing import Dict, List, Optional, Set, Iterable, Union, Callable
import random

import numpy as np
import pandas as pd
import requests
from lark.exceptions import UnexpectedInput

import feyn
import _qepler
from feyn import Model
from feyn._typings import check_types

from ._program import Program
from ._context import Context
from ._config import DEFAULT_SERVER, Config, resolve_config
from ._httpclient import HttpClient

from ._ql_notebook_mixin import QLatticeNotebookMixin
from ._compatibility import detect_notebook

class _RemoteQL:
    def __init__(self, cfg):
        headers = {
            "Authorization": f'Bearer {cfg.api_token or "none"}',
            "User-Agent": f"feyn/{feyn.__version__}",
        }

        qlattice_server = cfg.server.rstrip("/")
        api_base_url = f"{qlattice_server}/api/v2/qlattice/{cfg.qlattice}"

        self.http_client = HttpClient(api_base_url, headers)

    def reset(self, random_seed):
        req = self.http_client.post("/reset", json={"seed": random_seed})
        req.raise_for_status()

    def generate_programs(self, ar0_codes, ar1_codes, ar2_codes, output_code, max_complexity, query):
        req = self.http_client.post(
            "/generate",
            json={
                "ar0_codes": ar0_codes,
                "ar1_codes": ar1_codes,
                "ar2_codes": ar2_codes,
                "max_complexity": max_complexity,
                "output_code": output_code,
                "query_program": query,
            },
        )

        if req.status_code == 422:
            raise ValueError(req.text)

        req.raise_for_status()

        programs = []
        for json in req.json()["programs"]:
            programs.append(Program.from_json(json))

        return programs

    def update(self, programs):
        programs_json = [p.to_json() for p in programs]
        req = self.http_client.post("/update", json={"programs": programs_json})

        if req.status_code == 422:
            raise ValueError(req.text)

        req.raise_for_status()

    def update_priors(self, priors, reset):
        req = self.http_client.post("/priors", json={"priors": priors, "reset": reset})
        req.raise_for_status()


def InProcQL(cfg):
    try:
        from qlattice.qcells import QLNew

        return QLNew()
    except ModuleNotFoundError:
        raise ValueError("Inproc QLattice cannot be instatiated: Module qlattice not found")


class QLattice(QLatticeNotebookMixin if detect_notebook() else object):
    def __init__(self, cfg):
        """Construct a new 'QLattice' object."""

        if cfg.server == "inproc":
            self._qlproxy = InProcQL(cfg)
        else:
            self._qlproxy = _RemoteQL(cfg)

        self.qlattice_id = cfg.qlattice
        self.context = Context()

    @property
    def registers(self):
        """
        The registers of the QLattice

        The register collection is used to find the inputs and output already used in the QLattice.
        """
        # Ensure that we return a copy
        return list(self.context.registers)

    @check_types()
    def update(self, models: Iterable[Model]):
        """Update QLattice with learnings from a list of models. When updated, the QLattice learns to produce models that are similar to what is included in the update. Without updating, the QLattice will keep generating models with a random structure.

        Arguments:
            models {Union[Model, Iterable[Model]]} -- The models to use in a QLattice update.

        Raises:
            TypeError: if inputs don't match the correct type.
        """
        qid_counter = Counter()
        programs = []

        for m in models:
            qid = m._program.qid
            if qid_counter[qid] >= 6:
                continue
            programs.append(m._program)
            qid_counter[qid] += 1

        self._qlproxy.update(programs)

    @check_types()
    def sample_models(
        self,
        input_names: Iterable[str],
        output_name: str,
        kind: str = "regression",
        stypes: Optional[Dict[str, str]] = None,
        max_complexity: int = 10,
        query_string: Optional[str] = None,
        function_names: Optional[List[str]] = None,
    ) -> List[feyn.Model]:
        """
        Sample models from the QLattice simulator. The QLattice has a probability density for generating different models, and this function samples from that density.

        Arguments:
            input_names {List[str]} -- The names of the inputs.
            output_name {str} -- The name of the output.

        Keyword Arguments:
            kind {str} -- Specify the kind of models that are sampled. One of ["classification", "regression"]. (default: {"regression"})
            stypes {Optional[Dict[str, str]]} -- An optional map from input names to semantic types. (default: {None})
            max_complexity {int} -- The maximum complexity for sampled models. Currently the maximum number of edges that the graph representation of the models has. (default: {10})
            query_string {Optional[str]} -- An optional query string for specifying specific model structures. (default: {None})
            function_names {Optional[List[str]]} -- A list of function names to use in the QLattice simulation. Defaults to all available functions being used. (default: {None})

        Raises:
            TypeError: if inputs don't match the correct type.
            ValueError: if input_names contains duplicates.
            ValueError: if max_complexity is negative.
            ValueError: if kind is not a regressor or classifier.
            ValueError: if function_names is not recognised.
            ValueError: if query_string is invalid.

        Returns:
            List[Model] -- The list of sampled models.
        """
        if len(input_names) == 0:
            raise ValueError("input_names cannot be empty.")
        if len(list(input_names)) != len(set(input_names)):
            raise ValueError("input_names must consist of only unique values.")
        if max_complexity <= 0:
            raise ValueError(f"max_complexity must be greater than 0, but was {max_complexity}.")
        max_complexity = min(max_complexity, Program.SIZE - 1)

        stypes = stypes or {}
        stypes[output_name] = feyn.tools.kind_to_output_stype(kind)

        if output_name in input_names:
            input_names = list(input_names)
            input_names.remove(output_name)

        function_names = _get_fnames(function_names)

        res = []
        ar0_codes = self.context.get_codes(0, input_names)
        ar1_codes = self.context.get_codes(1, function_names)
        ar2_codes = self.context.get_codes(2, function_names)
        output_code = self.context.lookup_by_fname(output_name, 0)

        query_string = query_string or "_"
        try:
            query_complexity, query_codes = self.context.query_to_codes(output_name, query_string)
            if query_complexity > max_complexity:
                raise ValueError(
                    f"The complexity of the query, {query_complexity}, is greater than the max_complexity {max_complexity} of this sample_models."
                )
        except UnexpectedInput as ui:
            query_mistake = ui.get_context(query_string)
            mistake_here = " " * ui.pos_in_stream + "This is where something went wrong!"
            raise ValueError(
                f"\nFailed to parse the following query string:\n\n{query_mistake + mistake_here}\n\nYou can read more about using the query language here:\nhttps://docs.abzu.ai/docs/guides/advanced/query_language.html\n"
            ) from None

        programs = self._qlproxy.generate_programs(
            ar0_codes, ar1_codes, ar2_codes, output_code, max_complexity, query_codes
        )

        for p in programs:
            model = self.context.to_model(p, output_name=output_name, stypes=stypes)
            if model is None:
                # Silently ignore invalid programs
                continue

            res.append(model)

        return res

    def reset(self, random_seed=-1):
        """Clear all learnings in this QLattice.

        Keyword Arguments:
            random_seed {int} -- If not -1, seed the qlattice and feyn random number generator to get reproducible results. (default: {-1})
        """

        if random_seed != -1:
            random.seed(random_seed)
            np.random.seed(random_seed)
            _qepler.srand(random_seed)

        self._qlproxy.reset(random_seed)
        self.context = Context()

    def update_priors(self, priors: Dict, reset: bool = True):
        """Update input priors for the QLattice

        Keyword Arguments:
            priors - a dictionary of prior probabilities of each input to impact the output.
            reset - a boolean determining whether to reset the current priors, or merge with the existing priors.
        """
        priors = [(self.context.lookup_by_fname(key, 0), val) for key, val in priors.items()]

        self._qlproxy.update_priors(priors, reset)

    @check_types()
    def auto_run(
        self,
        data: pd.DataFrame,
        output_name: str,
        kind: str = "regression",
        stypes: Optional[Dict[str, str]] = None,
        n_epochs: int = 10,
        threads: Union[int, str] = "auto",
        max_complexity: int = 10,
        query_string: Optional[str] = None,
        loss_function: Optional[str] = None,
        criterion: Optional[str] = "bic",
        sample_weights: Optional[Iterable[float]] = None,
        function_names: Optional[List[str]] = None,
        starting_models: Optional[List[feyn.Model]] = None,
    ) -> List[feyn.Model]:
        """A convenience function for running the QLattice simulator for many epochs. This process can be interrupted with a KeyboardInterrupt, and you will get back the best models that have been found thus far. Roughly equivalent to the following:

        >>> priors = feyn.tools.estimate_priors(data, output_name)
        >>> ql.update_priors(priors)
        >>> models = []
        >>> for i in range(n_epochs):
        >>>     models += ql.sample_models(data, output_name, kind, stypes, max_complexity, query_string, function_names)
        >>>     models = feyn.fit_models(models, data, loss_function, criterion, None, sample_weights)
        >>>     models = feyn.prune_models(models)
        >>>     ql.update(models)
        >>> best = feyn.get_diverse_models(models, n=10)

        Arguments:
            data {Iterable} -- The data to train models on. Input names are inferred from the columns (pd.DataFrame) or keys (dict) of this variable.
            output_name {str} -- The name of the output.

        Keyword Arguments:
            kind {str} -- Specify the kind of models that are sampled. One of ["classification", "regression"]. (default: {"regression"})
            stypes {Optional[Dict[str, str]]} -- An optional map from input names to semantic types. (default: {None})
            n_epochs {int} -- Number of training epochs. (default: {10})
            threads {int} -- Number of concurrent threads to use for fitting. If a number, that many threads are used. If "auto", set to your CPU count - 1. (default: {"auto"})
            max_complexity {int} -- The maximum complexity for sampled models. (default: {10})
            query_string {Optional[str]} -- An optional query string for specifying specific model structures. (default: {None})
            loss_function {Optional[Union[str, Callable]]} -- The loss function to optimize models for. If None (default), 'MSE' is chosen for regression problems and 'binary_cross_entropy' for classification problems. (default: {None})
            criterion {Optional[str]} -- Sort by information criterion rather than loss. Either "aic", "bic" or None (loss). (default: {"bic"})
            sample_weights {Optional[Iterable[float]]} -- An optional numpy array of weights for each sample. If present, the array must have the same size as the data set, i.e. one weight for each sample. (default: {None})
            function_names {Optional[List[str]]} -- A list of function names to use in the QLattice simulation. Defaults to all available functions being used. (default: {None})
            starting_models {Optional[List[feyn.Model]]} -- A list of preexisting feyn models you would like to start finding better models from. The inputs and output of these models should match the other arguments to this function. (default: {None})

        Raises:
            TypeError: if inputs don't match the correct type.

        Returns:
            List[feyn.Model] -- The best models found during this run.
        """
        from time import time

        feyn.validate_data(data, kind, output_name, stypes)

        if n_epochs <= 0:
            raise ValueError("n_epochs must be 1 or higher.")

        if threads == "auto":
            threads = feyn.tools.infer_available_threads()
        elif isinstance(threads, str):
            raise ValueError("threads must be a number, or string 'auto'.")

        models = []
        if starting_models is not None:
            models = [m.copy() for m in starting_models]
        m_count = len(models)

        priors = feyn.tools.estimate_priors(data, output_name)
        self.update_priors(priors)

        try:
            start = time()
            for epoch in range(1, n_epochs + 1):
                new_sample = self.sample_models(
                    data,
                    output_name,
                    kind,
                    stypes,
                    max_complexity,
                    query_string,
                    function_names,
                )
                models += new_sample
                m_count += len(new_sample)

                models = feyn.fit_models(
                    models,
                    data=data,
                    loss_function=loss_function,
                    criterion=criterion,
                    n_samples=None,
                    sample_weights=sample_weights,
                    threads=threads,
                )
                models = feyn.prune_models(models)
                elapsed = time() - start

                if len(models) > 0:
                    feyn.show_model(
                        models[0],
                        feyn.tools.get_progress_label(epoch, n_epochs, elapsed, m_count),
                        update_display=True,
                    )

                self.update(models)

            best = feyn.get_diverse_models(models)
            return best

        except KeyboardInterrupt:
            best = feyn.get_diverse_models(models)
            return best

def connect_qlattice(
    qlattice: Optional[str] = None,
    api_token: Optional[str] = None,
    server: str = DEFAULT_SERVER,
    config: Optional[str] = None,
) -> QLattice:
    """
    Utility function for connecting to a QLattice. A QLattice (short for Quantum Lattice) is a device which can be used to generate and explore a vast number of models linking a set of input observations to an output prediction. The actual QLattice runs on a dedicated computing cluster which is operated by Abzu. The `feyn.QLattice` class provides a client interface to communicate with, sample models from, and update the QLattice.

    Keyword Arguments:
        qlattice {Optional[str]} -- The qlattice you want to connect to, such as: `a1b2c3d4`. (Should not to be used in combination with the config parameter). (default: {None})
        api_token {Optional[str]} -- Authentication token for the communicating with this QLattice. (Should not to be used in combination with the config parameter). (default: {None})
        server {str} -- The server hosting your QLattice. (Should not to be used in combination with the config parameter). (default: {DEFAULT_SERVER})
        config {Optional[str]} -- The configuration setting in your feyn.ini or .feynrc file to load the url and api_token from. These files should be located in your home folder. (default: {None})

    Returns:
        QLattice -- The QLattice connection handler to your remote QLattice.
    """
    # Config cannot be combined with anything else
    if config and (qlattice or api_token):
        raise ValueError("Must specify either a config or both qlattice and token.")

    # If either qlattice or token specified, then both must be specified.
    if qlattice or api_token:
        if not (qlattice and api_token):
            raise ValueError("Must specify either a config or both qlattice and token.")

    if qlattice or server == "inproc":
        cfg = Config(qlattice, api_token, server)
    else:
        cfg = resolve_config(config)

        if cfg is None:
            cfg = _get_community_qlattice_config(server)

    return QLattice(cfg)


def _get_community_qlattice_config(server: str) -> Config:
    resp = requests.post(f"{server}/api/v1/qlattice/community/create", timeout=20)
    resp.raise_for_status()
    data = resp.json()
    print(
        "A new community QLattice has been allocated for you. This temporary QLattice is available for personal/non-commercial use. "
        "By using this community QLattice you agree to the terms and conditions which can be found at `https://abzu.ai/privacy`."
    )

    return Config(data["qlattice_id"], data["api_token"], data["server"])


def _get_fnames(fnames: Optional[List[str]]):
    all_fnames = feyn.OPCODE_MAP.values()

    if not fnames:
        return all_fnames

    function_names = []
    for name in fnames:
        if name == "gaussian":
            function_names.append("gaussian1")
            function_names.append("gaussian2")
        elif name not in all_fnames:
            raise ValueError(f"{name} is not a valid function name.")
        else:
            function_names.append(name)

    return function_names

# Magic signature population
if hasattr(QLattice, 'expand_auto_run'):
    QLattice.expand_auto_run.__annotations__ = QLattice.auto_run.__annotations__
    QLattice.expand_auto_run.__annotations__['return'] = 'IPython cell'
    QLattice.expand_auto_run.__wrapped__ = QLattice.auto_run
