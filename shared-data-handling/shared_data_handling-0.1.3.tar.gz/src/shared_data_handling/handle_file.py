from collections.abc import Sequence
from tqdm import tqdm
import re, os, errno

class Handle_File:
    def __init__(
        self,
        pathToFile: str,
        regexPattern: Sequence,
        enableBeginMidEndPattern = False,
        firstMatchOnly = False):
        
        self.pathToFile = pathToFile
        self.regexPattern = regexPattern
        self.enableBeginMidEndPattern = enableBeginMidEndPattern
        self.firstMatchOnly = firstMatchOnly
        self.HandleBeginMidEndRegexPattern()

    def HandleBeginMidEndRegexPattern(self):

        if(not os.path.isfile(self.pathToFile)):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.rootdir)

        if len(self.regexPattern) == 0:
            raise os.error(errno.ENOENT, os.strerror(errno.ENOENT), "At least one regex pattern must be passed as parameter")
        #determine the internal function call
        results = []
        if len(self.regexPattern) > 0 and not self.enableBeginMidEndPattern:
            return self.ParseFileRegexPatternList(self.regexPattern)
        if len(self.regexPattern) > 1 and len(self.regexPattern) < 3:
            return self.ParseFileBeginMidEndRegexPattern(beginRegex=self.regexPattern[0], midRegexes=[], endRegex=self.regexPattern[-1])
        if len(self.regexPattern) > 2 and self.enableBeginMidEndPattern:
            return self.ParseFileBeginMidEndRegexPattern(beginRegex=self.regexPattern[0], midRegexes=self.regexPattern[1:len(self.regexPattern)-1], endRegex=self.regexPattern[-1])
    
    def ParseFileBeginMidEndRegexPattern(self, beginRegex, midRegexes, endRegex):
        beginFound = False
        results = []
        result = {}
    
        with open(self.pathToFile, 'r') as f:
            for line in f:
                begin = beginRegex.search(line)
                if not begin is None:
                    beginFound = True
                    result['file'] = self.pathToFile
                    result.update(begin.groupdict())
                    midRegexIndex = 0
                    continue
                if beginFound:
                    midFound = False
                    for midRegex in midRegexes:
                        tempvalue = midRegex.search(line)
                        if not tempvalue is None:
                            midFound = True
                            for t in tempvalue.groupdict():
                                result[f"{t}_{midRegexIndex}"] = tempvalue.groupdict()[t]
                            midRegexIndex += 1
                            break
                    if midFound:
                        continue
                    end = endRegex.search(line)
                    if not end is None:
                        beginFound = False
                        result.update(end.groupdict())
                        results.append(result)
                        result = {}
                        midRegexIndex = 0
                        if self.firstMatchOnly:
                            break
        return results

    def ParseFileRegexPatternList(self, regexPatternList):
        results = []
        with open(self.pathToFile, 'r') as f:
            for line in f:
                for regexPattern in regexPatternList:
                    data = regexPattern.search(line)
                    if not data is None:
                        result = {}
                        result['file'] = self.pathToFile
                        result.update(data.groupdict())
                        results.append(result)
                        break
                if self.firstMatchOnly and len(results) == len(regexPatternList):
                    break
        return results