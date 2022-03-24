from posixpath import normcase
from zipfile import ZipFile
from tempfile import TemporaryDirectory
from functools import partial
from itertools import repeat
from multiprocessing import Pool, freeze_support, cpu_count

import subprocess
import os
import re
import logging
import datetime
import time
import shutil
import json
import re
import EventStreamDataExtractor
import HWErrorsFromSyslog
from shared_data_handling import process_data

#from datetime import datetime

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ICExtractorVersion = "0.10"
# path to the compressed IC data inside the problem report
logandconfig_path = 'instrumentlogs'
# compressed IC data inside the problem report
logandconfig_name = 'logandconfig.zip'
# path to the event steam files within the problem report
eventStream_FullName = 'eventstream'
# shall the sensordata be retained?
keepICDataFolders = {'persistentdata': False, 'pipettingparametersets': False, 'sensordata': True, 
                    'teachdata': True, 'ECPGenConfigurationFiles': False, 'ECPConfigurationFiles': False}

# Windows path to the 7zip executable
#z7zipPath = "C:/Program Files/7-Zip/7z.exe"
# for ubuntu use sudo apt-get install p7zip-full
z7zipPath = "7z"

# File filter for the ic log folder, by default all files will be merged into one file
# the original files will be removed from the output if set to 'True'
# If the flag is set to false, the original log will be retained in the output folder.
handleLogFiles = {'sar-avg.log': True, 'sar-bdio.log': True, 'disk.log': True, 'mem.log': True,
                  'sar-cpu.log': True, 'sar-cswi.log': True, 'sar-dev.log': True,
                  'sar-edev.log': True, 'sar-io.log': True, 'sar-mem.log': True,
                  'sar-sock.log': True, 'sar-tcp.log': True, 'sar-udp.log': True,
                  'syslog': True}


