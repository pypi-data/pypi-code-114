import logging
from functools import wraps
from typing import Optional
import os

class log:
    """Log initiate a global lgging instance, and keep all runtime error in log file
    """
    def __init__(self, logPath:str='error.log', excInfo:bool=False, 
                       headLines:str='| Time                  | User                    | Level  | Messeage\n'+\
                                     '|-----------------------|-------------------------|--------|--------------------------------------------------\n'):
        """Construction setting for log instance

        :param logPath: File name (including path) of log file, defaults to 'error.log'
        :param excInfo: Set True/False to track/ignore stack frame information; set False when testing, defaults to False
        :param headLines: Headlines of log file, defaults to '| Time                  | User                    | Level  | Messeage\n'+\'|-----------------------|--------------------|--------|--------------------------------------------------\n'
        """

        self.logPath = logPath
        self.excInfo = excInfo # False for testing
                               # 
        self.headLines = headLines
        self.nHeadLines = len([_ for _ in self.headLines.split('\n') if _]) # line number of self.headLines
        

        if not os.path.isfile(self.logPath):
            with open(self.logPath, 'w') as log:
                log.write(self.headLines)
        # create 
        self.logger = logging.getLogger(self.logPath)
        self.logger.setLevel(logging.ERROR)

        if not self.logger.handlers:
            log_handler = logging.FileHandler(self.logPath)
            log_format = logging.Formatter('|{asctime}|{name:25s}|{levelname:8s}|{message}', style='{')
            log_handler.setFormatter(log_format)
            self.logger.addHandler(log_handler)
        # self.logging.basicConfig(filename=self.logPath,
        #                     filemode='a',
        #                     format='|{asctime}|{name:25s}|{levelname:8s}|{message}', style='{',
        #                     level=logging.ERROR)

    def readLog(self, skipLine:Optional[int]=None, skipChar:int=0) -> str:
        """Return content of log file but start from StartLine and skip first skipChar chars for each line.

        :param startLine: Start, defaults to self.nHeadLines 
        :param skipChar: _description_, defaults to 0
        :return: log file content
        """
        if skipLine is None: skipLine = self.nHeadLines # set default to self.nHeadLines
        with open(self.logPath, 'r') as rf:
            content = "".join([ line[skipChar:] for line in rf][skipLine:])
        return content
            
    def errlog(self, path:str='') -> callable(object):
        """Return a decorator which log exceptions when executing wrapped function 

        :param path: File name (including path) where decorated function locate , defaults to ''
        :return: wrapped function
        """
        def decorator(func):
            import inspect
            # to avoid RuntimeWarning: coroutine  was never awaited
            # so use inspect.iscoroutinefunction to check async function
            if inspect.iscoroutinefunction(func): 
                @wraps(func)
                async def wrapped(*args, **kwargs):
                    try: 
                        return await func(*args, **kwargs)
                    except Exception as e: self.logger.error(f"@{path}/{func.__name__}: {e}", exc_info=self.excInfo)
                return wrapped                
            else:
                @wraps(func)
                def wrapped(*args, **kwargs):
                    try: 
                        return func(*args, **kwargs)
                    except Exception as e: self.logger.error(f"@{path}/{func.__name__}: {e}", exc_info=self.excInfo)
                return wrapped
        return decorator