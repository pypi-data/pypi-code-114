#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classes for post processing based on datas from vtu-files of FEAMG-TS
"""
__version__ = '1.0.4'
__author__ = 'werner b. vetter'

import femagtools
import femagtools.nc

import vtk
import glob
import numpy as np
import netCDF4 as nc
from scipy import interpolate
import scipy.integrate as integrate
import warnings


class ts_vtu(object):
    '''Class to read vtu-files'''

    def __init__(self, modelname, directory):
        '''Read the vtu-files
        Parameters
        ----------
        modelname : str
            Name of the model (nc-file)
        directory : str
            Directory of result files (vtu-files)
        '''

        self.data = {}

        self.reader = vtk.vtkXMLUnstructuredGridReader()
        self.output = self.reader.GetOutput()

        self.field_data_names = []
        self.point_data_names = []
        self.cell_data_names = []
        self.filenames = sorted(glob.glob(
            "{0}{1}_[0-9][0-9][0-9][0-9].vtu".format(directory, modelname)))
        self.reader.SetFileName(self.filenames[0])
        self.reader.Update()
        for i in range(self.output.GetFieldData().GetNumberOfArrays()):
            self.field_data_names.append(
                self.output.GetFieldData().GetAbstractArray(i).GetName())
        for i in range(self.output.GetPointData().GetNumberOfArrays()):
            self.point_data_names.append(self.output.GetPointData().GetAbstractArray(i).GetName())
        for i in range(self.output.GetCellData().GetNumberOfArrays()):
            self.cell_data_names.append(self.output.GetCellData().GetAbstractArray(i).GetName())
            
        self.set_time_window(0.0,0.0)
        
        
    def get_data_names(self):
        '''Read the list of values stored in the vtu files
        Parameters
        ----------
            None
        Returns
        -------
            List of values stored in the vtu files
        '''
        return self.field_data_names+self.point_data_names+self.cell_data_names


    def read_data(self,data_list):
        '''Extracts data from the vtu files
        Parameters
        ----------
        data_list : fist of str
            List of values to extract from vtu_files
        '''
        for data_name in data_list:
            if data_name in self.field_data_names:
                self.data[data_name]=[]
            elif data_name in self.point_data_names:  
                self.data[data_name]=[]
            elif data_name in self.cell_data_names:  
                self.data[data_name]=[]
            else:
                raise Exception('unknown data name "'+ data_name+'"')
                
        for filename in self.filenames:            
            self.reader.SetFileName(filename)
            self.reader.Update()
            
            for data_name in data_list:
                if data_name in self.field_data_names:
                    self.data[data_name].append(self.output.GetFieldData().GetAbstractArray(data_name))
                if data_name in self.point_data_names:  
                    self.data[data_name].append(self.output.GetPointData().GetAbstractArray(data_name))
                if data_name in self.cell_data_names: 
                    self.data[data_name].append(self.output.GetCellData().GetAbstractArray(data_name))
        
        return "done"
                            

    def set_time_window(self,start,end):
        '''Set time window
        Parameters
        ----------
        start: float
            Start of the time window
        end: float
            End of the time window
            
        Only values within the time window are output by the functions
            get_field_vector
            get_point_vector
            get_cell_vector
            get_data_vector
        At start = 0.0 the values are read out starting from the first value
        At end = 0.0 the values are read out up to the last value
        '''
        try:
            if "time [s]" not in self.data:
                self.read_data(['time [s]'])
                
            if start == 0 or start <= self.data['time [s]'][0].GetValue(0):
                self.istart = 0
            else:
                self.istart = 0
                for i in range(len(self.data['time [s]'])):
                    if start >= self.data['time [s]'][i].GetValue(0):
                        self.istart = i+1 
            if end == 0 or end >= self.data['time [s]'][-1].GetValue(0):
                self.iend = len(self.data['time [s]'])
            else:
                self.iend = 0
                for i in range(len(self.data['time [s]'])):
                    if end <= self.data['time [s]'][i].GetValue(0):
                        self.iend = i
        except:
            self.istart = None
            self.iend = None

    def get_field_vector(self,field_data):
        '''Read field data
        Parameters
        ----------
        field_data : str
            Name of field to read
        Returns
        -------
        field_vec : list of float   
            List of field values within the time window
        '''
        if field_data not in self.data:
            self.read_data([field_data])

        if self.istart:
            start = self.istart
        else:
            start = 0
        if self.iend:
            end = self.iend
        else:
            end = len(self.data[field_data])
            
        field_vec=[]
        #for i in range(self.istart,self.iend):
        for i in range(start,end):
            field_vec.append(self.data[field_data][i].GetValue(0))
        return field_vec
            
    # pnt = node-key, >0
    def get_point_vector(self,pnt_data,pnt):
        '''Read point data
        Parameters
        ----------
        point_data : str
            Name of field to read
        pnt : int
            Key of point
        Returns
        -------
        point_vec : list of float   
            List of point values within the time window
        '''
        if pnt_data not in self.data:
            self.read_data([pnt_data])

        if self.istart:
            start = self.istart
        else:
            start = 0
        if self.iend:
            end = self.iend
        else:
            end = len(self.data[pnt_data])

        point_vec=[]
        for i in range(start,end):
            point_vec.append(self.data[pnt_data][i].GetValue(pnt-1))
        return point_vec
       
    def get_cell_vector(self,cell_data,cell):
        '''Read cell data
        Parameters
        ----------
        cell_data : str
            Name of field to read
        cell : int
            Key of cell
        Returns
        -------
        cell_vec : list of float   
            List of cell values within the time window
        '''
        if cell_data not in self.data:
            self.read_data([cell_data])

        i = self.cell_data_names.index(cell_data)
        noc = self.output.GetCellData().GetAbstractArray(i).GetNumberOfComponents()
        if noc ==1:
            cell_vec=[]
        else:
            cell_vec_x=[]
            cell_vec_y=[]
            cell_vec_z=[]
            
        if self.istart:
            start = self.istart
        else:
            start = 0
        if self.iend:
            end = self.iend
        else:
            end = int(len(self.data[cell_data]))

        for i in range(start,end):
            if noc == 1:
                cell_vec.append(self.data[cell_data][i].GetValue(cell-1))
            else:
                cell_vec_x.append(self.data[cell_data][i].GetValue(noc*(cell-1)))
                cell_vec_y.append(self.data[cell_data][i].GetValue(noc*(cell-1)+1))
                cell_vec_z.append(self.data[cell_data][i].GetValue(noc*(cell-1)+2))               
        if noc == 1:
            return cell_vec
        else:
            return [cell_vec_x,cell_vec_y,cell_vec_z]
        
    def get_data_vector(self,data_name,key=0):    
        '''Read data of fiels, point or cell
        Parameters
        ----------
        data_name : str
            Name of data to read
        hey : int (optional)
            Key of point or cell
        Returns
        -------
        data_vec : list of float   
            List of values within the time window
        '''
        if data_name in self.field_data_names:
            return self.get_field_vector(data_name)
        if data_name in self.point_data_names:  
            return self.get_point_vector(data_name,key)
        if data_name in self.cell_data_names:  
            return self.get_cell_vector(data_name,key)
    

class time_vector(object):
    def __init__ (self,data_sets):
        '''Read time vector in and generate an equidistant vector if necessary.
           Also the base frequency is determined.
        Parameters
        ----------
        data_sets : objects
            Data set of vtu_data, nc_data, nc_data_set
        '''
       
        try: #FEMAG-TS files
            data_list=['time [s]']
            data_sets.vtu_data.read_data(data_list)
            self.vector = data_sets.vtu_data.get_data_vector('time [s]')
            self.freq = 1/(self.vector[-1]-self.vector[0]+
                           (self.vector[1]-self.vector[0])/2+
                           (self.vector[-1]-self.vector[-2])/2)
            dt = self.vector[1]-self.vector[0]
            dt_min = 1e32
            self.equidistant = True
            for i in range(len(self.vector)-2):
                dti = self.vector[i+1]-self.vector[i]
                if dt < 0.999*dti or dt > 1.001*dti:
                    self.equidistant = False
                if dti < dt_min:
                    dt_min = dti
            if not self.equidistant:
                numpnt = int((self.vector[-1]-self.vector[0])/dt_min)
                self.vector_equi = np.linspace(self.vector[0], 
                                               self.vector[-1], 
                                               num=numpnt)
        except: #FEMAG-DC files
            speed = data_sets.nc_data_set.groups['machine'].variables['speed'][0]               
            self.freq = speed/60*data_sets.nc_data.pole_pairs
            self.equidistant = True


class losses(object):
    def __init__(self, modelname, directory):
        '''Loss calculation for FEMAG-TS simulations
        Parameters
        ----------
        modelname : str
            Name of the model (nc-file)
        directory : str
            Directory of result files (vtu-files)
        '''
        self.vtu_data = ts_vtu(modelname,directory)
        self.nc_data = femagtools.nc.read(modelname+'.nc')
        self.nc_data_set = nc.Dataset(modelname+'.nc')
        
        # self.vtu_time=object
        # self.vtu_time.vector=[]
        # self.vtu_time.equidistant = True
        
        '''Read iron losses coefficients'''
        self.iron_loss_coefficient = []
        try:
            for i in range(len(self.nc_data_set.groups['magn_curves'].variables['ch'])):
                name = self.nc_data_set.groups['mc'].variables['name'][i].tostring().decode('UTF-8')
                base_frequency = self.nc_data_set.groups['magn_curves'].variables['base_frequency'][i]
                base_induction = self.nc_data_set.groups['magn_curves'].variables['base_induction'][i]
                ch = self.nc_data_set.groups['magn_curves'].variables['ch'][i]
                ch_freq_exp = self.nc_data_set.groups['magn_curves'].variables['ch_exp'][i]
                ch_ind_exp = self.nc_data_set.groups['magn_curves'].variables['ind_exp'][i]
                kh =  ch/(base_induction**ch_ind_exp*base_frequency**ch_freq_exp)
                khml = 0.65
                cw = self.nc_data_set.groups['magn_curves'].variables['cw'][i]
                cw_freq_exp = self.nc_data_set.groups['magn_curves'].variables['cw_exp'][i]
                cw_ind_exp = self.nc_data_set.groups['magn_curves'].variables['ind_exp'][i]
                if cw_freq_exp == cw_ind_exp:
                    kw = self.coeff_frequency_to_time(base_induction,base_frequency,cw,cw_freq_exp)
                else:
                    warnings.warn('Waterfall methode not possible, specify parameter kw')
                    kw = 0.0
                ce = 0.0
                ce_freq_exp = 1.5
                ce_ind_exp = 1.5
                ke = 0.0
                spec_weight = self.nc_data_set.groups['magn_curves'].variables['spec_weight'][i]
                fillfactor = self.nc_data_set.groups['magn_curves'].variables['fillfac'][i]
                shapefactor = self.nc_data_set.groups['loss_coeffs'].variables['shape_factor'][i]

                coeffdict = {
                    "Name": np.char.strip(name).tolist(),
                    "base_frequency": base_frequency.tolist(),
                    "base_induction": base_induction.tolist(),
                    "ch": ch.tolist(),
                    "ch_freq_exp": ch_freq_exp.tolist(),
                    "ch_ind_exp": ch_ind_exp.tolist(),
                    "kh": kh,
                    "khml":khml,
                    "cw": cw.tolist(),
                    "cw_freq_exp": cw_freq_exp.tolist(),
                    "cw_ind_exp": cw_ind_exp.tolist(),
                    "kw": kw,
                    "ce": ce,
                    "ce_freq_exp": ce_freq_exp,
                    "ce_ind_exp": ce_ind_exp,
                    "ke": ke,
                    "spec_weight": spec_weight.tolist(),
                    "fillfactor": fillfactor.tolist(),
                    "shapefactor": shapefactor.tolist()
                }
                self.iron_loss_coefficient.append(coeffdict)
        except:
            pass
            
        '''Read loss coefficients'''    
        for i in range(2):
            if i == 0:
                name = 'Outside'
            else:
                name = 'Inside'
                
            base_frequency = self.nc_data_set.groups['loss_coeffs'].variables['freq_0'][i]
            base_induction = self.nc_data_set.groups['loss_coeffs'].variables['ind_0'][i]
            ch = self.nc_data_set.groups['loss_coeffs'].variables['ch'][i]
            ch_freq_exp = self.nc_data_set.groups['loss_coeffs'].variables['fa_hyst'][i]
            ch_ind_exp = self.nc_data_set.groups['loss_coeffs'].variables['fa_ind'][i]
            kh =  ch/(base_induction**ch_ind_exp*base_frequency**ch_freq_exp)
            khml = 0.65
            cw = self.nc_data_set.groups['loss_coeffs'].variables['cw'][i]
            cw_freq_exp = self.nc_data_set.groups['loss_coeffs'].variables['fa_eddy'][i]
            cw_ind_exp = self.nc_data_set.groups['loss_coeffs'].variables['fa_ind'][i]
            if cw_freq_exp == cw_ind_exp:
                kw = self.coeff_frequency_to_time(base_induction,base_frequency,cw,cw_freq_exp)
            else:
                warnings.warn('Waterfall methode not possible, specify parameter kw')
                kw = 0.0
            ce = 0.0
            ce_freq_exp = 1.5
            ce_ind_exp = 1.5
            ke = 0.0
            spec_weight = self.nc_data_set.groups['loss_coeffs'].variables['spec_mass_fe'][i]
            fillfactor = self.nc_data_set.groups['loss_coeffs'].variables['fill_factor_fe'][i]
            shapefactor = self.nc_data_set.groups['loss_coeffs'].variables['shape_factor'][i]

            coeffdict = {
                "Name": name,
                "base_frequency": base_frequency.tolist(),
                "base_induction": base_induction.tolist(),
                "ch": ch.tolist(),
                "ch_freq_exp": ch_freq_exp.tolist(),
                "ch_ind_exp": ch_ind_exp.tolist(),
                "kh":kh,
                "khml":khml,
                "cw": cw.tolist(),
                "cw_freq_exp": cw_freq_exp.tolist(),
                "cw_ind_exp": cw_ind_exp.tolist(),
                "kw": kw,
                "ce": ce,
                "ce_freq_exp": ce_freq_exp,
                "ce_ind_exp": ce_ind_exp,
                "ke": ke,
                "spec_weight": spec_weight.tolist(),
                "fillfactor": fillfactor.tolist(),
                "shapefactor": shapefactor.tolist()
            }
            self.iron_loss_coefficient.append(coeffdict)
            

    def scale_factor(self):
        '''Returns the scale dactor
        Parameters
        ----------
        None
            
        Returns
        -------
        scale_facor : int
        '''
        try:
            poles = 2*self.nc_data.pole_pairs
        except:
            poles = 2
        try:
            poles_sim = self.nc_data.poles_sim
        except:
            poles_sim = poles
            
        scale_factor = poles/poles_sim
            
        return scale_factor
    
    def coeff_frequency_to_time(self,B0,f0,c,exp):
        '''Convert Bertotti-coefficient of frequency domain to time domains coefficient
        Parameters
        ----------
        B0 : float
            Base flux density [T]
        f0 : float
            Base freuency [Hz]
        c : float
            Bertotti-coefficient
        exp : float
            Bertotti-exponent
        Return
        -------
        k : float   
            Losse coefficient in time domains
            
        The conversion is only possible for losses-coefficient with
        equal exponent for flux density and frequency,
        as eddy current losses (cw*(B/B0(*)*2*(f/f0)**2) or
        anomalous losses (ce*(B/B0(*)**1.5*(f/f0)**1.5)
        '''
        factor = (2*np.pi)**exp*integrate.quad(lambda x: np.abs(np.cos(2*np.pi*x))**(exp), 0, 1)[0]
        k = c/(B0**exp*f0**exp)/factor
        return k
            
              
#ohmic losses
    def ohm_lossenergy_sr(self,sr):
        '''Ohmic loss energy of a subregion
        Parameters
        ----------
        sr : object
            Subregion
            
        Returns
        -------
        lossenergy : float
            Ohmic loss energy of the subregion
        
        The loss energy is determined by adding up the loss energy of the
        individual elements.
        '''
        scale_factor = self.scale_factor()
        length = self.nc_data.arm_length
        time = self.time_vector
        
        srlossenergy = 0.0
        for supel in sr.superelements:
            selossenergy = 0.0
            if supel.conduc > 0.0:
                ff=self.nc_data_set.groups['superelements'].variables['fillfactor'][supel.key-1]
                if ff == 0.0:
                    ff = 1.0
                #print(supel.key, supel.conduc, supel.length, ff)
                for el in supel.elements:
                    #print(el.key,  el.area)  
                    ellossenergy = 0.0
                    cd_vec=self.vtu_data.get_data_vector('curd',el.key)
                    for j in range(len(time)-1):
                        cd = (cd_vec[j]+cd_vec[j+1])/2
                        dt = time[j+1]-time[j]
                        ellossenergy = ellossenergy + dt*cd**2*el.area/ff/supel.conduc*supel.length
                    selossenergy = selossenergy + ellossenergy*length*scale_factor         
            
            srlossenergy = srlossenergy + selossenergy
                
        return srlossenergy


    def ohm_lossenergy_subregion(self,srname,start=0.0,end=0.0):
        '''Ohmic loss energy of a subregion
        Parameters
        ----------
        srname:  str
            Name of subregion
        start: float
            Start of the time window (optional)
        end : float
            End of the time window (optional)
            
        Returns
        -------
        lossenergy : float
            Ohmic loss energy of the subregion
        
        The loss energy is determined by adding up the loss energy of the
        individual elements over the time window.
        If start and end are not specified, the time window of the 
        previous calculation is used.
        '''       
        while len(srname)<4:
            srname = srname+' '
            
        data_list=['time [s]','curd']
        self.vtu_data.read_data(data_list)

        if start != 0.0 or end != 0.0:
            self.vtu_data.set_time_window(start,end)
            
        self.time_vector = self.vtu_data.get_data_vector('time [s]')
        
        sr = self.nc_data.get_subregion(srname)
        srlossenergy = self.ohm_lossenergy_sr(sr)
        return srlossenergy
    
    def ohm_powerlosses_subregion(self,srname,start=0.0,end=0.0):
        '''Ohmic loss dissipation of a subregion within the time window
        Parameters
        ----------
        srname : str
            Name of subregion
        start : float
            Start of the time window (optional)
        end : float
            End of the time window (optional)
            
        Returns
        -------
        powerlosses : float
            Ohmic loss dissipation of the subregion
        
        The loss energy is determined by adding up the loss energy of the
        individual elements over the time window.
        The loss energy is divided by the time window length
        to obtain the averaged power loss
        If start and end are not specified, the time window of the 
        previous calculation is used.
        '''
        while len(srname)<4:
            srname = srname+' '
            
        srlossenergy = self.ohm_lossenergy_subregion(srname,start,end)       
        srpowerlosses = srlossenergy/(self.time_vector[-1]-self.time_vector[0])
        return srpowerlosses
        
    def ohm_lossenergy(self,start=0.0,end=0.0):
        '''Ohmic loss energy of all subregions
        Parameters
        ----------
        start: float
            Start of the time window (optional)
        end: float
            End of the time window (optional)
            
        Returns
        -------
        loss_data: dict
            Dictonary of subregions and ohmic loss energy of it
        
        The loss energy is determined by adding up the loss energy of the
        individual elements over the time window.
        If start and end are not specified, the time window of the 
        previous calculation is used.
        '''
        
        data_list=['time [s]','curd']
        self.vtu_data.read_data(data_list)

        if start != 0.0 or end != 0.0:
            self.vtu_data.set_time_window(start,end)
            
        self.time_vector = self.vtu_data.get_data_vector('time [s]')
       
        loss_data = []
        for sr in self.nc_data.subregions:
            srlossenergy = self.ohm_lossenergy_sr(sr)
            
            srname = sr.name
            if sr.wb_key >= 0:
                #print(sr.key,"is winding",sr.wb_key+1)
                if srname == '    ':
                    srname = "wdg "+str(sr.wb_key+1)
                        
            loss_data.append({'key':sr.key, 'name':srname, 'losses':srlossenergy})

        return loss_data

    def ohm_powerlosses(self,start=0.0,end=0.0):
        '''Ohmic loss dissipation of all subregions
        Parameters
        ----------
        start : float
            Start of the time window (optional)
        end : float
            End of the time window (optional)
            
        Returns
        -------
        loss_data : dict
            Dictonary of subregions and ohmic loss dissipation of it
        
        The loss energy is determined by adding up the loss energy of the
        individual elements over the time window.
        The loss energy is divided by the time window length
        to obtain the averaged power loss
        If start and end are not specified, the time window of the 
        previous calculation is used.
        '''

        data_list=['time [s]','curd']
        self.vtu_data.read_data(data_list)

        if start != 0.0 or end != 0.0:
            self.vtu_data.set_time_window(start,end)
        
        self.time_vector = self.vtu_data.get_data_vector('time [s]')
         
        loss_data = []
        for sr in self.nc_data.subregions:
            srlossenergy = self.ohm_lossenergy_sr(sr)
            srpowerlosses = srlossenergy/(self.time_vector[-1]-self.time_vector[0])
            
            srname = sr.name
            if sr.wb_key >= 0:
                #print(sr.key,"is winding",sr.wb_key+1)
                if srname == '    ':
                    srname = "wdg "+str(sr.wb_key+1)
                        
            loss_data.append({'key':sr.key, 'name':srname, 'losses':srpowerlosses})

        return loss_data

    def ohm_powerlosses_fft_sr(self,sr):
        '''Power dissipation of a subregion
        Parameters
        ----------
        sr : object
            Subregion
            
        Returns
        -------
        powerlosses : float
            Ohmic power losses of the subregion
        
        A FFT from the current density is made. 
        The power losses of each harmonic is determined and added.
        '''
        scale_factor = self.scale_factor()
        length = self.nc_data.arm_length
                
        srpowerlosses = 0.0
        for supel in sr.superelements:
            sepowerlosses = 0.0
            if supel.conduc > 0.0:
                ff=self.nc_data_set.groups['superelements'].variables['fillfactor'][supel.key-1]
                if ff == 0.0:
                    ff = 1.0
                    #print(supel.key, supel.conduc, supel.length, ff)
                for el in supel.elements:
                    #print(el.key,  el.area)  
                    elpowerlosses = 0.0
                    cd_vec_0 = self.vtu_data.get_data_vector('curd',el.key)
                    if not self.times.equidistant:
                        cd_vec = np.interp(self.times.vector_equi, 
                                            self.times.vector, cd_vec_0, 
                                            period=1.0/self.times.freq)
                        # f = interpolate.interp1d(self.times.vector, cd_vec_0, kind="cubic")
                        # cd_vec = f(self.times.vector_equi)
                    else:
                        cd_vec = cd_vec_0
                    cd_spec = abs(np.fft.fft(cd_vec))/(len(cd_vec)/2)               
                    for j in range(int(len(cd_vec)/2)):
                        elpowerlosses = elpowerlosses + cd_spec[j]**2/2*el.area/ff/supel.conduc*supel.length

                    sepowerlosses = sepowerlosses + elpowerlosses*length*scale_factor
                    
            srpowerlosses = srpowerlosses + sepowerlosses

        return srpowerlosses

    def ohm_powerlosses_fft_subregion(self,srname,start=0.0,end=0.0):
        '''Power dissipation of a subregion
        Parameters
        ----------
        srname:  str
            Name of subregion
        start: float
            Start of the time window (optional)
        end : float
            End of the time window (optional)
            
        Returns
        -------
        lossenergy : float
            Power dissipation of the subregion
        
        A FFT from the current density is made. 
        The power losses of each harmonic is determined and added.
        The time window has to be pariode or a multiple of it.
        If start and end are not specified, the time window of the 
        previous calculation is used.
        '''
        while len(srname)<4:
            srname = srname+' '
                    
        data_list=['time [s]','curd']
        self.vtu_data.read_data(data_list)

        if start != 0.0 or end != 0.0:
            self.vtu_data.set_time_window(start,end)
            
        self.times = time_vector(self)
        
        sr = self.nc_data.get_subregion(srname)
        srpowerlosses = self.ohm_powerlosses_fft_sr(sr)
        return srpowerlosses


    def ohm_powerlosses_fft(self,start=0.0,end=0.0):
        '''Power dissipation of all subregions
        Parameters
        ----------
        start : float
            Start of the time window (optional)
        end : float
            End of the time window (optional)
           
        Returns
        -------
        loss_data : dict
            Dictonary of subregions and power dissipation of it
       
        A FFT from the current density is made. 
        The power losses of each harmonic is determined and added.
        The time window has to be pariode or a multiple of it.
        If start and end are not specified, the time window of the 
        previous calculation is used.
        '''
        
        data_list=['time [s]','curd']
        self.vtu_data.read_data(data_list)

        if start != 0.0 or end != 0.0:
            self.vtu_data.set_time_window(start,end)
       
        self.times = time_vector(self)

        loss_data = []
        for sr in self.nc_data.subregions:
            srpowerlosses= self.ohm_powerlosses_fft_sr(sr)
            
            srname = sr.name
            if sr.wb_key >= 0:
                #print(sr.key,"is winding",sr.wb_key+1)
                if srname == '    ':
                    srname = "wdg "+str(sr.wb_key+1)
                        
            loss_data.append({'key':sr.key, 'name':srname, 'losses':srpowerlosses})

        return loss_data

# iron losses 
    def iron_losses_fft_se(self,se):
        '''Iron losses of a superelement
        Parameters
        ----------
        se: object
            Superelement
            
        Returns
        -------
        ironlosses : float
            Iron losses of the superlement
        
        A FFT is made from the flux density. 
        The iron losses of each harmonic is determined  by 
        Bertotti formula 
        
            Physt = ch * (f/f0)**hfe * (B/B0)**hBe * V * rho
            Peddy = ch * (f/f0)**wfe * (B/B0)**wBe * V * rho
            Pexce = ch * (f/f0)**efe * (B/B0)**eBe * V * rho
            
        and added to the total losses of the superelement
        
            Ptot  = (Physt + Peddy + Pexce) * shape_factor
        '''

        scale_factor = self.scale_factor()
        length = self.nc_data.arm_length
        freq = self.times.freq
        
        sehystlosses = 0.0
        seeddylosses = 0.0
        seexcelosses = 0.0
        if se.elements[0].reluc[0]<1.0 or se.elements[0].reluc[1]<1.0:
            if (se.mcvtype == 0):
                center_pnt = se.elements[0].center
                if (np.sqrt(center_pnt[0]**2+center_pnt[1]**2) > self.nc_data.FC_RADIUS):
                    ldi = len(self.iron_loss_coefficient)-2  #outside
                else:
                    ldi = len(self.iron_loss_coefficient)-1  #inside
            else:
                ldi = se.mcvtype-1
            bf = self.iron_loss_coefficient[ldi]['base_frequency']
            bb = self.iron_loss_coefficient[ldi]['base_induction']
            ch = self.iron_loss_coefficient[ldi]['ch']
            chfe = self.iron_loss_coefficient[ldi]['ch_freq_exp']
            chbe = self.iron_loss_coefficient[ldi]['ch_ind_exp']
            cw = self.iron_loss_coefficient[ldi]['cw']
            cwfe= self.iron_loss_coefficient[ldi]['cw_freq_exp']
            cwbe= self.iron_loss_coefficient[ldi]['cw_ind_exp']
            ce = self.iron_loss_coefficient[ldi]['ce']
            cefe = self.iron_loss_coefficient[ldi]['ce_freq_exp']
            cebe = self.iron_loss_coefficient[ldi]['ce_ind_exp']
            sw = self.iron_loss_coefficient[ldi]['spec_weight']*1000
            ff = self.iron_loss_coefficient[ldi]['fillfactor']
            sf = self.iron_loss_coefficient[ldi]['shapefactor']
 
            for el in se.elements:
                #print(el.key,  el.area)             
                elhystlosses = 0.0
                eleddylosses = 0.0
                elexcelosses = 0.0
                
                bx_vec_0 = self.vtu_data.get_data_vector('b',el.key)[0]
                if not self.times.equidistant:
                    bx_vec = np.interp(self.times.vector_equi, 
                                        self.times.vector, bx_vec_0, 
                                        period=1.0/self.times.freq)
                    # f = interpolate.interp1d(self.times.vector, bx_vec_0, kind="cubic")
                    # bx_vec = f(self.times.vector_equi)
                else:
                    bx_vec = bx_vec_0
                bx_spec = abs(np.fft.fft(bx_vec))/(len(bx_vec)/2)    
                
                by_vec_0 = self.vtu_data.get_data_vector('b',el.key)[1]
                if not self.times.equidistant:
                    by_vec = np.interp(self.times.vector_equi, 
                                        self.times.vector, by_vec_0, 
                                        period=1.0/self.times.freq)
                    # f = interpolate.interp1d(self.times.vector, by_vec_0, kind="cubic")
                    # by_vec = f(self.times.vector_equi)
                else:
                    by_vec = by_vec_0
                by_spec = abs(np.fft.fft(by_vec))/(len(by_vec)/2)  
                
                b_spec = np.sqrt((bx_spec**2+by_spec**2))

                for j in range(int(len(b_spec)/2)):
                    elhystlosses = elhystlosses + ch*(j*freq/bf)**chfe*(b_spec[j]/bb)**chbe
                    eleddylosses = eleddylosses + cw*(j*freq/bf)**cwfe*(b_spec[j]/bb)**cwbe
                    elexcelosses = elexcelosses + ce*(j*freq/bf)**cefe*(b_spec[j]/bb)**cebe
                   
                sehystlosses = sehystlosses + elhystlosses*el.area*length*ff*sf*sw*scale_factor
                seeddylosses = seeddylosses + eleddylosses*el.area*length*ff*sf*sw*scale_factor
                seexcelosses = seexcelosses + elexcelosses*el.area*length*ff*sf*sw*scale_factor
                 
        setotallosses = sehystlosses + seeddylosses + seexcelosses
        
        return {'total':setotallosses,
                'hysteresis':sehystlosses,
                'eddycurrent':seeddylosses,
                'excess':seexcelosses}


    def iron_losses_fft_subregion(self,srname,start=0.0,end=0.0):
        '''Iron losses of a subregion
        Parameters
        ----------
        srname:  str
            Name of subregion
        start: float
            Start of the time window (optional)
        end : float
            End of the time window (optional)
            
        Returns
        -------
        losses : dict
            Iron losses of the subregion
        
        The iron losses are calculated based on the Bertotti formula
        (see also ron_losses_fft_se)
        '''
        while len(srname)<4:
            srname = srname+' '
            
        if start != 0.0 or end != 0.0:
            self.vtu_data.set_time_window(start,end)
        
        data_list=['b']
        self.vtu_data.read_data(data_list)
        self.times = time_vector(self)

        srtotallosses = 0.0
        srhystlosses = 0.0
        sreddylosses = 0.0
        srexcelosses = 0.0
        sr = self.nc_data.get_subregion(srname)
        for se in sr.superelements:
            selosses = self.iron_losses_fft_se(se)
            srtotallosses = srtotallosses + selosses['total']
            srhystlosses = srhystlosses + selosses['hysteresis']
            sreddylosses = sreddylosses + selosses['eddycurrent']
            srexcelosses = srexcelosses + selosses['excess']
            
        srlosses = {'subregion':srname,
                    'total':srtotallosses,
                    'hysteresis':srhystlosses,
                    'eddycurrent':sreddylosses,
                    'excess':srexcelosses 
                    }
        return srlosses

    def iron_losses_fft(self,start=0.0,end=0.0):
        '''Iron losses of all subregion and superelements
        Parameters
        ----------
        start: float
            Start of the time window (optional)
        end : float
            End of the time window (optional)
            
        Returns
        -------
        losses : dict
            Iron losses of the subregion
        
        The iron losses are calculated based on the Bertotti formula
        (see also iron_losses_fft_se)
        '''
        
        if start != 0.0 or end != 0.0:
            self.vtu_data.set_time_window(start,end)
        
        data_list=['b']
        self.vtu_data.read_data(data_list)        
        self.times = time_vector(self)
            
        losseslist = []
 
        for se in self.nc_data.superelements:
            selosses = self.iron_losses_fft_se(se)

            if se.subregion:
                for sr in self.nc_data.subregions:
                    if se in sr.superelements:
                        srname = sr.name
                        #print(se.key, "in", sr.key, sr.name)                
            else:
                if (se.mcvtype == 0):
                    center_pnt = se.elements[0].center
                    if (np.sqrt(center_pnt[0]**2+center_pnt[1]**2) > self.nc_data.FC_RADIUS):
                        srname = "no, outside"
                    else:
                        srname = "no, inside"
                        
            found = False
            for srlosses in losseslist:
                if srlosses['subregion'] == srname:
                        srlosses['total'] = srlosses['total']+selosses['total']
                        srlosses['hysteresis'] = srlosses['hysteresis']+selosses['hysteresis']
                        srlosses['eddycurrent'] = srlosses['eddycurrent']+selosses['eddycurrent']
                        srlosses['excess'] = srlosses['excess']+selosses['excess']
                        found = True
            if not found:
                if selosses['total'] > 0.0:
                    srlosses = {'subregion':srname,
                        'total':selosses['total'],
                        'hysteresis':selosses['hysteresis'],
                        'eddycurrent':selosses['eddycurrent'],
                        'excess':selosses['excess']
                        }
                    losseslist.append(srlosses)                         

        return losseslist


    def iron_lossenergy_time_se(self,se):
        '''Iron losses of a superelement in time domain
        Parameters
        ----------
        se: object
            Superelement
            
        Returns
        -------
        lossenergies : float
            Iron losses of the superlement
        
        The iron losses are calculated based on the Bertotti formula
        in time domaine.
        The loss coefficients in frequency domain are converted into 
        time domain coefficients.
        For the hysteresis losses is a water fall methode implemented.
        Eddy current losses and anomalous losses are calculated by
        add up the losses of each time step.
        '''

        scale_factor = self.scale_factor()
        length = self.nc_data.arm_length
        time = self.times.vector
        
        sehystenergy = 0.0
        seeddyenergy = 0.0
        seexceenergy = 0.0
        if se.elements[0].reluc[0]<1.0 or se.elements[0].reluc[1]<1.0:
            if (se.mcvtype == 0):
                center_pnt = se.elements[0].center
                if (np.sqrt(center_pnt[0]**2+center_pnt[1]**2) > self.nc_data.FC_RADIUS):
                    ldi = len(self.iron_loss_coefficient)-2  #outside
                else:
                    ldi = len(self.iron_loss_coefficient)-1  #inside
            else:
                ldi = se.mcvtype-1
            kh = self.iron_loss_coefficient[ldi]['kh']
            chbe = self.iron_loss_coefficient[ldi]['ch_ind_exp']
            khml = self.iron_loss_coefficient[ldi]['khml']
            kw = self.iron_loss_coefficient[ldi]['kw']
            cwbe = self.iron_loss_coefficient[ldi]['cw_ind_exp']
            ke = self.iron_loss_coefficient[ldi]['ke']
            cebe = self.iron_loss_coefficient[ldi]['ce_ind_exp']
            sw = self.iron_loss_coefficient[ldi]['spec_weight']*1000
            ff = self.iron_loss_coefficient[ldi]['fillfactor']
            sf = self.iron_loss_coefficient[ldi]['shapefactor']
 
            for el in se.elements:
                elhystenergy = 0.0
                eleddyenergy = 0.0
                elexceenergy = 0.0
                
                bx_vec = self.vtu_data.get_data_vector('b',el.key)[0]
                by_vec = self.vtu_data.get_data_vector('b',el.key)[1]                

                #Maximalwert und Richtung des Haupfeldes
                Bpeak = np.sqrt(bx_vec[0]**2+by_vec[0]**2)
                phi = np.arctan2(by_vec[0],bx_vec[0])
                for i in range(1,len(time)):
                    b1 = np.sqrt(bx_vec[i-1]**2+by_vec[i-1]**2)
                    b2 = np.sqrt(bx_vec[i]**2+by_vec[i]**2)
                    if abs(b2)>Bpeak:
                        Bpeak = abs(b2)
                        phi = np.arctan2(by_vec[i],bx_vec[i])
                        
                #Transformation in Hauptrichutng
                br_vec = []
                bt_vec = []
                for i in range(len(time)):   
                    br_vec.append(np.cos(phi)*bx_vec[i]+np.sin(phi)*by_vec[i])
                    bt_vec.append(np.sin(phi)*bx_vec[i]-np.cos(phi)*by_vec[i])
                        
                Bpeak_p = np.sqrt(bx_vec[0]**2+by_vec[0]**2)
                Bx = []
                tp_beg = 0.0
                tp_end = 0.0
                Tp = 0.0
                nzeros = 0
                zero = (br_vec[0]>=0)
                if br_vec[1]>br_vec[0]:
                    up = True
                else:
                    up = False
                for i in range(1,len(time)):
                    b1 = np.sqrt(br_vec[i-1]**2+bt_vec[i-1]**2)
                    b2 = np.sqrt(br_vec[i]**2+bt_vec[i]**2)
                    #Maximalwert innerhalb letzter Periode
                    if abs(b2)>Bpeak_p:
                        Bpeak_p = abs(b2)
                    #Nulldurchgaenge und Periodendauer
                    if zero != (br_vec[i]>=0):
                        zero = (not zero)
                        tp_beg = tp_end
                        tp_end = time[i]
                        if tp_beg > 0.0:
                            nzeros = nzeros+1
                            if nzeros > 1:
                                #Tp = (Tp*(nzeros-1)/nzeros+2*(tp_end-tp_beg)/nzeros)/2
                                Tp = 2*(tp_end-tp_beg)
                                Bpeak = Bpeak_p
                                elhystenergy = elhystenergy+kh*Bpeak**chbe/2
                                Bpeak_p = 0.0
                            else:
                                Tp = 2.0*(tp_end-tp_beg)
                                Bpeak = Bpeak_p
                                elhystenergy = elhystenergy+kh*Bpeak**chbe * (tp_end-time[0])/Tp
                                Bpeak_p = 0.0
                        Bx = []
                    #Wendepunkte       
                    if up and b2<b1:
                        Bx.append(b1)
                    if not up and b2>b1:
                        Bx.append(b1)
                    #Steigungsrichtung       
                    if b2>b1:
                        up = True
                    else:
                        up = False
             
                    try:
                        if b2>0 and up and b2>Bx[-2]:
                            Bm = abs(Bx[-2]+Bx[-1])/2
                            dB = abs(Bx[-2]-Bx[-1])
                            elhystenergy = elhystenergy+kh*Bm**(chbe-1)*khml*dB/2
                            Bx.remove(Bx[-2])
                            Bx.remove(Bx[-1])
                        if b2<0 and not up and b2<Bx[-2]:
                            elhystenergy = elhystenergy+kh*Bm**(chbe-1)*khml*dB/2
                            Bx.remove(Bx[-2])
                            Bx.remove(Bx[-1])
                        if b2>0 and not up and Bx[-1]>Bx[-2]:
                            elhystenergy = elhystenergy+kh*Bm**(chbe-1)*khml*dB/2
                            Bx.remove(Bx[-2])
                            Bx.remove(Bx[-1])
                        if b2<0 and up and Bx[-1]<Bx[-2]:                           
                            elhystenergy = elhystenergy+kh*Bm**(chbe-1)*khml*dB/2
                            Bx.remove(Bx[-2])
                            Bx.remove(Bx[-1])
                                  
                    except:
                        pass
                    
                    dt = time[i]-time[i-1]
                    dbr = br_vec[i]-br_vec[i-1]
                    dbt = bt_vec[i]-bt_vec[i-1]
                    db = np.sqrt(dbr**2+dbt**2)
                    eleddyenergy = eleddyenergy + kw*(db/dt)**cwbe * dt
                    elexceenergy = elexceenergy + ke*(db/dt)**cebe * dt
                    
                #elhystenergy = elhystenergy+kh*Bpeak**chbe * T/(time[-1]-time[0])
                if nzeros >= 1:
                    elhystenergy = elhystenergy+kh*Bpeak**chbe * (time[-1]-tp_end)/Tp
                
                sehystenergy = sehystenergy + elhystenergy*el.area*length*ff*sf*sw*scale_factor
                seeddyenergy = seeddyenergy + eleddyenergy*el.area*length*ff*sf*sw*scale_factor
                seexceenergy = seexceenergy + elexceenergy*el.area*length*ff*sf*sw*scale_factor
                 
        setotalenergy = sehystenergy + seeddyenergy + seexceenergy
        
        return {'total':setotalenergy,
                'hysteresis':sehystenergy,
                'eddycurrent':seeddyenergy,
                'excess':seexceenergy}

    def iron_lossenergy_time_subregion(self,srname,start=0.0,end=0.0):
        '''Iron loss energy of a subregion
        Parameters
        ----------
        srname:  str
            Name of subregion
        start: float
            Start of the time window (optional)
        end : float
            End of the time window (optional)
            
        Returns
        -------
        losses : dict
            Iron losses energy of the subregion
        
        The iron losses are calculated based on the Bertotti formula
        in time domaine (see also iron_lossenergy_time_se)
        '''
        while len(srname)<4:
            srname = srname+' '
            
        if start != 0.0 or end != 0.0:
            self.vtu_data.set_time_window(start,end)
        
        data_list=['b']
        self.vtu_data.read_data(data_list)
        self.times = time_vector(self)

        srtotalenergy = 0.0
        srhystenergy = 0.0
        sreddyenergy = 0.0
        srexceenergy = 0.0
        sr = self.nc_data.get_subregion(srname)
        for se in sr.superelements:
            seenergy = self.iron_lossenergy_time_se(se)
            srtotalenergy = srtotalenergy + seenergy['total']
            srhystenergy = srhystenergy + seenergy['hysteresis']
            sreddyenergy = sreddyenergy + seenergy['eddycurrent']
            srexceenergy = srexceenergy + seenergy['excess']
            
        srenergy = {'subregion':srname,
                    'total':srtotalenergy,
                    'hysteresis':srhystenergy,
                    'eddycurrent':sreddyenergy,
                    'excess':srexceenergy 
                    }
        return srenergy

    def iron_losses_time_subregion(self,srname,start=0.0,end=0.0):
        '''Iron power losses of a subregion
        Parameters
        ----------
        srname:  str
            Name of subregion
        start: float
            Start of the time window (optional)
        end : float
            End of the time window (optional)
            
        Returns
        -------
        losses : dict
            Iron losses energy of the subregion
        
        The iron losses are calculated based on the Bertotti formula
        in time domaine (see also iron_lossenergy_time_se)
        '''
        while len(srname)<4:
            srname = srname+' '

        srenergy = self.iron_lossenergy_time_subregion(srname,start,end)
        time = self.times.vector[-1]-self.times.vector[0]
        
        srlosses = {'subregion':srname,
                    'total':srenergy['total']/time,
                    'hysteresis':srenergy['hysteresis']/time,
                    'eddycurrent':srenergy['eddycurrent']/time,
                    'excess':srenergy['excess']/time
                    }
                                          
        return srlosses
        
    def iron_lossenergy_time(self,start=0.0,end=0.0):
        '''Iron losses of all subregion and superelements
        Parameters
        ----------
        start: float
            Start of the time window (optional)
        end : float
            End of the time window (optional)
            
        Returns
        -------
        energies : dict
            Iron losses enegies of the subregion
        
        The iron losses are calculated based on the Bertotti formula
        in time domaine (see also iron_lossenergy_time_se)
        '''
        
        if start != 0.0 or end != 0.0:
            self.vtu_data.set_time_window(start,end)
        
        data_list=['b']
        self.vtu_data.read_data(data_list)        
        self.times = time_vector(self)
            
        energylist = []
 
        for se in self.nc_data.superelements:
            selossenergy = self.iron_lossenergy_time_se(se)

            if se.subregion:
                for sr in self.nc_data.subregions:
                    if se in sr.superelements:
                        srname = sr.name
                        #print(se.key, "in", sr.key, sr.name)                
            else:
                if (se.mcvtype == 0):
                    center_pnt = se.elements[0].center
                    if (np.sqrt(center_pnt[0]**2+center_pnt[1]**2) > self.nc_data.FC_RADIUS):
                        srname = "no, outside"
                    else:
                        srname = "no, inside"
                        
            found = False
            for srlosses in energylist:
                if srlosses['subregion'] == srname:
                        srlosses['total'] = srlosses['total']+selossenergy['total']
                        srlosses['hysteresis'] = srlosses['hysteresis']+selossenergy['hysteresis']
                        srlosses['eddycurrent'] = srlosses['eddycurrent']+selossenergy['eddycurrent']
                        srlosses['excess'] = srlosses['excess']+selossenergy['excess']
                        found = True
            if not found:
                if selossenergy['total'] > 0.0:
                    srlosses = {'subregion':srname,
                        'total':selossenergy['total'],
                        'hysteresis':selossenergy['hysteresis'],
                        'eddycurrent':selossenergy['eddycurrent'],
                        'excess':selossenergy['excess']
                        }
                    energylist.append(srlosses)                         

        return energylist

    def iron_losses_time(self,start=0.0,end=0.0):
        '''Iron losses of all subregion and superelements
        Parameters
        ----------
        start: float
            Start of the time window (optional)
        end : float
            End of the time window (optional)
            
        Returns
        -------
        losses : dict
            Iron losses of the subregion
        
        The iron losses are calculated based on the Bertotti formula
        in time domaine (see also iron_lossenergy_time_se)
        '''
        
        energylist = self.iron_lossenergy_time(start,end)
        time = self.times.vector[-1]-self.times.vector[0]
        
        losseslist = []
        for sr in energylist:
            sr['total'] = sr['total']/time
            sr['hysteresis'] = sr['hysteresis']/time
            sr['eddycurrent'] = sr['eddycurrent']/time
            sr['excess'] = sr['excess']/time
            losseslist.append(sr)
            
        return losseslist
