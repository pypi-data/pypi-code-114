from pathlib import Path
from typing import List, Tuple, Any
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from ._g_pipeline import _GPipeline
from .bead_msd import BeadMSD, EnsembleMSDData
from ...analysis.microrheology.plateau_modulus import G0Data
from ...tools.experiment_configuration import ExperimentConfiguration
from ...tools.experiment_iterator import GroupIterator
from ...analysis.microrheology.paust_method import (fit_msd,
                                                    paust_model,
                                                    compute_G_via_fit_parameters)
from ...file_io.tables import merge_and_save_table
from ...tools.group_results_container import GroupResultsContainer
from ...tools.group_table_index_generator import GroupTableIndexGenerator


class PaustMethod(_GPipeline):

    def __init__(self, experiment_configuration: ExperimentConfiguration,
                 overwrite: bool=False):
        super().__init__(experiment_configuration)
        self.plot_files.update({
            'PaustFit': os.path.join(experiment_configuration['G'], 'paust_fit_{label}.svg'),
            'G': os.path.join(experiment_configuration['G'], 'G.svg'),
            'G0': os.path.join(experiment_configuration['G0'], 'G_with_G0.svg')
        })
        self.output_files.update({
            'PaustFit': os.path.join(experiment_configuration['G'], 'paust_fit.csv'),
            'G0': os.path.join(experiment_configuration['G0'], 'G0.csv')
        })
        self._bead_msd = BeadMSD(experiment_configuration, overwrite)
        if overwrite:
            self._remove_output_files()

    def run_analysis(self, exclude_Gpp: bool=False) -> Tuple[plt.Figure, plt.Axes]:
        msd_data = self._bead_msd.get_ensemble_msds()
        fig, ax = self._run_paust_analysis(msd_data, exclude_Gpp)
        return fig, ax

    def _validate_configuration(self):
        assert "G" in self.experiment_configuration
        assert "G0" in self.experiment_configuration


    def get_msds_and_fit_results(self) -> Tuple['EnsembleMSDData', pd.DataFrame]:
        msd_data = self._bead_msd.get_ensemble_msds()
        fit_results = self._fit_paust_model_to_msds(msd_data)
        return msd_data, fit_results

    def _run_paust_analysis(
            self,
            msd_data: 'EnsembleMSDData',
            exclude_Gpp: bool
    ) -> Tuple[plt.Figure, plt.Axes]:
        fit_results = self._fit_paust_model_to_msds(msd_data)
        self.plot_paust_fits(msd_data, fit_results)
        omegas, Gs = PaustMethod._get_omegas_and_Gs_from_fit_parameters(fit_results,
                                                                        msd_data.lag_times,
                                                                        msd_data.bead_radii)
        fig, ax = self._plot_Gs(omegas, Gs, save_file_name=self.plot_files['G'], exclude_Gpp=exclude_Gpp)
        G0s = self._find_G0_via_saddle_point_method(omegas, Gs, self.output_files["G0"])
        self._plot_Gs_with_G0s(omegas, Gs, G0s, self.plot_files['G0'], exclude_Gpp=exclude_Gpp)
        return fig, ax

    def plot_Gs_with_G0s(
            self,
            exclude_Gpp: bool=True
    ) -> Tuple[plt.Figure, plt.Axes]:
        omegas, Gs = self.get_omegas_and_Gs()
        G0s = self._find_G0_via_saddle_point_method(omegas, Gs, self.output_files["G0"])
        return self._plot_Gs_with_G0s(omegas, Gs, G0s, self.plot_files['G0'], exclude_Gpp)

    def get_omegas_and_Gs(self) -> Tuple[List[np.ndarray], List[np.ndarray]]:
        msd_data = self._bead_msd.get_ensemble_msds()
        fit_results = self._fit_paust_model_to_msds(msd_data)
        omegas, Gs = PaustMethod._get_omegas_and_Gs_from_fit_parameters(fit_results,
                                                                        msd_data.lag_times,
                                                                        msd_data.bead_radii)
        return omegas, Gs

    def load_fit_results(self) -> GroupResultsContainer[np.ndarray]:
        container = GroupResultsContainer[np.ndarray]()
        p = Path(self.output_files['PaustFit'])
        if not p.exists():
            raise FileNotFoundError("Paust fit results table does not exist yet. Method load_fit_results "
                                    "only works after the PaustMethod analysis has been performed at "
                                    "least once.")
        n_index_cols = self._create_group_index_with_skip_index().nlevels
        table = pd.read_csv(str(p), index_col=list(range(n_index_cols)))
        for group in self.experiment_configuration.experiment_iterator.groups:
            idx = self._group_to_table_index(group)
            row = table.loc[idx]
            fit_result = np.array(row)[0, :4]
            container[group] = fit_result
        return container

    def load_G0_results(self) -> GroupResultsContainer[G0Data]:
        container = GroupResultsContainer[G0Data]()
        group_index = self.experiment_configuration.experiment_iterator.create_index_from_groups()
        p = Path(self.output_files['G0'])
        if not p.exists():
            raise FileNotFoundError("G0 results table does not exist yet. Method load_G0_results "
                                    "only works after the PaustMethod analysis has been performed at "
                                    "least once.")
        table = pd.read_csv(self.output_files['G0'], index_col=list(range(0, group_index.nlevels+1)))
        for i, group in enumerate(self.experiment_configuration.experiment_iterator.groups):
            row = table.iloc[i]
            g0 = G0Data(i, row['omega'], row['G0'])
            container[group] = g0
        return container


    def _fit_paust_model_to_msds(self, msd_data: 'EnsembleMSDData') -> pd.DataFrame:
        fit_results = self._create_fit_results_table()
        for i, group in enumerate(self.experiment_configuration.experiment_iterator):
            row = fit_results.iloc[i]
            self._check_table_values_match_group_values(group, row)
            lag_time, msd = msd_data.get_lag_time_and_msd(i)
            parameters, covariance_errors = fit_msd(lag_time, msd)
            p_errors = np.sqrt(np.diag(covariance_errors))
            fit_results.iloc[i] = np.concatenate([parameters, p_errors])
        merge_and_save_table(self.output_files['PaustFit'], fit_results)
        return fit_results.xs(self.skip, level='frames skipped')

    @staticmethod
    def _check_table_values_match_group_values(group: GroupIterator, row):
        group_values = list(tuple(group.values.values()))
        for i, gv in enumerate(group_values):
            if isinstance(gv, float):
                group_values[i] = np.round(gv, decimals=3)
        group_values = tuple(group_values)
        #if not (row.name[:-1] == group_value_array).all():
        #    raise RuntimeError("Order of fit results table does not match order"
        #                       " of groups.")
        if row.name[:-1] != group_values:
            raise RuntimeError("Order of fit results table does not match order"
                               " of groups.")

    def _create_fit_results_table(self) -> pd.DataFrame:
        index = self._create_group_index_with_skip_index()
        table = pd.DataFrame(index=index, columns=['A', 'B', 'C', 'D', 'sigma_A',
                                                   'sigma_B', 'sigma_C', 'sigma_D'])
        return table

    def plot_paust_fits(self, msd_data: 'EnsembleMSDData', fit_results: pd.DataFrame):
        groups = self.experiment_configuration.experiment_iterator.groups
        for i in range(msd_data.length):
            lag_time, msd = msd_data.get_lag_time_and_msd(i)
            fit_params = np.array(fit_results[['A', 'B', 'C', 'D']].iloc[i])
            self._plot_single_paust_fit(lag_time, msd, fit_params, groups[i])

    def _plot_single_paust_fit(self, lag_time: np.ndarray,
                               msd: np.ndarray,
                               fit_params,
                               group: GroupIterator):
        label = group.label
        file_label = group.get_label_from_values()
        fig, ax = plt.subplots(1, 1)
        filename = self.plot_files['PaustFit'].format(label=file_label)

        ax.plot(lag_time, msd, 'o')
        ax.plot(lag_time, paust_model(lag_time, *fit_params), label='Paust fit')
        ax.legend()
        ax.set(
            title=label,
            xlabel='$\\Delta t / t_0$',
            ylabel='MSD $\\langle \\Delta r^2 \\rangle / x_0^2$',
        )

        fig.savefig(filename)

    @staticmethod
    def _get_omegas_and_Gs_from_fit_parameters(
            fit_results: pd.DataFrame,
            lag_times: List[np.ndarray],
            bead_radii: List[float]
    ) -> Tuple[List[np.ndarray], List[np.ndarray]]:
        omegas, Gs = [], []
        for i in range(len(bead_radii)):
            kT = 1
            bead_radius = bead_radii[i]
            omega = 1/lag_times[i]
            fit_parameters = np.array(fit_results[['A', 'B', 'C', 'D']].iloc[i])
            G = compute_G_via_fit_parameters(omega, bead_radius, kT, *fit_parameters)
            omegas.append(omega)
            Gs.append(G)
        return omegas, Gs

    def _group_to_table_index(self, group: GroupIterator) -> List[Any]:
        index_gen = GroupTableIndexGenerator(group)
        g_index = index_gen()
        return list(g_index) + [self.experiment_configuration.skip_n_frames]
