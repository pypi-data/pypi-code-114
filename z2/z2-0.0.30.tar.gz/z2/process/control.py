from __future__ import annotations
from multiprocessing import SimpleQueue as MSimpleQueue
from multiprocessing import Process as MProcess
from multiprocessing import Manager

try:
    # queue.SimpleQueue is only available in python >= (3, 7)
    from queue import SimpleQueue as TSimpleQueue

    USE_T_SIMPLEQUEUE = True
except ImportError:
    from queue import Queue as TQueue

    USE_T_SIMPLEQUEUE = False

from typing import Union, Text, Dict, Any, Tuple, List
from subprocess import Popen, PIPE, STDOUT
from queue import Empty as QueueEmpty
from threading import Timer, Thread
import tempfile
import signal
import shlex
import errno
import time
import sys
import os
import io

from z2.strings import C, Color
from loguru import logger
import loguru
import sh

from z2.utils import LogIt

ITERATIONS = 1500
MAX_CONCURRENCY_COUNT = 5
CONCURRENCY_MODE = ""

@logger.catch(default=True, onerror=lambda _: sys.exit(1))
def process_cmd_line(line, print_stdout, realtime, blocking_delay, debug=0):
    """Process cmd stdout and raise errors as required.  Valid lines are returned to the caller."""
    assert isinstance(line, str) or isinstance(line, int)
    assert isinstance(print_stdout, bool)
    assert isinstance(realtime, bool)
    assert isinstance(blocking_delay, float)
    assert isinstance(debug, int)
    assert (debug >= 0) and (debug <= 5)

    if line is None:
        raise ValueError("The value of line is None.  Not sure what happened.")

    # while line is not None:
    if isinstance(line, str):
        line = line.rstrip()
        if debug >= 1:
            LogIt().debug("stdout: '{}'".format(line))

        if print_stdout is True:
            print(line)

        return line


    elif line == errno.EWOULDBLOCK:
        if debug >= 2:
            LogIt().debug(
                    "Caught errno.EWOULDBLOCK, sleeping for {} seconds".format(
                        blocking_delay
                    ),
                )
        time.sleep(blocking_delay)
        return line

    elif isinstance(line, int):
        raise ValueError("Caught unknown errno: %s" % line)

    elif line is None:
        if debug >= 0:
            message = "UNKNOWN condition: line='%s'" % line
            LogIt().warning(message)
            raise ValueError(message)

    else:
        raise NotImplementedError()


@logger.catch(default=True, onerror=lambda _: sys.exit(1))
def zrun(
    cmd=None, err_to_out=False, bg=False, print_stdout=None, realtime=False, blocking_delay=0.001, debug=0
):
    # Default realtime to print to stdout...
    if print_stdout is None:
        print_stdout = realtime

    assert isinstance(cmd, str) or isinstance(cmd, list)
    assert isinstance(bg, bool)
    assert isinstance(err_to_out, bool)
    assert isinstance(print_stdout, bool)
    assert isinstance(realtime, bool)
    assert isinstance(blocking_delay, float)
    assert isinstance(debug, int)

    stdout_lines = list()
    if isinstance(cmd, str):
        cmd_parts = shlex.split(cmd)
    cmd_obj = sh.Command(cmd_parts[0])

    if realtime is True:
        if debug >= 1:
            LogIt().info(
                    "Run '{}' at debug={}, with streaming, realtime stdout".format(
                        cmd, debug
                    ),
                )
        # Run cmd with **streaming stdout** (i.e. _iter_noblock is True)
        for line in cmd_obj(
            cmd_parts[1:],
            _err_to_out=err_to_out,
            _bg=bg,
            _bg_exc=bg,
            _long_sep=" ",
            _iter_noblock=realtime,
        ):
            # If the cmd blocks stdout, briefly sleep and do something else...
            line = process_cmd_line(line, print_stdout, realtime, blocking_delay, debug)

            if isinstance(line, str):
                stdout_lines.append(line)
            yield line

    else:
        if debug >= 1:
            message = "Run '{}' at debug={}, with blocked stdout".format(cmd, debug)
            LogIt().info(message)
        # Run cmd with blocked stdout (i.e. _iter_noblock is False)
        for line in cmd_obj(
            cmd_parts[1:],
            _err_to_out=err_to_out,
            _bg=bg,
            _bg_exc=bg,
            _long_sep=" ",
            _iter_noblock=realtime,
        ).splitlines():

            #line = line.strip()
            line = process_cmd_line(line, print_stdout, realtime, blocking_delay, debug)

            #if debug >= 1:
            #    LogIt().debug("stdout: '{0}'".format(line))

            if isinstance(line, str):
                stdout_lines.append(line)
            yield line

    return stdout_lines


