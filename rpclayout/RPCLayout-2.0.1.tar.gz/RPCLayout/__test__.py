import platform

class __test__:
    def callback_os(void):
        '''
        :param def void:
        Detect operating system and do a function
        '''
        if platform.system() == "Windows":
            void()
        elif platform.system() == "Darwin":
            void()
    