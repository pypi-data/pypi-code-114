import atexit
import errno
import fcntl
import itertools
import pickle
import resource
import signal
import struct
import sys
import os
import os.path
import warnings


class Daemonize(object):
    def __init__(
            self, target, /, *, args=None, kwargs=None, pidfile=None,
            fds_to_keep=None
    ):
        if pidfile is None:
            raise TypeError("pidfile must be specified")
        self._target = target
        self._target_args = args if args else ()
        self._target_kwargs = kwargs if args else {}
        self._pidfilepath = pidfile
        self._fds_to_keep = set(fds_to_keep) if fds_to_keep else set()
        self._pidfile_fd = None

    def _cleanup_pidfile(self):
        if self._pidfile_fd is not None:
            os.unlink(self._pidfilepath)
            os.close(self._pidfile_fd)
            self._pidfile_fd = None

    def start(self):
        def iter_over_fds_ranges_to_close(fds_to_keep, maxfd, /):
            if len(fds_to_keep) == 0:
                yield (0, maxfd)
                return
            fds_to_keep = sorted(fds_to_keep)
            a, b = iter(fds_to_keep), iter(fds_to_keep)
            next(b, None)
            yield from itertools.chain(
                ((0, fds_to_keep[0]), ),
                zip((e + 1 for e in a), b),
                ((fds_to_keep[-1] + 1, maxfd), )
            )
        def iter_over_fds_to_close(fds_to_keep, maxfd, /):
            for x, y in iter_over_fds_ranges_to_close(fds_to_keep, maxfd):
                yield from range(x, y)

        # Close all opened file descriptors but stderr and the provided file
        # descriptors to keep
        maxfd = resource.getrlimit(resource.RLIMIT_NOFILE)[0]
        if maxfd is resource.RLIM_INFINITY:
            maxfd = os.sysconf(os.sysconf_names("OPEN_MAX"))
            if maxfd == -1:
                raise Exception()
        fds_to_keep = set(self._fds_to_keep)
        fds_to_keep.add(sys.__stdin__.fileno())
        fds_to_keep.add(sys.__stdout__.fileno())
        fds_to_keep.add(sys.__stderr__.fileno())
        for fd in iter_over_fds_to_close(fds_to_keep, maxfd):
            try:
                os.close(fd)
            except OSError as exc:
                if exc.errno != errno.EBADF:
                    print(
                        "Error: Couldn't close fd {:d}: {:s}"
                        .format(fd, exc.strerror),
                        file=sys.stderr
                    )
                    sys.exit(1)

        # Reset signals handlers
        for sig in range(1, signal.NSIG):
            try:
                signal.signal(sig, signal.SIG_DFL)
            except OSError as exc:
                if exc.errno != errno.EINVAL:
                    print(
                        "Error: Couldn't reset handler for signal {:d}: {:s}"
                        .format(sig, exc.strerror),
                        file=sys.stderr
                    )
                    sys.exit(1)

        # Reset blocked signals mask
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore", category=RuntimeWarning, module="signal"
            )
            signal.pthread_sigmask(signal.SIG_UNBLOCK, range(1, signal.NSIG))

        # Create an unamed pipe so the daemon process (grand-child) and
        # the current process can communicate
        try:
            pr, pw = os.pipe()
        except OSError as exc:
            print(
                "Error: Couldn't create an unamed pipe: {:s}"
                .format(exc.strerror),
                file=sys.stderr
            )
            sys.exit(1)

        # Fork the parent
        try:
            child_pid = os.fork()
        except OSError as exc:
            print(
                "Error: Couldn't fork the parent process: {:s}"
                .format(exc.strerror),
                file=sys.stderr
            )
            sys.exit(1)

        if child_pid != 0:
            # In parent ...
            os.close(pw)
            while True:
                raw_msg_size = os.read(pr, 4)
                if len(raw_msg_size) != 4:
                    break
                msg_size = struct.unpack("=I", raw_msg_size)[0]
                raw_msg = os.read(pr, msg_size)
                if len(raw_msg) != msg_size:
                    break
                msg = pickle.loads(raw_msg)
                if msg[0] == "CHILD_SETSID_FAILED":
                    print(
                        "Error: Child couldn't create a new session: {:s}"
                        .format(msg[1].strerror),
                        file=sys.stderr
                    )
                    sys.exit(1)
                elif msg[0] == "CHILD_FORK_FAILED":
                    print(
                        "Error: Couldn't fork the child process: {:s}"
                        .format(msg[1].strerror),
                        file=sys.stderr
                    )
                    sys.exit(1)
                elif msg[0] == "CHILD_FORK_SUCCESS":
                    grandchild_pid = msg[1]
                elif msg[0] == "GRANDCHILD_PRERUN":
                    os._exit(0)
                elif msg[0] == "GRANDCHILD_PIDFILE_OPEN_FAILED":
                    print(
                        "Error: Couldn't open pidfile: {:s}"
                        .format(msg[1].strerror),
                        file=sys.stderr
                    )
                    sys.exit(1)
                elif msg[0] == "GRANDCHILD_PIDFILE_LOCK_FAILED":
                    if msg[1].errno in (errno.EAGAIN, errno.EACCES):
                        print(
                            "Error: Couldn't acquire a lock on the pidfile"
                            " (the deamon might already be running): {:s}"
                            .format(msg[1].strerror),
                            file=sys.stderr
                        )
                    else:
                        print(
                            "Error: Couldn't acquire a lock on the pidfile:"
                            " {:s}"
                            .format(msg[1].strerror),
                            file=sys.stderr
                        )
                    sys.exit(1)
                else:
                    # Better be dead code
                    print(
                        "Error: Unknown message {!r}".format(msg[0]),
                        file=sys.stderr
                    )
                    sys.exit(1)
            # Better be dead code
            print("Caca", file=sys.stderr)
            sys.exit(1)

        # In child ...
        os.close(pr)
        try:
            os.setsid()
        except OSError as exc:
            msg = pickle.dumps(("CHILD_SETSID_FAILED", exc))
            os.write(pw, struct.pack("=I", len(msg)) + msg)
            sys.exit(1)

        # Fork the child
        try:
            grandchild_pid = os.fork()
        except OSError as exc:
            msg = pickle.dumps(("CHILD_FORK_FAILED", exc))
            os.write(pw, struct.pack("=I", len(msg)) + msg)
            sys.exit(1)

        if grandchild_pid != 0:
            # In child ...
            msg = pickle.dumps(("CHILD_FORK_SUCCESS", grandchild_pid))
            os.write(pw, struct.pack("=I", len(msg)) + msg)
            os._exit(0)

        # In grand-child ...

        # Redirect stdin, stdout and stderr to devnull
        devnull_fd_ro = os.open(os.devnull, os.O_RDONLY)
        devnull_fd_wo = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull_fd_ro, sys.__stdin__.fileno())
        os.dup2(devnull_fd_wo, sys.__stdout__.fileno())
        os.close(devnull_fd_ro)
        os.close(devnull_fd_wo)

        # Reset umask
        os.umask(0)

        # Change working directory to /
        os.chdir("/")

        # Try to get an exclusive lock on pidfile
        try:
            self._pidfile_fd = os.open(
                self._pidfilepath, os.O_WRONLY | os.O_CREAT
            )
        except OSError as exc:
            msg = pickle.dumps(("GRANDCHILD_PIDFILE_OPEN_FAILED", exc))
            os.write(pw, struct.pack("=I", len(msg)) + msg)
            sys.exit(1)

        atexit.register(self._cleanup_pidfile)

        try:
            fcntl.lockf(self._pidfile_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            msg = pickle.dumps(("GRANDCHILD_PIDFILE_LOCK_FAILED", exc))
            os.write(pw, struct.pack("=I", len(msg)) + msg)
            sys.exit(1)

        os.write(
            self._pidfile_fd,
            "{:d}".format(os.getpid()).encode(encoding="ascii")
        )
        os.fsync(self._pidfile_fd)

        # Step 13 (Drop privs, change users, etc.)

        msg = pickle.dumps(("GRANDCHILD_PRERUN", None))
        os.write(pw, struct.pack("=I", len(msg)) + msg)
        os.close(pw)

        # Call the deamon entry-point
        self.run()

    def run(self):
        self._target(*self._target_args, **self._target_kwargs)
