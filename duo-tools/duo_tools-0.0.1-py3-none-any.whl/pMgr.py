import os
import time
import subprocess
import logging
import signal
os.environ['QHOME'] = '/home/chenduo/miniconda3/q'


class pMgr:
    """
    process manager
    """

    def __init__(self,
                 file='',
                 project='',
                 set_logger=True,
                 q_bin='/home/chenduo/miniconda3/bin/q',
                 py_bin='/home/chenduo/miniconda3/envs/bitmexd/bin/python3'):
        self.project = project
        self.q_bin = q_bin
        self.py_bin = py_bin
        self.file = file
        self.log_file = ''
        self.set_logger = set_logger
        if file and set_logger:
            self.set_log()

    def start_q(self, full_path, port=0, s=8):
        if self.log_file:
            with open(self.log_file, 'a') as f:
                if port == 0:
                    return subprocess.Popen(['taskset', '-c', '0-15', self.q_bin, full_path, '-p', '0W', '-s', str(s), '-q'], stderr=f)
                return subprocess.Popen(['taskset', '-c', '0-15', self.q_bin, full_path, '-p', str(port), '-s', str(s), '-q'], stderr=f)
        if port == 0:
            return subprocess.Popen(['taskset', '-c', '0-15', self.q_bin, full_path, '-p', '0W', '-s', str(s), '-q'])
        return subprocess.Popen(['taskset', '-c', '0-15', self.q_bin, full_path, '-p', str(port), '-s', str(s), '-q'])

    def start_current_q(self, file_name, port=0, s=8, file=''):
        """
        file = __file__
        """
        file = file if file else self.file
        if self.file and self.set_logger:
            logging.info(f'{file_name} starts on {port}')
        full_path = os.path.join(os.path.dirname(file), file_name)
        return self.start_q(full_path, port, s)

    def start_py(self, full_path):
        if self.log_file:
            with open(self.log_file, 'a') as f:
                return subprocess.Popen([self.py_bin, full_path], stderr=f)
        return subprocess.Popen([self.py_bin, full_path])

    def start_current_py(self, file_name, file=''):
        """
        file = __file__
        """
        file = file if file else self.file
        if self.file and self.set_logger:
            logging.info(f'{file_name} starts')
        full_path = os.path.join(os.path.dirname(file), file_name)
        return self.start_py(full_path)

    def stop(self, regex):
        stop_cmd = f"ps aux|grep -v grep|grep {regex}|awk -F ' ' '{{print $2}}'|xargs kill -9"
        if self.project:
            stop_cmd = f"ps aux|grep -v grep|grep {self.project}|grep {regex}|awk -F ' ' '{{print $2}}'|xargs kill -9"
        return subprocess.run(stop_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def stop_current(self, file_name, file=''):
        """
        file = __file__
        """
        file = file if file else self.file
        if self.file and self.set_logger:
            logging.info(f'{file_name} stops')
        full_path = os.path.join(os.path.dirname(file), file_name)
        stop_cmd = f"ps aux|grep -v grep|grep -F {full_path}|awk -F ' ' '{{print $2}}'|xargs kill -9"
        subprocess.run(stop_cmd, shell=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)

    def stop_port(self, port):
        """
        file = __file__
        """
        if self.file and self.set_logger:
            logging.info(f'port : {port} stops')
        stop_cmd = f"fuser -k {port}/tcp"
        subprocess.run(stop_cmd, shell=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)

    def set_log(self, file=''):
        """
        file = __file__
        """
        file = file if file else self.file
        dirname, basename = os.path.split(file)
        log_dir = os.path.join(dirname, 'log')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.log_file = os.path.join(
            log_dir, os.path.splitext(basename)[0] + '.log')
        logging.basicConfig(level=logging.INFO,
                            filename=self.log_file,
                            format='%(asctime)s : %(levelname)s : %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    def set_logging(self, file=''):
        """
        name compatible
        """
        self.set_log(file)

    def restart_current_py(self, file_name, file='', sleep_sec=0):
        time.sleep(sleep_sec)
        self.stop_current(file_name, file)
        return self.start_current_py(file_name, file)

    def restart_current_q(self, file_name, port=0, s=2, file='', sleep_sec=0):
        time.sleep(sleep_sec)
        if type(port) == int and port != 0:
            self.stop_port(port)
        else:
            self.stop_current(file_name, file)
        return self.start_current_q(file_name, port, s, file)

    def restart_current(self, file_name, port=0, s=2, file='', sleep_sec=0):
        _, ext = os.path.splitext(file_name)
        if ext == '.q':
            return self.restart_current_q(file_name, port, s, file, sleep_sec)
        if ext == '.py':
            return self.restart_current_py(file_name, file, sleep_sec)

    def start_current(self, file_name, port=0, s=2, file=''):
        _, ext = os.path.splitext(file_name)
        if ext == '.q':
            return self.start_current_q(file_name, port, s, file)
        if ext == '.py':
            return self.start_current_py(file_name, file)

    def get_current_logger(self, name='', file=''):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        file = file if file else self.file
        dirname, basename = os.path.split(file)
        log_file = os.path.join(
            dirname, 'log', os.path.splitext(basename)[0] + '.log')
        # set file handle
        fh = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        logger.handlers = [fh]
        return logger

    @staticmethod
    def info(info):
        logging.info(info)

    @staticmethod
    def get_pid(regex):
        pid_cmd = f"ps aux|grep -v grep|grep -F {regex}|awk -F ' ' '{{print $2}}'"
        response = subprocess.run(
            pid_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        return [int(i) for i in response.stdout.decode("utf-8").split('\n')[:-1]]

    def get_current_file_pid(self):
        return pMgr.get_pid(self.file)

    @staticmethod
    def kill_pid(pid):
        os.kill(pid, signal.SIGKILL)

    @staticmethod
    def get_current_pid():
        return os.getpid()

    def restart_current_file(self):
        current_pid = pMgr.get_current_pid()
        pids = self.get_current_file_pid()
        for pid in pids:
            if pid != current_pid:
                pMgr.kill_pid(pid)
