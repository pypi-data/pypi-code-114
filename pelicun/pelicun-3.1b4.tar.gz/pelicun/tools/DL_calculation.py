# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Leland Stanford Junior University
# Copyright (c) 2018 The Regents of the University of California
#
# This file is part of pelicun.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# You should have received a copy of the BSD 3-Clause License along with
# pelicun. If not, see <http://www.opensource.org/licenses/>.
#
# Contributors:
# Adam Zsarnóczay
# Joanna J. Zou

from time import gmtime, strftime

def log_msg(msg):

    formatted_msg = '{} {}'.format(strftime('%Y-%m-%dT%H:%M:%SZ', gmtime()), msg)

    print(formatted_msg)

log_msg('First line of DL_calculation')

import sys, os, json, ntpath, posixpath, argparse
import numpy as np
import pandas as pd
import shutil

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from pelicun.base import set_options, convert_to_MultiIndex, convert_to_SimpleIndex
from pelicun.assessment import *
from pelicun.file_io import *

def add_units(raw_demands, config):

    demands = raw_demands.T

    if "Units" not in demands.index:
        demands.insert(0, "Units", np.nan)
    else:
        return raw_demands

    try:
        length_unit = config['GeneralInformation']['units']['length']
    except:
        log_msg("No units assigned to the raw demand input and default unit "
                "definition missing from the input file. Raw demands cannot "
                "be parsed. Terminating analysis. ")

        return None

    if length_unit == 'in':
        length_unit = 'inch'

    demands = convert_to_MultiIndex(demands, axis=0).sort_index(axis=0).T

    demands.drop(demands.columns[demands.columns.get_level_values(1)== ''], axis=1, inplace=True)

    demands[('1','PRD','1','1')] = demands[('1','PRD','1','1')]*10.0
    demands[('1','PFA','3','1')] = demands[('1','PFA','3','1')]/50.0

    for EDP_type in ['PFA', 'PGA', 'SA']:
        demands.iloc[0, demands.columns.get_level_values(1) == EDP_type] = length_unit+'ps2'

    for EDP_type in ['PFV', 'PWS', 'PGV', 'SV']:
        demands.iloc[0, demands.columns.get_level_values(1) == EDP_type] = length_unit+'ps'

    for EDP_type in ['PFD', 'PIH', 'SD', 'PGD']:
        demands.iloc[0, demands.columns.get_level_values(1) == EDP_type] = length_unit

    for EDP_type in ['PID', 'PRD', 'DWD', 'RDR', 'PMD', 'RID']:
        demands.iloc[0, demands.columns.get_level_values(1) == EDP_type] = 'rad'

    return convert_to_SimpleIndex(demands, axis=1)