# Source -> https://stackoverflow.com/a/54775443/667301
@logger.catch(default=True, onerror=lambda _: sys.exit(1))
def iter_cmd_realtime(
    cmd: str = "",
    timeout: float = 0.0,
    shell: bool = True,
    encoding: str = "utf-8",
    debug: bool = 0,
) -> str:
    """Iterate over Popen() stdout lines in real-time with an optional timeout.
    This function sends stderr to stdout.

    Use this function if you want to handle output from a command
    as it happens.

    If timeout is non-zero kill this command after timeout seconds.

    Usage
    -----

    for line in iter_cmd_realtime('ping 192.0.2.1', 5.0):
        print(line)

    """
    if debug > 0:
        LogIt().info("Calling iter_cmd_realtime(cmd='{}')".format(cmd))
    timeout = float(timeout)
    assert isinstance(cmd, str) and str != ""
    assert isinstance(timeout, float) and (timeout >= 0.0)
    assert isinstance(shell, bool)
    assert isinstance(encoding, str)
    assert isinstance(debug, int)

    def kill_process_on_timeout(cmd, timeout, process, shell):
        # timer_thread.cancel()
        print(
            C.BRIGHT_RED
            + "Popen('{}') timed out after {} seconds".format(cmd, timeout)
            + C.ENDC
        )
        if shell is False:
            process.kill()
        else:
            pid = process.pid
            os.killpg(os.getpgid(pid), signal.SIGTERM)

    #
    os.environ["PYTHONUNBUFFERED"] = "1"
    # Combine STDOUT and STDERR into STDOUT...
    if shell is False:
        cmd = shlex.split(cmd)
    process = Popen(cmd, shell=shell, bufsize=0, stdout=PIPE, stderr=STDOUT)

    if timeout > 0.0:
        # Start a timer thread which will call kill_process_on_timeout()
        # if cmd runs too long...
        timer_thread = Timer(
            timeout,
            kill_process_on_timeout,
            args=(
                cmd,
                timeout,
                process,
                shell,
            ),
        )
        timer_thread.start()

    if debug > 0:
        LogIt().debug("Popen() done.  Yielding per-stdout line values")
    # yield cmd stdout until it runs to completion or hits the timeout...
    for stdout_line in iter(process.stdout.readline, b""):
        stdout_line = stdout_line.decode(encoding).rstrip()
        if debug > 0:
            LogIt().debug("    yield:{}".format(stdout_line))
        yield stdout_line

    process.stdout.close()
    retcode = process.wait()

    if timeout > 0.0:
        timer_thread.cancel()


@logger.catch(default=True, onerror=lambda _: sys.exit(1))
def run_cmd(
    # cmd takes a dictionary with a cmd key, or a string with a command in it
    cmd: str = None,
    cwd: str = os.getcwd(),
    colors: bool = False,
    debug: int = 0,
) -> tuple[str, str]:
    """run a shell command and return stdout / stderr strings

    To run a shell command, call like this...  a value in cwd is optional...

    ############
    # Call with a cmd string...
    ############
    cmd = "ls -la"
    stdout, stderr = run_cmd(cmd)
    """
    # ^ is a logical xor...
    #    -->   https://stackoverflow.com/a/432844/667301
    assert isinstance(cmd, str)
    assert sys.version_info >= (3, 6)  # Popen() encoding parameter requires 3.6

    if debug > 0:
        LogIt().info("Calling run_cmd(cmd='%s')".format(cmd))

    if debug > 1:
        LogIt().debug("Processing Popen() string cmd='{}'".format(cmd))
    assert cmd != ""
    assert cwd != ""
    cwd = os.path.expanduser(cwd)

    if debug > 1:
        LogIt().debug("Popen() started")

    process = Popen(
        shlex.split(cmd),
        shell=False,
        universal_newlines=True,
        cwd=cwd,
        stderr=PIPE,
        stdout=PIPE,
        # bufsize = 0  -> unbuffered
        # bufsize = 1  -> line buffered
        bufsize=0,
        # encoding parameter... https://stackoverflow.com/a/57970619/667301
        encoding="utf-8",
    )
    if debug > 1:
        LogIt().debug("Calling Popen().communicate()")
    stdout, stderr = process.communicate()
    if debug > 1:
        LogIt().debug("Popen().communicate() returned stdout=%s" % stdout)
    return (stdout, stderr)


