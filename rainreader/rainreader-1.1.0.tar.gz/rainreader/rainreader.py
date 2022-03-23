import datetime  # time series management
from datetime import datetime as dtnow  # get time of code
import matplotlib.dates as dates  # time series management
import numpy as np
import re
import os
from subprocess import call
import bisect  # math bisection method

def __rolling_sum(intensity, window_size):
    window_size = min(len(intensity), window_size)
    ret = np.cumsum(intensity, axis=0, dtype=float)
    ret[window_size:] = ret[window_size:] - ret[:-window_size]
    return np.max(ret[window_size - 1:])
    
class KM2:
    __timeseries = None
    
    def __init__(self, kmd_file_path, initial_loss = 0, concentration_time = 0, skip_flags = []):
        # Read KM2 file as string
        with open(kmd_file_path, 'r') as km2:
            km2Str = km2.readlines()
    
        # Pre-compile regex search patterns
        eventstartlineRE = re.compile(r"^1 \d{8}")
        eventinfoRE = re.compile(
            r"^1 ?(\d{8}) {0,}(\d{4}) {1,}\d+ {1,}\d+ {1,}(\d+) {1,}([\d\.]+) {1,}([\w\d]+)")
        gaugeintRE = re.compile("([\d\.]+)")
    
        # Definining vectors for event information
        eventstarttime = []  # The start time of each event
        gaugetime = []  # The time vector of the rain gauge
        gaugeint = []  # The intensity vector of the rain gauge in [mu m/s]
        timedelay = 0
        eventrejected = False
    
        # Read the KM2 line by line
        for i, line in enumerate(km2Str):
            # If the line contains information about the event:
            if eventstartlineRE.search(line):
                # Split the information into segments
                eventinfo = eventinfoRE.match(line)
                # If it's not rejected ( == 2 ), include it
                # THIS IS NOW DISABLED: It doesn't appear like this feature works
                if len(skip_flags) > 0 and any([1 for flag in skip_flags if flag in eventinfo.group(5)]):
                    eventrejected = True
                else:
                    # Get the start time of the event
                    eventstarttime.append(
                        dates.date2num(
                            datetime.datetime.strptime(
                                eventinfo.group(1) +
                                " " +
                                eventinfo.group(2),
                                "%Y%m%d %H%M")))
                    # Remember that the next line will be the first registrered intensity for the event, so the first measurement can be excluded
                    # It's not rejected, so don't reject the following measurements
                    eventrejected = False
                    if timedelay > 0:
                        gaugeint.extend([0])
                        gaugetime.extend([gaugetime[-1] + 1. / 60 / 24])
                        timedelay = 0
            # If the line does not contain information about the event, it must contain intensities.
            # If it's not rejected, read the intensities
            elif not eventrejected:
                ints = list(map(float, gaugeintRE.findall(line)))
                # Exclude the first measurement
                gaugeint.extend(ints)
                gaugetime.extend((np.arange(0, len(ints), dtype=float) +
                                  timedelay) / 60 / 24 + eventstarttime[-1])
                timedelay += len(ints)
                
        if initial_loss > 0:
            gauge_initial_loss = initial_loss
            import copy
            initial_loss_recovery = (initial_loss/12/1e3)/60*1e3
            gaugeintReduced = copy.deepcopy(gaugeint[:])
            for i in range(len(gaugetime)):
                if (gaugetime[i]-gaugetime[i-1])*24*60>1.5:
                    gauge_initial_loss = min([gauge_initial_loss+
                                            (gaugetime[i]-gaugetime[i-1])*24*60
                                            * initial_loss_recovery,initial_loss])
                gaugeintReduced[i] = max([0,gaugeint[i]-gauge_initial_loss*1e3/60])
                gauge_initial_loss = max([gauge_initial_loss - gaugeint[i]*60/1000,0])
            gaugeint = gaugeintReduced
        
        if concentration_time>0:
            gaugetime = [np.round(t*24.0*60) for t in gaugetime]
            
            concentration_time = int(concentration_time)
            gaugetimePadded = []
            gaugeintPadded = []
            timeskips = np.concatenate(([-1],np.where(np.diff(gaugetime)>1.5)[0]))
    
            for timeskipi in range(1,len(timeskips)):
                gaugetimePadded.extend(gaugetime[timeskips[timeskipi-1]+1:timeskips[timeskipi]+1])
                paddedTimes = [a+gaugetime[timeskips[timeskipi]] for a in 
                                        range(1,min([int((gaugetime[timeskips[timeskipi]+1]-gaugetime[timeskips[timeskipi]])),
                                                     concentration_time]))]
                gaugetimePadded.extend(paddedTimes)
                gaugeintPadded.extend(gaugeint[timeskips[timeskipi-1]+1:timeskips[timeskipi]+1])
                gaugeintPadded.extend(np.zeros((len(paddedTimes))))
                # print([int((gaugetime[timeskips[timeskipi]+1]-gaugetime[timeskips[timeskipi]])*60.0*24),concentration_time])
                # A = np.diff(gaugetime)*60*24
                # B = np.diff(gaugetimePadded)*60*24
                # if timeskipi == 2:
                #     break
            gaugetime = gaugetimePadded
            gaugeint = gaugeintPadded
            # print(gaugeint)
            
            gaugeintTA = np.zeros((len(gaugeint)))
                
            for i in range(len(gaugeint)):
                iStart = bisect.bisect(gaugetime, gaugetime[i]-concentration_time)
    
                gaugeintTA[i] = np.sum(gaugeint[iStart:i+1])/concentration_time
            gaugeint = gaugeintTA
            gaugetime = np.array([t/24/60 for t in gaugetime])
        self.gaugetime, self.gaugeint = np.asarray(gaugetime, dtype=float), np.asarray(gaugeint)
        self.rain_gauge_duration = (gaugetime[-1]-gaugetime[0])/365.25
    
    @property
    def timeseries(self):
        if self.__timeseries is None:
            import pandas as pd
            self.__timeseries = pd.Series(self.gaugeint, index = dates.num2date(self.gaugetime))
        return self.__timeseries
    
    def rainStatistics(self, time_aggregate_periods, merge_period = None):
        time_aggregate_periods = [int(t) for t in time_aggregate_periods]
       
        gaugetime_minutes = np.int32(self.gaugetime * 24 * 60)
        mergePeriod = max(time_aggregate_periods) if merge_period is None else merge_period
        events_limits = np.where(np.int64(np.round(np.diff(gaugetime_minutes, n=1, axis=0)))>mergePeriod)[0].astype(int)
        events_startindex = np.hstack(([0], 1+events_limits))
        events_endindex = np.hstack((events_limits, len(gaugetime_minutes)))
    
        rain_statistics = np.empty((len(events_startindex), len(time_aggregate_periods)+1), dtype = np.float32)
        for periodi, period in enumerate(time_aggregate_periods):
            rolling_sum = self.timeseries.rolling("%dS" % (period*60)).sum().values
            
            for event_i in range(len(events_startindex)):
                rain_statistics[event_i, periodi] = np.max(rolling_sum[events_startindex[event_i]:events_endindex[event_i]+1])/1000*60
        for event_i in range(len(events_startindex)):
            rain_statistics[event_i, -1] = np.sum(self.gaugeint[events_startindex[event_i]:events_endindex[event_i]+1])/1000*60  
        return rain_statistics, np.transpose(np.vstack((events_startindex, events_endindex)))
    
    def eventAccRain(self):
        eventidx = 0
        tminutes = np.int32(self.gaugetime * 24 * 60)
        mergePeriod = 60
        # Calculate time diff between each intensitety data point
        tdiff = np.int64(np.round(np.diff(tminutes, n=1, axis=0)))
        eventStartTime = np.empty((0, 1), dtype=np.float)
        # Initialize rain aggregate matrix
        RDAgg = np.empty(1, dtype=np.float)
        # Initialize starttime and stop time for each event
        startj = np.empty((0, 0), dtype=np.int)
        # Loop over all intensity data points
        j = 0
        while j < np.size(tminutes) - 1:
            eventStartTime = np.append(eventStartTime, self.gaugetime[j])
            # End of each event is when there's a dry period of xxx minutes
            jend = np.argmax(tdiff[j:] > mergePeriod) + j
            # Initialize time aggregate set for this event
            RDAgg = np.append(
                RDAgg, np.zeros(
                    (1), dtype=np.float), axis=0)
            # Start time of this event
            startj = np.append(startj, np.int(j))
            # Calculate total rain depth for event
            RDAgg[eventidx] = np.sum(self.gaugeint[j:jend]) / 1000 * 60
            j = jend
            # End time of this event
            j += 1
            eventidx += 1  # Change event index
        return eventStartTime, RDAgg
    def plot_IDF(self, time_aggregate_periods, rain_gauge_duration = None):
        if rain_gauge_duration is None:
            rain_gauge_duration = self.rain_gauge_duration
        import matplotlib.pyplot as plt
        rain_depth_aggregated, index = self.rainStatistics(time_aggregate_periods)
    
        rain_depth_aggregated_sort = np.sort(rain_depth_aggregated, axis=0)
        plt.figure()
        for i in range(len(time_aggregate_periods)):
            plt.plot(np.flipud([rain_gauge_duration/(i+1) for i in range(len(rain_depth_aggregated_sort[:,i]))]), rain_depth_aggregated_sort[:,i]/time_aggregate_periods[i]*1000/60, 'o--', label = "%d min" % time_aggregate_periods[i])
        plt.xlabel(u"Gentagelsesperiode [år]")
        plt.ylabel(r"Intensitet [μm/s]")
        plt.legend()
        plt.grid()