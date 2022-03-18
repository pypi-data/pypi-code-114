from asyncio import subprocess
import re
import os
import numpy as np
import shutil 
from DataProcesser import Processor
class InputVariables:
    def __init__(self):
        return
    def datareturn(ParameterNumber,ParameterMean,ParameterStd,ParameterDists, forcedMax=None):
        """
        This class reads in a list of parameter information from the provided input file.
        Using this data, the correct number of samples to reach statistics are found. Lists of Parameter Data is found.
        Data is then passed to the InputFileGeneratorClas
        """
        #First find where variables converge
        diff = .1
        temp = 1
        Nsamplesmax = 0
        Nsamples = 0
        sig = np.zeros((ParameterNumber))
        #Find the signma values, there will be one for each input value
        for i in range((ParameterNumber)):
            sig[i] = ParameterMean[i] * (ParameterStd[i])**2
            #Find the point where the difference between randoms falls below 1 < e-6
            while (diff > 1e-5):
                if (ParameterDists[i]) == "Normal":
                    Nsamples = Nsamples + 1
                    s = np.random.normal(ParameterMean[i], ParameterStd[i], Nsamples)
                    diff = abs((temp-s.mean()))
                    temp = s.mean()
                if ParameterDists[i] == "Uniform" :
                    Nsamples = Nsamples + 1
                    s = np.random.uniform(ParameterMean[i]-sig[i]*3, ParameterMean[i]+sig[i]*3, Nsamples)
                    diff = abs((temp-s.mean()))
                    temp = s.mean()
                #Every data point must be run to the same number of samples, so Saving it here will save time later      
                if Nsamples > Nsamplesmax:
                    Nsamplesmax = Nsamples
                #For testing purposes, the Samples value can be forced.
                if forcedMax:
                    Nsamplesmax = forcedMax    
                data = np.zeros(((ParameterNumber),(Nsamplesmax)))
                for i in range((ParameterNumber)):  
                    if ParameterDists[i] == "Uniform":
                        data[i] = np.random.uniform(ParameterMean[i]-sig[i]*3, ParameterMean[i]+sig[i]*3, Nsamplesmax)
                    if ParameterDists[i] == "Normal":
                        data[i] = np.random.normal(ParameterMean[i],ParameterStd[i],Nsamplesmax)
            return data



class InputFileGenerator:
    def __init__(self,ParameterNumber,inpFilePath,filename,inpfiletype,inpdir,data):
        """
        This class generates the input files to be used by your blackbox, based off of the data found by the InputVariables class.
        The user defines the location where the Input files are generated to.
        """
        inputfile =  filename + "."+inpfiletype
        if(os.getcwd()!=inpFilePath):
            os.chdir(inpFilePath) 
            #copy the Input file to the input directory.
            shutil.copy(inputfile, inpdir)
        if(os.getcwd()!=inpdir):
            #Change to the inputfile directory.
            os.chdir(inpdir)
        parent_dir = os.getcwd()
        for i in range((ParameterNumber)):
            #Define the search string, changes for each parameter
            searchstring = '{parameter' + str(i+1) + '}'
            for j in range(len(data[i,:]  )):
                path = os.path.join(parent_dir, str(data[i,j])) 
                os.mkdir(path)
                #Make unique input file names for each input variable
                newinpfilename =str([i+1])+ ',' + str(data[i,j]) + '.' + inpfiletype    
                #Copy the user modified input file to the path
                shutil.copy(inputfile, path)
                #Change the directory to the newly created path
                os.chdir(path)
                #Rename input file to reflect input variable
                os.rename(inputfile,newinpfilename)     
                #Replace string
                with open(newinpfilename, 'r') as file :
                    filedata = file.read()
                    # Replace the target string
                    filedata = filedata.replace(searchstring, str(data[i,j]))
                    # Write the file out again
                with open(newinpfilename, 'w') as file:
                    file.write(filedata)
                #Change directory back to repeat for next data point
                os.chdir(inpdir)
