import re

from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class CommaSeparatedListValidator(validators.RegexValidator):
    regex = r'^\w+(?:,\w+)*$'
    message = ',（カンマ）で区切られている必要があります。'
    flags = 0


@deconstructible
class ColorCodeValidator(validators.RegexValidator):
    """ 16進数表記カラーコードバリデータ """
    regex = r'^#([0-9a-zA-Z]{3}|[0-9a-zA-Z]{6})$'
    message = '#A1B, #A1B2C3のようにカラーコードで入力してください。'
    flags = re.ASCII


@deconstructible
class KanaValidator(validators.RegexValidator):
    regex = r'^[{}-{}]+$'.format(chr(0x3040), chr(0x309F))
    message = 'ひらがなで入力してください。'
    flags = 0


@deconstructible
class NonStrictEmailValidator(validators.EmailValidator):
    user_regex = validators._lazy_re_compile(
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*\Z"  # dot-atom
        r"|^[-!#$%&.'*+/=?^_`{}|~0-9A-Z]+\Z"  # docomoの古いアドレスなどである'.@'を許容する
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]'
        r'|\\[\001-\011\013\014\016-\177])*"\Z)',  # quoted-string
        re.IGNORECASE)


@deconstructible
class PhoneNumberValidator(validators.RegexValidator):
    regex = r'^[0-9]+-[0-9]+-[0-9]+$'
    message = 'xxx-xxxx-xxxxのようにハイフン付きで入力してください。'


@deconstructible
class PostcodeValidator(validators.RegexValidator):
    regex = r'^[0-9]{3}-[0-9]{4}$'
    message = 'xxx-xxxxのようにハイフン付きで入力してください。'


@deconstructible
class StrictUsernameValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+$'
    message = '使用できない文字列が含まれています。'
    flags = re.ASCII


@deconstructible
class Uuid4Validator(validators.RegexValidator):
    regex = r'^[0-9a-zA-Z]{8}-?([0-9a-zA-Z]{4}-?){3}[0-9a-zA-Z]{12}$'
    message = 'UUID4のフォーマットとして正しくありません。'


validate_comma_separeted_list = CommaSeparatedListValidator()
validate_only_kana = KanaValidator()
validate_phone_number = PhoneNumberValidator()
validate_postcode = PostcodeValidator()
validate_non_strict_email = NonStrictEmailValidator()
validate_strict_username = StrictUsernameValidator()
validate_uuid4 = Uuid4Validator()
