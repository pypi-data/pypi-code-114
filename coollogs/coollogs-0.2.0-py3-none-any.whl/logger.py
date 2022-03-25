"""Main source code for ``coollogs`` package. Visit github repository
for more information:
https://github.com/LeKSuS-04/Cool-logs
"""

import time


class Colors:
    """Console stylization constants"""    
    class style:
        """Different styles for text"""
        RESET         = '\033[0m'
        BOLD          = '\033[01m'
        DISABLE       = '\033[02m'
        UNDERLINE     = '\033[04m'
        REVERSE       = '\033[07m'
        STRIKETHROUGH = '\033[09m'
        INVISIBLE     = '\033[08m'
    class fg:
        """Foreground colors for text"""
        BLACK         = '\033[30m'
        RED           = '\033[31m'
        GREEN         = '\033[32m'
        ORANGE        = '\033[33m'
        BLUE          = '\033[34m'
        PURPLE        = '\033[35m'
        CYAN          = '\033[36m'
        LIGHTGRAY     = '\033[37m'
        DARKGRAY      = '\033[90m'
        LIGHTRED      = '\033[91m'
        LIGHTGREEN    = '\033[92m'
        YELLOW        = '\033[93m'
        LIGHTBLUE     = '\033[94m'
        PINK          = '\033[95m'
        LIGHTCYAN     = '\033[96m'
    class bg:
        """Background colors for text"""
        BLACK         = '\033[40m'
        RED           = '\033[41m'
        GREEN         = '\033[42m'
        ORANGE        = '\033[43m'
        BLUE          = '\033[44m'
        PURPLE        = '\033[45m'
        CYAN          = '\033[46m'
        LIGHTGRAY     = '\033[47m'


class log_level:
    """Avaliable log levels for logger"""
    CRITICAL = 1
    ERROR    = 2
    WARNING  = 4
    INFO     = 8
    DEBUG    = 16
    ALL      = 31

class Logger():
    """Beautifies console printing"""
    def __init__(self, colorful: bool = True, log_level: int = log_level.ALL, 
                    label_size: int = 9, time_color: Colors = Colors.fg.CYAN):
        """Initializes ``Logger`` object with some settings

        Args:
            colorful (bool, optional): specifies if colors need to be
                applied to logger. Is useful when terminal doesn't
                support colors. Defaults to True.
            log_level (int, optional): Log levels to show by default. 
                Defaults to log_level.ALL.
            label_size (int, optional): Size of information label of logger.
                Defaults to 9.
            time_color (Colors, optional): Color of time block of logger.
                Defaults to Colors.fg.CYAN.
        """        
        self._colorful = colorful
        self._label_size = label_size
        self._time_color = time_color
        self._log_level = log_level

    def _get_time(self):
        return '[' + time.strftime("%H:%M:%S", time.localtime()) + ']'

    def _get_label(self, label_name):
        length = self._label_size

        if len(label_name) >= length:
            prefix = '['
            postfix = ']'
            label_name = label_name[:length]
        else:
            prefix = '[' + ' ' * ((length + 1- len(label_name)) // 2)
            postfix = ' ' * ((length - len(label_name)) // 2) + ']'

        return prefix + label_name + postfix

    def set_level(self, log_level: int):
        """Sets logging level of this logger. Logging level is
        represented by integer, where each bit shows whether or not
        this level needs to be shown:
            1: CRITICAL
            2: ERROR
            4: WARNING
            8: INFO
            16: DEBUG
            31: ALL

        You can use log_level class with pre-defined constants or pass
        integer to specify custom rules
        """
        self._log_level = log_level

    def custom(self, *data, label_name: str = '', label_color: Colors = Colors.fg.CYAN):
        """Logs data with custom label. Logging format is as follows:
            $ [TIME] [LABEL] data
        
        Arguments:
            label_name (str): string that is displayed on label.
                Defaults to empty string.
            label_color (Colors): style of label. Can be sum of
                multiple Colors instances. Defaults to Colors.fg.CYAN.
        """
        if self._colorful:
            time_color = self._time_color + Colors.style.BOLD
            label_color = label_color + Colors.style.BOLD
            reset = Colors.style.RESET
        else:
            time_color = label_color = reset = ''

        time = time_color + self._get_time() + reset

        label = label_color + self._get_label(label_name) + reset
        text = f'{" ".join([str(x) for x in data])}'

        print(f'{time} {label} {text}')
        
    def critical(self, *data):
        """Logs data with ``critical`` label"""
        if self._log_level & (1 << 0):
            self.custom(*data, label_name='CRITICAL', label_color=Colors.bg.RED)

    def error(self, *data):
        """Logs data with ``error`` label"""
        if self._log_level & (1 << 1):
            self.custom(*data, label_name='ERROR', label_color=Colors.fg.RED)

    def warning(self, *data):
        """Logs data with ``warning`` label"""
        if self._log_level & (1 << 2):
            self.custom(*data, label_name='WARNING', label_color=Colors.fg.ORANGE)

    def info(self, *data):
        """Logs data with ``info`` label"""
        if self._log_level & (1 << 3):
            self.custom(*data, label_name='INFO', label_color=Colors.fg.CYAN)

    def debug(self, *data):
        """Logs data with ``debug`` label"""
        if self._log_level & (1 << 4):
            self.custom(*data, label_name='DEBUG', label_color=Colors.fg.PURPLE)

    def plus(self, *data):
        """Logs data with ``plus`` label"""
        self.custom(*data, label_name='+', label_color=Colors.fg.GREEN)

    def minus(self, *data):
        """Logs data with ``minus`` label"""
        self.custom(*data, label_name='-', label_color=Colors.fg.RED)
    
    def success(self, *data):
        """Logs data with ``success`` label"""
        self.custom(*data, label_name='SUCCESS', label_color=Colors.fg.GREEN)

    def failure(self, *data):
        """Logs data with ``failure`` label"""
        self.custom(*data, label_name='FAILURE', label_color=Colors.fg.RED)

    def demo(self):
        """Shows all possible logging levels"""
        self.critical('This is .critical()')
        self.error('This is .error()')
        self.warning('This is .warning()')
        self.info('This is .info()')
        self.debug('This is .debug()')
        print()
        self.plus('This is .plus()')
        self.minus('This is .minus()')
        print()
        self.success('This is .success()')
        self.failure('This is .failure()')
        print()
        self.custom('This is custom one, with labelcolor = Colors.fg.ORANGE', label_name='CUSTOM #1', label_color=Colors.fg.ORANGE)
        self.custom('This is custom one, with labelcolor = Colors.bg.PURPLE', label_name='CUSTOM #2', label_color=Colors.bg.PURPLE)
        self.custom('This is custom one, with labelcolor = Colors.fg.BLACK + Colors.bg.ORANGE', label_name='CUSTOM #3', label_color=Colors.fg.BLACK + Colors.bg.ORANGE)


if __name__ == '__main__':
    log = Logger()
    log.demo()