from jija.config.base import Base
from jija.utils.path import Path


class StructureConfig(Base):
    PROJECT_PATH = None
    CORE_PATH = None
    APPS_PATH = None

    def __init__(self, *, project_dir=None, core_dir='core', apps_dir='apps'):
        StructureConfig.PROJECT_PATH = self.__get_project_path(project_dir)
        StructureConfig.CORE_PATH = StructureConfig.PROJECT_PATH + core_dir
        StructureConfig.APPS_PATH = StructureConfig.PROJECT_PATH + apps_dir

        super().__init__()

    @staticmethod
    def __get_project_path(project_dir):
        if isinstance(project_dir, Path):
            return project_dir

        return Path('' if project_dir is None else project_dir)
