from jija.config.base import Base


class ProjectConfig(Base):
    SECRET_KEY = None

    def __init__(self, *, secret_key=b'*' * 32):
        super().__init__()

        ProjectConfig.SECRET_KEY = secret_key
