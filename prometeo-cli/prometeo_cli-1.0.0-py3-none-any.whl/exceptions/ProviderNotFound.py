class ProviderNotFound(Exception):

    def __init__(self, msg='Provider not found'):
        super().__init__(msg)
