#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# This is an EXUDYN python utility library
#
# Details: 	Plot utility functions based on matplotlib, including plotting of sensors and FFT.
#
# Author:   Johannes Gerstmayr
# Date:     2020-09-16 (created)
#
# Copyright:This file is part of Exudyn. Exudyn is free software. You can redistribute it and/or modify it under the terms of the Exudyn license. See 'LICENSE.txt' for more details.
#
# Notes:	For a list of plot colors useful for matplotlib, see also utilities.PlotLineCode(...)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


import matplotlib
import matplotlib.pyplot as plt
import numpy as np #for loading
import matplotlib.ticker as ticker
import exudyn #for sensor index
from exudyn.utilities import PlotLineCode

#from exudyn.utilities import PlotLineCode

#**function: parse header of output file (solution file, sensor file, genetic optimization output, ...) given in file.readlines() format
#**output: return dictionary with 'type'=['sensor','solution','geneticOptimization','parameterVariation'], 'variableType', 
def ParseOutputFileHeader(lines):
    nLines = len(lines)
    parseLines = min(10, nLines) #max 10 lines to parse
    output = {}
    output['type'] = 'unknown'
    columns = []
    if len(lines) < 1:
        return {} #empty dictionary
    variableTypes = []
    if lines[0].find('EXUDYN genetic optimization results file') != -1:
        output['type'] = 'geneticOptimization'
        for i in range(parseLines): #header is max. 10 lines
            if i+1 < len(lines) and lines[i][0:9] == '#columns:':
                cols = lines[i+1].strip('#').split(',')
                for j in range(len(cols)):
                    variableTypes += [cols[j].strip()]
                break
    if lines[0].find('EXUDYN parameter variation results file') != -1:
        output['type'] = 'parameterVariation'
        for i in range(parseLines): #header is max. 10 lines
            if i+1 < len(lines) and lines[i][0:9] == '#columns:':
                cols = lines[i+1].strip('#').split(',')
                for j in range(len(cols)):
                    variableTypes += [cols[j].strip()]
                break
    elif lines[0].find('sensor output file') != -1:
        #print("SENSOR")
        output['type'] = 'sensor'
        outputVariableType = ''
        for i in range(parseLines): #header is max. 10 lines
            if lines[i].find('Object number') != -1:
                output['objectNumber'] = int(lines[i].split('=')[1])
            elif lines[i].find('OutputVariableType') != -1:
                outputVariableType = lines[i].split('=')[1].strip() #without spaces
                output['outputVariableType'] = outputVariableType #for PlotSensor
            elif lines[i].find('number of sensor values') != -1:
                output['numberOfSensors'] = int(lines[i].split('=')[1]) 

            if lines[i].find('#measure') != -1:
                output['sensorType'] = lines[i].split(' ')[1] #for PlotSensor
                output['itemNumber'] = int(lines[i].split('=')[1]) #unused
                
            if lines[i][0] != '#': #break after comment
                break
        variableTypes = ['time']
        for i in range(output['numberOfSensors']):
            variableTypes += [outputVariableType+str(i)] #e.g., Position0, Position1, ...
    elif lines[0].find('solution file') != -1: #coordinates solution file
        output['type'] = 'solution'
        writtenCoordinateTypes = []
        writtenCoordinates = []
        for i in range(parseLines): #header is max. 10 lines
            if lines[i].find('number of written coordinates') != -1:
                line = lines[i]
                writtenCoordinateTypes = line.split('=')[0].split('[')[1].split(']')[0].replace(' ','').split(',')
                writtenCoordinates = line.split('=')[1].split('[')[1].split(']')[0].replace(' ','').split(',')
                variableTypes = ['time']
                print('writtenCoordinates=',writtenCoordinates)
                for j in range(len(writtenCoordinateTypes)):
                    for k in range(int(writtenCoordinates[j])):
                       variableTypes += [writtenCoordinateTypes[j].strip('n')+'-'+str(k)]
                #variableTypes += [writtenCoordinateTypes[j]]*int(writtenCoordinates[j])
            elif lines[i].find('number of time steps') != -1:
                output['numberOfSteps'] = int(lines[i].split('=')[1])

            if lines[i][0] != '#': #break after comment
                break

    output['columns'] = variableTypes
    return output
   

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#**function: Helper function for direct and easy visualization of sensor outputs, without need for loading text files, etc.; PlotSensor can be used to simply plot, e.g., the measured x-Position over time in a figure. PlotSensor provides an interface to matplotlib (which needs to be installed). 
#**input: 
#  mbs: must be a valid MainSystem (mbs)
#  sensorNumbers: consists of one or a list of sensor numbers (type SensorIndex or int) as returned by the mbs function AddSensor(...); alternatively, it may contain FILENAMES (incl. path) to stored sensor or solution files instead of sensor numbers; if components is a list and sensorNumbers is a scalar, sensorNumbers is adjusted automatically to the components
#  components: consists of one or a list of components according to the component of the sensor to be plotted; if components is a list and sensorNumbers is a scalar, sensorNumbers is adjusted automatically to the components; as always, components are zero-based, meaning 0=X, 1=Y, etc.
#  xLabel: string for text at x-axis
#  colorCodeOffset: int offset for color code, color codes going from 0 to 27 (see PlotLineCode(...))
#  newFigure: if True, a new matplotlib.pyplot figure is created; otherwise, existing figures are overwritten
#  fileName: if this string is non-empty, figure will be saved to given path and filename (use figName.pdf to safe as PDF or figName.png to save as PNG image); use matplotlib.use('Agg') in order not to open figures if you just want to save them
#  useXYZcomponents: of True, it will use X, Y and Z for sensor components, e.g., measuring Position, Velocity, etc. wherever possible
#  closeAll: if True, close all figures before opening new one (do this only in first PlotSensor command!)
#  [*kwargs]:
#        yLabel: string for text at y-axis (otherwise outputvalues are used)
#        componentsX: optional list of components (or scalar) representing x components of sensors in plotted curves; DON'T forget to change xLabel accordingly! Using componentsX=[...] with a list of column indices specifies the respective columns used for the x-coordinates in all sensors; by default, values are plotted against the first column in the files, which is time; according to counting in PlotSensor, this represents componentX=-1; plotting y over x in a position sensor thus reads: components=[1], componentsX=[0]; plotting time over x reads: components=[-1], componentsX=[0]; the default value reads componentsX=[-1,-1,...]
#        fontSize: optional fontSize; default = 16, which is a little bit larger than default (12)
#        figureName: optional name for figure, if newFigure=True
#        majorTicksX: number of major ticks on x-axis (default=10)
#        majorTicksY: number of major ticks on y-axis (default=10)
#        minorTicksXon: if True, turn minor ticks for x-axis on
#        minorTicksYon: if True, turn minor ticks for y-axis on
#        title: optional string representing plot title 
#        offsets: provide as scalar or list (per sensor) to add offset to each sensor output; for an original value fOrig, the new value reads fNew = factor*(fOrig+offset)
#        factors: provide as scalar or list (per sensor) to add factor to each sensor output; for an original value fOrig, the new value reads fNew = factor*(fOrig+offset)
#**output: plots the sensor data
#**example: 
##assume to have some position-based nodes 0 and 1:
#s0=mbs.AddSensor(SensorNode(nodeNumber=0, fileName='s0.txt',
#                            outputVariableType=exu.OutputVariableType.Position))
#s1=mbs.AddSensor(SensorNode(nodeNumber=1, fileName='s1.txt',
#                            outputVariableType=exu.OutputVariableType.Position))
#PlotSensor(mbs, s0, 0) #plot x-coordinate
##plot x for s0 and z for s1:
#PlotSensor(mbs, sensorNumbers=[s0,s1], components=[0,2], xLabel='time in seconds')
#PlotSensor(mbs, sensorNumbers=s0, components=[0,1,2], factors=1000., title='Answers to the big questions')
#PlotSensor(mbs, sensorNumbers=s0, components=[0,1,2,3], 
#           yLabel='Coordantes with offset 1\nand scaled with $\\frac{1}{1000}$', 
#           factors=1e-3, offsets=1,fontSize=12, closeAll=True)
#
##assume to have body sensor sBody, marker sensor sMarker:
#PlotSensor(mbs, sensorNumbers=[sBody]*3+[sMarker]*3, components=[0,1,2,0,1,2], 
#           colorCodeOffset=3, newFigure=False, fontSize=10, 
#           yLabel='Rotation $\\alpha, \\beta, \\gamma$ and\n Position $x,y,z$',
#           title='compare marker and body sensor')
##assume having file plotSensorNode.txt:
#PlotSensor(mbs, sensorNumbers=[s0]*3+ [filedir+'plotSensorNode.txt']*3, 
#           components=[0,1,2]*2)
##plot y over x:
#PlotSensor(mbs, sensorNumbers=s0, components=[1], componentsX=[0], xLabel='x-Position', xLabel='x-Position')
def PlotSensor(mbs, sensorNumbers=[], components=0, xLabel='time (s)', colorCodeOffset=0, newFigure=True, closeAll=False, fileName='', useXYZcomponents=True, **kwargs):
    #could also be imported from exudyn.utilities import PlotLineCode
    #CC = ['k-','g-','b-','r-','c-','m-','y-','k:','g:','b:','r:','c:','m:','y:','k--','g--','b--','r--','c--','m--','y--','k-.','g-.','b-.','r-.','c-.','m-.','y-.']
    
    if isinstance(sensorNumbers,list):
        sensorList = sensorNumbers
    else:
        sensorList = [sensorNumbers]

    if isinstance(components,list):
        componentList = components
    else:
        componentList = [components]

    if len(componentList) == 1 and len(sensorList) != 1:
        componentList = componentList*len(sensorList)
        
    if len(componentList) != 1 and len(sensorList) == 1:
        sensorList = sensorList*len(componentList)
        
    if len(componentList) !=  len(sensorList):
        raise ValueError('ERROR in PlotSensor: size of sensorNumbers and size of components must be same or either components or sensorNumbers is scalar, sensorNumbers='+str(sensorNumbers)+', components='+str(components))

    nSensors = len(sensorList)

    componentsX = [-1]*nSensors
    if 'componentsX' in kwargs:
        componentsX = kwargs['componentsX']
        if not isinstance(components,list):
            componentsX = [kwargs['componentsX']]*nSensors
        elif len(componentsX) != nSensors:
            raise ValueError('ERROR in PlotSensor: size of componentsX and size of sensors or components must be agree; componentsX='+str(componentsX))

    
    if closeAll:
        plt.close('all')
        
    #increase font size as default is rather small
    if 'fontSize' in kwargs:
        plt.rcParams.update({'font.size': kwargs['fontSize']})
    else:
        plt.rcParams.update({'font.size': 16})

    factorOffsetUsed = False
    factors = [1.]*nSensors
    offsets = [0.]*nSensors
    if 'factors' in kwargs:
        factors = kwargs['factors']
        if type(factors) != list:
            factors = [factors]*nSensors
        if len(factors) != nSensors:
            raise ValueError('PlotSensor: factors must be scalar or have same dimension as sensors')
        factorOffsetUsed = True
    if 'offsets' in kwargs:
        offsets = kwargs['offsets']
        if type(offsets) != list:
            offsets = [offsets]*nSensors
        if len(offsets) != nSensors:
            raise ValueError('PlotSensor: offsets must be scalar or have same dimension as sensors')
        factorOffsetUsed = True


    if nSensors:
        if 'figureName' in kwargs:
            figureName = kwargs['figureName']
            if newFigure and plt.fignum_exists(figureName):
                plt.close(figureName)
            plt.figure(figureName)
        elif newFigure:
            plt.figure()


    sensorFileNames = [] #for loading of files
    sensorLabels = []    #plot label (legend)
    sensorTypes = []     #for comparison, if all are of the same type
    
    for i in range(nSensors):
        component = componentList[i]
        sensorNumber = sensorList[i]
        if not (isinstance(sensorNumber, exudyn.SensorIndex) or 
                type(sensorNumber) == int or
                type(sensorNumber) == str):
            raise ValueError('ERROR in PlotSensor: *args must contain valid sensor numbers (SensorIndex or integers) or represent a filename string')

        #retrieve sensor information:
        if type(sensorNumber) == str: #direct path to file name
            sensorDict={}
            sensorDict['fileName'] = sensorNumber #this must contain a file name, otherwise will fail
            sensorDict['outputVariableType']=''
            sensorDict['name'] = sensorNumber.split('/')[-1].split('\\')[-1].split('.')[0] #use filename without path and ending
            
            with open(sensorDict['fileName']) as file:
                sensorDict.update(ParseOutputFileHeader(file.readlines()) )
            
            if sensorDict['type'] == 'solution':
                sensorDict['outputVariableType'] = 'Coordinates'
                
        else:
            sensorDict = mbs.GetSensor(sensorNumber)
        
        #print('sensorDict=',sensorDict)
        sensorName = sensorDict['name']

        variableStr = '' #in case of markers, etc.
        if 'outputVariableType' in sensorDict:
            variable = sensorDict['outputVariableType']
            variableStr = str(variable).replace('OutputVariableType.','')
        elif 'sensorType' in sensorDict:
            if sensorDict['sensorType'] == 'Load':
                loadNumber = sensorDict['loadNumber']
                loadDict = mbs.GetLoad(loadNumber)
                loadType = loadDict['loadType']
                if (loadType == 'ForceVector' or
                    loadType == 'TorqueVector'):
                    variableStr = loadType.replace('Vector','')
                else:
                    variableStr = 'Load'
            else:
                variableStr = sensorDict['sensorType']

        #+++++++++++++++++++++++++++++++++++        
        #create name for component
        sComponent=''
        #if len(componentList) != 1: #changed 2022-01-25: should show up anyway
        varStrNoLocal = variableStr.replace('Local','')
        compXYZ = ['X','Y','Z']
        compXYZ2 = ['XX','YY','ZZ','YZ','XZ','XY'] #for stress, strain,...
        
        if (useXYZcomponents and component < 3 and component >= 0 and 
            (varStrNoLocal == 'Force' or varStrNoLocal == 'Torque' or 
             varStrNoLocal == 'Position' or varStrNoLocal == 'Displacement' or 
             varStrNoLocal == 'Velocity' or varStrNoLocal == 'Acceleration' or
             varStrNoLocal == 'Rotation' or varStrNoLocal == 'AngularVelocity' or
             varStrNoLocal == 'AngularAcceleration' or 
             varStrNoLocal == 'Force' or varStrNoLocal == 'Torque' or 
             varStrNoLocal == 'AngularVelocity' or varStrNoLocal == 'AngularAcceleration')):
            sComponent = compXYZ[component]
        elif (useXYZcomponents and component < 6 and component >= 0 and 
            (varStrNoLocal == 'Strain' or varStrNoLocal == 'Stress')):
            sComponent = compXYZ2[component]
        else:
            sComponent = str(component)

        sensorFileNames += [sensorDict['fileName']]
        sensorLabels += [sensorName+', '+variableStr+sComponent]
        sensorTypes += [variableStr]
    #+++++++++++++++++++++++++++++++++++++++++++
    #check if all sensor outputvariables are the same => generate ylabel automatically!
    checkStr = ''
    allVariablesSame = True
    for i in range(nSensors):

        if i == 0:
            checkStr = sensorTypes[i]
        elif checkStr != sensorTypes[i]:
            allVariablesSame = False

    yLabel = ''
    if allVariablesSame:
        yLabel = checkStr

    if 'yLabel' in kwargs:
        yLabel = kwargs['yLabel']
        

    #+++++++++++++++++++++++++++++++++++++++++++
    #finally plot:
    for i in range(nSensors):
        componentY = componentList[i] + 1
        componentX = componentsX[i] + 1
        
        #now load sensor file:
        data = np.loadtxt(sensorFileNames[i], comments='#', delimiter=',')

        #select color and style for sensor
        col = PlotLineCode(i+colorCodeOffset)
        
        #extract additional paramters
        if not 'yLabel' in kwargs and not allVariablesSame:
            yLabel += variableStr
            if i < nSensors-1:
                yLabel += ', '
        
        #+++++++++++++++++++++++++++++++++++        
        #add factor and offset if defined:
        if factorOffsetUsed:
            yData = factors[i]*(data[:,componentY] + offsets[i])
        else:
            yData = data[:,componentY]

        #+++++++++++++++++++++++++++++++++++        
        #finally plot curve:
        plt.plot(data[:,componentX], yData, col, label=sensorLabels[i]) #numerical solution
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        ax=plt.gca() # get current axes
        ax.grid(True, 'major', 'both')
        
        majorTicksX = 10
        majorTicksY = 10
        if 'majorTicksX' in kwargs:
            majorTicksX = kwargs['majorTicksX']
        if 'majorTicksY' in kwargs:
            majorTicksY = kwargs['majorTicksY']

        ax.xaxis.set_major_locator(ticker.MaxNLocator(majorTicksX)) 
        ax.yaxis.set_major_locator(ticker.MaxNLocator(majorTicksY)) 

        if 'minorTicksOn' in kwargs:
            if kwargs['minorTicksOn']:
                ax.minorticks_on()
            else:
                ax.minorticks_off()

        if 'title' in kwargs:
            plt.title(kwargs['title'])

    #do this finally!!!
    if nSensors > 0:
        plt.legend() #show labels as legend
        plt.tight_layout()
        if matplotlib.get_backend() != 'agg': #this is used to avoid showing the figures, if they are just saved
            plt.show() 
        
        if fileName != '':
            plt.savefig(fileName)
        
    
