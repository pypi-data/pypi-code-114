from tabnanny import verbose
from tqdm import tqdm
import re, os, errno

def FindFiles(
    rootdir,
    fileNameMask = '(syslog.*)'):
    pattern = re.compile(fileNameMask)
    matches = []
    for root, dirnames, filenames in os.walk(rootdir):
       for filename in filter(lambda name:pattern.match(name),filenames):
           matches.append(os.path.join(root, filename))
    return matches

def ParseFolderRegexPatternList(
    rootdir,
    regexPatternAsVerboseStringList = [r""" """, r""" """],
    fileNameMask = '(syslog.*)',
    firstMatchOnly = False):

    results = []

    files_pbar = tqdm(FindFiles(rootdir, fileNameMask))
    for file in files_pbar:
        files_pbar.set_description(f"Processing {file}")
        data = ParseFileRegexPatternList(
            file, 
            regexPatternAsVerboseStringList,
            firstMatchOnly=firstMatchOnly)
        if not data is None :
            results.extend(data)
    return results

def ParseFolder(rootdir, 
    regexPatternAsVerboseString = r""" """,
    fileNameMask = '(syslog.*)',
    firstMatchOnly = False,
    verboseTracing = False):
    '''
    Path to the syslogs, sub dirs will also be scanned
    '''
    if(not os.path.isdir(rootdir)):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), rootdir)

    results = []
    files_pbar = tqdm(FindFiles(rootdir, fileNameMask))
    for file in files_pbar:
        files_pbar.set_description(f"Processing {file}")
        data = ParseFileSingleRegexPattern(
            file, 
            regexPatternAsVerboseString,
            firstMatchOnly=firstMatchOnly,
            verboseTracing=verboseTracing)
        if not data is None :
            results.extend(data)
    return results
    #return sorted(results, key=lambda x: datetime.datetime.strptime(x['DateTime'], '%Y-%m-%dT%H:%M:%S'))

def ParseFolderBeginMidEndRegexPattern(
    rootdir = ".",
    regexPatternAsVerboseStringBegin = r"""""",
    regexPatternAsVerboseListMiddle = [r"""""",r""""""],
    regexPatternAsVerboseStringEnd = r"""""",
    fileNameMask = '(syslog.*)',
    firstMatchOnly = False,
    verboseTracing = False):

    results = []
    files_pbar = tqdm(FindFiles(rootdir, fileNameMask))
    for file in files_pbar:
        files_pbar.set_description(f"Processing {file}")
        data = ParseFileBeginMidEndRegexPattern(
            file,
            regexPatternAsVerboseStringBegin,
            regexPatternAsVerboseListMiddle,
            regexPatternAsVerboseStringEnd,
            firstMatchOnly=firstMatchOnly,
            verboseTracing = verboseTracing)
        if not data is None :
            results.extend(data)
    return results



def ParseFileRegexPatternList(
    fullFilePath, 
    regexPatternAsVerboseStringList,
    firstMatchOnly = False, 
    completeOnlyLine = False,
    verboseTracing = False):
    '''
    fullFilePath path to a syslog containing the STVolumeCheck data to be analyzed
    clearData: clears the before collecting the data
    '''
    results = []
    with open(fullFilePath, 'r') as f:
        for line in f:
            for regexPatternAsString in regexPatternAsVerboseStringList:
                regexPattern = re.compile(regexPatternAsString, re.VERBOSE)
                data = regexPattern.search(line)
                if not data is None:
                    if completeOnlyLine:
                        result = data.string
                    else:
                        result = {}
                        result['file'] = fullFilePath
                        result.update(data.groupdict())
                    results.append(result)
                    break
            if firstMatchOnly and len(results) == len(regexPatternAsVerboseStringList):
                break
    if(len(results)>0):
        #print(f"Source: {fullFilePath} result length {len(results)}")
        return results
    else:
        #print(f"Source: {fullFilePath}, no data found") 
        return None

def ParseFileSingleRegexPattern(
    fullFilePath, 
    regexPatternAsVerboseString,
    firstMatchOnly = False,
    verboseTracing = False):
    '''
    fullFilePath path to a syslog containing the STVolumeCheck data to be analyzed
    clearData: clears the before collecting the data
    '''
    results = []
    result = {}
    regexPattern = re.compile(regexPatternAsVerboseString, re.VERBOSE)
    with open(fullFilePath, 'r') as f:
        for line in f:
            begin = regexPattern.search(line)
            if not begin is None:
                result['file'] = fullFilePath
#                result['pattern'] = regexPatternAsVerboseString
                result.update(begin.groupdict())
                results.append(result)
                result = {}
                if firstMatchOnly:
                    break
    if(verboseTracing):
        if(len(results)>0):
            print(f"Source: {fullFilePath} result length {len(results)}")
        else:
           print(f"Source: {fullFilePath}, no data found")
    return results

def ParseFileBeginMidEndRegexPattern(
    fullFilePath,
    regexPatternAsVerboseStringBegin,
    regexPatternAsVerboseListMiddle,
    regexPatternAsVerboseStringEnd,
    firstMatchOnly = False,
    verboseTracing = False):
    '''
    fullFilePath path to a syslog containing the STVolumeCheck data to be analyzed
    clearData: clears the before collecting the data
    '''
    beginRegex = re.compile(regexPatternAsVerboseStringBegin, re.VERBOSE)
    midRegexes = [re.compile(midRegex, re.VERBOSE) for midRegex in regexPatternAsVerboseListMiddle]
    endRegex = re.compile(regexPatternAsVerboseStringEnd, re.VERBOSE)

    beginFound = False
    results = []
    result = {}
   
    with open(fullFilePath, 'r') as f:
        for line in f:
            begin = beginRegex.search(line)
            if not begin is None:
                beginFound = True
                if verboseTracing:
                    print(f"Begin found {line}")
                result['file'] = fullFilePath
                result.update(begin.groupdict())
                midRegexIndex = 0
                continue
            if beginFound:
                midFound = False
                for midRegex in midRegexes:
                    tempvalue = midRegex.search(line)
                    if not tempvalue is None:
                        midFound = True
                        if verboseTracing:
                            print(f"Mid {midRegexIndex} found {line}")
                        for t in tempvalue.groupdict():
                            result[f"{t}_{midRegexIndex}"] = tempvalue.groupdict()[t]
                        midRegexIndex += 1
                        break
                if midFound:
                    continue
                end = endRegex.search(line)
                if not end is None:
                    if verboseTracing:
                        print(f"End found {line}")
                    beginFound = False
                    result.update(end.groupdict())
                    if verboseTracing:
                        print(f"{result}")
                    results.append(result)
                    result = {}
                    midRegexIndex = 0
                    if firstMatchOnly:
                        break
    if(verboseTracing):
        if(len(results)>0):
            print(f"Source: {fullFilePath} result length {len(results)}")
        else:
           print(f"Source: {fullFilePath}, no data found")
    return results