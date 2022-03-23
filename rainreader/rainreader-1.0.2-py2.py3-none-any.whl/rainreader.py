import datetime  # time series management
from datetime import datetime as dtnow  # get time of code
import matplotlib.dates as dates  # time series management
import numpy as np
import re
import os
from subprocess import call
import bisect  # math bisection method

def rolling_sum(intensity, window_size):
    window_size = min(len(intensity), window_size)
    ret = np.cumsum(intensity, axis=0, dtype=float)
    ret[window_size:] = ret[window_size:] - ret[:-window_size]
    return np.max(ret[window_size - 1:])
    
def readKM2(filename, initial_loss = 0, concentration_time = 0, skip_flags = [], return_pandas_dataframe = False):
    # Read KM2 file as string
    with open(filename, 'r') as km2:
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
    if return_pandas_dataframe:
        import pandas as pd
        # dataframe_dictionairy = {"index": dates.num2date(gaugetime), "intensity": gaugeint}
        return pd.Series(gaugeint, index = pd.to_datetime((np.array(gaugetime)*24*60*60).astype(np.int64),unit="s"))
    else:
        return np.asarray(gaugetime, dtype=float), np.asarray(gaugeint)
    
def rainStatisticsOld(gaugetime, gaugeint, time_aggregate_periods, rain_depth_cutoff = None):
    eventidx = 0
    time_aggregate_periods = np.int32(time_aggregate_periods)
    tminutes = np.int32(gaugetime * 24 * 60)
    mergePeriod = max(time_aggregate_periods)
    # Calculate time diff between each intensitety data point
    tdiff = np.int64(np.round(np.diff(tminutes, n=1, axis=0)))
    # Initialize rain aggregate matrix
    rain_depth_aggregated = np.empty((0, len(time_aggregate_periods) + 1), dtype=np.float)
    # Initialize starttime and stop time for each event
    startj = endj = np.empty((0, 0), dtype=np.int)
    # Loop over all intensity data points
    j = 0
    while j < np.size(tminutes)-1:
        # End of each event is when there's a dry period of xxx minutes
        jend = np.argmax(tdiff[j:] > mergePeriod) + j + 1
        # print(j, jend-1)
        # print(np.sum(gaugeint[j:jend]) / 1000 * 60)
        if rain_depth_cutoff is None or np.sum(gaugeint[j:jend]) / 1000 * 60 > rain_depth_cutoff:
            # Initialize time aggregate set for this event
            rain_depth_aggregated = np.append(
                rain_depth_aggregated, np.zeros(
                    (1, len(time_aggregate_periods) + 1), dtype=np.float), axis=0)
            # Start time of this event
            startj = np.append(startj, np.int(j))
            # Calculate total rain depth for event
            rain_depth_aggregated[eventidx, -1] = np.sum(gaugeint[j:jend]) / 1000 * 60
            # Loop over all intensities in event
            # for j in range(j, jend):
                #   Loop over all time aggregate periods
            for i, dt in enumerate(time_aggregate_periods):
                    # Calculate total rain depth over aggregate period
                # if dt < 60:
                    # rain_depth_aggregated[eventidx, i] = rolling_sum(gaugeint[j:jend], window_size = dt)/1e3*60
                # else:
                rain_depth = np.sum(
                    gaugeint[j:j + bisect.bisect_left((tminutes[j:j + dt] - tminutes[j]), dt)]) / 1000 * 60
                if rain_depth > rain_depth_aggregated[eventidx, i]:
                    rain_depth_aggregated[eventidx, i] = rain_depth
            eventidx += 1  # Change event index
            
        j = jend - 1
        # End time of this event
        endj = np.append(endj, np.int(jend))
        j += 1
    return rain_depth_aggregated, startj    

def rainStatistics(gaugetime, gaugeint, time_aggregate_periods, merge_period = None):
    import pandas as pd
    time_aggregate_periods = [int(t) for t in time_aggregate_periods]
    gaugeDF = pd.Series(gaugeint, index = pd.to_datetime((gaugetime*24*60*60).astype(np.int32),unit="s"))
    gaugetime_minutes = np.int32(gaugetime * 24 * 60)
    mergePeriod = max(time_aggregate_periods)
    gaugetime_deltatime = np.int64(np.round(np.diff(gaugetime_minutes, n=1, axis=0)))
   
    gaugetime_minutes = np.int32(gaugetime * 24 * 60)
    mergePeriod = max(time_aggregate_periods) if merge_period is None else merge_period
    events_limits = np.where(np.int64(np.round(np.diff(gaugetime_minutes, n=1, axis=0)))>mergePeriod)[0].astype(int)
    events_startindex = np.hstack(([0], 1+events_limits))
    events_endindex = np.hstack((events_limits, len(gaugetime_minutes)))

    rain_statistics = np.empty((len(events_startindex), len(time_aggregate_periods)+1), dtype = np.float32)
    for periodi, period in enumerate(time_aggregate_periods):
        rolling_sum = gaugeDF.rolling("%dS" % (period*60)).sum().values
        
        for event_i in range(len(events_startindex)):
            rain_statistics[event_i, periodi] = np.max(rolling_sum[events_startindex[event_i]:events_endindex[event_i]+1])/1000*60
    for event_i in range(len(events_startindex)):
            rain_statistics[event_i, -1] = np.sum(gaugeint[events_startindex[event_i]:events_endindex[event_i]+1])/1000*60  
    return rain_statistics, np.transpose(np.vstack((events_startindex, events_endindex)))        

def eventAccRain(gaugetime,gaugeint):
    eventidx = 0
    tminutes = np.int32(gaugetime * 24 * 60)
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
        eventStartTime = np.append(eventStartTime, gaugetime[j])
        # End of each event is when there's a dry period of xxx minutes
        jend = np.argmax(tdiff[j:] > mergePeriod) + j
        # Initialize time aggregate set for this event
        RDAgg = np.append(
            RDAgg, np.zeros(
                (1), dtype=np.float), axis=0)
        # Start time of this event
        startj = np.append(startj, np.int(j))
        # Calculate total rain depth for event
        RDAgg[eventidx] = np.sum(gaugeint[j:jend]) / 1000 * 60
        j = jend
        # End time of this event
        j += 1
        eventidx += 1  # Change event index
    return eventStartTime, RDAgg
  