class Extract:
    def __init__(self, zip, output_directory, archive_password, extractEventStreamData=True):
        self.zip = zip
        self.output_directory = output_directory
        self.archive_password = archive_password
        self.z7ZipPath = z7zipPath
        self.logandconfig_path = logandconfig_path
        self.logandconfig_name = logandconfig_name
        self.logandconfig_FullName = os.path.join(self.logandconfig_path, self.logandconfig_name)
        self.eventStream_FullName = eventStream_FullName
        self.extractEventStreamData = extractEventStreamData
        self.handleLogFiles = handleLogFiles
        self.keepICDataFolders = keepICDataFolders
        self.ICExtractorVersion = ICExtractorVersion
        self.LogFileRanges = {}
        if(not os.path.exists(self.output_directory)):
            os.mkdir(self.output_directory)

        self.extractICData(self.zip)

    def extractICData(self, fullProblemReportName):
        '''
        Extract the logandconfig.zip file into a temp folder and extract the data to the target output directory.
        The log files will be maerged and renamed except for the syslogs. Can be set in the handleLogFiles dictionary
        '''
        try:
            s = time.perf_counter()
            self.problemReportName = os.path.splitext(os.path.basename(fullProblemReportName))[0]

            if not fullProblemReportName.endswith(".zip"):
                raise Exception(f"the file \"{self.problemReportName}\" is not a zip file")

            # Extend the output path with the datetime if the extract already exists in the output folder
            self.outputFullPath = os.path.join(self.output_directory, self.problemReportName)
            if os.path.isdir(self.outputFullPath):
                raise Exception(f"ProblemReport extract already existant. Skipping...")
                self.outputFullPath += datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

            self.logger = logging.getLogger(self.problemReportName)
            self.logger.info(f"Processing ProblemReport \"{self.problemReportName}\"")
            # write the ic problem report to the temp folder
            with TemporaryDirectory(prefix=self.problemReportName) as tempDirName:
                # Extract the logandConfig.zip file to a temp folder
                self.ExtractDataFromZip(
                    fullProblemReportName, tempDirName, self.logandconfig_FullName)
                # Extract the extracted logandconfig.zip file to the output folder
                with ZipFile(os.path.join(tempDirName, self.logandconfig_FullName), "r") as zf:
                    zf.extractall(self.outputFullPath)

            # merge the IC log files
            for k, v in handleLogFiles.items():
                try:
                    filename, first_row, last_row = self.mergeLogFiles(k, "log", deleteFilesAfterMerge=v)
                    self.LogFileRanges[filename] = (first_row, last_row)
                except Exception as e:
                    self.logger.exception(e)
            self.RelativeSyslogPath = [key for key, value in self.LogFileRanges.items() if 'syslog' in key.lower()][0]

            # extract the event stream data
            if self.extractEventStreamData:
                self.ExtractDataFromZip(fullProblemReportName, self.outputFullPath, self.eventStream_FullName)
                esName, esFirstLine, esLastLine, self.counters = EventStreamDataExtractor.ParseFolder(
                    rootdir=os.path.join(self.outputFullPath, self.eventStream_FullName), relativeOutputFilePath=os.path.join("..","log", f"{self.problemReportName}_systemeventstream.log"))

                self.LogFileRanges[esName] = self.extractDateTimeFromStings([esFirstLine, esLastLine])
                self.RelativeEventStreamPath = esName
                shutil.rmtree(os.path.join(self.outputFullPath, self.eventStream_FullName))

            self.logger.debug(f"All files successfully extracted to {self.problemReportName}")
            # do some clean up of the temp files
            self.logger.debug("Delete temporary files")
           # delete not used data
            for folder, shallKeepFolder in self.keepICDataFolders.items():
                if not shallKeepFolder:
                    try:
                        shutil.rmtree(os.path.join(self.outputFullPath, folder))
                    except:
                        pass
            
            self.logger.info("Generating meta data")
            #This may take some time since the merged syslog will be searched for regex patterns
            self.HWErrors = HWErrorsFromSyslog.ParseFile(os.path.join(self.outputFullPath, self.RelativeSyslogPath))
            self.toJSON()
            self.logger.info(f"Processed ProblemReport \"{self.problemReportName}\"")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Unable to extract \"{self.problemReportName}\" from the ProblemReport. ReturnValue from 7zip: \"{e.output}\"")
        except Exception as e:
            self.logger.error(f"Failed to process ProblemReport \"{self.problemReportName}\", {e}")
            self.logger.exception(e)

        self.ExecutionTime = time.perf_counter() - s
        self.logger.info(f"Execution took {self.ExecutionTime:0.2f} seconds.")

    def ExtractDataFromZip(self, zipfileFullName, outputDirFullName, fileInZipFileToExtract):
        '''
        method for extracting the data, has to handle password encrypted files and folders.
        for performance reason the default python lib has been replaced with 7-zip
        '''
        if self.archive_password == "":
            command = f'{self.z7ZipPath} x \"{zipfileFullName}\" -o\"{outputDirFullName}\" \"{fileInZipFileToExtract}\" -y'
        else:
            command = f'{self.z7ZipPath} x \"{zipfileFullName}\" -o\"{outputDirFullName}\" -p{self.archive_password} \"{fileInZipFileToExtract}\" -y'
        # omit traces from 7-zip
        self.logger.debug(command)
        returnValue = subprocess.check_call(
            command, stdout=open(os.devnull, 'w'), shell=True)
        self.logger.debug(
            f"Extracting IC problem report contents from {zipfileFullName}, return value {returnValue}.")

    def mergeLogFiles(self, fileNamePrefix, pathToLogs, deleteFilesAfterMerge=False):
        '''
        :param fileNamePrefix: e.g syslog when syslog.1 ... have to be processed
        :param pathToLogs: relative or absolute path
        :param deleteFilesAfterMerge: boolean deletes original logs after the files being combined
        :return: None
        Note: The log files are being sorted by there names.
        The merged file will have the name defined in the prefix (e.g syslog)
        the original syslog will be renamed to syslog.0
        '''
        message = f"merging all {fileNamePrefix}s into one {fileNamePrefix}"
        if deleteFilesAfterMerge:
            self.logger.debug(f"{message} and removing the excess files")
        else:
            self.logger.debug(f"{message} and keeping the excess files")

        # rename the log file to simplify the sorting algo
        try:
            fullpathToLogs = os.path.join(self.outputFullPath, pathToLogs)
            if os.path.exists(os.path.join(fullpathToLogs, fileNamePrefix)):
                os.rename(os.path.join(fullpathToLogs, fileNamePrefix),
                          os.path.join(fullpathToLogs, f"{fileNamePrefix}.0"))
                filenames = [f for f in os.listdir(
                    fullpathToLogs) if re.match(f'{fileNamePrefix}\.\d+', f)]
                sortedFileName = sorted(filenames, key=lambda x: int(
                    x.split('.')[-1]), reverse=True)
                # merge the files into one log and optionally discard the old logs
                fileName = f"{self.problemReportName}_{fileNamePrefix}"
                fullFileName = os.path.join(fullpathToLogs, fileName)
                lines = []
                for names in sortedFileName:
                    with open(os.path.join(fullpathToLogs, names)) as infile:
                        lines.append(infile.read())
                with open(fullFileName, 'w') as outfile:
                    outfile.writelines(lines)

                if deleteFilesAfterMerge:
                    for logfile in sortedFileName:
                        os.remove(os.path.join(fullpathToLogs, logfile))
                first_row, last_row = self.glimpse(fullFileName, 1)
                return (os.path.join(pathToLogs, fileName), first_row, last_row)
            else:
                return (os.path.join(pathToLogs, fileNamePrefix), None, None)
        except:
            raise
            self.logger.debug(f'Unable to handle files with "{fileNamePrefix}", check log folder for suspicious files...')

    def glimpse(self, fullFileName, skipRows=0):
        # glimpse into syslogs to show the datetime at the beginning and ending of the file
        lines = []
        with open(fullFileName, "r") as file:
            for line in range(-1, skipRows, 1):
                nth_line = file.readline()
            for last_line in file:
                pass
        lines.append(nth_line)
        lines.append(last_line)
        # Extract date time information from the string
        return self.extractDateTimeFromStings(lines)

    def extractDateTimeFromStings(self, lines):
        dateTimeHandlers = [
            ('(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{0,6})','%Y-%m-%dT%H:%M:%S.%f'),
            ('(\w{3}\s+\d+\s\d{2}:\d{2}:\d{2}\sUTC\s\d{4})','%b %d %H:%M:%S UTC %Y')]
        results = []
        for line in lines:
            for dateTimeHandler in dateTimeHandlers:
                try:
                    matched = re.compile(
                        dateTimeHandler[0], re.VERBOSE).search(line)
                    if (matched is not None):
                        timeStamp = datetime.datetime.strptime(
                            matched.group(1), dateTimeHandler[1])
                        results.append(
                            {"TimeStamp": timeStamp, "LineContent": line})
                        break
                except Exception as e:
                    self.logger.exception(f"unable to parse date from line")
                    pass
        #check if both lines exist
        if(len(results)==0):
            results.append("")
        if(len(results)==1):
            results.append("")
        return (results[0], results[1])

    def toJSON(self):
        with open(os.path.join(self.outputFullPath, "metadata.json"), 'w') as metafile:
            metafile.write(json.dumps(self, default=self.json_default, sort_keys=True, indent=4))

    def json_default(self, value):
        # resolve circular, to logger is not needed in the matadata
        if isinstance(value, logging.Logger):
            return None
        if isinstance(value, datetime.datetime):
            return value.strftime("%Y-%m-%dT%H:%M:%S.%f")
        else:
            return value.__dict__

if __name__ == "__main__":

    PRs = process_data.FindFiles(rootdir='/home/rnd/notebooks/nas/05_Reliability/', fileNameMask=r'(.*PR-c5800-.*.zip)')    
    with open("PRList.json", 'w') as PRList:
        PRList.write(json.dumps(PRs, indent=4))

    output_directory='/media/rnd/Data/output'
    archive_password='TDFU@Bsting17'
    extractEventStreamData=True
    # This is not a pure multiprocessing but this gives a speedbump with more then 5 PRs
    with Pool(cpu_count() + 1) as pool:
        for r in pool.starmap(Extract, zip(PRs, repeat(output_directory), repeat(archive_password), repeat(extractEventStreamData))):
            pass
    freeze_support()