@logger.catch(default=True, onerror=lambda _: sys.exit(1))
class WorkerObject:
    """This object is spawned under threading or multiprocessing as
    a python concurrency provider.  It accepts arguments for
    an input queue and an output queue.

    Messages are sent to and from this worker as python dictionaries.

    The worker object loops over qq_in and does something with any
    messages that are received.  The worker output is sent to the
    caller via qq_out.

    I tried to optimize this worker for speed... I've found that
    python stdlib SimpleQueue() instances are fastest to send
    and receive messages.
    """

    # FYI, python has a bug... A queue type is not available...
    #     https://bugs.python.org/issue33315
    # For now, I'm using Any until python supports the proper type annotation
    def __init__(
        self,
        qq_in: Any = None,
        qq_out: Any = None,
        debug: int = 0,
    ) -> None:
        assert CONCURRENCY_MODE == "threading" or CONCURRENCY_MODE == "multiprocessing"
        assert (qq_in is not None) and (qq_out is not None)
        assert isinstance(debug, int)

        self.debug = debug

        finished = False
        while not finished:

            msg = self.poll_queue_in(qq_in)
            assert isinstance(msg, dict)
            if debug > 0:
                LogIt().debug("WorkerObject() got msg: %s" % msg)

            msg_type = msg.get("msg_type")
            if msg_type == "shell_command":
                cmd = msg["cmd"]
                # Run the shell command and return results through qq_out...
                (stdout, stderr) = run_cmd(cmd=cmd)
                result_msg = {
                    "msg_type": "shell_command_result",
                    "stdout": stdout,
                    "stderr": stderr,
                    "cmd": msg.get("cmd"),
                }
                qq_out.put(result_msg)

            elif msg_type == "stop_processing":
                LogIt().info("WorkerObject() stopping")
                return None

            elif msg_type == "empty":
                pass

            else:
                raise NotImplementedError("Invalid msg_type: %s" % msg_type)

    # FYI, python has a bug... the typing module doesn't have a queue type...
    #     https://bugs.python.org/issue33315
    # For now, I'm using Any until python supports the proper type annotation
    def poll_queue_in(self, qq_in: Any = None) -> dict[str, str]:
        """
        Poll the input queue for messages.  When poll_queue_in() gets a
        message
        """

        msg = {"msg_type": "empty"}
        try:
            if CONCURRENCY_MODE == "threading" and USE_T_SIMPLEQUEUE is False:
                # PIZZA msg = qq_in.get(block=Q_BLOCKING)
                msg = qq_in.get(block=Q_BLOCKING)
            else:
                # Using SimpleQueue() which doesnt like the block keyword
                msg = qq_in.get()

            if self.debug > 0:
                LogIt().debug("qq_in delivered msg=%s" % msg)
            msg = self.format_msg(msg)

        except QueueEmpty:
            pass

        return msg

    def format_msg(self, msg: dict[str, str] = None) -> dict[str, str]:
        assert isinstance(msg, dict)

        return_msg = dict()
        msg_type = msg.get("msg_type", "empty")

        if msg_type == "empty":
            # Default to an empty message if there's nothing in qq_in..
            return_msg = {"msg_type": msg_type}

        elif msg_type == "shell_command":
            cmd = msg.get("cmd", "")
            split_cmd = shlex.split(cmd)
            cwd = os.path.expanduser(msg.get("cwd", "."))
            return_msg = {
                "msg_type": msg_type,
                "cmd": cmd,
                "split_cmd": split_cmd,
                "cwd": cwd,
            }

        elif msg_type == "stop_processing":
            return_msg = {"msg_type": msg_type}

        else:
            raise NotImplementedError("msg_type: '%s' is not supported" % msg_type)

        return return_msg

    def get_stdin_lines(self) -> list[str]:

        # Do something manually with stdin_lines before run_cmd()...
        stdin_lines = list()
        for line in sys.stdin.read().splitlines():
            stdin_lines.append(line.rstrip())
        return stdin_lines


