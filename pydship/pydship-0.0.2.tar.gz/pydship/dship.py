import datetime
import numpy as np
import geojson

def test_time_format(lsplit):
    """ Tests which format the time has
    """
    # The index with the date/time information
    time_ind0 = 0
    # The index with the time information, this is used if the time is in a seperate column
    time_ind1 = -1    
    # Dship 1 has two different fields, dship2 one field for date/time
    time_fmts = ['%H:%M:%S']
    date_fmts = ['%Y/%m/%d', '%d.%m.%Y']
    time_fmt = [None,None,None]
    print('Testing time formats')
    for itest in range(2):
        if(time_ind1 <0):
            datestr = lsplit[time_ind0]
        else:
            datestr = lsplit[time_ind0] + ' ' + lsplit[time_ind1]
            
        for itmp,date_fmt_test in enumerate(date_fmts):
            date_fmt_merged = date_fmt_test + ' ' + time_fmts[0]
            try:
                ttmp = datetime.datetime.strptime(datestr,date_fmt_merged)
                time_fmt = [date_fmt_merged,time_ind0,time_ind1]
                print('Found valid time format for:' + datestr + ' ' + date_fmt_merged)
                break
            except Exception as e:
                print(e)
                time_fmt = [None,None,None]                
                pass

        if(time_fmt[0] is not None):
            break
        # If we didnt find a proper format, try with the next column
        time_ind1 = time_ind0 + 1

    return time_fmt

def convert_time(lsplit,time_fmt):
    date_fmt = time_fmt[0]
    time_ind0 = time_fmt[1]
    time_ind1 = time_fmt[2]    
    if(time_ind1 <0):
        datestr = lsplit[time_ind0]
    else:
        datestr = lsplit[time_ind0] + ' ' + lsplit[time_ind1]

    ttmp = datetime.datetime.strptime(datestr,date_fmt)
    return ttmp


def parse_dship(fname, encoding='latin-1', delimiter=';'):
    """Parses WERUM DSHIP data

    """
    f = open(fname,encoding =  encoding)
    # Test to parse time
    for nl in range(10):
        l = f.readline()
        ds = l.split(delimiter)
        time_fmt = test_time_format(ds)
        if(time_fmt[0] is not None):
            break

    if(time_fmt[0] is None):
        print('Could not find valid date, aborting')
        return None
        
    print('Found valid time in line:' + str(nl))
    # Rewind
    f.seek(0)
    if(nl == 3):     # First line is sensors        
        l = f.readline()
        l = l.replace('\n','')
        sensors = l.split(delimiter)
    else: # First line is group, second line is sensors        
        lgr = f.readline()
        lsen = f.readline()
        lgr = lgr.replace('\n','')
        lsen = lsen.replace('\n','')
        lgrs = lgr.split(delimiter)
        lsens = lsen.split(delimiter)
        sensors = []
        for i in range(len(lsens)):
            sensor = lgrs[i] + '.' + lsens[i].replace('\n','')
            #print('Sensor',sensor)
            sensors.append(sensor)

    # Next line is something
    l = f.readline()
    # Last header line is units
    l = f.readline()    
    units = l.split(delimiter)
    data = {}
    header = l[:]
    for i,s in enumerate(sensors):
        print(s)
        data[s] = {'data':[],'unit':units[i]}

    data['datetime'] = []
    # Now the data begins
    nline = -1
    while True:
        nline += 1
        d = f.readline()
        d = d.replace('\n','')
        if(len(d) == 0):
            break

        ds = d.split(delimiter)        
        ttmp = convert_time(ds,time_fmt)
        #print('Convert time',ttmp,time_fmt)
        data['datetime'].append(ttmp)
        for i,s in enumerate(sensors):
            try: 
                dtmp = float(ds[i])
            except:
                dtmp = np.NaN

            data[s]['data'].append(dtmp)

    return data

def dship2geojson(filename,data,lonkey,latkey,attributes=None):
    
    """ Writes a geojson file from a parsed dship dataset. Required a the key for latitude and longitude
    attributes: 'all',None
    """
    #data[s]['data'].append(ttmp)
    crs = { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } } # Reference coordinate system
    nrecords = len(data[lonkey]['data'])
    if True:
        features = []
        points = []
        for i in range(nrecords):
            lon = data[lonkey]['data'][i]
            lat = data[latkey]['data'][i]
            p = geojson.Point((lon, lat))
            points.append((lon, lat))
            prop = {}
            for o in data.keys():
                dat = data[o]['data'][i]
                if(type(dat) == datetime.datetime):
                    dat = datetime.datetime.strftime(dat,'%Y-%m-%d %H:%M:%S')
                elif(np.isnan(dat)):
                    dat = -9999
                    
                prop[o] = dat

            feature = geojson.Feature(geometry=p, properties=prop)
            features.append(feature)

        mpoints = geojson.MultiPoint(points,crs=crs) 
        featurecol = geojson.FeatureCollection(features,name='dship',crs=crs)
        with open(filename, 'w') as outfile:
            if(attributes == None):
                geojson.dump(mpoints, outfile)            
            elif(attributes == 'all'):
                geojson.dump(featurecol, outfile)                


        outfile.close()
