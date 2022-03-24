import re, os, json

dataPatterns = [re.compile(r"""Roche.c5800.ProcessScheduler.RunScheduleChanged.*?RunState""", re.VERBOSE),
                re.compile(r"""Roche.Sting.InstrumentAccess.Messages.\S+.Events.""", re.VERBOSE),
                re.compile(r"""Roche.c5800.ProcessExecution.*?ContentChange.*?RfidData""", re.VERBOSE),
                re.compile(r"""Roche.c5800.ProcessExecution.WorkOrderFlagged""", re.VERBOSE)]

countersPattern = re.compile(r"""Roche.Sting.InstrumentAccess.Messages.(?P<UnitType>\w+).Events.Get_Packet_CountersCompleted\",\"body\":(?P<body>.*ModuleId\":"(?P<ModuleId>\w+).*)}""")

def ParseFile(fullFilePath):
    '''
    gets the matching regex patterns and keeps them in a list
    '''
    results = []
    with open(fullFilePath, mode='r', encoding="utf8") as f:
        for line in f:
            for dataPattern in dataPatterns:
                data = dataPattern.search(line)
                if data:
                    results.append(line)
                    break
    if(len(results)>0):
        return list(filter(None, results))
    else:
        return None
    
def ParseFolder(rootdir, fileFilter = r".*.log", relativeOutputFilePath = "ICRelevantEventStream.log"):
    '''
    writes the content of the extracted event stream into a output file.
    '''
    results = []
    counters = {}
    regex = re.compile(fileFilter)
    for path, _, files in os.walk(rootdir):
        for file in files:
            if regex.match(file):
                results_new = ParseFile(os.path.join(path,file))
                if not results_new is None :
                    results.extend(results_new)
    with open(os.path.join(rootdir, relativeOutputFilePath), 'w') as file:
        file.writelines(results)
    with open(os.path.join(rootdir, relativeOutputFilePath), 'r') as file:
            first_line = file.readline()
            for line in file:
                counter = countersPattern.search(line)
                if counter:
                    temp = counter.groupdict()
                    counters[temp["ModuleId"]] = json.loads(temp["body"])
    return (relativeOutputFilePath, first_line, line, counters)


if __name__ == '__main__':
    #For testing purposes only!
    #ParseFolder(f'C:/ProblemReportExtracts/PR-c5800-543-20210330_070015/eventstream')
    ParseFile("/home/rnd/notebooks/output/PR-c5800-518-20210119_162111/log/PR-c5800-518-20210119_162111_systemeventstream.log")