#**function: plot fft spectrum of signal
#**input: 
#   frequency:  frequency vector (Hz, if time is in SECONDS)   
#   data:       magnitude or phase as returned by ComputeFFT() in exudyn.signal
#   xLabel:     label for x-axis, default=frequency
#   yLabel:     label for y-axis, default=magnitude
#   label:      either empty string ('') or name used in legend
#   freqStart:  starting range for frequency
#   freqEnd:    end of range for frequency; if freqEnd==-1 (default), the total range is plotted
#   logScaleX:  use log scale for x-axis
#   logScaleY:  use log scale for y-axis
#   majorGrid:  if True, plot major grid with solid line 
#   minorGrid:  if True, plot minor grid with dotted line 
#**output: creates plot and returns plot (plt) handle
def PlotFFT(frequency, data, 
               xLabel='frequency', yLabel='magnitude', 
               label = '',
               freqStart = 0, freqEnd = -1, 
               logScaleX = True, logScaleY = True,
               majorGrid = True, minorGrid = True):
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    indStart = 0
    indEnd = len(data)
    for i in range(len(frequency)):
        if frequency[i] <= freqStart:
            indStart = i
        if frequency[i] <= freqEnd:
            indEnd = i

    #print("fft ind=", indStart, indEnd)
    if len(label) != 0:
        plt.plot(frequency[indStart:indEnd], data[indStart:indEnd], label=label)
        plt.legend() #show labels as legend
    else:
        plt.plot(frequency[indStart:indEnd], data[indStart:indEnd])
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    ax=plt.gca() # get current axes
    ax.xaxis.set_major_locator(ticker.MaxNLocator(10)) 
    ax.yaxis.set_major_locator(ticker.MaxNLocator(10)) 
    xScale = 'linear'
    yScale = 'linear'
    if logScaleX:
        plt.xscale('log')
    if logScaleY:
        plt.yscale('log')
    ax.grid(b=True, which='major', color='k', linestyle='-')
    ax.grid(b=True, which='minor', color='k', linestyle=':')
    ax.minorticks_on()

    plt.tight_layout()
    plt.show() 

    return plt
        