@logger.catch(default=True, onerror=lambda _: sys.exit(1))
def spawn_workers(
    qq_in: Any = None,
    qq_out: Any = None,
    num_workers: int = 0,
    debug: int = 0,
) -> list:
    global CONCURRENCY_MODE

    assert (qq_in is not None) and (qq_out is not None)
    assert CONCURRENCY_MODE == "threading" or CONCURRENCY_MODE == "multiprocessing"
    assert isinstance(num_workers, int) and num_workers >= 1
    assert isinstance(debug, int)

    all_procs = list()
    # Spawn off workers to read from qq_in and return work in qq_out...
    for idx in range(0, num_workers):
        if CONCURRENCY_MODE == "threading":
            name = "Thread-%s" % str(idx).zfill(3)
            process_thread = Thread(
                target=WorkerObject,
                name=name,
                args=(
                    qq_in,
                    qq_out,
                    debug,
                ),
            )
            # If it's a daemon, it dies with the rest of the script... leave daemon = True
            # process_thread.daemon = True
            process_thread.start()
            all_procs.append(process_thread)

        elif CONCURRENCY_MODE == "multiprocessing":
            name = "Process-%s" % str(idx).zfill(3)
            process_mp = MProcess(
                target=WorkerObject, name=name, args=(qq_in, qq_out, debug)
            )
            # If it's a daemon, it dies with the rest of the script... leave daemon = True
            # process_mp.daemon = True
            process_mp.start()
            all_procs.append(process_mp)

        else:
            raise NotImplementedError("Invalid CONCURRENCY_MODE: %s" % CONCURRENCY_MODE)

        return all_procs


@logger.catch(default=True, onerror=lambda _: sys.exit(1))
def send_receive_work(cmd="", num_workers=MAX_CONCURRENCY_COUNT, debug=0):
    """Build queues, send work, poll for output, return to the caller"""

    global Q_BLOCKING
    global CONCURRENCY_MODE

    if CONCURRENCY_MODE == "threading":
        if USE_T_SIMPLEQUEUE is False:  # SimpleQueue requires 3.7
            qq_in = TQueue()
            qq_out = TQueue()
        else:
            # SimpleQueue() is much faster in my tests...
            qq_in = TSimpleQueue()
            qq_out = TSimpleQueue()
        # my tests show that threading is faster
        # with Queue().get(block=True)
        Q_BLOCKING = True

    elif CONCURRENCY_MODE == "multiprocessing":
        qq_in = MSimpleQueue()
        qq_out = MSimpleQueue()
        # with Queue().get(block=False)
        Q_BLOCKING = True

    else:
        raise NotImplementedError("CONCURRENCY_MODE=%s" % CONCURRENCY_MODE)

    all_procs = list()
    num_workers = min(ITERATIONS, MAX_CONCURRENCY_COUNT)
    all_procs = spawn_workers(
        qq_in=qq_in,
        qq_out=qq_out,
        num_workers=num_workers,
    )

    # qq_in.put({"msg_type": "shell_command", "cmd": "ls -la",})
    # qq_in.put({"msg_type": "stop_processing"})

    num_cmds = 0
    all_results = list()
    cwd = os.path.expanduser(".")
    finished = False
    while finished is False:

        # Build a msg dictionary with the requested shell command...
        if num_cmds < ITERATIONS:
            input_msg = {"msg_type": "shell_command", "cmd": cmd, "cwd": cwd}
            qq_in.put(input_msg)
            num_cmds += 1

        # Poll the output queue for returned values...
        # Keep the default value outside of try / except for Queue().get()...
        output_msg = {}
        try:
            if (CONCURRENCY_MODE == "threading") and (USE_T_SIMPLEQUEUE is False):
                output_msg = qq_out.get(block=Q_BLOCKING)
            else:
                # SimpleQueue() doesn't like the block keyword...
                output_msg = qq_out.get()

            msg_keys = output_msg.keys()
            assert "stdout" in msg_keys
            assert "stderr" in msg_keys
            assert output_msg["stdout"] != "" or output_msg["stderr"] != ""
            all_results.append(output_msg)

        except QueueEmpty:
            pass

        if len(all_results) == ITERATIONS:
            # Tell all workers to exit...
            if debug > 0:
                LogIt().info("Sending 'stop_processing' message to all workers")
            for ii in range(0, num_workers):
                msg = {"msg_type": "stop_processing"}
                qq_in.put(msg)

            finished = True

    return all_results


def main():
    # Run a command with threading or multiprocessing...
    start_time = time.time()
    global CONCURRENCY_MODE
    CONCURRENCY_MODE = "multiprocessing"
    # all_results = run_cmd(cmd="ls -la", concurrency=ccc, concurrency_count=5)

    all_results = send_receive_work(cmd="ls -la", num_workers=5, debug=2)

    duration = time.time() - start_time
    ops_per_second = round(float(ITERATIONS) / duration, 4)
    print(
        C.YELLOW
        + "{} OPS per second {}".format(CONCURRENCY_MODE, ops_per_second)
        + C.ENDC
    )


if __name__ == "__main__":
    foo()
    main()
    # stdout, stderr = run_cmd(cmd={"cmd": "uptime", "cwd": "/tmp"})
    # print(stdout)

    # for line in iter_cmd_realtime(cmd="ping 4.2.2.2", timeout=2):
    #    print("LINE", line)
