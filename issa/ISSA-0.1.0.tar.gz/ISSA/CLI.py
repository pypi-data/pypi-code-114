import argparse
from xmlrpc.client import boolean
import os
import yaml
from Functions import InputVariables
from Functions import InputFileGenerator
from Functions import InputFileRunner
from Functions import OutputFileReader

#Main Driver Function of the code
def run(args):
    ReadOutputBoolean = args.ReadOutputs
    inpFilePath = args.PathInp
    #Check if the user placed their yaml file in the current directory
    if(os.getcwd()!=args.PathYml):
        #Change Director to the same directory that contains the input yaml file
        os.chdir(args.PathYml)
    with open('config.yaml', 'r') as file:
        #Import the run settings from the user defined yaml file.
        RunSettings = yaml.safe_load(file)
        #Store all run settings.
        filename = RunSettings['Input_file']['file_name']
        inpfiletype = RunSettings['Input_file']['in_file_type']
        SoftwareCall = RunSettings['Input_file']['software_call']
        inpcmd = RunSettings['Input_file']['input_command']
        inpdir = RunSettings['Input_file']['Inp_File_directory']
        ParameterNumber = RunSettings['Input_param']['Param_count']
        ParameterMean = RunSettings['Input_param']['Param_means']
        ParameterStd = RunSettings['Input_param']['Param_std']
        ParameterDists = RunSettings['Input_param']['Param_pdf']
        outCount = RunSettings['Output_file']['out_count']
        outfiletype = RunSettings['Output_file']['out_file_type']
        outfilename = RunSettings['Output_file']['outfile_name']
        outdir = RunSettings['Output_file']['Out_File_directory']
        outputsearch = RunSettings['Output_file']['output_searchline']
        #If you are forcing a number of samples
        ForcedSamples = RunSettings['Input_param']['forced_max']

    #Pass The information here to the base Functions
    #Generate data points from the inputVariablesfunction
    datavalues = InputVariables.datareturn(ParameterNumber,ParameterMean,ParameterStd,ParameterDists,ForcedSamples)
    #Pass data found in the first function, to the next.
    #Function that builds lists of Input Parameter values and subsequent input files
    InputFileGenerator(ParameterNumber,inpFilePath,filename,inpfiletype,inpdir,datavalues)
    #Fucntion that runs subprocess/readoutputs. If user is providing output files, call the output reader command here.
    if ReadOutputBoolean == True:
        outputvalues = OutputFileReader.outputreader(ParameterNumber,outCount,outdir,datavalues,outfilename)
    else:
        outputvalues = InputFileRunner.FileRunner(ParameterNumber,inpfiletype,inpdir,datavalues,SoftwareCall,inpcmd,outfiletype,outputsearch,outCount,)

    
def main():
    parser=argparse.ArgumentParser(description="Generate, Run and Analyze BlackBox Code Input Files")
    parser.add_argument("--Input File Path:",help="If the Path containing the Input File is different from the Current Working Directory, please provide it here.", dest="PathInp", type=str, default=os.getcwd(), required=False )
    parser.add_argument("--YAML File Path:",help="If the Path containing the Yaml File, config.yaml, is Different from the Current Working Directory, Please provide it here.", dest="PathYml", type=str, default=os.getcwd(),required=False)
    parser.add_argument("--Provided Output Values? T/F",help="If your program requires a third party software to extract data, or you have written your own program to do so, set this variable to True and provide the file containing output values when prompted. Default False." ,dest="ReadOutputs", type=boolean, default=False)
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__=="__main__":
	main()