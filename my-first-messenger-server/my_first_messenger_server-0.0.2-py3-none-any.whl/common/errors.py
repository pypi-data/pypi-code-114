class IncorrectDataReceivedError(Exception):

    """Класс - исключение, для обработки ошибок когда некорректные данные получены от сокета"""
    def __str__(self):
        return 'Принято некорректное сообщение от удаленного компьютера'


class NonDictInputError(Exception):
    """Класс - исключение, для обработки ошибок когда аргумент функции не словарь."""
    def __str__(self):
        return 'Аргумент функции должен быть словорём'


class ReqFieldMissingError(Exception):
    """Класс - исключение, для обработки ошибок когда отсутствует обязательное поле в принятом словаре."""

    def __init__(self, missing_field):
        self.missing_field = missing_field

    def __str__(self):
        return f'В принятом словоре отсутствует обязательной поле {self.missing_field}'


class ServerError(Exception):
    '''
    Класс - исключение, для обработки ошибок сервера.
    При генерации требует строку с описанием ошибки,
    полученную с сервера.
    '''

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text
