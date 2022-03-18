import subprocess

class Terminal:
    def __init__(self, output=False):
        self.__output__ = output
        self.__oldCds__ = []

    def __checkStore__(self, command):
        if command[0:2] == 'cd':
            self.__oldCds__.append(command)
            return True
        return False

    def type(self, command):
        check = self.__checkStore__(command)

        if check:
            commands = '; '.join(self.__oldCds__)
            output = subprocess.check_output(commands, shell=True)

            if output[-1:len(output)] == '\n':
                output = output[0:-1]

        else:
            if len(self.__oldCds__) >= 1:
                commands = '; '.join(self.__oldCds__)
                output = subprocess.check_output(f'{commands}; {command}', shell=True)

                if isinstance(output, bytes):
                    output = output.decode()

                if output[-1:len(output)] == '\n':
                    output = output[0:-1]

            else:
                output = subprocess.check_output(command, shell=True)

                if isinstance(output, bytes):
                    output = output.decode()

                if output[-1:len(output)] == '\n':
                    output = output[0:-1]

        if self.__output__:
            return output