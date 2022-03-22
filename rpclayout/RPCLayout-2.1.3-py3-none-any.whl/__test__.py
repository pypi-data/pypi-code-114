import platform

class __test__:
    def callback_os(functionA):
        '''
        :param def void:
        Detect operating system and do a function
        '''
        if platform.system() == "Windows":
            functionA()
        elif platform.system() == "Darwin":
            functionA()
    