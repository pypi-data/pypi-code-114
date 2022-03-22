from m3.actions import (
    Action,
)
from recordpack.recordpack import (
    READONLY_CATEGORY,
    WRITE_CATEGORY,
)


class ChangeElectronicDocumentStatusParametersDialogAction(Action):
    """
    Экшен получения диалогового окна с настройкой параметров функции "ЭДО - Смена статуса электронного документа"
    """

    url = '/parameters-dialog'

    def __init__(self):
        super().__init__()
        self.need_atomic = False
        self.category = READONLY_CATEGORY

    def run(self, request, context):
        raise NotImplementedError


class ChangeElectronicDocumentStatusExecuteAction(Action):
    """
    Экшен исполнения функции системы "ЭДО - Смена статуса электронного документа"
    """

    url = '/execute'

    def __init__(self):
        super().__init__()

        self.need_atomic = False
        self.category = WRITE_CATEGORY

    def run(self, request, context):
        raise NotImplementedError
