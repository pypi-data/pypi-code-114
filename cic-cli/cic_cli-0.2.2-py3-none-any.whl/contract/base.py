# standard imports
import os
import hashlib


mod_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
root_dir = os.path.join(mod_dir, '..')
data_dir = os.path.join(mod_dir, 'data')
schema_dir = os.path.join(mod_dir, 'schema')


class Data:
    """Base class for all parts of the token data deployment.
    """

    __default_version = 0

    def __init__(self):
        self.dirty = False
        self.inited = False
        self.__version = self.__default_version
        self.__hasher = self.__basehasher


    def __basehasher(self, v):
        h = hashlib.sha256()
        h.update(v)
        return h.digest()


    def hash(self, v):
        """Compute digest of the given data

        :param v: Data to hash
        :type v: bytes
        :rtype: bytes
        :return: Hashed data
        """
        return self.__hasher(v)


    def load(self):
        """Prevents overwriting data from settings if data state has changed.

        :raises RuntimeError: If state is dirty
        """
        if self.dirty:
            raise RuntimeError('Object contains uncommitted changes')


    def start(self):
        """Prevents double initialization of data item.

        :raises RuntimeError: If already initialized
        """
        if self.inited:
            raise RuntimeError('Object already initialized')


    def verify(self):
        """Verify data state (noop)
        """
        return True


    def version(self):
        """Return version of data schema.
        """
        return self.__version


    def set_version(self, version):
        """Set version of data schema. The version number is a single integer.

        :param version: version
        :type version: int
        """
        self.__version = version
