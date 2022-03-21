class BaseModel:
    class Config:
        """you can set any field you like in your config class"""

        pass

    def infer(self, X={}, Y=[]):
        """infer function you can do anything here"""
        raise NotImplementedError()

    def evaluate(self, *args, **kwargs):
        raise NotImplementedError()

    @classmethod
    def load_from(cls, usermodel):
        """you shuold set your wrapper from usermodel, and set Config like"""
        cls.Config = getattr(usermodel.Config, cls.__name__)
        usermodel.model = cls()
        return usermodel
