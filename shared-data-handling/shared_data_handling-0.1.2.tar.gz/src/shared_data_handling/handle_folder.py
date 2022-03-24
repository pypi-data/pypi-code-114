from collections.abc import Sequence
from decimal import InvalidOperation
from xmlrpc.client import boolean
from psutil import cpu_count
from tqdm.contrib.concurrent import process_map  # or thread_map
import re, os, errno

from shared_data_handling.handle_file import Handle_File
from shared_data_handling.find_files import Find_Files

class Handle_Folder:
    def __init__(self,
    rootdir,
    regexPattern: Sequence,
    enableBeginMidEndPattern: boolean,
    fileNameMask = '(syslog.*)',
    firstMatchOnly = False) -> None:

        self.rootdir = rootdir
        self.regexPattern = regexPattern
        self.enableBeginMidEndPattern = enableBeginMidEndPattern
        self.fileNameMask = fileNameMask
        self.firstMatchOnly = firstMatchOnly

    def ParseFolder(self):
        '''
        Path to the syslogs, sub dirs will also be scanned
        '''
        if(not os.path.isdir(self.rootdir)):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.rootdir)
        if len(self.regexPattern) == 0:
            raise InvalidOperation(errno.ENOENT, os.strerror(errno.ENOENT), "At least one regex pattern must be passed as parameter")

        results = []
        self.files = Find_Files(self.rootdir, self.fileNameMask).FindFiles()
        results = process_map(self._HandleFiles, self.files, max_workers=cpu_count()+4)
        #remove the empty list entries
        return list(filter(None, results))

    def _HandleFiles(self, file):
        data = Handle_File(
            file,
            self.regexPattern,
            self.enableBeginMidEndPattern,
            self.firstMatchOnly)
        result = data.HandleBeginMidEndRegexPattern()
        if not result is None :
            return result