class InputFileRunner:
    """
    This class runs the inputfile using a subprocess command.
    """
    def __init__(self):
        return
    def FileRunner(ParameterNumber,inpfiletype,inpdir,datavalues,SoftwareCall,inpcmd,outfiletype,outputsearch,outCount):
        if(os.getcwd()!=inpdir):
            #Change to the inputfile directory.
            os.chdir(inpdir)
        #define the current directory
        parent_dir =os.getcwd()
        #For different number of output counts, generate different arrays      
        if(outCount>1):
            outputvalues =np.zeros((ParameterNumber,len(datavalues[0,:]),outCount))
        else:
            outputvalues = np.zeros((ParameterNumber,len(datavalues[0,:])))        
        #Run the files
        for i in range((ParameterNumber)):
            #Reset the directory
            os.chdir(inpdir)
            parent_dir =os.getcwd()
            for j in range(len(datavalues[0,:])):
                path = os.path.join(parent_dir, str(datavalues[i,j])) 
                if os.path.exists(path):
                    #Seeif the tree exists, if it does enter it
                    os.chdir(path)
                    #Define the input file name in the same way it was generated as above.
                    newinpfilename =str([i+1])+ ',' + str(datavalues[i,j]) + '.' + inpfiletype   
                    #Call the subprocess
                    subprocess.call([SoftwareCall,inpcmd +newinpfilename ]) 
                    os.chdir(parent_dir)
            try:
                for i in range((ParameterNumber)):
                    for j in range(len(datavalues[0,:])):
                        path = os.path.join(parent_dir, str(datavalues[i,j])) 
                        if(outCount>1):
                            #For each of the output variables, one needs to parse over them
                            #Reset a temporary array
                            OutValueHolder = []
                            #Read in the output file
                            with open(str([i+1])+ ',' + str(datavalues[i,j]) + outfiletype, 'r+') as output:
                                #Store the output lines as a string
                                output_string = output.read()
                                #Store values from each line to be used later
                                m = re.search(outputsearch,output_string)
                                if m:
                                    for k in range(outCount):
                                        outputvalues[i,j,k] = float(m.group(k+1))
                        else:
                        #Reset a temporary array
                            OutValueHolder = []
                            with open(str([i+1])+ ',' + str(datavalues[i,j]) + outfiletype, 'r+') as output:
                                output_string = output.read()
                                m = re.search(outputsearch +"\s+(d\d\.\d+)",output_string)
                                if m:
                                #Store values from each line to be used later                       
                                    OutValueHolder.float(m.group(1))
                                outputvalues[i] = OutValueHolder
            except FileNotFoundError:
                print("File Not Found")
                os.chdir(parent_dir)

        return 
class OutputFileReader:
    """
    This class reads in values from a provided output file.
    """
    def __init__(self):
        return
    def outputreader(ParameterNumber,outCount,outdir,datavalues,outfile):
        #Change the working directory to the same directory as the output file.
        if(os.getcwd()!=outdir):
            os.chdir(outdir) 
        #Change the working directory to the same directory as the output file.
        OutValueHolder = []
        #If there is more than one output value, make an array of the corresponding size.
        #For every input value there will be at least one corresponding output value, if there are more the array becomes 3d.
        if(outCount>1):
            outputvalues =np.zeros((ParameterNumber,len(datavalues[0,:]),outCount))
        else:
            outputvalues = np.zeros((ParameterNumber,len(datavalues[0,:])))

        for i in range((ParameterNumber)):
            if(outCount>1):
                #For each of the output variables, one needs to parse over them
                for j in range(outCount):
                    #Reset a temporary array
                    OutValueHolder = []
                    #Read in the output file
                    with open(outfile, 'r+') as output:
                        #Read through the lines of the output file
                        lines = output.readlines()
                        for line in lines:
                            #Store values from each line to be used later
                            OutValueHolder.append(line.split(',')[j])
                        outputvalues[i,:,j] = OutValueHolder
            else:
                #Reset a temporary array
                OutValueHolder = []
                with open(outfile, 'r+') as output:
                    lines = output.readlines()
                    for line in lines:
                         #Store values from each line to be used later                       
                        OutValueHolder.append(line)
                    outputvalues[i] = OutValueHolder
        #pass the output values into the data processor
        Processor(ParameterNumber,outputvalues,outCount,datavalues) 
