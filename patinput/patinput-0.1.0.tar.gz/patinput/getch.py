from patinput import its_win32

if its_win32:
    from msvcrt import getch
else:
    def getch() -> bytes:
        """
        Gets a single character from STDIO.
        """
        import sys
        import tty
        import termios

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.encode("ascii")

        