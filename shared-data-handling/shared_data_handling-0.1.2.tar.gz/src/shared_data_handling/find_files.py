from fileinput import filename
import re, os

class Find_Files:
    def __init__(
        self,
        rootdir,
        fileNameMask = '(syslog.*)') -> None:
        self.fileNameMask = fileNameMask
        self.rootdir = rootdir

    def FindFiles(self):
        pattern = re.compile(self.fileNameMask)
        matches = []
        for root, dirnames, filenames in os.walk(self.rootdir):
            for filename in filter(lambda name:pattern.match(name),filenames):
                matches.append(os.path.join(root, filename))
        return matches