def run_pelicun(config_path, demand_path=None,
    #DL_method, realization_count, BIM_file, EDP_file, DM_file, DV_file,
    #output_path=None, detailed_results=True, coupled_EDP=False,
    #log_file=True, event_time=None, ground_failure=False,
    #auto_script_path=None, resource_dir=None
    ):

    config_path = os.path.abspath(config_path)

    with open(config_path, 'r') as f:
        config = json.load(f)

    if demand_path is not None:
        demand_path = os.path.abspath(demand_path) # response.csv

        # check if the raw demands have units identified
        raw_demands = pd.read_csv(demand_path, index_col=0)

        demands = add_units(raw_demands, config)

        if demands is None:
            return -1

        demand_path = demand_path[:-4]+'_ext.csv'

        demands.to_csv(demand_path)

    # Initial setup -----------------------------------------------------------
    general_info = config.get('GeneralInformation', None)
    if general_info is None:
        log_msg("General Information is missing from the input file. "
                "Terminating analysis.")

        return -1

    DL_config = config.get('DamageAndLoss', None)
    if DL_config is None:

        log_msg("Damage and Loss configuration missing from input file. "
                "Terminating analysis.")

        return -1

    PAL = Assessment(DL_config.get("Options", None))

    if general_info.get('NumberOfStories', False):
        PAL.stories = general_info['NumberOfStories']

    asset_config = config.get('Asset', None)
    demand_config = config.get('Demand', None)
    damage_config = config.get('Damage', None)
    loss_config = config.get('Loss', None)


    return 0
    # Demand Assessment -----------------------------------------------------------

    # if a demand assessment is requested
    if demand_config is not None:

        # if demand calibration is requested
        if demand_config.get('Calibration', False):

            cal_config = demand_config['Calibration']

            # load demand samples to serve as reference data
            PAL.demand.load_sample(cal_config['LoadSampleFrom'])

            # then use it to calibrate the demand model
            PAL.demand.calibrate_model(cal_config['Marginals'])

            # if requested, save the model to files
            if cal_config.get('SaveModelTo', False):
                PAL.demand.save_model(file_prefix=cal_config['SaveModelTo'])

        # if demand resampling is requested
        if demand_config.get('Sampling', False):

            sample_config = demand_config['Sampling']

            # if requested, load the calibrated model from files
            if sample_config.get('LoadModelFrom', False):
                PAL.demand.load_model(data_source= sample_config['LoadModelFrom'])

            # generate demand sample
            PAL.demand.generate_sample(sample_config)

            # if requested, save the sample to a file
            if sample_config.get('SaveSampleTo', False):
                PAL.demand.save_sample(sample_config['SaveSampleTo'])

    # Damage Assessment -----------------------------------------------------------

    # if a damage assessment is requested
    if damage_config is not None:

        # if component quantity sampling is requested
        if damage_config.get('Components', False):

            cmp_config = damage_config['Components']

            # if requested, load a component model and generate a sample
            if cmp_config.get('LoadModelFrom', False):
                # load component model
                PAL.asset.load_cmp_model(data_source= cmp_config['LoadModelFrom'])

                # generate component quantity sample
                PAL.asset.generate_cmp_sample(damage_config['SampleSize'])

            # if requested, save the quantity sample to a file
            if cmp_config.get('SaveSampleTo', False):
                PAL.asset.save_cmp_sample(cmp_config['SaveSampleTo'])

            # if requested, load the quantity sample from a file
            if cmp_config.get('LoadSampleFrom', False):
                PAL.asset.load_cmp_sample(cmp_config['LoadSampleFrom'])

        # if requested, load the demands from file
        # (if not, we assume there is a preceding demand assessment with sampling)
        if damage_config.get('Demands', False):

            if damage_config['Demands'].get('LoadSampleFrom', False):

                PAL.demand.load_sample(damage_config['Demands']['LoadSampleFrom'])

        # load the fragility information
        PAL.damage.load_damage_model(damage_config['Fragilities']['LoadModelFrom'])

        # calculate damages
        # load the damage process if needed
        if damage_config['Calculation'].get('DamageProcessFrom', False):
            with open(damage_config['Calculation']['DamageProcessFrom'], 'r') as f:
                dmg_process = json.load(f)
        else:
            dmg_process = None
        PAL.damage.calculate(damage_config['SampleSize'], dmg_process=dmg_process)

        # if requested, save the damage sample to a file
        if damage_config['Calculation'].get('SaveDamageQNTSampleTo', False):
            PAL.damage.save_qnt_sample(
                damage_config['Calculation']['SaveDamageQNTSampleTo'])

        if damage_config['Calculation'].get('SaveDamageDSSampleTo', False):
            PAL.damage.save_ds_sample(
                damage_config['Calculation']['SaveDamageDSSampleTo'])

    # Loss Assessment -----------------------------------------------------------

    # if a loss assessment is requested
    if loss_config is not None:

        # if requested, load the demands from file
        # (if not, we assume there is a preceding demand assessment with sampling)
        if loss_config.get('Demands', False):

            if loss_config['Demands'].get('LoadSampleFrom', False):

                PAL.demand.load_sample(loss_config['Demands']['LoadSampleFrom'])

        # if requested, load the component data from file
        # (if not, we assume there is a preceding assessment with component sampling)
        if loss_config.get('Components', False):

            if loss_config['Components'].get('LoadSampleFrom', False):

                PAL.asset.load_cmp_sample(loss_config['Components']['LoadSampleFrom'])

        # if requested, load the damage from file
        # (if not, we assume there is a preceding damage assessment with sampling)
        if loss_config.get('Damage', False):

            if loss_config['Damage'].get('LoadQNTSampleFrom', False):
                PAL.damage.load_qnt_sample(
                    loss_config['Damage']['LoadQNTSampleFrom'])

            if loss_config['Damage'].get('LoadSampleFrom', False):
                PAL.damage.load_ds_sample(
                    loss_config['Damage']['LoadDSSampleFrom'])

        # if requested, calculate repair consequences
        if loss_config.get('CalculateBldgRepair', False):

            PAL.bldg_repair.load_model(loss_config['CalculateBldgRepair']['LoadModelFrom'],
                                     loss_config['CalculateBldgRepair']['LoadMappingFrom'])

            PAL.bldg_repair.calculate(loss_config['SampleSize'])

            # if requested, save the loss sample to a file
            if loss_config['CalculateBldgRepair'].get('SaveLossSampleTo', False):

                PAL.bldg_repair.save_sample(loss_config['CalculateBldgRepair']['SaveLossSampleTo'])

        # if requested, aggregate results
        if loss_config.get('SaveAggregateResultsTo', False):

            agg_DF = PAL.bldg_repair.aggregate_losses()

            save_to_csv(agg_DF, loss_config['SaveAggregateResultsTo'])

    return 0

def main(args):

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--configFile')
    parser.add_argument('-d', '--demandFile', default = None)
    #parser.add_argument('--DL_Method', default = None)
    #parser.add_argument('--Realizations', default = None)
    #parser.add_argument('--outputBIM', default='BIM.csv')
    #parser.add_argument('--outputEDP', default='EDP.csv')
    #parser.add_argument('--outputDM', default = 'DM.csv')
    #parser.add_argument('--outputDV', default = 'DV.csv')
    #parser.add_argument('--dirnameOutput', default = None)
    #parser.add_argument('--event_time', default=None)
    #parser.add_argument('--detailed_results', default = True,
    #    type = str2bool, nargs='?', const=True)
    #parser.add_argument('--coupled_EDP', default = False,
    #    type = str2bool, nargs='?', const=False)
    #parser.add_argument('--log_file', default = True,
    #    type = str2bool, nargs='?', const=True)
    #parser.add_argument('--ground_failure', default = False,
    #    type = str2bool, nargs='?', const=False)
    #parser.add_argument('--auto_script', default=None)
    #parser.add_argument('--resource_dir', default=None)
    args = parser.parse_args(args)

    log_msg('Initializing pelicun calculation...')

    #print(args)
    out = run_pelicun(
        args.configFile, args.demandFile,
        #args.DL_Method, args.Realizations,
        #args.outputBIM, args.outputEDP,
        #args.outputDM, args.outputDV,
        #output_path = args.dirnameOutput,
        #detailed_results = args.detailed_results,
        #coupled_EDP = args.coupled_EDP,
        #log_file = args.log_file,
        #event_time = args.event_time,
        #ground_failure = args.ground_failure,
        #auto_script_path = args.auto_script,
        #resource_dir = args.resource_dir
    )

    if out == -1:
        log_msg("pelicun calculation failed.")
    else:
        log_msg('pelicun calculation completed.')

if __name__ == '__main__':

    main(sys.argv[1:])
