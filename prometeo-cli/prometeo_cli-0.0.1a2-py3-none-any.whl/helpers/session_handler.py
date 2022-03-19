from pmo.exceptions import ExistsSessionException

class SessionHandler:

    def __init__(self):
        pass


    def _create_file(self):
        pass


    def _exists_file(self):
        pass


    def _create_file_if_not_exists(self):
        if not self._exists_file():
            self._create_file();
        pass

    def _exists_session(self):
        pass

    def create_session(self):
        if self._exists_session():
            raise ExistsSessionException('')

        pass




    def retrieve_session(self):
        pass



